# Formatter Report — Esposizione fatti e norme mediazione

**Data:** 2026-06-09  
**Input:** input.docx  
**Output:** documento_ricevuto_formattato.docx / final.docx  
**Genere:** GENERICO (Esposizione dei fatti e riferimenti normativi per mediazione)  
**Script:** _format_esposizione.py  

---

## Struttura rilevata

| Para | Tipo | Trattamento applicato |
|------|------|-----------------------|
| 0 | Titolo principale | CENTER, 16pt, bold, TNR |
| 1 | Sottotitolo parentetico | CENTER, 16pt, bold+italic (preservato italic sorgente), TNR |
| 2 | Vuoto | Omesso (spaziatura gestita da space_after) |
| 3 | Titoletto I. I FATTI | LEFT, 14pt, bold, keep_with_next |
| 4–9 | Corpo numerato (I FATTI, punti 1–6) | JUSTIFY, 12pt, bold/italic originali preservati |
| 10 | Titoletto II. ACCENNI NORMATIVI | LEFT, 14pt, bold, keep_with_next |
| 11–15 | Corpo numerato (ACCENNI NORMATIVI, punti 7–11) | JUSTIFY, 12pt, bold/italic originali preservati |
| 16 | Titoletto III. ALLEGATI | LEFT, 14pt, bold, keep_with_next |
| 17–20 | Voci allegato (All. 1–4) | LEFT, 12pt, indent 0.5cm |
| 21 | Vuoto | Omesso |
| 22 | Disclaimer finale | CENTER, 10pt, italic |

---

## Interventi tipografici effettuati

1. **En dash / em dash → trattino** (HARD_004B): sostituiti tutti `–` e `—` con `-` in tutti i paragrafi.
2. **Spaziatura verticale**: `space_before`/`space_after` coerenti con STYLE_011; paragrafi vuoti omessi.
3. **Font e size espliciti**: `Times New Roman`, size esplicita su ogni run (HARD_003).
4. **keep_with_next** su tutti i titoletti (HARD_007) per evitare titoli orfani.
5. **Disclaimer finale**: 10pt italic CENTER, con `space_before=14pt` per separazione visiva.

## Contenuto

Nessuna modifica al contenuto giuridico sostanziale. Tutte le date, importi, nomi, riferimenti normativi, codici allegato e marker `[VERIFICA]` preservati integralmente.

## Note di stile

- Il sottotitolo parentetico (para 1) è bold+italic: la micro-scelta preserva l'italic semantico del sorgente (segnala natura descrittiva/parentetica), mantenendo la dimensione 16pt richiesta per titoli centrali.
- I `[VERIFICA su DeJure/Italgiure]` e `[VERIFICA estremi]` nel corpo sono annotazioni editoriali intenzionali, non artefatti OCR: conservati.
- Nessun blocco firma/data nel documento (è un allegato tecnico): non applicabile HARD_005.

---

**Verifiche automatiche:** font ✓ | size ✓ | allineamenti ✓ | en/em dash ✓ | contenuto ✓ | issues: 0
