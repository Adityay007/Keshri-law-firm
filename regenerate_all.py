#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Regenerates every page of the Kesari Law Firm site from the gen_part*.py
scripts, in the correct order. Use this after editing shared chrome in
build.py (header/footer/disclaimer) or content inside any gen_part*.py file.

Usage:  python3 regenerate_all.py
"""
import subprocess
import sys

SCRIPTS = [
    "gen_part1.py",   # about.html
    "gen_part2.py",   # practice-areas.html, team.html
    "gen_part3.py",   # insights.html, contact.html
    "gen_part4.py",   # disclaimer.html, privacy-policy.html
    "gen_part5.py",   # terms-conditions.html, cookie-policy.html, accessibility-statement.html
]

if __name__ == "__main__":
    # index.html is hand-authored (not generated) and is left untouched.
    for script in SCRIPTS:
        print(f"--- running {script} ---")
        subprocess.run([sys.executable, script], check=True)
    print("\nAll pages regenerated successfully.")
