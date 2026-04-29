<h1 align="center">📡 RSS Opportunity Radar</h1>

<p align="center">
  <strong>AI-powered RSS feed monitor that filters opportunities by keywords and generates digest summaries.</strong><br>
  Runs 100% locally with Ollama. No API keys. No subscriptions.
</p>

<p align="center">
  <a href="https://nexusmind30.gumroad.com/l/usxexm">
    <img src="https://img.shields.io/badge/Get%20Pro%20Version-Gumroad-36b37e?style=for-the-badge&logo=gumroad" alt="Get on Gumroad">
  </a>
  <a href="https://github.com/NexusFernandez/rss-opportunity-radar/stargazers">
    <img src="https://img.shields.io/github/stars/NexusFernandez/rss-opportunity-radar?style=social" alt="Stars">
  </a>
</p>

---

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

- **Python 3.10+**
- **[Ollama](https://ollama.ai)** running locally (for AI summaries)

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

## 🔒 Privacy First

| Feature | RSS Opportunity Radar | Typical SaaS Monitor |
|:--------|:----------------------|:---------------------|
| **Your feeds** | Stay on your machine | Sent to cloud |
| **AI processing** | Local (Ollama) | Remote API |
| **API keys needed** | None | OpenAI, etc. |
| **Monthly cost** | €0 after purchase | $10-50/month |
| **Source code** | Full Python source | Black box |

## ⬆️ Pro Version — €19

The free version is MIT-licensed and fully functional. **[Get the Pro version on Gumroad →](https://nexusmind30.gumroad.com/l/usxexm)** for:

- Scheduled cron mode with hourly/daily runs
- Email digest delivery
- Slack/Discord webhook integration
- Historical trend analysis

## 🛠️ Tech Stack

- **Python 3.10+** — core runtime
- **feedparser** — RSS/Atom feed parsing
- **Ollama** — local AI inference for summaries

---

## 📦 More Tools from Nexus

- **[Telegram AI Business Bot](https://github.com/NexusFernandez/telegram-automation-bot)** — Reports, notes, alerts, and AI chat in Telegram (€21)
- **[All 12 AI Tools →](https://nexusmind30.gumroad.com)** — Python tools for freelancers, founders, and data analysts

---

**⭐ Star this repo** if you find it useful!

Built by [Nexus Fernandez](https://github.com/NexusFernandez) · [nexusmind30.gumroad.com](https://nexusmind30.gumroad.com)