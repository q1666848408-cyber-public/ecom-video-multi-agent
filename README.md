# Ecom-Video-Multi-Agent

![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)

> **Showcase** — ~15% skeleton. Core implementation not included.

Multi-agent system for TikTok e-commerce video production. One orchestrator coordinates 7 specialist subagents across the full production chain, from product selection to TikTok publish.

## Stack

- Python
- Claude Code CLI (orchestrator and subagents)
- Playwright (TikTok upload)
- Seedance (AI video generation)
- Feishu Bitable API

## Agent Map

```
Orchestrator
├── product-selector    # scrapes and ranks products
├── script-writer       # generates hook + body + CTA
├── storyboard-agent    # produces shot-by-shot breakdown
├── seedance-prompter   # writes Seedance generation prompts
├── asset-collector     # downloads product images/clips
├── video-assembler     # stitches final video
└── tiktok-publisher    # uploads via Playwright
```

13 on-demand skills are available to any agent (e.g., web search, image resize, subtitle burn).

## Usage

```bash
pip install -r requirements.txt
cp .env.example .env   # Claude API key, TikTok credentials, Feishu token

# Run the full pipeline for one product
python orchestrator.py --product-url "https://..."

# Run a single subagent in isolation
python agents/script_writer.py --product-json product.json
```

## Structure

```
Ecom-Video-Multi-Agent/
├── orchestrator.py
├── agents/
│   ├── product_selector.py
│   ├── script_writer.py
│   ├── storyboard_agent.py
│   ├── seedance_prompter.py
│   ├── asset_collector.py
│   ├── video_assembler.py
│   └── tiktok_publisher.py
├── skills/            # 13 reusable skill modules
├── prompts/           # prompt templates per agent
└── .env.example
```

## Configuration

| Variable | Description |
|----------|-------------|
| `ANTHROPIC_API_KEY` | Claude API key |
| `SEEDANCE_API_KEY` | Seedance video generation key |
| `FEISHU_APP_ID` | Feishu app credentials |
| `TIKTOK_SESSION` | Playwright storage state for TikTok |
