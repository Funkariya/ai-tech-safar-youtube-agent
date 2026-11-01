"""Create an approval-gated content workspace from the command line."""
import argparse, json, re
from pathlib import Path
from datetime import datetime, timezone

def slugify(value):
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", value.lower())).strip("-")[:55] or "video-draft"

def main():
    p=argparse.ArgumentParser(description="Create a YouTube content draft; never publishes.")
    p.add_argument("topic")
    p.add_argument("--format",default="8–12 minute video")
    p.add_argument("--audience",default="International English-speaking viewers")
    p.add_argument("--outcome",default="")
    a=p.parse_args()
    root=Path("drafts"); root.mkdir(exist_ok=True)
    base=slugify(a.topic); folder=root/base; n=2
    while folder.exists():
        folder=root/f"{base}-{n}"; n+=1
    folder.mkdir()
    meta={"topic":a.topic,"format":a.format,"audience":a.audience,"viewer_outcome":a.outcome,
          "created_at":datetime.now(timezone.utc).isoformat(),"status":"DRAFT",
          "approval_required":True,"approved_by_user":False,"published":False}
    (folder/"metadata.json").write_text(json.dumps(meta,indent=2),encoding="utf-8")
    (folder/"brief.md").write_text(
        f"# {a.topic}\n\n## Audience\n{a.audience}\n\n## Format\n{a.format}\n\n"
        f"## Viewer outcome\n{a.outcome}\n\n## Research\n- [ ] Add primary sources\n"
        "- [ ] Verify dates, numbers and product claims\n\n## Script\n"
        "Use skills/yt-script/SKILL.md. Mark uncertain claims [VERIFY].\n\n"
        "## Packaging\nUse skills/yt-package/SKILL.md.\n\n"
        "## Final review\n- [ ] Facts checked\n- [ ] Copyright checked\n"
        "- [ ] Title and thumbnail match the content\n- [ ] Human approval recorded\n",
        encoding="utf-8")
    print(f"Created draft: {folder}")
    print("Status: DRAFT — no upload or publication performed.")
if __name__=="__main__": main()
