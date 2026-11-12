# News-summary-01 entry (Python 3.13, standard library only): the summary is the
# summary.txt beside this file, and the program copies it to /output/entry.txt.
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil
import sys

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "summary.txt")
dst = os.path.join(out_dir, "entry.txt")
shutil.copyfile(src, dst)

# Fail loudly instead of submitting a bad file: the gate takes 1-2000
# UTF-8 characters that are not only white space.
text = open(dst, encoding="utf-8").read()
if not 1 <= len(text) <= 2000 or not any(c not in " \t\n\r" for c in text):
    print(f"entry.txt invalid: {len(text)} chars", file=sys.stderr)
    sys.exit(1)
