# 📡 RSS Opportunity Radar

> AI-powered RSS feed monitor that filters opportunities by keywords and generates digest summaries.

Built for founders, freelancers, and operators who want to **catch signals before competitors**.

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Ollama](https://img.shields.io/badge/AI-Ollama-orange)

## ✨ Features

- **Multi-feed monitoring** — Watch any number of RSS/Atom feeds simultaneously
- **Keyword filtering** — Define keywords that matter to your business
- **AI summaries** — Each matched opportunity gets an Ollama-powered digest
- **Dual output** — Generates both `opportunities.json` and `opportunities.md` for easy integration
- **Zero SaaS dependency** — Runs 100% locally, no API keys needed (just Ollama)

## 🚀 Quick Start

```bash
# 1. Clone and install
git clone https://github.com/NexusFernandez/rss-opportunity-radar.git
cd rss-opportunity-radar
pip install -r requirements.txt

# 2. Run with your feeds and keywords
python radar.py --feeds https://news.ycombinator.com/rss \
                --feeds https://indiehacker.com/feed.xml \
                --keywords ai,automation,telegram,startup

# 3. Check results
cat opportunities.md
```

### Prerequisites

- Python 3.10+
- [Ollama](https://ollama.ai) running locally (for AI summaries)

## 📋 Output Format

Each matched item includes:
- **Feed source** — which RSS feed it came from
- **Matching keywords** — why it was flagged
- **Direct link** — to the original article
- **AI summary** — one-paragraph digest of why this matters

### Example

```markdown
## 🔥 [New AI Agent Framework Released](https://example.com/article)
- **Source**: Hacker News
- **Keywords**: ai, agent
- **Summary**: A new open-source framework for building autonomous AI agents...
```

## ⚙️ Configuration

```bash
# Custom output directory
python radar.py --feeds <url> --keywords <words> --output-dir ./my-digests

# Custom Ollama model
OLLAMA_MODEL=llama3 python radar.py --feeds <url> --keywords <words>
```

## 🔗 Commercial License

This repository contains the open-source version under MIT license.

**For the full commercial version with premium features:**

👉 **[Get RSS Opportunity Radar Pro — €19](https://nexusmind30.gumroad.com)**

Premium features include:
- Scheduled cron mode with hourly/daily runs
- Email digest delivery
- Slack/Discord webhook integration
- Historical trend analysis

## 🛠️ Tech Stack

- **Python 3.10+** — core runtime
- **feedparser** — RSS/Atom feed parsing
- **Ollama** — local AI inference for summaries

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

**More tools:** [Telegram AI Business Bot](https://github.com/NexusFernandez/telegram-automation-bot) — Reports, Notes, Alerts and AI Chat — €21

**Full catalog:** [nexusmind30.gumroad.com](https://nexusmind30.gumroad.com) · 10+ AI tools starting at €9

---

Built by [Nexus Fernandez](https://github.com/NexusFernandez)