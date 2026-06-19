# Tests & Examples — Letters Formatter

## Run

The formatter needs `python-docx`; use the project venv:

```bash
WebApp/.venv/bin/python -m pytest tests/test_letters.py -q
```

## What the suite covers

`tests/test_letters.py`:

- **Unit** — `normalize()` (dash/space/zero-width), `strip_letterhead()`.
- **Contract** (must always hold):
  - runs and produces a valid `.docx`;
  - template letterhead (header + logo) and margins (5.91/4.54/2.0/2.0 cm) preserved;
  - every run is Times New Roman with an explicit size;
  - no `–`/`—` in output;
  - text preserved (no content token lost beyond letterhead);
  - OGGETTO on a single, non-centered paragraph (regression guard for feedback 027/009);
  - recipient block at `left_indent 8.5 cm`; date and signature right-aligned;
  - placeholders → `needs_review`; clean letter not flagged;
  - single-paragraph (`\n`-separated) input still segmented;
  - missing OGGETTO → `needs_review`.
- **Known issues** (`xfail`, from feedback — see `docs/feedback_review_lettere.md`):
  - `I1` OGGETTO content must be 12 pt;
  - `I2` studio partner lines after the header must be stripped;
  - `I3` isolated honorific must merge with the name line.
  These XFAIL today and will XPASS once fixed — a built-in fix tracker.

## Example letters

`tests/make_examples.py` writes 5 synthetic raw letters to `examples/` (not from the
historical corpus). Regenerate and format them with:

```bash
V=WebApp/.venv/bin/python
$V tests/make_examples.py
for f in examples/esempio_*.docx; do
  $V format_document.py --mode letters --input "$f" \
     --output "out/examples/$(basename "$f")"
done
```

| Example | Exercises |
|---|---|
| `esempio_1_diffida` | letterhead strip, Fatto/Diritto, `(i)(ii)`, DIFFIDA, allegati |
| `esempio_2_pec` | delivery RIGHT, recipient, OGGETTO inline, studio signature |
| `esempio_3_comunicazione` | single-paragraph input, greeting, bullet list, no placeholders |
| `esempio_4_riscontro` | typed-letterhead strip, isolated honorific (I3), closing RIGHT |
| `esempio_5_recesso` | raccomandata, numbered, ritual title RECEDE, placeholders |

Outputs and per-file reports land in `out/examples/`.
