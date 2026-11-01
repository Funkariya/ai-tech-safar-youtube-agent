# AI Tech Safar — YouTube Agent

An approval-first YouTube production toolkit for AI Tech Safar.

## Safety model
- This repository prepares scripts, titles, descriptions, chapters, Shorts candidates and review plans.
- It does **not** publish videos, schedule uploads, modify channel settings, or send comments.
- Every deliverable must be reviewed and explicitly approved by a human.
- Never add OAuth tokens, API keys, cookies, or channel credentials to this repository.

## Channel defaults
- Brand: AI Tech Safar
- Website: https://www.aitechsafar.com/
- Channel: https://youtube.com/@ai_tech_safar
- Niche: practical AI tools, AI news and emerging technology
- Audience: international English-speaking viewers
- Style: useful, evidence-led, clear, no fabricated claims

## Toolkit
- 11 reusable workflow skill guides in `skills/`
- 6 local Python utilities in `scripts/`
- No external API key is required for the local utilities.

## Run locally
Python 3.10+:
```bash
python scripts/hookscore.py "Your opening hook"
python scripts/title.py "Your video topic"
python scripts/deadair.py transcript.txt
python scripts/chapters.py transcript.txt
python scripts/swipe.py "Your topic" --ideas 5
```

Retention CSV analysis:
```bash
python scripts/retention.py retention.csv --baseline 100
```

## Android workflow
See [CODESPACES.md](CODESPACES.md) for exact mobile setup. In Codespaces run:
```bash
python -m pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0
```
The dashboard is a review desk only; it does not publish. Use `python workflow.py "Your topic"` to create a draft folder.

## Approval checklist
1. Verify every factual claim against a primary source.
2. Check title and thumbnail promise match the actual video.
3. Check copyright, privacy and attribution.
4. Review description, links, chapters and subtitles.
5. Obtain explicit human approval before any upload or publication.

## Disclaimer
This is a content-planning and quality-control toolkit, not a guaranteed growth or monetization system.
