# AI Tech Safar — YouTube Agent

Cloud-first, Android-controlled automation project for AI Tech Safar.

## Target publishing cadence
- Daily: 1 Short (30–60 seconds).
- Tuesday + Friday: 1 detailed video (8–12 minutes) per slot.
- English-language AI tools, AI news, launches and practical tutorials for a global audience.
- Target: automated production and scheduled public publishing, with automated safety checks and a kill switch.

**Important:** the target pipeline is not live yet. This repository currently contains planning, draft review tools and utilities. It does not yet research topics autonomously, generate finished videos, connect to TTS providers or publish to YouTube.

## Existing tools
- 11 reusable workflow skill guides in `skills/`
- 6 local Python utilities in `scripts/`
- Streamlit draft/review dashboard in `app.py`
- Draft folder CLI in `workflow.py`
- Architecture: [docs/youtube-automation-architecture.md](docs/youtube-automation-architecture.md)
- Channel schedule: [channel-config.json](channel-config.json)
- Android setup: [CODESPACES.md](CODESPACES.md)

## Run the current prototype
Python 3.10+:
```bash
python -m pip install -r requirements.txt
streamlit run app.py --server.address 0.0.0.0
```
Open forwarded port 8501 in the Codespaces browser.

Local utilities:
```bash
python scripts/hookscore.py "Your opening hook"
python scripts/title.py "Your video topic"
python scripts/deadair.py transcript.txt
python scripts/chapters.py transcript.txt
python scripts/swipe.py "Your topic" --ideas 5
python scripts/retention.py retention.csv --baseline 100
```

## Activation requirements
1. Deploy a persistent cloud runner and media storage.
2. Configure a research/LLM provider, TTS provider and visual asset source.
3. Install FFmpeg in the render worker.
4. Configure provider API keys as deployment secrets — never commit them.
5. Connect the channel using Google OAuth and YouTube Data API.
6. Test an unlisted/private video, verify processing and metadata, then enable scheduled public publishing.
7. Monitor cost, quota, job failures and policy checks.

No API keys or OAuth credentials are included. Do not assume a free tier can sustain unlimited AI video generation; provider quotas and compute limits apply.
