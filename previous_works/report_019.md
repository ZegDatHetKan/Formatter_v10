# Formatter Report - Bergamo Legal

**Data:** 2026-05-28  
**Documento:** Ricorso in opposizione a decreto di revoca della patente di guida  
**Cliente:** Campos Omar  
**Avvocato:** Avv. Matteo Bertocchi  
**Script:** `_format_ricorso_campos.py`

---

## Documento sorgente

- 8 paragrafi sorgente con righe interne separate da `\n`
- Nessun stile Word applicato (tutti "Normal"), nessun bold/italic nei runs
- Paragrafo 0: intestazione studio (già presente nel template → saltato)
- Paragrafo 7: data e firma fuse su un'unica riga tramite `&nbsp;` multipli → separate

## Struttura output (79 paragrafi)

| Blocco | Para | Formato applicato |
|---|---|---|
| Giudice di Pace di Brescia | 0 | CENTER, 16pt, bold |
| Ricorso in opposizione... | 1-2 | CENTER, 16pt, bold |
| Parte ricorrente / Parti intimate / Provvedimento impugnato | 3-9 | Label LEFT 14pt bold + corpo JUST 12pt |
| Oggetto del giudizio | 10-11 | Label LEFT 14pt bold + corpo JUST 12pt |
| Premesso che / In fatto | 12-20 | Intestazioni CENTER 16pt bold + corpo JUST 12pt |
| In diritto (argomenti I-V) | 21-50 | Intestazione CENTER 16pt bold; arg. headings LEFT 14pt bold; liste JUST 12pt indent 0.75cm; corpo JUST 12pt |
| tanto premesso / ricorre | 51-54 | CENTER 16pt bold (formule rituali) |
| Conclusioni (sub-sezioni) | 55-65 | CENTER 16pt bold; sub-intestazioni LEFT 14pt bold; corpo JUST 12pt |
| Si producono (7 allegati) | 66-73 | Label LEFT 14pt bold; voci LEFT 12pt indent 0.5cm |
| Dichiarazione di valore | 74-75 | Label LEFT 14pt bold; corpo JUST 12pt |
| Con osservanza | 76 | RIGHT 12pt |
| Bergamo, 12 maggio 2026 | 77 | RIGHT 12pt |
| Avv. Matteo Bertocchi | 78 | RIGHT 12pt bold |

## Interventi tecnici

- **Artefatti OCR corretti:** `proclivit[à]` → `proclività`; `nel[l']infrangere` → `nell'infrangere`
- **En dash sostituiti:** tutti i `–` → `-` (HARD_004B)
- **&nbsp; rimossi:** riga data+firma separata in due paragrafi distinti
- **Studio header:** paragrafo 0 del sorgente saltato (già nel template)
- **Font esplicito:** Times New Roman su ogni run
- **keep_with_next=True:** su tutte le intestazioni di sezione e argomento
- **keep_together=True:** sulle formule rituali brevi

## Verifica checklist (HARD_006)

- [x] Contenuto giuridico preservato integralmente
- [x] Template Template_Vuoto.docx usato come base
- [x] Font e size espliciti su ogni run
- [x] Gerarchia visiva: titolo → macro-sezioni → sottosezioni → corpo → elenchi → firma
- [x] Corpo testo JUSTIFY 12pt
- [x] Elenchi con rientro coerente (0.75cm per Art., 0.5cm per allegati)
- [x] Data e firma separati in paragrafi distinti
- [x] Nessun artefatto OCR residuo
- [x] Nessun en/em dash residuo
- [x] Blocco firma/data/congedo allineato a destra
