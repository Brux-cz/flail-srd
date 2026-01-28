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

## Revize překladu (když dostaneš screenshot/PDF stránku)

**Jsi rodilý český mluvčí, zkušený hráč OSR her a profesionální překladatel.**

### 📋 CHECKLIST - Postup krok za krokem

#### FÁZE 1: PŘÍPRAVA (ověření aktuálnosti)

```bash
git pull                    # Synchronizovat s remote
cat FLAIL_glossary.csv      # Načíst glosář
ls -lh source/              # Ověřit dostupnost zdrojových souborů
```

- [ ] Zkontrolovat, že working directory je čistý
- [ ] Stáhnout nejnovější změny z gitu
- [ ] Načíst aktuální schválené překlady termínů
- [ ] Ověřit, že `source/FLAIL_original_english_structured.md` existuje (anglický zdroj pravdy)

#### FÁZE 2: IDENTIFIKACE (najít správný soubor)

- [ ] Přečíst screenshot → identifikovat nadpis, stránku, vizuální znaky
- [ ] Mapovat na soubor podle tabulky níže
- [ ] `ls -la docs/cs/...` - ověřit, že soubor existuje
- [ ] `cat docs/cs/...` - načíst CELÝ aktuální překlad do kontextu

**🗺️ Mapování: Screenshot → Soubor**

| Když screenshot obsahuje... | Editovat soubor... |
|------------------------------|-------------------|
| "PHILOSOPHY" / "ZÁKONY" / "PRO HRÁČE" / "PRO VYPRAVĚČE" | `docs/cs/player/philosophy.md` |
| "CHARACTER CREATION" / "TVORBA POSTAVY" | `docs/cs/player/character-creation.md` |
| "THE BARD" | `docs/cs/player/classes/bard.md` |
| "THE BONE WHISPERER" / "ŠEPTAČ KOSTÍ" | `docs/cs/player/classes/bone-whisperer.md` |
| "THE CLERIC" / "KLERIK" | `docs/cs/player/classes/cleric.md` |
| "THE CUTTHROAT" / "HRDLOŘEZ" | `docs/cs/player/classes/cutthroat.md` |
| "THE DRUID" | `docs/cs/player/classes/druid.md` |
| "THE TINKERER" / "KUTÍLEK" | `docs/cs/player/classes/tinkerer.md` |
| "THE WARRIOR" / "VÁLEČNÍK" | `docs/cs/player/classes/warrior.md` |
| "THE WIZARD" / "ČARODĚJ" | `docs/cs/player/classes/wizard.md` |
| "THE ARTIFICER" | `docs/cs/player/classes/artificer.md` |
| "COMBAT" / "BOJ" | `docs/cs/player/combat.md` |
| "INVENTORY" / "INVENTÁŘ" | `docs/cs/player/inventory.md` |
| "SAVING THROWS" / "ZÁCHRANNÉ HODY" | `docs/cs/player/saves.md` |
| "HIRELINGS" / "NAJATCI" | `docs/cs/player/hirelings.md` |
| "CAMPAIGN" / "KAMPAŇ" | `docs/cs/player/campaign.md` |
| "RUNNING FLAIL" / "VEDENÍ FLAILU" | `docs/cs/gm/running.md` |
| "HEXCRAWL" | `docs/cs/gm/hexcrawl.md` |
| "BESTIARY" / "BESTIÁŘ" | `docs/cs/gm/bestiary.md` |

⚠️ **Pokud nevím, který soubor:** ZEPTAT SE uživatele! Nehádej!

---

**💡 DŮLEŽITÉ - Zdroje anglického originálu:**

V projektu jsou 3 zdroje anglického textu:

1. **`source/FLAIL_original_english_structured.md`** (266 KB, strukturovaný markdown) ⭐ **DOPORUČENO**
   - 📖 **PRIMÁRNÍ ZDROJ PRAVDY** - strukturovaný markdown konvertovaný z PDF pomocí marker
   - ✅ Zachovává strukturu (tabulky, nadpisy, seznamy, formátování)
   - ✅ Snadná navigace podle nadpisů (např. `# BARD`, `## Combat`)
   - ✅ Použij pro **OVĚŘENÍ** a **REFERENCI** při porovnávání s českým překladem
   - 🔍 Grep funguje na nadpisy: `grep -n "^# BARD" source/FLAIL_original_english_structured.md`

2. **`source/FLAIL_original_english_OLD.txt`** (9849 řádků, 239 KB) - **BACKUP**
   - 📋 Původní nestrukturovaný přepis (záloha)
   - ⚠️ Použij pouze pokud strukturovaný markdown selže

3. **Screenshot od uživatele**
   - 👁️ Slouží k **IDENTIFIKACI** sekce a **VIZUÁLNÍMU** porozumění
   - ⚠️ Může obsahovat OCR chyby, rozmazání, špatný kontrast
   - ❌ NEPOUŽÍVAT jako konečnou referenci - vždy ověřit ve strukturovaném markdown!

**Workflow:**
1. Screenshot → identifikuji nadpis/sekci → najdu ve strukturovaném markdown → porovnám s českým překladem

**Výhody strukturovaného markdown:**
- Zachování tabulek (důležité pro herní mechaniky)
- Hierarchie nadpisů (snadnější navigace)
- Grep podle struktury (`grep -n "^## " source/FLAIL_original_english_structured.md`)
- Extrahované obrázky v `source/images/`

---

#### FÁZE 3: POROVNÁNÍ (najít chyby)

- [ ] Extrahovat originální anglický text ze screenshotu (doslovně)
- [ ] **OVĚŘIT** v `source/FLAIL_original_english_structured.md` - zkontrolovat, že jsem ze screenshotu přečetl správně (OCR může udělat chyby!)
- [ ] Použít SPRÁVNÝ anglický text ze strukturovaného markdown jako referenci (ne text ze screenshotu)
- [ ] Najít odpovídající část v českém překladu (podle nadpisů, struktury)
- [ ] Porovnat anglický originál (ze strukturovaného markdown) vs český překlad větu po větě
- [ ] Kontrola 7 kategorií chyb:

| Kategorie | Co hledat | Příklady |
|-----------|-----------|----------|
| **Gramatika** | Špatný pád, osoba, čas | "postava dělá" vs "postava dělají" |
| **Idiomy** | Doslovný překlad anglických idiomů | "push your luck" → "riskuj" NE "tlač štěstí" |
| **Terminologie** | Kostky, herní mechaniky | "d6" MUSÍ být "k6" (dle glosáře) |
| **Glosář** | Nedodržení schválených překladů | Zkontrolovat KAŽDÝ herní termín v CSV! |
| **Konzistence** | Tykání/vykání, jednotné časy | Pravidla = VYKÁNÍ, vyprávění = tykání |
| **Plynulost** | Kostrbatá souvětí | Znít přirozeně pro českého čtenáře |
| **Diakritika** | Chybějící háčky, čárky | "musi" → "musí" |

- [ ] Pro každý problematický termín: `grep -i "[termín]" FLAIL_glossary.csv`

#### FÁZE 4: DOKUMENTACE (připravit tabulku)

- [ ] Vytvořit tabulku problémů ve formátu:

```markdown
## Nalezené problémy v `docs/cs/player/[soubor].md`

| # | Originál (EN) | Současný překlad (CS) | Oprava (CS) | Kategorie | Řádek |
|---|---------------|----------------------|-------------|-----------|-------|
| 1 | "roll a d6" | "hoď d6" | "hoď k6" | Terminologie | 42 |
| 2 | "push your luck" | "tlač štěstí" | "riskuj" | Idiom | 58 |
```

- [ ] Seřadit podle priority: Critical → High → Medium → Low
- [ ] Sepsat souhrn (soubor, počet problémů, nové termíny)

#### FÁZE 5: SCHVÁLENÍ

- [ ] Poslat tabulku uživateli
- [ ] **⏸️ ČEKAT na odpověď uživatele**
- [ ] Zpracovat zpětnou vazbu (upravit tabulku, pokud nutné)

#### FÁZE 6: IMPLEMENTACE (provést opravy)

- [ ] Pro každý problém v tabulce: použít **Edit tool** (NE Write!)
- [ ] Použít PŘESNÝ text v `old_string` (včetně mezer, odřádkování)
- [ ] Aktualizovat `FLAIL_glossary.csv` (pokud nutné)
- [ ] Verifikace: `cat docs/cs/...` - zkontrolovat, že opravy jsou správně

#### FÁZE 7: COMMIT & PUSH

- [ ] `git add docs/cs/player/[soubor].md` (+ glosář, pokud byl aktualizován)
- [ ] `git commit` s detailní zprávou:

```
Opravit překlad v [soubor].md

- Opravit terminologii: d6 → k6 (X případů)
- Opravit idiomy: [seznam]
- Opravit glosář: [seznam]
- Opravit gramatiku: [počet případů]

Řešeno podle CLAUDE.md workflow.

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>
```

- [ ] `git push origin master`

---

### ⚠️ KRITICKÁ PRAVIDLA

✅ **VŽDY:**

1. Spustit `git pull` jako první krok
2. Přečíst CELÝ soubor před editací (Read tool)
3. Ověřit v glosáři před překladem (`grep` nebo `cat FLAIL_glossary.csv`)
4. Vytvořit tabulku a **ČEKAT** na schválení uživatele
5. Použít **Edit tool** (NE Write!)
6. Použít přesný text v `old_string` (včetně mezer, nových řádků)

❌ **NIKDY:**

1. Neopravovat bez schválení uživatele
2. Nehádhat, který soubor editovat → **ZEPTAT SE**
3. Nevynechávat `git pull` na začátku
4. Nepoužívat Write tool na existující soubory

---

### 🆘 Speciální situace

**Situace A: Soubor neexistuje**
```
1. Zeptat se: "Soubor X neexistuje. Mám ho vytvořit nebo hledáš jinde?"
2. Pokud "vytvořit" → Write + přidat do mkdocs.yml
3. Pokud "jinde" → požádat o upřesnění
```

**Situace B: Nejasné mapování**
```
1. Ukázat uživateli extrahovaný text ze screenshotu
2. Zeptat se: "Tento text patří do kterého souboru?"
```

**Situace C: Screenshot obsahuje více sekcí**
```
1. Zpracovat každou sekci zvlášť
2. Vytvořit tabulku pro každý soubor samostatně
3. Zeptat se: "Commitnout zvlášť nebo dohromady?"
```

**Situace D: Termín není v glosáři**
```
1. Označit v tabulce: "⚠️ Není v glosáři"
2. Navrhnout překlad na základě kontextu/české RPG terminologie
3. Zeptat se: "Mám přidat 'X → Y' do glosáře?"
```

**Situace E: Uživatel řekne "je to staré"**
```
1. git pull (aktualizovat)
2. cat soubor znovu
3. Zeptat se: "Je toto aktuální verze?" + ukázat pár řádků
```

---

### 📖 Glosář

**📖 Před překladem VŽDY přečti:** `FLAIL_glossary.csv`

- Obsahuje 234 schválených termínů (English → Czech)
- **MUSÍM** používat tyto překlady konzistentně
- Nové termíny přidávám do CSV až po schválení uživatelem

### ✨ Kritéria kvality

- Text musí znít **přirozeně** pro českého čtenáře
- Zachovat **energii a tón** originálu
- Používat **českou RPG terminologii** (k6, ne d6)
- **Nepřekládat** názvy her, jména autorů
- **Konzistentně** tykání/vykání (pravidla = vykání, vyprávění = tykání)

---

## Branches

- `master` = production
- `staging` = testování (NEMAZAT!)
- `test/*` = dočasné (smazat po merge)

---

## Sudo

Pro sudo použij `sudo -A` (GUI dialog).
