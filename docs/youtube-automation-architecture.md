# AI Tech Safar — Full channel automation architecture

## Approved operating target

- **Every day:** 1 YouTube Short, target length 30–60 seconds.
- **Twice weekly:** 1 detailed video per slot, target length 8–12 minutes.
- **Language:** English, for an international audience (US, UK, Canada, Australia and Europe).
- **Niche:** AI product launches, useful AI tools, model updates, practical workflows and emerging technology.
- **Publishing target:** unattended scheduled public publishing after the owner connects and authorizes the required services.
- **Device:** Android-first control panel; compute and rendering run in the cloud.

This is the target configuration, not a claim that the pipeline is already live. Current repo code is still a foundation.

## End-to-end pipeline

1. **Discover topics** from official product blogs, release notes, research papers, documentation and reputable technology publications. Deduplicate against recent channel topics.
2. **Score topics** for freshness, usefulness, audience relevance, source quality, originality and production cost. Keep source URLs and dates.
3. **Research and fact-check** every material claim. Reject rumours, unsupported benchmarks, invented hands-on testing and stale launch claims.
4. **Generate formats**:
   - Short: 30–60 sec, one clear idea, fast hook, concise explanation and useful CTA.
   - Detailed: 8–12 min, clear problem, context, demo/workflow, limitations, practical takeaway and source list.
5. **Create voiceover** using a configured TTS provider. Voice, pronunciation and pacing checks are required.
6. **Create visuals** using licensed stock, original graphics, screen recordings, diagrams or an approved image/video generation provider. Keep asset provenance and licence notes.
7. **Render** with FFmpeg: voice, visuals, subtitles, transitions, licensed/original music and platform-specific aspect ratio.
8. **Create packaging**: thumbnail, title, description, chapters for long-form, relevant tags and disclosure fields. Avoid misleading metadata.
9. **Automated QA**: validate duration, resolution, aspect ratio, audio level/clipping, subtitle timing, black frames, missing media, source coverage, metadata, duplicate similarity and policy/disclosure checklist.
10. **Publish and schedule** through the YouTube Data API only after OAuth is configured. Set privacy and publish time explicitly; verify returned video status and processing state. If API auth, compliance, quota or QA fails, stop and alert instead of silently skipping checks.
11. **Measure results** using authorized YouTube Analytics data: impressions, CTR, average view duration, retention and traffic sources. Use channel-specific baselines; do not optimize solely for clickbait.

## Schedule configuration

See [channel-config.json](channel-config.json). Times are defaults in Asia/Kolkata and can be changed. Avoid publishing two videos at the same time. Suggested detailed-video slots: Tuesday and Friday at 18:30 IST; Shorts daily at 12:30 IST. The schedule is a proposal until configured in the live runner.

## Architecture

- Android-friendly web dashboard for status, logs, costs, failed jobs and emergency pause.
- Cloud job runner with persistent job queue, retries, idempotency and timeouts.
- Object storage for source evidence, scripts, audio, images, thumbnails and MP4 renders; do not commit media binaries to Git.
- Pluggable research, LLM, TTS and visual providers; all credentials stored as deployment secrets.
- FFmpeg rendering worker.
- YouTube OAuth 2.0 connection using the minimum required scope.
- Analytics integration read-only at first.
- Usage/cost ledger per video and provider.

## Publishing safeguards

- Auto-publish is the intended mode, but **fail closed**: if sources are weak, a factual claim is unresolved, copyright/licence provenance is missing, QA fails, disclosure is uncertain, or API status is ambiguous, do not publish.
- Never upload with an accidental default visibility. Set intended privacy explicitly.
- Keep a kill switch that pauses all scheduled publishing.
- Log source URLs, asset provenance, prompt/model versions, render hash, metadata, API response and publish URL.
- Never store API keys, OAuth refresh tokens, cookies or credentials in Git.
- Do not auto-reply to comments or perform channel moderation without a separate scope and approval.
- Avoid mass-produced near-identical videos. Each video must add distinct, accurate value and meaningful narration/visual explanation.

## Current implementation status

Already in the repository:
- Draft review dashboard and draft folder workflow.
- Script/SEO skill guides and small local quality utilities.
- Architecture and Android Codespaces setup notes.

Not yet implemented or connected:
- Live topic research and evidence storage.
- LLM scripting integration.
- TTS and visual asset generation.
- FFmpeg end-to-end renderer and automated QA.
- Persistent cloud job queue and media storage.
- YouTube OAuth, upload/scheduling and Analytics.
- Hosted Android dashboard and monitoring.

Therefore **nothing is currently auto-generating or publishing videos**. To activate it, deploy the runner, add provider secrets, connect the YouTube channel through OAuth, test an unlisted/private upload, and then enable the public schedule deliberately.

## YouTube API notes

The official API supports video upload and metadata including privacy status and scheduled publish time. Quota allocation and project restrictions must be checked in the actual Google Cloud project. Official documentation has had conflicting language around unverified-project visibility, so the implementation must inspect the actual API response and channel/project status rather than assume public scheduling will work.

References:
- https://developers.google.com/youtube/data/reference/rest/v3/videos/insert
- https://developers.google.com/youtube/data/reference/rest/v3/videos
- https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
