#!/usr/bin/env python3
"""Extract candidate chapter timestamps from SRT/VTT cue text."""
import argparse, re
from pathlib import Path
TIME=re.compile(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->")
def main():
    p=argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--every",type=int,default=60,help="Minimum seconds between candidate chapters")
    a=p.parse_args()
    lines=Path(a.file).read_text(encoding="utf-8-sig").splitlines()
    cues=[]
    for i,line in enumerate(lines):
        m=TIME.search(line)
        if m:
            stamp=m.group(1).replace(",",".")
            text=" ".join(x.strip() for x in lines[i+1:i+4] if x.strip() and not x.strip().isdigit())
            if text: cues.append((stamp,text))
    last=-a.every
    for stamp,text in cues:
        h,m,s=stamp.split(":"); sec=int(h)*3600+int(m)*60+float(s)
        if sec-last>=a.every:
            label=re.sub(r"\s+"," ",text)[:65]
            print(f"{stamp[:8]} {label}")
            last=sec
    print("\nCandidate labels only. Verify topic transitions and format timestamps as YouTube chapters (MM:SS).")
if __name__=="__main__": main()
