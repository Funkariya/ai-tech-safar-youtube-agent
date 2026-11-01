#!/usr/bin/env python3
"""Summarize a simple CSV with timestamp and retention columns."""
import argparse, csv
from pathlib import Path
def main():
    p=argparse.ArgumentParser()
    p.add_argument("csv_file")
    p.add_argument("--time-column",default="timestamp")
    p.add_argument("--value-column",default="retention")
    p.add_argument("--baseline",type=float,default=100.0)
    a=p.parse_args()
    with Path(a.csv_file).open(newline="",encoding="utf-8-sig") as f:
        rows=list(csv.DictReader(f))
    if not rows: p.error("CSV is empty.")
    try: points=[(r[a.time_column],float(r[a.value_column])) for r in rows]
    except (KeyError,ValueError) as e: p.error(f"Check column names and numeric retention values: {e}")
    points.sort(key=lambda x:x[0])
    print(f"Rows: {len(points)} | First: {points[0][1]:.1f} | Last: {points[-1][1]:.1f}")
    drops=sorted(((points[i-1][1]-points[i][1],points[i][0],points[i-1][0]) for i in range(1,len(points))),reverse=True)
    print("\nLargest adjacent drops:")
    for amount,t,prev in drops[:10]:
        print(f"- {prev} -> {t}: drop {amount:.1f} points")
    print("\nThis is descriptive only. Export column formats vary; confirm units and timestamps before interpreting.")
if __name__=="__main__": main()
