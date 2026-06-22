#!/usr/bin/env python3
"""Build a colored document anatomy HTML page from a tool profile."""

from __future__ import annotations

import argparse
import html
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


TOOL_ROOT = Path(__file__).resolve().parents[1]

BASE_COLORS = {
    "page": "#ffffff",
    "ink": "#1f2933",
    "muted": "#687385",
    "border": "#cfd7e3",
}


def resolve_path(value: str) -> Path:
    path = Path(value)
    return path if path.is_absolute() else TOOL_ROOT / path


def load_profile(path: Path) -> dict[str, Any]:
    data = json.loads(path.read_text(encoding="utf-8"))
    required = ["profile_id", "title", "output_html", "output_report", "blocks", "legend", "rules"]
    missing = [key for key in required if key not in data]
    if missing:
        raise SystemExit(f"missing required profile keys: {', '.join(missing)}")
    return data


def css_vars(colors: dict[str, str]) -> str:
    merged = {**BASE_COLORS, **colors}
    return "\n".join(f"  --{key}: {value};" for key, value in merged.items())


def style_for_kind(kind: str) -> str:
    common = f"background: var(--{kind});"
    if kind == "template":
        return common + " text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: 14px; color: #334155;"
    if kind in {"delivery", "date", "closing", "signature"}:
        return common + " text-align: right;"
    if kind in {"recipient", "party"}:
        return common + " margin-left: 34%;"
    if kind in {"court", "title", "section"}:
        return common + " text-align: center; font-weight: 700; font-size: 20px;"
    if kind == "subsection":
        return common + " font-weight: 700;"
    if kind in {"list", "claim", "exhibit"}:
        return common + " text-align: justify; padding-left: 26px;"
    return common + " text-align: justify;"


def render_css(profile: dict[str, Any]) -> str:
    kinds = {item["kind"] for item in profile["legend"]} | {item["kind"] for item in profile["blocks"]}
    kind_rules = "\n".join(f".{kind} {{ {style_for_kind(kind)} }}" for kind in sorted(kinds))
    min_height = int(profile.get("page", {}).get("min_height_px", 920))
    return f"""
:root {{
{css_vars(profile.get("colors", {}))}
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0;
  color: var(--ink);
  background: #f4f6f8;
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.45;
}}
main {{
  max-width: 1180px;
  margin: 0 auto;
  padding: 32px 24px 48px;
}}
h1 {{
  margin: 0 0 8px;
  font-size: 28px;
  font-weight: 700;
  letter-spacing: 0;
}}
h2 {{
  margin: 28px 0 12px;
  font-size: 18px;
  letter-spacing: 0;
}}
p {{
  margin: 0 0 14px;
  color: var(--muted);
  max-width: 860px;
}}
.layout {{
  display: grid;
  grid-template-columns: minmax(360px, 740px) minmax(260px, 1fr);
  gap: 24px;
  align-items: start;
}}
.page {{
  background: var(--page);
  border: 1px solid var(--border);
  box-shadow: 0 10px 24px rgba(31, 41, 51, 0.08);
  min-height: {min_height}px;
  padding: 22px;
}}
.doc-block {{
  border: 1px solid rgba(31, 41, 51, 0.18);
  border-radius: 6px;
  padding: 10px 12px;
  margin: 8px 0;
  font-family: "Times New Roman", Times, serif;
  font-size: 16px;
}}
{kind_rules}
.subject-label {{ font-size: 20px; }}
.legend {{
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 16px;
  position: sticky;
  top: 16px;
}}
.legend-row {{
  display: grid;
  grid-template-columns: 22px 1fr;
  gap: 10px;
  align-items: start;
  margin: 10px 0;
  font-size: 14px;
}}
.swatch {{
  width: 22px;
  height: 22px;
  border-radius: 4px;
  border: 1px solid rgba(31, 41, 51, 0.18);
}}
.rules, .questions {{
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
  gap: 14px;
  margin-top: 18px;
}}
.rule, .question {{
  background: #ffffff;
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 14px;
}}
.rule strong, .question strong {{
  display: block;
  margin-bottom: 6px;
}}
code {{
  background: #eef2f6;
  border: 1px solid #d8e0eb;
  border-radius: 4px;
  padding: 1px 4px;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: 0.92em;
}}
@media (max-width: 860px) {{
  main {{ padding: 20px 14px 36px; }}
  .layout {{ grid-template-columns: 1fr; }}
  .legend {{ position: static; }}
  .page {{ padding: 14px; min-height: auto; }}
  .recipient, .party {{ margin-left: 20%; }}
}}
""".strip()


def render_html(profile: dict[str, Any], profile_path: Path) -> str:
    blocks = "\n".join(
        f'        <div class="doc-block {html.escape(item["kind"])}">{item["sample"]}</div>'
        for item in profile["blocks"]
    )
    legend = "\n".join(
        f'        <div class="legend-row"><span class="swatch {html.escape(item["kind"])}"></span>'
        f'<span><strong>{html.escape(item["label"])}</strong><br>{item["description"]}</span></div>'
        for item in profile["legend"]
    )
    rules = "\n".join(
        f'      <div class="rule"><strong>{html.escape(item["label"])}</strong>{item["text"]}</div>'
        for item in profile["rules"]
    )
    questions = "\n".join(
        f'      <div class="question"><strong>Domanda {i}</strong>{html.escape(question)}</div>'
        for i, question in enumerate(profile.get("acceptance_questions", []), start=1)
    )
    questions_section = ""
    if questions:
        questions_section = f"""
    <h2>Domande di conferma</h2>
    <div class="questions">
{questions}
    </div>"""
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    page_label = html.escape(profile.get("page", {}).get("label", "Schema colorato"))
    return f"""<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(profile["title"])}</title>
  <style>
{render_css(profile)}
  </style>
</head>
<body>
  <!-- Generated by tool/scripts/build_anatomy_html.py from {html.escape(str(profile_path))} at {generated}. -->
  <main>
    <h1>{html.escape(profile["title"])}</h1>
    <p>{profile.get("intro", "")}</p>
    <div class="layout">
      <section class="page" aria-label="{page_label}">
{blocks}
      </section>
      <aside class="legend" aria-label="Legenda blocchi">
        <h2>Legenda</h2>
{legend}
      </aside>
    </div>
    <h2>Pipeline deterministica</h2>
    <div class="rules">
{rules}
    </div>{questions_section}
  </main>
</body>
</html>
"""


def render_report(profile: dict[str, Any], profile_path: Path) -> str:
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    sources = "\n".join(f"- `{item}`" for item in profile.get("source_of_truth", [])) or "- none"
    block_lines = "\n".join(
        f"- {item['kind']}: {html.escape(item['sample'])[:90]}" for item in profile["blocks"]
    )
    question_lines = "\n".join(
        f"- {question}" for question in profile.get("acceptance_questions", [])
    ) or "- none"
    return f"""# Document Anatomy Report

- generated_at: {generated}
- script: `tool/scripts/build_anatomy_html.py`
- profile: `{profile_path}`
- profile_id: `{profile["profile_id"]}`
- client: {profile.get("client", "unknown")}
- document_family: {profile.get("document_family", "unknown")}
- output: `{profile["output_html"]}`

## Source Of Truth

{sources}

## Tool / Formatter Boundary

- This report was produced by the format-definition tool.
- It is a preparation artifact, not a production formatter output.
- Once confirmed, the profile can be handed to `formatters/` for implementation.

## What changed

- Wrote the colored HTML anatomy page.
- Preserved historical input/output files.
- Did not run a production formatter or alter corpus/reference files.

## Blocks rendered

{block_lines}

## Client confirmation questions

{question_lines}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", help="Path to a tool/profiles/*.json file")
    args = parser.parse_args()

    profile_path = Path(args.profile).resolve()
    profile = load_profile(profile_path)
    output_html = resolve_path(profile["output_html"])
    output_report = resolve_path(profile["output_report"])
    output_html.parent.mkdir(parents=True, exist_ok=True)
    output_report.parent.mkdir(parents=True, exist_ok=True)
    output_html.write_text(render_html(profile, profile_path), encoding="utf-8")
    output_report.write_text(render_report(profile, profile_path), encoding="utf-8")
    print(f"wrote {output_html}")
    print(f"wrote {output_report}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
