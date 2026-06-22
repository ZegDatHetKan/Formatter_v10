#!/usr/bin/env python3
"""Compatibility wrapper for the Bergamo Legal letters anatomy page."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / "tool" / "profiles" / "bergamo_legal_letters.json"
BUILDER = ROOT / "tool" / "scripts" / "build_anatomy_html.py"


def main() -> int:
    return subprocess.call([sys.executable, str(BUILDER), str(PROFILE)])


if __name__ == "__main__":
    raise SystemExit(main())
