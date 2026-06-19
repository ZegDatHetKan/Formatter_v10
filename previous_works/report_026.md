# Formatter Report — Memoria di replica e istanza Colnaghi

**Data elaborazione:** 2026-05-28  
**Input:** input.docx (126 paragrafi)  
**Output:** documento_ricevuto_formattato.docx / final.docx (111 paragrafi)  
**Script:** _format_memoria_colnaghi.py  
**Template:** Template_Vuoto.docx  

---

## Documento

Memoria di replica e istanza dell'Amministratore di Sostegno (Prof.ssa Alice Melocchi)
nel procedimento R.G. n. 861/2024 V.G. davanti al Giudice Tutelare del Tribunale di Bergamo,
relativa all'Amministrazione di Sostegno di Walter Andrea Colnaghi.

---

## Operazioni eseguite

### Struttura

| Blocco | Trattamento |
|---|---|
| Paragrafi 0–6 (intestazione studio) | SALTATI: già nel template |
| Para 7 (Bergamo, 2 luglio 2026) | date_line, LEFT, 12pt, space_after=12pt |
| Para 9–14 (blocco AdS mittente) | sender, LEFT, 12pt, bold preservato |
| Para 15 (vuoto) | divider |
| Para 16–17 (Tribunale, Ufficio GT) | court_bold, LEFT, 12pt, bold forzato |
| Para 18–20 (giudice, R.G., udienza) | court_info, LEFT, 12pt |
| Para 22 (Per conoscenza:) | label_bold, LEFT, bold, 12pt |
| Para 23–27 (lista CC) | list_cc, JUSTIFY, indent 0.5cm, 12pt |
| Para 29 (OGGETTO) | oggetto, JUSTIFY, bold 12pt, keep_with_next |
| Para 31 (Ill.mo Giudice Tutelare,) | salutation, LEFT, bold 12pt, space_before=8pt |
| Para 33 (intro corpo) | body, JUSTIFY, 12pt |
| Para 35 (Premessa di metodo) | subsection_header, LEFT, bold 14pt, keep_with_next |
| Para 40 (IN FATTO) | section_header, CENTER, bold 16pt, keep_with_next |
| Para 41, 46, 54 (§ 1, 2, 3) | subsection_header, LEFT, bold 14pt, keep_with_next |
| Para 69 (IN DIRITTO) | section_header, CENTER, bold 16pt, keep_with_next |
| Para 70, 72, 78, 82, 85, 89, 93 (§ 4–10) | subsection_header, LEFT, bold 14pt, keep_with_next |
| Para 42–44, 47–67, 71, 73–77, 79–81, 83–84, 86–88, 90–96 (corpo) | body, JUSTIFY, 12pt, bold/italic preservati |
| Para 98 (RICHIESTE) | section_header, CENTER, bold 16pt, keep_with_next |
| Para 99 (intro richieste) | body, JUSTIFY, 12pt |
| Para 100–104 (a)–e)) | request_item, JUSTIFY, indent 0.5cm, 12pt |
| Para 106 (Allegati:) | label_bold, LEFT, bold 12pt |
| Para 107–109 (allegati 1–3) | exhibit_item, JUSTIFY, indent 0.5cm, 12pt |
| Para 111 (Con osservanza,) | closing, RIGHT, space_before=20pt |
| Para 113 (Prof.ssa Alice Melocchi) | sig_name, RIGHT, bold 12pt |
| Para 114–115 (ruolo + c/o studio) | sig_body, RIGHT, 12pt |
| Para 117 (Avv. Matteo Bertocchi) | sig_name, RIGHT, bold 12pt |
| Para 118 ((firma digitale)) | sig_field, RIGHT, italic 12pt |
| Para 119–125 (vuoti + footer) | SALTATI: footer già nel template |

### Pulizia testo

- **En dash (–):** 28 occorrenze → sostituito con `-`
- **Em dash (—):** 3 occorrenze → sostituito con `-`
- **Artefatti OCR:** nessuno identificato
- **`[…]`:** PRESERVATI come omissis giuridici (citazioni letterali, non artefatti)
- **Parentesi quadre tipo `[à]`, `[l']`:** ASSENTI nel documento

### Font e size

- Font: Times New Roman esplicito su tutti i run
- Size 16pt: IN FATTO, IN DIRITTO, RICHIESTE
- Size 14pt: Premessa di metodo, § 1–10 (intestazioni numerate)
- Size 12pt: tutto il corpo
- Nessun run con size=None nell'output

### keep_with_next

Impostato su: OGGETTO, Premessa di metodo, IN FATTO, §1–10, IN DIRITTO, RICHIESTE.

---

## Verifica checklist

| Criterio | Esito |
|---|:---:|
| Contenuto giuridico preservato | ✅ |
| Template corretto | ✅ |
| Font espliciti su ogni run | ✅ |
| Size esplicite su ogni run | ✅ |
| Gerarchia visiva: 16/14/12pt | ✅ |
| Body JUSTIFY | ✅ |
| En/em dash rimossi | ✅ (0 rimasti) |
| Data e firma separate | ✅ |
| Firma RIGHT | ✅ |
| Con osservanza RIGHT | ✅ |
| Artefatti rimossi | ✅ |
| Header template integro | ✅ |
| Footer template integro | ✅ |
| Titoletti orfani (keep_with_next) | ✅ |
| Nomi, date, importi, R.G. preservati | ✅ |

