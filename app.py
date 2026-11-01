"""Mobile-friendly Streamlit review dashboard. No publishing functionality exists."""
from pathlib import Path
import json
import streamlit as st

ROOT = Path(__file__).parent
DRAFTS = ROOT / "drafts"
st.set_page_config(page_title="AI Tech Safar Agent", page_icon="🎬", layout="centered")
st.title("AI Tech Safar — Review Desk")
st.caption("Draft preparation and human approval only. This app cannot upload or publish.")
DRAFTS.mkdir(exist_ok=True)

with st.form("new_draft"):
    topic = st.text_input("Video topic", placeholder="e.g. Best free AI video tools")
    audience = st.text_input("Target audience", value="International English-speaking viewers")
    format_type = st.selectbox("Format", ["YouTube Short", "8–12 minute video", "20–30 minute deep dive"])
    objective = st.text_area("Viewer outcome", placeholder="What should the viewer learn or do?")
    submitted = st.form_submit_button("Create review draft")
if submitted:
    if not topic.strip():
        st.error("Enter a topic first.")
    else:
        slug = "".join(c.lower() if c.isalnum() else "-" for c in topic).strip("-")
        slug = "-".join(filter(None, slug.split("-")))[:55] or "video-draft"
        folder = DRAFTS / slug
        suffix = 2
        while folder.exists():
            folder = DRAFTS / f"{slug}-{suffix}"
            suffix += 1
        folder.mkdir(parents=True)
        data = {"topic": topic.strip(), "audience": audience.strip(), "format": format_type,
                "viewer_outcome": objective.strip(), "status": "DRAFT",
                "approval_required": True, "published": False}
        (folder / "metadata.json").write_text(json.dumps(data, indent=2), encoding="utf-8")
        (folder / "brief.md").write_text(
            f"# {topic}\n\n## Audience\n{audience}\n\n## Format\n{format_type}\n\n"
            f"## Viewer outcome\n{objective}\n\n## Research and script\n"
            "Add verified sources, then prepare the script using skills/yt-script/SKILL.md.\n",
            encoding="utf-8")
        st.success(f"Draft created: {folder.name}")

st.divider()
st.subheader("Drafts awaiting review")
folders = sorted([p for p in DRAFTS.iterdir() if p.is_dir()])
if not folders:
    st.info("No drafts yet. Create one above.")
for folder in folders:
    meta_path = folder / "metadata.json"
    if not meta_path.exists():
        continue
    meta = json.loads(meta_path.read_text(encoding="utf-8"))
    with st.expander(f"{meta.get('topic', folder.name)} — {meta.get('status','DRAFT')}"):
        st.write(f"**Format:** {meta.get('format','—')}")
        st.write(f"**Audience:** {meta.get('audience','—')}")
        brief = folder / "brief.md"
        if brief.exists():
            st.markdown(brief.read_text(encoding="utf-8"))
        if meta.get("status") == "DRAFT":
            st.warning("Not approved. Do not publish.")
            if st.button("Mark approved for manual upload", key=f"approve-{folder.name}"):
                meta["status"] = "APPROVED_FOR_MANUAL_UPLOAD"
                meta["approved_by_user"] = True
                meta["published"] = False
                meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
                st.rerun()
        elif meta.get("status") == "APPROVED_FOR_MANUAL_UPLOAD":
            st.success("Approved for manual upload only. This app has not uploaded anything.")
            if st.button("Revoke approval", key=f"revoke-{folder.name}"):
                meta["status"] = "DRAFT"
                meta["approved_by_user"] = False
                meta["published"] = False
                meta_path.write_text(json.dumps(meta, indent=2), encoding="utf-8")
                st.rerun()

st.caption("Safety: approval here only marks a draft as reviewed. Actual upload must be performed manually in YouTube Studio.")
