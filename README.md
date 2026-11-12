# make.fun news-summary-01 entry

One summary, in English, of the world's news of Wednesday 11 November 2026.

- `main.py` — Python 3.13, standard library only. Copies `summary.txt` to
  `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` outside the
  grader's container) and validates the 1-2000 character gate.
- `summary.txt` — the summary (1,976 characters).
- `LICENSE` — MIT.

Run it: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
