#!/usr/bin/env python3
"""Heuristic hook checklist score. Not a predictor of views."""
import argparse
import re

PATTERNS = {
    "specific audience or problem": r"\b(you|your|creators|business|students|developers)\b",
    "clear payoff or outcome": r"\b(how to|learn|build|save|avoid|fix|turn|create|discover)\b",
    "specificity (number or concrete detail)": r"\b\d+\b|\b(today|2026|minutes|hours|steps|tools)\b",
    "tension or contrast": r"\b(but|instead|without|stop|mistake|problem|secret|actually)\b",
}
def main():
    p = argparse.ArgumentParser()
    p.add_argument("hook", help="Opening hook text")
    args = p.parse_args()
    text = args.hook.strip()
    score = 0
    print(f"Hook: {text}\n")
    for label, pattern in PATTERNS.items():
        passed = bool(re.search(pattern, text, re.I))
        score += int(passed)
        print(f"[{'x' if passed else ' '}] {label}")
    words = len(text.split())
    length_ok = 6 <= words <= 35
    score += int(length_ok)
    print(f"[{'x' if length_ok else ' '}] concise opening (6–35 words; found {words})")
    print(f"\nHeuristic checklist: {score}/5 — use editorial judgment; this is not a performance forecast.")
if __name__ == "__main__":
    main()
