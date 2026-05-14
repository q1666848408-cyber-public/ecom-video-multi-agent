<div align="center">

# 🤖 E-Commerce Video Multi-Agent System

[![Claude Code](https://img.shields.io/badge/Claude-Code-D4A843?style=flat-square&logo=anthropic&logoColor=white)](https://claude.com/code)
[![Multi-Agent](https://img.shields.io/badge/Multi--Agent-7B68EE?style=flat-square)](https://github.com)
[![Lark](https://img.shields.io/badge/Lark-Bitable-00D6B9?style=flat-square&logo=bytedance&logoColor=white)](https://open.feishu.cn)
[![Seedance](https://img.shields.io/badge/Seedance-2.0-FF6B35?style=flat-square)](https://www.volcengine.com)
[![TikTok](https://img.shields.io/badge/TikTok-Shop-000000?style=flat-square&logo=tiktok&logoColor=white)](https://shop.tiktok.com)

**End-to-end TikTok US e-commerce content operations agent — main agent + 7 subagents + 13 skills, covering sourcing → script → storyboard → video → publish**

> ⚠️ **Showcase Only** — ~15% skeleton. Production agents, skills, prompts & business logic not included.

</div>

---

## ✨ Overview

The most ambitious project in this portfolio: a unified Claude Code multi-agent architecture that runs the entire TikTok US e-commerce content operation. Drama videos and dance / traffic videos share the **same agent pipeline** — only the routing differs. The system covers product sourcing, script ideation, storyboard generation, video assembly via Seedance, and final TikTok publishing.

---

## 🏗️ Architecture

```
                  ┌────────────────────────────────────┐
                  │           Main Agent               │
                  │     (orchestrator + routing)       │
                  └──┬──────────┬──────────┬───────┬───┘
                     │          │          │       │
       ┌─────────────┘          │          │       └──────────────┐
       ▼                        ▼          ▼                      ▼
  ┌──────────┐         ┌──────────────┐ ┌──────────┐       ┌──────────────┐
  │ ecom-    │         │ director     │ │ art-     │       │ storyboard-  │
  │researcher│         │ (script)     │ │ designer │       │ artist       │
  └────┬─────┘         └──────┬───────┘ └────┬─────┘       └──────┬───────┘
       │                      │              │                    │
  ┌────▼─────┐          ┌─────▼──────┐  ┌────▼─────┐         ┌────▼──────┐
  │ image-   │          │ video-     │  │ live-    │         │ + 13      │
  │ generator│          │ operator   │  │ operator │         │ skills    │
  └──────────┘          └────────────┘  └──────────┘         └───────────┘
                                                       (compliance, dreamina-cli,
                                                        publish, nurture, ...)
```

---

## 🧠 Agents (8 total)

| Agent | Role |
|---|---|
| Main | Orchestrator + routing (drama / ecom / dance) |
| ecom-researcher | Sourcing + competitor analysis |
| director | Script ideation + arc design |
| art-designer | Character + scene design |
| storyboard-artist | 12-grid storyboard + Seedance prompts |
| image-generator | Reference image generation |
| video-operator | Video assembly + TikTok publish |
| live-operator | Live-stream operations |

---

## 🛠️ Skills (13 total)

`art-design` · `art-direction-review` · `compliance-review` · `director-skill` · `dreamina-cli` · `ecom-research` · `ecom-script-review` · `feishu-sync` · `image-generation` · `nurture` · `publish` · `script-analysis-review` · `seedance-storyboard` · `seedance-prompt-review` · `traffic-video` · `video-workflow`

---

## 📁 Structure

```
ecom-video-multi-agent/
├── .claude/
│   ├── agents/
│   │   ├── director.md
│   │   └── ecom-researcher.md
│   └── skills/
│       ├── seedance-storyboard-skill/SKILL.md
│       └── ecom-research-skill/SKILL.md
├── src/
│   └── orchestrator.py        # Routing & dispatch
└── tools/
    └── feishu_sync.py         # Bitable sync utility
```

---

## 🔧 Tech Stack

| Layer | Technology |
|---|---|
| Agent Platform | Claude Code (Anthropic) |
| LLM | Claude Sonnet / Opus |
| Multi-modal | Gemini 2.5 Pro (image gen) |
| Video | Seedance 2.0 |
| Storage | Feishu Bitable |
| Publish | AdsPower + Playwright |

---

<div align="center">
<sub>Showcase version · Production agents & skills not included · For portfolio reference only</sub>
</div>
