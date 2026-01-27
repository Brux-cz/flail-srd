# Claude - Instrukce pro FLAIL SRD

## 🚨 DŮLEŽITÉ - Translation Workflow

**Když uživatel zmíní "nová verze", "update od autora", "nový PDF":**

1. **Otevři a přečti `WORKFLOW.md`**
2. Postupuj podle kroků krok za krokem
3. V případě problémů čti `TEST_REPORT.md`

---

## Běžné úkoly

### Oprava překladu (malé změny)

```bash
# Edituj, test, commit, push na master přímo
vim docs/cs/player/classes/bard.md
mkdocs serve
git add docs/cs/ && git commit -m "Fix" && git push
```

### Aktualizace verze (velké změny)

**👉 Použij `WORKFLOW.md`** - tam je všechno!

---

## Revize překladu (když uživatel pošle obrázek/PDF stránku)

**Jsi rodilý český mluvčí, zkušený hráč OSR her a profesionální překladatel.**

### Postup:

1. **Načti** přiložený obrázek/PDF s originálem
2. **Najdi** odpovídající překlad v `docs/cs/`
3. **Porovnej** originál s překladem větu po větě
4. **Zkontroluj** tyto kategorie chyb:

| Kategorie | Příklady |
|-----------|----------|
| Gramatika | Špatný pád, osoba, čas |
| Idiomy | Doslovný překlad ang. idiomů místo českého ekvivalentu |
| Herní terminologie | d6→k6, swingy→rozkolísané |
| Konzistence | Střídání tykání/vykání |
| Plynulost | Kostrbatá souvětí |

5. **Vytvoř tabulku** s problémy (Originál | Překlad | Oprava)
6. **Počkej na schválení** uživatele
7. **Proveď opravy**, commitni a pushni

### Kritéria kvality:

- Text musí znít **přirozeně** pro českého čtenáře
- Zachovat **energii a tón** originálu
- Používat **českou RPG terminologii**
- **Nepřekládat** názvy her, jména autorů
- **Konzistentně** tykání/vykání (pravidla = vykání)

### Aktivní glosář:

| EN | CS |
|----|-----|
| roll-under | hod pod hodnotu |
| save / saving throw | záchranný hod |
| hit points (HP) | body životů (HP) |
| swingy | rozkolísané |
| d6, d20 | k6, k20 |
| dungeon crawl | průzkum kobky |
| hexcrawl | hexcrawl |
| push your luck | riskovat |
| GM / DM | Vypravěč / GM |
| turn | tah |
| round | kolo |
| melee | boj na blízko |
| ranged | boj na dálku |

---

## Správa glosáře

### Jak to funguje:

1. **Aktivní glosář** (výše) = schválené termíny, které MUSÍM používat
2. **Glosář ke schválení** (`GLOSSARY_PENDING.md`) = nové návrhy čekající na review

### Při revizi překladu:

1. Když najdu nový termín, který by měl být v glosáři → přidám do `GLOSSARY_PENDING.md`
2. Každý návrh obsahuje:
   - **EN** = anglický termín
   - **CS** = navrhovaný český překlad
   - **Kontext** = kde se termín vyskytuje
   - **Zdůvodnění** = proč volím tento překlad
3. Po revizi upozorním uživatele na nové návrhy
4. Uživatel schválí/upraví návrhy
5. Schválené termíny přesunu do aktivního glosáře

### Pravidla pro návrhy:

- **Konzistence** = jeden termín = jeden překlad (žádné varianty)
- **Česká RPG tradice** = preferovat zažité české termíny (záchranný hod, kolo, tah...)
- **Nepřekládat** = vlastní jména, názvy her, anglicismy které se v CZ RPG komunitě běžně používají
- **Vysvětlit** = u neobvyklých voleb vždy napsat proč

---

## Branches

- `master` = production
- `staging` = testování (NEMAZAT!)
- `test/*` = dočasné (smazat po merge)

---

## Sudo

Pro sudo použij `sudo -A` (GUI dialog).
