# Android-first setup with GitHub Codespaces

## Open on Android
1. Open https://github.com/Funkariya/ai-tech-safar-youtube-agent
2. Tap the green **Code** button → **Codespaces** → **Create codespace on main**.
3. Wait for the browser editor to load. Use the terminal panel.

## Install and run
```bash
python -m pip install -r requirements.txt
python -m pip install streamlit
python workflow.py "Your AI video topic" --format "8–12 minute video"
streamlit run app.py --server.address 0.0.0.0
```
Codespaces will show a forwarded port (usually 8501). Open it in the browser to use the Review Desk.

## What it does
- Creates a draft folder and metadata.
- Shows draft items in a simple mobile-friendly review dashboard.
- Allows marking a draft approved for manual upload, or revoking that approval.
- Keeps `published=false`; it does not call YouTube APIs.

## Important limitations
This is not an AI model integration and does not generate researched scripts by itself. Use the skill guides as structured prompts in your chosen AI assistant, then paste the reviewed content into the draft brief. No YouTube OAuth, upload token or auto-publishing feature is included. Never add secrets to source files.
