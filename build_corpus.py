#!/usr/bin/env python3
"""Build previous_works/ corpus + manifest.json from the historical source archive.

Read-only over _source/. Copies the 32 jobs into stable numbered files and
records provenance + initial classification (validated against subject/body
evidence) in previous_works/manifest.json.
"""
from __future__ import annotations

import json
import re
import shutil
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "_source" / "inspect_2026-20260619T124623Z-3-001"
DST = ROOT / "previous_works"
W_NS = "http://schemas.openxmlformats.org/wordprocessingml/2006/main"

# Initial classification from docs/previous_works_plan.md (ID -> family).
CLASSIFICATION = {
    "letters": {1, 2, 3, 4, 5, 7, 10, 11, 13, 15, 25, 27, 28, 29, 32},
    "acts": {12, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 30, 31},
    "other_pending_name": {6, 8, 9},
}
ID_TO_TYPE = {n: fam for fam, ids in CLASSIFICATION.items() for n in ids}

# Keyword heuristics used only to corroborate the plan classification.
LETTER_KW = ("lettera", "pec", "comunicazione", "diffida", "riscontro",
             "recesso", "raccomandata", "spett")
ACT_KW = ("ricorso", "istanza", "memoria", "denuncia", "querela",
          "tribunale", "giudice", "ill.mo", "ecc.mo", "prefett")
OTHER_KW = ("delega", "esposizione dei fatti", "esposizione fatti")


def docx_paragraphs(path: Path, limit: int = 6) -> list[str]:
    """Return up to `limit` non-empty paragraph texts from a .docx (stdlib only)."""
    out: list[str] = []
    try:
        with zipfile.ZipFile(path) as z:
            xml = z.read("word/document.xml")
    except (KeyError, zipfile.BadZipFile, FileNotFoundError):
        return out
    tree = ET.fromstring(xml)
    for p in tree.iter(f"{{{W_NS}}}p"):
        text = "".join(t.text or "" for t in p.iter(f"{{{W_NS}}}t")).strip()
        if text:
            out.append(text)
        if len(out) >= limit:
            break
    return out


def guess_family(subject: str, evidence: list[str]) -> str:
    blob = (subject + " " + " ".join(evidence)).lower()
    # Third-family markers are decisive only in the "title zone" (subject + first
    # paragraph): "esposizione dei fatti" / "delega" as a document title means the
    # third family, whereas the same phrase as a section heading inside an act
    # (e.g. a denuncia-querela) must not override the act classification.
    title_zone = (subject + " " + (evidence[0] if evidence else "")).lower()
    if any(k in title_zone for k in OTHER_KW):
        return "other_pending_name"
    score = {
        "acts": sum(k in blob for k in ACT_KW),
        "letters": sum(k in blob for k in LETTER_KW),
    }
    best = max(score, key=lambda f: (score[f], f != "letters"))
    return best if score[best] else "letters"


def one(glob_dir: Path, pattern: str) -> Path | None:
    hits = sorted(glob_dir.glob(pattern)) if glob_dir.is_dir() else []
    return hits[0] if hits else None


def main() -> None:
    job_dirs = sorted(p for p in SRC.glob("2026/*/*/*") if p.is_dir())
    assert len(job_dirs) == 32, f"expected 32 jobs, found {len(job_dirs)}"
    DST.mkdir(exist_ok=True)

    manifest = []
    for idx, job in enumerate(job_dirs, start=1):
        jid = f"{idx:03d}"
        rel_job = job.relative_to(SRC).as_posix()

        src_input = job / "input" / "original.docx"
        src_output = one(job / "output", "*.docx")
        src_report = one(job / "reports", "*-formatter_report.md")
        src_verif = one(job / "reports", "*-verification.md")
        subj_file = job / "workspace" / "subject.txt"
        subject = subj_file.read_text(encoding="utf-8").strip().splitlines()[0] \
            if subj_file.exists() else src_output.stem

        # Copy into stable numbered files.
        shutil.copy2(src_input, DST / f"input_{jid}.docx")
        shutil.copy2(src_output, DST / f"output_{jid}.docx")
        shutil.copy2(src_report, DST / f"report_{jid}.md")
        shutil.copy2(src_verif, DST / f"verification_{jid}.md")

        evidence = docx_paragraphs(src_input)
        plan_type = ID_TO_TYPE[idx]
        guess = guess_family(subject, evidence)
        agrees = guess == plan_type
        record = {
            "id": jid,
            "document_type": plan_type,
            "subject": subject,
            "original_job_path": rel_job,
            "original_input_name": src_input.name,
            "original_output_name": src_output.name,
            "input_path": f"previous_works/input_{jid}.docx",
            "output_path": f"previous_works/output_{jid}.docx",
            "report_path": f"previous_works/report_{jid}.md",
            "verification_path": f"previous_works/verification_{jid}.md",
            "classification_confidence": "high" if agrees else "low",
            "classification_evidence": evidence[:3],
            "heuristic_guess": guess,
            "needs_review": not agrees,
            "feedback_notes": [],
            "known_issues": [] if agrees else [
                f"plan={plan_type} but body/subject heuristic suggests {guess}"
            ],
            "desired_rule_change": [],
            "resolved_by_script": False,
        }
        manifest.append(record)

    (DST / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )

    # Console summary.
    by_type: dict[str, int] = {}
    review = []
    for r in manifest:
        by_type[r["document_type"]] = by_type.get(r["document_type"], 0) + 1
        if r["needs_review"]:
            review.append(r["id"])
    print(f"jobs: {len(manifest)}")
    print(f"by type: {by_type}")
    print(f"needs_review: {review or 'none'}")


if __name__ == "__main__":
    main()
