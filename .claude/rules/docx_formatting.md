---
paths:
  - "**/*.docx"
  - "**/*formatter*.py"
  - "**/formatters/**/*.py"
  - "**/common/**/*.py"
---

# DOCX Formatting Rules

- Preserve legal text content and ordering unless explicitly instructed otherwise.
- Formatting scripts may change paragraph boundaries, styles, alignment, indentation, spacing, margins, and section layout.
- Avoid duplicating header/footer content already present in the template.
- Detect and report placeholders such as `[DA INSERIRE: ...]`; do not invent missing values.
- Treat object lines, recipient blocks, delivery channels, and signature blocks as first-class structures.
- Every generated document must have a companion report.
