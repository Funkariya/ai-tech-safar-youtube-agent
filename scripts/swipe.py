#!/usr/bin/env python3
"""Generate structured topic-angle prompts for manual research."""
import argparse
def main():
    p=argparse.ArgumentParser()
    p.add_argument("topic")
    p.add_argument("--ideas",type=int,default=5)
    a=p.parse_args()
    angles=[
      ("Beginner walkthrough","What does a first-time user need to do?"),
      ("Comparison","What alternatives exist and what are the trade-offs?"),
      ("Mistakes","What common errors waste time or money?"),
      ("Real workflow","How does this solve a concrete task end to end?"),
      ("Limitations","Where does it fail, and who should avoid it?"),
      ("Update watch","What materially changed and what is still unchanged?"),
      ("Use-case test","Can it complete one measurable task reliably?"),
    ]
    print(f"Research angles for: {a.topic}")
    for i,(name,q) in enumerate(angles[:max(1,min(a.ideas,len(angles)))],1):
        print(f"{i}. {name}: {q}")
    print("\nResearch each angle using primary sources and record evidence. These are prompts, not trend data.")
if __name__=="__main__": main()
