#!/usr/bin/env python3
"""CLI entry point for the Python-first legal formatter.

Only `letters` is implemented in this slice.

Usage:
    python format_document.py --mode letters --input in.docx --output out.docx
"""
from __future__ import annotations

import argparse
from pathlib import Path

from formatters import letters


def main() -> None:
    ap = argparse.ArgumentParser(description="Legal document formatter")
    ap.add_argument("--mode", required=True, choices=["letters"],
                    help="document family (only 'letters' implemented)")
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=True)
    ap.add_argument("--template", default=None)
    ap.add_argument("--report", default=None, help="path for the markdown report")
    args = ap.parse_args()

    rep = letters.format_letter(args.input, args.output, args.template)
    report_path = args.report or (Path(args.output).with_suffix("").as_posix()
                                  + "_report.md")
    Path(report_path).write_text(letters.render_report(rep), encoding="utf-8")
    print(f"OK mode={args.mode} -> {args.output}")
    print(f"   report={report_path}  needs_review={rep.needs_review}  "
          f"blocks={len(rep.blocks)}")


if __name__ == "__main__":
    main()
