#!/usr/bin/env python3
"""Flag long gaps in timestamped subtitle/transcript files (SRT or VTT)."""
import argparse, re
from pathlib import Path
TIME = re.compile(r"(\d{2}:\d{2}:\d{2}[,.]\d{3})\s*-->\s*(\d{2}:\d{2}:\d{2}[,.]\d{3})")
def seconds(s):
    h,m,rest=s.replace(",",".").split(":")
    return int(h)*3600+int(m)*60+float(rest)
def main():
    p=argparse.ArgumentParser()
    p.add_argument("file")
    p.add_argument("--threshold",type=float,default=2.0,help="Flag gaps longer than this many seconds")
    a=p.parse_args()
    lines=Path(a.file).read_text(encoding="utf-8-sig").splitlines()
    cues=[]
    for line in lines:
        m=TIME.search(line)
        if m: cues.append((seconds(m.group(1)),seconds(m.group(2))))
    if not cues:
        p.error("No SRT/VTT timestamps found.")
    cues.sort()
    found=0
    for prev,cur in zip(cues,cues[1:]):
        gap=cur[0]-prev[1]
        if gap>a.threshold:
            print(f"Possible dead air: {prev[1]:.3f}s–{cur[0]:.3f}s ({gap:.2f}s)")
            found+=1
    print(f"\n{found} gap(s) over {a.threshold:.1f}s. Silence may be intentional; review audio.")
if __name__=="__main__": main()
