# Prompting Guide for Formatter Agents

This guide defines how to write prompts and agent instructions for the legal formatter project.

It is based on one principle: precision beats polish. A good prompt is short, structured, and testable. Every word should carry information the model needs.

## Minimum Viable Prompt

Before sending a prompt, ask:

> Does every word help the model produce the correct output?

If not, cut it.

Avoid greetings, apologies, social padding, and vague requests. The model does not need polite prose. It needs context, task, constraints, and output format.

## Intention To Prompt Pipeline

Do not transcribe raw intention directly.

Use this pipeline:

```text
Raw intention -> decomposed problem -> structured prompt
```

Example:

```text
Raw intention:
I want Claude to understand whether this legal document is a letter or an act.

Decomposed problem:
- Input: extracted text from a legal document.
- Task: classify document family.
- Constraints: choose only known labels.
- Output: JSON with label, confidence, evidence.

Structured prompt:
Classify legal document.
Labels: letters | acts | other_pending_name | unknown.
Use subject, first paragraphs, recipient, and procedural markers.
Return JSON only: label, confidence, evidence_quotes, needs_review.
```

## Four Prompt Dimensions

Use these dimensions when writing any important prompt:

- Context: environment, corpus, document family, current step.
- Task: exact action the model must perform.
- Constraints: what to preserve, avoid, or not infer.
- Output format: JSON, Markdown table, code only, report, diff summary.

If a task is complex, include all four.

## Context Economy

Treat context like expensive RAM.

- Paste only relevant excerpts, not whole files, unless full context is necessary.
- Replace boilerplate with clear placeholders.
- Restate critical project context at the top of each standalone task.
- Ask for minimal output when appropriate.
- Split tasks that need more than three sentences to describe.

## Good Sentence Patterns

Use compact technical English.

Telegram style:

```text
Legal document classification. Italian law firm. Input: first 20 paragraphs. Need family label and evidence. JSON only.
```

Spec-list style:

```text
Generate Python function:
- Input: python-docx Document
- Detect object line
- Preserve text
- Return block metadata
No file writes.
Code only.
```

Fill-in-the-blank style:

```text
Complete this formatter rule: detect [block] -> apply [style]. Use examples [ids]. Return function + tests.
```

Before/after style:

```text
Transform this extracted structure into the target docx layout. Preserve paragraph text. Change only style and paragraph boundaries.
```

## Anti-Patterns

Avoid:

- "Can you help me with..."
- "I was wondering if..."
- "Please make this better."
- "Use your best judgment" without criteria.
- "Explain everything" when code or JSON is needed.
- Asking for implementation, documentation, tests, and architecture in one prompt.
- Assuming the model remembers constraints from many turns ago.

Prefer:

- "Task: classify document."
- "Need: root cause + fix."
- "Output: JSON only."
- "Preserve: text content and original order."
- "Stop if evidence is insufficient."

## Iterative Work

For complex work, use rounds:

1. Inspect and summarize.
2. Propose structure.
3. Implement smallest useful slice.
4. Verify against examples.
5. Record gaps.

Do not ask for the entire formatter in one prompt.

## Agent Prompt Templates

### Classifier Agent

```text
Role: legal document classifier.
Context: Italian law firm formatter corpus.
Task: classify one document into letters, acts, other_pending_name, or unknown.
Input: subject, original filename, first paragraphs, optional report excerpt.
Constraints:
- Use evidence from the input.
- Do not infer beyond available text.
- Mark needs_review when confidence is low.
Output JSON:
{
  "document_type": "...",
  "confidence": "high|medium|low",
  "evidence": ["..."],
  "needs_review": true|false
}
```

### Formatter Script Agent

```text
Role: Python formatter engineer.
Context: Python-first legal document formatter using python-docx.
Task: implement one deterministic rule or one small formatter slice.
Constraints:
- Preserve legal text.
- Do not modify historical references.
- Prefer explicit warnings over silent guesses.
- Keep code testable and small.
Output: code changes + short implementation report.
```

### Verification Agent

```text
Role: formatter verification reviewer.
Context: compare generated docx with historical reference.
Task: identify differences that matter for legal formatting.
Check:
- Text preservation
- Paragraph structure
- Object line
- Recipient block
- Signature block
- Font, size, alignment, margins
Output: Markdown report with pass/fail, differences, and recommended rule updates.
```

### Feedback Ingestion

```text
Role: feedback normalizer.
Task: convert user feedback into manifest updates and rule candidates.
Input: user feedback, document id, current manifest record.
Output JSON:
{
  "feedback_notes": [],
  "known_issues": [],
  "desired_rule_change": [],
  "priority": "low|medium|high"
}
```

## Writing Agent Instructions

Agent instructions should be:

- Focused on one task.
- Specific enough to verify.
- Short enough to stay in context.
- Written in direct English.
- Clear about inputs, outputs, allowed actions, and stop conditions.

Do not mix unrelated responsibilities in one agent.

## Formatter-Specific Prompt Rules

- Always say whether historical outputs are reference-only.
- Always say whether the agent may edit files.
- Always specify the document family.
- Always require a report for formatter changes.
- Always preserve legal text unless the user explicitly asks for content edits.
- Prefer `needs_review` over hidden assumptions.
- For specialized formatters, prompt AI to extract semantic blocks only.
- Do not prompt AI to decide fonts, sizes, margins, alignment, indentation, or paragraph styling when Python has a deterministic formatter.
- Prompt outputs for extraction should be structured JSON, not prose.
- If the document contains unsupported structure, ask the model to mark `needs_review` instead of inventing layout.

## Semantic Extraction Frame

Use this frame when AI prepares input for a deterministic formatter:

```text
Task: extract semantic blocks for the letters formatter.
Context: Italian law firm document. Python owns all DOCX styling.
Input: document text.
Constraints:
- Preserve text exactly.
- Do not decide visual formatting.
- Use only allowed block kinds.
- Mark needs_review for unsupported structure.
Output: JSON only matching the schema.
```

## Future Additions

This guide will evolve as the pipeline matures. Add examples only when they improve repeatability.
