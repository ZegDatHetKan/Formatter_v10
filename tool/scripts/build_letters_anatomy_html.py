#!/usr/bin/env python3
"""Build the rich Bergamo Legal letters anatomy page.

This page is the visual confirmation artifact for the work documented in:
- previous_works/manifest.json
- docs/letters_formatter_design.md
- docs/feedback_review_lettere.md
- tests/make_examples.py
- formatters/letters.py
"""

from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path


TOOL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = TOOL_ROOT.parent
OUT = TOOL_ROOT / "output" / "html" / "lettera_anatomia_colori.html"
REPORT = TOOL_ROOT / "output" / "reports" / "lettera_anatomia_colori_report.md"


CSS = """
:root {
  --ink: #1f2933;
  --muted: #667085;
  --line: #cfd7e3;
  --paper: #ffffff;
  --bg: #f4f6f8;
  --template: #e8eef7;
  --delivery: #d7f3ec;
  --date: #fff0bf;
  --recipient: #fde1d9;
  --subject: #dfe5ff;
  --opening: #efe3ff;
  --body: #eef7df;
  --section-left: #f7e6c6;
  --section-center: #ffd9e8;
  --numbered: #d8ecff;
  --enum: #dff7ff;
  --closing: #ffe5c8;
  --attachments: #e2e3e5;
  --warning: #f5d0fe;
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--bg);
  color: var(--ink);
  font-family: Arial, Helvetica, sans-serif;
  line-height: 1.45;
}
main {
  max-width: 1320px;
  margin: 0 auto;
  padding: 28px 24px 48px;
}
h1 {
  margin: 0 0 8px;
  font-size: 30px;
  letter-spacing: 0;
}
h2 {
  margin: 30px 0 12px;
  font-size: 19px;
  letter-spacing: 0;
}
h3 {
  margin: 0 0 8px;
  font-size: 15px;
  letter-spacing: 0;
}
p {
  margin: 0 0 12px;
  color: var(--muted);
}
code {
  padding: 1px 4px;
  border: 1px solid #d8e0eb;
  border-radius: 4px;
  background: #eef2f6;
  font-family: ui-monospace, SFMono-Regular, Menlo, Consolas, monospace;
  font-size: .92em;
}
.top-grid, .rules-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 14px;
}
.panel {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 14px;
}
.panel ul {
  margin: 8px 0 0;
  padding-left: 18px;
}
.workspace {
  display: grid;
  grid-template-columns: minmax(420px, 760px) minmax(340px, 1fr);
  gap: 22px;
  align-items: start;
}
.letter-page {
  min-height: 1080px;
  border: 1px solid var(--line);
  background: var(--paper);
  box-shadow: 0 12px 28px rgba(31,41,51,.09);
  padding: 24px;
}
.doc-block {
  border: 1px solid rgba(31,41,51,.22);
  border-radius: 6px;
  padding: 8px 10px;
  margin: 7px 0;
  font-family: "Times New Roman", Times, serif;
  font-size: 15px;
}
.template { background: var(--template); text-align: center; font-family: Arial, Helvetica, sans-serif; font-size: 13px; color: #334155; }
.delivery { background: var(--delivery); text-align: right; font-style: italic; }
.date { background: var(--date); text-align: right; }
.recipient { background: var(--recipient); margin-left: 42%; text-align: left; }
.subject { background: var(--subject); text-align: justify; }
.opening { background: var(--opening); text-align: justify; }
.body { background: var(--body); text-align: justify; }
.section-left { background: var(--section-left); font-weight: 700; }
.section-center { background: var(--section-center); text-align: center; font-weight: 700; font-size: 19px; }
.numbered { background: var(--numbered); text-align: justify; }
.enum { background: var(--enum); text-align: justify; padding-left: 28px; }
.closing { background: var(--closing); text-align: right; }
.attachments { background: var(--attachments); text-align: left; }
.warning { background: var(--warning); }
.legend {
  position: sticky;
  top: 14px;
}
.legend-row {
  display: grid;
  grid-template-columns: 22px 1fr;
  gap: 10px;
  align-items: start;
  padding: 8px 0;
  border-bottom: 1px solid #edf1f5;
  font-size: 14px;
}
.legend-row:last-child { border-bottom: 0; }
.swatch {
  width: 22px;
  height: 22px;
  border: 1px solid rgba(31,41,51,.22);
  border-radius: 4px;
}
.style-table {
  width: 100%;
  border-collapse: collapse;
  background: var(--paper);
  border: 1px solid var(--line);
}
.style-table th, .style-table td {
  border-bottom: 1px solid #e5ebf2;
  padding: 9px 10px;
  text-align: left;
  vertical-align: top;
  font-size: 14px;
}
.style-table th {
  background: #eef2f6;
}
.flow {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(170px, 1fr));
  gap: 10px;
}
.step {
  border: 1px solid var(--line);
  border-radius: 8px;
  background: var(--paper);
  padding: 12px;
  min-height: 92px;
}
.step strong { display: block; margin-bottom: 5px; }
@media (max-width: 980px) {
  main { padding: 18px 12px 36px; }
  .workspace { grid-template-columns: 1fr; }
  .legend { position: static; }
  .recipient { margin-left: 22%; }
}
""".strip()


LEGEND = [
    ("template", "template_header/footer", "Da Template_Vuoto.docx. Header, footer, logo e margini non sono ricreati dall'AI."),
    ("delivery", "delivery_method", "Riconosciuto prima del destinatario. RIGHT, italic, 12 pt."),
    ("date", "date_place", "Luogo/data breve. RIGHT, 12 pt."),
    ("recipient", "recipient_block", "Preambolo prima di OGGETTO. Rientro sinistro 8.5 cm; onorifico isolato fuso col nome."),
    ("subject", "subject_line", "Ancora strutturale. Etichetta Oggetto 16 pt bold + contenuto 12 pt bold, stesso paragrafo, JUSTIFY."),
    ("opening", "opening", "Prima riga del corpo se formula di saluto. JUSTIFY, 12 pt."),
    ("body", "body_paragraph", "Default del corpo. Times New Roman 12 pt, JUSTIFY, space_after 6 pt."),
    ("section-left", "section_left", "Titoletto tipo Fatto/Diritto. LEFT, 14 pt bold, keep_with_next."),
    ("section-center", "section_center", "Titolo rituale tipo DIFFIDA/INVITA. CENTER, 16 pt bold, keep_with_next/together."),
    ("numbered", "numbered", "Paragrafi 1. / 1.1. JUSTIFY 12 pt, prefisso numero in bold."),
    ("enum", "enum_item / bullet_item", "Elementi (i), (ii), a), bullet. JUSTIFY, rientro 0.5 cm."),
    ("closing", "closing_signature", "Chiusura e firme finali. RIGHT 12 pt; nome avvocato in bold."),
    ("attachments", "attachments", "Allegati e All. N. Label bold, item con rientro controllato."),
    ("warning", "needs_review", "Placeholder o blocchi non coperti. Meglio review esplicita che output sbagliato silenzioso."),
]


def swatch(kind: str) -> str:
    return f'<span class="swatch {kind}"></span>'


def render_legend() -> str:
    rows = []
    for kind, label, desc in LEGEND:
        rows.append(
            f'<div class="legend-row">{swatch(kind)}<span><strong>{label}</strong><br>{desc}</span></div>'
        )
    return "\n".join(rows)


def render_html() -> str:
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return f"""<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Bergamo Legal - anatomia lettera</title>
  <style>
{CSS}
  </style>
</head>
<body>
<main>
  <h1>Bergamo Legal - anatomia della lettera</h1>
  <p>
    Artefatto di conferma generato dal processo documentato: corpus storico classificato,
    lettere isolate, blocchi semantici estratti, formatter Python deterministico e lettera
    fittizia riprodotta con legenda.
  </p>

  <section class="top-grid" aria-label="Fonti e stato">
    <div class="panel">
      <h3>Fonti usate</h3>
      <ul>
        <li><code>previous_works/manifest.json</code></li>
        <li><code>docs/letters_formatter_design.md</code></li>
        <li><code>docs/feedback_review_lettere.md</code></li>
        <li><code>formatters/letters.py</code></li>
        <li><code>tests/make_examples.py</code></li>
      </ul>
    </div>
    <div class="panel">
      <h3>Corpus classificato</h3>
      <p>32 documenti storici: <strong>15 lettere</strong>, <strong>14 atti</strong>, <strong>3 other_pending_name</strong>.</p>
      <p>Lettere: <code>001 002 003 004 005 007 010 011 013 015 025 027 028 029 032</code>.</p>
    </div>
    <div class="panel">
      <h3>Stato formatter</h3>
      <p>Prima slice deterministica: gira su tutte le 15 lettere senza errori. Output in <code>out/output_*.docx</code>.</p>
      <p>Le reference storiche in <code>previous_works/</code> non vengono sovrascritte.</p>
    </div>
  </section>

  <h2>Lettera fittizia scomposta in blocchi</h2>
  <div class="workspace">
    <section class="letter-page" aria-label="Lettera fittizia sezionata">
      <div class="doc-block template">HEADER TEMPLATE: logo, BERGAMO LEGAL, soci, recapiti alti</div>
      <div class="doc-block delivery">A mezzo Raccomandata A/R, anticipata via email</div>
      <div class="doc-block date">Bergamo, lì [DA INSERIRE: data]</div>
      <div class="doc-block recipient"><strong>Spett.le Beta Costruzioni S.r.l.</strong><br>Via Roma, 12 - 24100 Bergamo (BG)<br>PEC: beta.costruzioni@pec.it</div>
      <div class="doc-block subject"><strong style="font-size:20px">OGGETTO:</strong> <strong>Diffida ad adempiere - pagamento fatture insolute n. 14/2026 e n. 21/2026</strong></div>
      <div class="doc-block opening">Egregi Signori,</div>
      <div class="doc-block body">lo Studio scrivente agisce in nome e per conto della Alfa S.p.A. in relazione ai fatti che seguono.</div>
      <div class="doc-block section-left">Fatto</div>
      <div class="doc-block numbered"><strong>1.</strong> In data 3 marzo 2026 la Alfa S.p.A. emetteva regolare fattura n. 14/2026 per l'importo di Euro 12.500,00.</div>
      <div class="doc-block numbered"><strong>2.</strong> Nonostante i solleciti, la S.V. non ha provveduto al pagamento delle seguenti fatture:</div>
      <div class="doc-block enum"><strong>(i)</strong> fattura n. 14/2026, scaduta il 2 aprile 2026;</div>
      <div class="doc-block enum"><strong>(ii)</strong> fattura n. 21/2026, scaduta il 30 aprile 2026.</div>
      <div class="doc-block section-left">Diritto</div>
      <div class="doc-block numbered"><strong>3.</strong> L'inadempimento integra una grave violazione degli artt. 1218 e 1453 c.c.</div>
      <div class="doc-block body">Tutto ciò premesso e considerato, lo Studio scrivente</div>
      <div class="doc-block section-center">DIFFIDA</div>
      <div class="doc-block body">la S.V., come sopra individuata, a voler provvedere entro 15 giorni al pagamento di quanto dovuto.</div>
      <div class="doc-block body">In difetto, si procederà nelle competenti sedi giudiziarie con aggravio di spese.</div>
      <div class="doc-block closing">In attesa di un cortese e sollecito riscontro, si porgono distinti saluti.<br><strong>Avv. Matteo Bertocchi</strong><br><strong>Avv. Daiana Chiappa</strong></div>
      <div class="doc-block attachments"><strong>Allegati:</strong><br>All. 1 - copia fattura n. 14/2026;<br>All. 2 - copia fattura n. 21/2026.</div>
      <div class="doc-block warning">needs_review: placeholder [DA INSERIRE: data] presente; compilazione manuale richiesta.</div>
      <div class="doc-block template">FOOTER TEMPLATE: R.E.A., P.IVA, indirizzi, contatti</div>
    </section>

    <aside class="panel legend" aria-label="Legenda tecnica">
      <h2>Legenda</h2>
{render_legend()}
    </aside>
  </div>

  <h2>Regole confermate per il formatter</h2>
  <table class="style-table">
    <thead>
      <tr><th>Area</th><th>Regola deterministica</th><th>Dove vive nel codice</th></tr>
    </thead>
    <tbody>
      <tr><td>Template</td><td>A4, header/footer/logo e margini: top 5.91 cm, bottom 4.54 cm, left/right 2.0 cm.</td><td><code>assets/Template_Vuoto.docx</code></td></tr>
      <tr><td>Classificazione</td><td><code>OGGETTO:</code> divide preambolo e corpo; prima: delivery/data/destinatario; dopo: body/sezioni/firma/allegati.</td><td><code>classify()</code></td></tr>
      <tr><td>Normalizzazione</td><td>Trattini lunghi a <code>-</code>, nbsp/zero-width rimossi, spazi collassati, paragrafi vuoti eliminati.</td><td><code>normalize()</code></td></tr>
      <tr><td>Letterhead duplicato</td><td>Righe studio in testa rimosse, incluse righe soci <code>Avv.</code>; firma finale preservata.</td><td><code>strip_letterhead()</code></td></tr>
      <tr><td>Oggetto</td><td>Un solo paragrafo: label 16 pt bold, contenuto 12 pt bold, JUSTIFY, keep_with_next.</td><td><code>emit()</code> subject branch</td></tr>
      <tr><td>Review</td><td>Placeholder <code>[...]</code> conservati, bold, e <code>needs_review=true</code>.</td><td><code>Report</code> + renderer</td></tr>
    </tbody>
  </table>

  <h2>Pipeline ripetibile</h2>
  <section class="flow">
    <div class="step"><strong>1. Corpus</strong>Creare <code>previous_works/</code>, assegnare ID stabili, preservare nomi originali.</div>
    <div class="step"><strong>2. Classificazione</strong>Separare <code>letters</code>, <code>acts</code>, <code>other_pending_name</code> nel manifest.</div>
    <div class="step"><strong>3. Anatomia</strong>Misurare output storici: testo, paragrafi, stili, margini, rientri, spaziature.</div>
    <div class="step"><strong>4. Regole</strong>Codificare in Python solo pattern stabili; incertezza a <code>needs_review</code>.</div>
    <div class="step"><strong>5. Esempi fittizi</strong>Generare input sintetici con casi rappresentativi e formatter deterministicamente.</div>
    <div class="step"><strong>6. Report</strong>Produrre DOCX + report per ogni run, poi HTML di conferma con legenda.</div>
  </section>

  <h2>Output collegati</h2>
  <section class="rules-grid">
    <div class="panel"><h3>Script</h3><p><code>formatters/letters.py</code><br><code>format_document.py --mode letters</code></p></div>
    <div class="panel"><h3>Esempi</h3><p><code>tests/make_examples.py</code><br><code>out/examples/esempio_1_diffida.docx</code></p></div>
    <div class="panel"><h3>Report</h3><p><code>out/examples/esempio_1_diffida_report.md</code><br><code>out/RUN_REPORT.md</code></p></div>
  </section>

  <p style="margin-top:28px">Generato da <code>tool/scripts/build_letters_anatomy_html.py</code> il {generated}.</p>
</main>
</body>
</html>
"""


def render_report() -> str:
    generated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    return f"""# Rich Letters Anatomy Report

- generated_at: {generated}
- script: `tool/scripts/build_letters_anatomy_html.py`
- output: `tool/output/html/lettera_anatomia_colori.html`
- purpose: visual confirmation artifact for the documented Bergamo Legal letters process

## Inputs represented

- `previous_works/manifest.json`: 32 historical jobs, 15 letters
- `docs/letters_formatter_design.md`: semantic block grammar and style rules
- `docs/feedback_review_lettere.md`: feedback review and anatomy
- `tests/make_examples.py`: synthetic example letters
- `formatters/letters.py`: deterministic formatter implementation

## What this page shows

- corpus classification summary
- a synthetic diffida letter split into semantic blocks
- a technical legend mapping colors to formatter blocks
- confirmed style/layout rules
- repeatable pipeline for future document families
"""


def main() -> int:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render_html(), encoding="utf-8")
    REPORT.write_text(render_report(), encoding="utf-8")
    print(f"wrote {OUT.relative_to(REPO_ROOT)}")
    print(f"wrote {REPORT.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
