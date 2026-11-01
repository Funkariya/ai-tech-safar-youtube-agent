# AI Tech Safar — Full channel automation architecture

## Goal
Build a mobile-first production pipeline for AI Tech Safar, from topic discovery to finished video package, with explicit human approval before publication.

## Pipeline

1. **Topic discovery**
   - Gather AI product launches, model releases, useful tools and practical workflows.
   - Save source URLs, publication dates and primary-source evidence.
   - Rank by audience relevance, timeliness, usefulness, differentiation and production effort.
   - Reject unsupported rumours and duplicate topics.

2. **Research and fact-check**
   - Prefer official product pages, release notes, documentation, research papers and company announcements.
   - Store each factual claim with a source URL and a short evidence note.
   - Flag uncertain or conflicting claims as [VERIFY]; do not fabricate tests or benchmarks.

3. **Script production**
   - Select format: Short, 8–12 minute explainer, or long-form deep dive.
   - Generate hook, outline, spoken script, visual/B-roll instructions and source notes.
   - Estimate runtime from spoken word count and target speaking pace.

4. **Packaging and SEO**
   - Draft title/thumbnail pairs, description, search phrases, tags where useful, chapters and pinned comment.
   - Ensure title and thumbnail promise exactly matches the video.
   - No keyword stuffing or unsupported performance promises.

5. **Voice and media**
   - Produce narration only after script approval.
   - Use licensed/original assets or assets with documented permission.
   - Generate captions and a visual edit plan; preserve source and licence notes.

6. **Editing and quality assurance**
   - Assemble video, captions, sound and thumbnail.
   - Check audio peaks, spelling, subtitle sync, aspect ratio, safe areas, copyright and factual claims.
   - Produce a private review render and checklist.

7. **Human approval**
   - Dashboard displays source evidence, script, title, thumbnail, video preview and QA checklist.
   - Status sequence: IDEA → RESEARCHED → SCRIPT_DRAFT → SCRIPT_APPROVED → MEDIA_READY → EDIT_READY → QA_PASSED → FINAL_APPROVED.
   - Only a person can set FINAL_APPROVED.
   - Approval is scoped to an exact version/hash of the package; any edit after approval resets approval.

8. **Publishing**
   - Initial deployment: manual upload in YouTube Studio only.
   - Future optional integration: YouTube Data API private/unlisted upload after a separate explicit authorization. Never auto-publish public.
   - A separate human confirmation must be required for visibility, schedule, title, description and final upload.
   - Keep upload logs and allow revoke/stop before publish.

9. **Analytics and learning**
   - Import YouTube Analytics exports or authorized API metrics.
   - Compare CTR, average view duration, retention, returning viewers and traffic sources against the channel's own baseline.
   - Convert findings into experiments; do not promise viral growth.

## Architecture recommendation

- **Mobile dashboard:** Streamlit prototype now; later a responsive web app.
- **Backend:** Python job runner with a persistent database for jobs, assets, sources, approval history and status.
- **Storage:** object storage for scripts, audio, thumbnails and video renders; never commit media binaries to Git.
- **Queue:** scheduled research and render jobs with retries, timeouts and idempotency.
- **AI providers:** pluggable model adapters; keep provider keys in environment secrets.
- **Media tools:** FFmpeg for assembly and validation; separate TTS and image/video generation providers.
- **Integrations:** YouTube Analytics read-only first; upload API only in a later, separately approved phase.
- **Observability:** job logs, error state, retry button, usage/cost tracking and source provenance.

## Critical safeguards

- Never store API keys, OAuth refresh tokens, cookies or credentials in Git.
- Do not auto-publish or auto-reply to comments.
- Require review of copyright, privacy, source reliability and factual accuracy.
- Rate-limit external calls and respect provider terms.
- Keep a human-readable audit trail of every approval and action.

## Current implementation reality

The repository currently has skill guides, command-line helpers, a Streamlit draft review desk and a basic workflow. It does not yet include autonomous web research, AI model integration, TTS, video rendering, persistent hosted storage, YouTube Analytics integration or YouTube upload. Those are separate implementation milestones, not completed features.
