#!/usr/bin/env python3
"""Generate title directions from a topic; review before use."""
import argparse
def main():
    p = argparse.ArgumentParser()
    p.add_argument("topic")
    args = p.parse_args()
    t = args.topic.strip().rstrip(".")
    if not t:
        p.error("Topic cannot be empty")
    print("TITLE DIRECTIONS (drafts — verify the promise)")
    for title in [
        f"{t}: What Actually Works in 2026",
        f"How to Use {t} (Step-by-Step Guide)",
        f"{t}: 5 Things to Know Before You Start",
        f"I Tested {t}: The Useful Parts and the Limits",
        f"{t} Explained: Features, Workflow and Real-World Uses",
    ]:
        print(f"- {title}")
    print("\nChoose the title that accurately matches the finished video. Do not claim testing unless testing was performed.")
if __name__ == "__main__":
    main()
