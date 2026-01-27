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

### Glosář:

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

## Branches

- `master` = production
- `staging` = testování (NEMAZAT!)
- `test/*` = dočasné (smazat po merge)

---

## Sudo

Pro sudo použij `sudo -A` (GUI dialog).
