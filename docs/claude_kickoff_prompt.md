# Claude Kickoff Prompt

Use this prompt to start Claude on the first implementation phase.

```text
You are working on a Python-first legal document formatter.

Read first:
1. CLAUDE.md
2. AGENTS.md
3. docs/spec.md
4. docs/previous_works_plan.md
5. docs/prompting_guide.md
6. docs/letters_formatter_design.md

Goal for this run:
Create the historical corpus and prepare the first deterministic formatter for letters.

Source archive:
/home/bgl1/inspect_2026-20260619T124623Z-3-001

Tasks:
1. Create previous_works/.
2. Copy the 32 historical jobs into stable numbered files:
   input_001.docx, output_001.docx, report_001.md, verification_001.md, ...
3. Generate previous_works/manifest.json.
4. Preserve original job paths and original output names in the manifest.
5. Validate the initial classification from docs/previous_works_plan.md.
6. Focus only on document_type = letters.
7. Analyze letters input/output/report examples.
8. Update docs/letters_formatter_design.md with the structure you infer.
9. Implement the first Python letters formatter slice.
10. Run it on at least 3 representative letters.
11. Produce a short final report with status, test results, known gaps, and next steps.

Constraints:
- Do not modify historical outputs.
- Do not implement acts yet.
- Do not hide uncertainty. Mark needs_review.
- Preserve legal text.
- Prefer deterministic Python rules over AI.
- Keep prompts and docs compact.

Output expected:
- previous_works/ corpus
- manifest.json
- initial letters formatter script
- updated docs/letters_formatter_design.md
- verification notes for at least 3 letter examples
```
