from __future__ import annotations

import argparse
import json
from pathlib import Path

import feedparser
import requests


def summarize_entry(entry: dict[str, str], keywords: list[str], ollama_url: str, model: str) -> str:
    prompt = (
        "Summarize this feed item for a founder looking for opportunities.\n"
        "Return 2 short lines: opportunity summary + why it matters.\n\n"
        f"Tracked keywords: {', '.join(keywords)}\n"
        f"Title: {entry.get('title', '')}\n"
        f"Summary: {entry.get('summary', '')}\n"
        f"Link: {entry.get('link', '')}"
    )
    response = requests.post(
        f"{ollama_url.rstrip('/')}/api/generate",
        json={"model": model, "prompt": prompt, "stream": False},
        timeout=120,
    )
    response.raise_for_status()
    return response.json().get("response", "").strip()


def main() -> None:
    parser = argparse.ArgumentParser(description="Monitor RSS feeds for keywords and build a digest.")
    parser.add_argument("--feeds", required=True, help="Comma-separated RSS/Atom feed URLs")
    parser.add_argument("--keywords", required=True, help="Comma-separated keywords")
    parser.add_argument("--limit", type=int, default=20, help="Max entries per feed")
    parser.add_argument("--ollama-url", default="http://localhost:11434", help="Base URL for Ollama")
    parser.add_argument("--model", default="llama3.1", help="Ollama model name")
    parser.add_argument("--json-out", default="opportunities.json", help="JSON output path")
    parser.add_argument("--markdown-out", default="opportunities.md", help="Markdown output path")
    args = parser.parse_args()

    feeds = [item.strip() for item in args.feeds.split(",") if item.strip()]
    keywords = [item.strip().lower() for item in args.keywords.split(",") if item.strip()]
    matches = []

    for feed_url in feeds:
        parsed = feedparser.parse(feed_url)
        for item in parsed.entries[: args.limit]:
            haystack = f"{item.get('title', '')}\n{item.get('summary', '')}".lower()
            matched_keywords = [keyword for keyword in keywords if keyword in haystack]
            if not matched_keywords:
                continue
            entry = {
                "feed": feed_url,
                "title": item.get("title", ""),
                "link": item.get("link", ""),
                "summary": item.get("summary", ""),
                "matched_keywords": matched_keywords,
            }
            entry["ai_summary"] = summarize_entry(entry, matched_keywords, args.ollama_url, args.model)
            matches.append(entry)
            print(f"[ok] matched: {entry['title']}")

    Path(args.json_out).write_text(json.dumps(matches, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    lines = ["# Opportunity Digest", ""]
    for item in matches:
        lines.extend(
            [
                f"## {item['title']}",
                f"- Feed: {item['feed']}",
                f"- Keywords: {', '.join(item['matched_keywords'])}",
                f"- Link: {item['link']}",
                "",
                item["ai_summary"],
                "",
            ]
        )
    Path(args.markdown_out).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"[done] wrote {args.markdown_out} and {args.json_out}")


if __name__ == "__main__":
    main()
