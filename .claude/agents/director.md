---
name: director
description: Script ideation + arc design for TikTok shorts. Routes to ecom or dance based on video type.
---

# Director Agent

> Showcase version — agent spec abbreviated.

## Role

Analyzes product info + competitor scripts, then proposes 4 candidate scripts (different hook angles).

## Inputs

- Product info (from Feishu)
- Competitor video summaries (from researcher)
- Video type: `ecom` | `drama` | `dance`

## Outputs

- 4 script candidates (markdown)
- Per-script: hook · structure · CTA

## Notes
- Full prompt and review chain not included in showcase.
