# 21st-ui — Review dashboard interface skill

Source project: https://github.com/21st-dev/magic-mcp (now 21st MCP).
Use this skill only when designing or improving the AI Tech Safar web/mobile dashboard.

## Useful capabilities
- Search a catalogue of existing React/Tailwind/shadcn UI components.
- Retrieve component source and adapt it to the existing app.
- Generate UI variants only when the connected account explicitly has AI generation access.
- Improve the review dashboard, content calendar, job status, draft preview and approval controls.

## Not for
This tool does not research YouTube topics, write scripts, generate voiceovers, edit videos, optimize SEO, read YouTube analytics, upload videos or publish posts. It is not a YouTube automation engine.

## Workflow
1. Inspect the current dashboard stack and design tokens first.
2. Search for a specific UI need (e.g. mobile content calendar, upload review queue, analytics cards).
3. Prefer an existing compatible component; check dependencies and accessibility.
4. Adapt it to project conventions and test responsive layout.
5. Keep approval actions explicit and auditable.
6. Never add an action that publishes content directly from a UI component.

## Access and limits
The 21st MCP is now the unified 21st MCP at https://21st.dev/api/mcp. The old Magic package is a compatibility proxy. A fresh API key is required; old Magic keys were reset. Free accounts have limited component-code retrievals, and hosted AI generation requires separate AI access. Check current account entitlements before using paid/generation features.

## Safety
No component may bypass the human approval gate. Avoid dark patterns, hidden toggles, destructive actions without confirmation, or storing secrets in client-side code.
