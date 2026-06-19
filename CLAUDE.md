# Claude Project Instructions

This project is the planning and implementation workspace for a Python-first legal document formatter.

Read these files first, in order:

1. `AGENTS.md`
2. `docs/spec.md`
3. `docs/previous_works_plan.md`
4. `docs/prompting_guide.md`
5. `docs/claude_kickoff_prompt.md`

Current objective: prepare the historical corpus and build the first deterministic Python formatter for `letters`.

Important constraints:

- Do not modify historical job outputs. Treat them as reference artifacts.
- Do not start implementing `acts` or the third document family until `letters` has a working baseline.
- Keep instructions, scripts, and reports concise and verifiable.
- Prefer deterministic Python over AI generation whenever a rule can be encoded.
- Use AI only for classification, ambiguous structure inference, fallback formatting, and script adaptation.

Historical source archive:

- Remote source: `/home/bgl1/inspect_2026-20260619T124623Z-3-001`
- Expected local corpus: `previous_works/`

Claude Code note:

- `CLAUDE.md` is the entrypoint for Claude Code.
- `AGENTS.md` contains shared agent workflow rules.
- `.claude/rules/` contains focused rules.
- `.claude/agents/` contains specialized subagent definitions.
