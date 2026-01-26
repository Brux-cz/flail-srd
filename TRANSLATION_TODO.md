# Translation TODO: master → v1.0-test

## Co se změnilo:

### HIGH PRIORITY (NOVÉ)
- [ ] docs/cs/player/classes/artificer.md - nová třída (celý soubor)
  - Potřeba: překlad ~300 slov
  - Kontrola glosáře: "Artificer" → "Řemeslník"
  - Status: NOVÝ SOUBOR

### MEDIUM PRIORITY (ZMĚNĚNO)
- [ ] docs/cs/player/combat.md - přidána sekce "Obklíčení (Flanking)"
  - Potřeba: překlad ~80 slov
  - Kontrola glosáře: "Flanking" → "Obklíčení"
  - Řádky: přidáno po řádku 45
  - Status: UPRAVENO

### LOW PRIORITY (SMAZÁNO)
- [ ] docs/cs/player/philosophy.md - smazána sekce "Pravidlo nula"
  - Řádky: 5-7 (smazáno)
  - Kontrola: Ověřit, že odstranění nedělá problémy v kontextu
  - Status: SMAZÁNO

### KONFIGURACE
- [x] mkdocs.yml - přidán artificer.md do navigace
  - Pozice: první v seznamu tříd
  - Label: "Artificer (v1.0)"

## Další kroky:
1. ✓ Vytvořit testovací změny
2. [ ] Commitnout změny
3. [ ] Git diff review (zkontrolovat co se změnilo)
4. [ ] Lokální test (mkdocs serve)
5. [ ] Staging deploy
6. [ ] Ověřit na webu
7. [ ] Merge do master pokud OK

## Poznámky k testování:
- Zkontrolovat, že se artificer.md zobrazuje v navigaci
- Ověřit, že nová sekce v combat.md je správně formátovaná
- Potvrdit, že philosophy.md stále dává smysl bez "Pravidla nula"
- Otestovat vyhledávání (search) pro nové termíny
