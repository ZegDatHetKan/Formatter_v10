# Formatter Report – Denuncia-Querela Dolazza

**Data:** 2026-05-29  
**Script:** `_format_denuncia_dolazza.py`  
**Input:** `input.docx` (107 paragrafi)  
**Output:** `documento_ricevuto_formattato.docx` / `final.docx`  
**Template:** `Template_Vuoto.docx`  
**Categoria:** GENERICO (nessuna regola di genere applicata)

---

## Documento

Denuncia-querela per frode informatica (*vishing*) presentata da **Maura Dolazza**, rappresentata dagli **Avv. Matteo Bertocchi** e **Avv. Daiana Chiappa** del Foro di Bergamo, indirizzata alla Polizia Postale - Centro Operativo per la Sicurezza Cibernetica per la Lombardia e, per il tramite, alla Procura della Repubblica presso il Tribunale di Bergamo.

---

## Struttura applicata

| Elemento | Trattamento |
|---|---|
| Destinatario (Polizia Postale, Procura) | CENTER, bold, 16 pt |
| Norma di riferimento (artt. 333 e ss.) | CENTER, italic, 12 pt |
| Blocco espositore (dati Dolazza, nomina difensori) | JUSTIFY, 12 pt, line-spacing 1.08 |
| Ritual headings: ESPONE E DENUNCIA / FORMALE DENUNCIA-QUERELA / FORMALE ISTANZA DI PUNIZIONE | CENTER, bold, 16 pt |
| Sezioni principali (I. – V.) | LEFT, bold, 14 pt, space_before 16 pt |
| Sottosezioni (II.1 – II.7) | LEFT, bold, 14 pt, space_before 10 pt |
| Voci di elenco (a)(b)...(v), a)b)... | JUSTIFY, 12 pt, left_indent 0.5 cm |
| Elenchi bullet (- ore..., - la...) | JUSTIFY, 12 pt, left_indent 0.5 cm |
| Corpo testo | JUSTIFY, 12 pt, line-spacing 1.08 |
| Label "Si allegano al presente atto:" | LEFT, bold, 12 pt |
| Allegati 1)–9) | JUSTIFY, 12 pt, left_indent 0.5 cm |
| Luogo e data (Bergamo, lì ___) | RIGHT, bold, 12 pt |
| Blocco firma querelante | RIGHT, 12 pt (nome bold) |
| Formula autenticazione | JUSTIFY, italic, 12 pt |
| Blocco firma avvocati | RIGHT, bold, 12 pt |

---

## Interventi eseguiti

1. **En dash / em dash** → rimpiazzati con `-` (ASCII):
   - `[007]`: "Banco BPM S.p.A. – titolare" e "Numia S.p.A. –" → "-"
   - `[019]`: "Le predette operazioni – analiticamente elencate – non hanno" → "-"
   - `[064]`: "on-line — atto dispositivo modificativo" → "-"
   - `[089]`: "Allegato A – prospetto analitico" → "-"

2. **Hyperlink**: il paragrafo `[007]` conteneva la PEC `bergamo.legal@ultracert.it` in un elemento `<w:hyperlink>` XML non accessibile tramite `para.runs`. Gestito con iterazione XML diretta. Underline da hyperlink rimosso; testo preservato integralmente.

3. **OCR bracket artefacts**: nessuno trovato nel documento.

4. **Font**: Times New Roman esplicito su ogni run.

5. **Size**: esplicita su ogni run (12 pt corpo, 14 pt sezioni/sottosezioni, 16 pt titoli/rituali).

6. **keep_with_next**: applicato su tutte le intestazioni di sezione e sottosezione per evitare titoletti orfani.

7. **Bold/italic** originali preservati (nomi, date, termini tecnici *vishing*, *modus operandi*, *pattern*, *transaction monitoring*, ecc.).

---

## Verifica finale

- ✅ 107/107 paragrafi: testi corrispondenti dopo normalizzazione
- ✅ PEC email integra (hyperlink gestito)
- ✅ Nessun dash en/em nel documento output
- ✅ Nessun artefatto OCR con quadre
- ✅ Tutti i run: font=Times New Roman, size esplicita
- ✅ Firme separate dalla data
- ✅ Blocco firma a destra
- ✅ Struttura gerarchica coerente
