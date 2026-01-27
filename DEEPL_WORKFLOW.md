# 🌍 DeepL Pro Workflow pro FLAIL SRD

> **Tvoje licence:** DeepL Pro
> **Datum vytvoření:** 2026-01-27
> **Účel:** Efektivní překlad FLAIL RPG pomocí DeepL Pro

---

## 📚 Co je DeepL Pro a proč je skvělý?

### Klíčové funkce DeepL Pro (2026)

Podle [oficiálního webu DeepL](https://www.deepl.com/en/pro) a [dokumentace API](https://www.deepl.com/en/products/api):

#### ✅ Co DeepL Pro umí:

1. **PDF překlad** - Ano! [DeepL překládá celé PDF soubory](https://www.deepl.com/en/features/document-translation/pdf) se zachováním formátování
2. **Glossary (slovník)** - [Vlastní terminologie](https://www.deepl.com/en/features/glossary) pro konzistenci (100+ jazykových kombinací)
3. **Formální/neformální tón** - Automatická detekce stylu
4. **CAT tool integrace** - Propojení s překladatelskými nástroji (vyžaduje API for Business)
5. **2x méně editů** než Google Translate ([zdroj](https://koanthic.com/en/translation-services-comparison-deepl-vs-human-2026/))
6. **Bezpečnost** - Nahrané dokumenty se ihned po překladu mažou

#### 🔥 Novinky 2026:

- **AI-powered Glossary Generator** - Automatické vytvoření glosáře z nahrané referenční soubory ([zdroj](https://www.prnewswire.com/apac/news-releases/deepl-unveils-industry-first-glossary-generator-to-solve-business-communication-and-brand-consistency-challenges-302254939.html))
- **In-house PDF překlad** - Data se už neposílají do USA
- **Style rules** - Programatické nastavení stylu překladu

---

## 🚀 Quick Start - Překlad FLAIL

### Varianta 1: PDF překlad (nejjednodušší)

```bash
# 1. Otevři DeepL Pro web
https://www.deepl.com/translator

# 2. Nahraj PDF
source/FLAIL_pravidla.pdf (56MB, anglicky)

# 3. Vyber jazyk: EN → CS

# 4. Použij glossary (viz sekce níže)

# 5. Stáhni přeložený PDF

# 6. Zkopíruj text do markdown souborů
```

**Výhoda:** Zachová formátování
**Nevýhoda:** Musíš ručně překopírovat text do .md souborů

---

### Varianta 2: Textový překlad (flexibilnější)

```bash
# 1. Použij extrahovaný text
source/FLAIL_original_english.txt (239KB, 9849 řádků)

# 2. Nahraj do DeepL Pro jako TXT/DOCX

# 3. Překládej po sekcích:
# - Character Creation
# - Combat
# - Saving Throws
# atd.

# 4. Vlož přeložený text do docs/cs/*.md
```

**Výhoda:** Přímá kontrola markdown formátování
**Nevýhoda:** Ztratíš tabulky/formátování z PDF

---

### Varianta 3: API automatizace (pro pokročilé)

```python
# Vyžaduje DeepL API for Business
# Automatický překlad všech souborů v dávce

import deepl

translator = deepl.Translator("YOUR_API_KEY")

# Přelož soubor
with open('source/FLAIL_original_english.txt', 'r') as f:
    text = f.read()
    result = translator.translate_text(
        text,
        source_lang="EN",
        target_lang="CS",
        glossary_id="YOUR_GLOSSARY_ID"
    )

with open('output_czech.txt', 'w') as f:
    f.write(result.text)
```

---

## 📖 Glosář pro FLAIL (DeepL Glossary)

### Vytvoření glosáře v DeepL Pro

1. **Přejdi na:** https://www.deepl.com/translator
2. **Klikni:** "Glossary" (horní menu)
3. **Vytvoř nový glosář:** "FLAIL RPG Czech"
4. **Jazyky:** English → Czech
5. **Nahraj CSV soubor** (viz níže) nebo zadej ručně

### Glosář pro stažení

Vytvoř soubor `FLAIL_glossary.csv`:

```csv
English,Czech
Saving throw,Záchranný hod
Hit roll,Hod na zásah
Advantage,Výhoda
Disadvantage,Nevýhoda
Health points,Body životů
Bone Whisperer,Šeptač kostí
Cutthroat,Hrdlořez
Tinkerer,Kutílek
Warrior,Válečník
Bard,Bard
Wizard,Čaroděj
Cleric,Klerik
Druid,Druid
Strength,Síla
Dexterity,Obratnost
Intelligence,Inteligence
Charisma,Charisma
Luck,Štěstí
Roll under,Hoď pod
Initiative,Iniciativa
Morale,Morálka
Hireling,Najatec
Campaign,Kampaň
Bestiary,Bestiář
Dungeon,Kobka
Hexcrawl,Hexcrawl
Adventure site,Místo dobrodružství
Unique item,Unikátní předmět
Quest,Výprava
GM,Vypravěč
Player character,Hráčská postava
NPC,NPC
Monster,Příšera
Creature,Tvor
Dragon,Drak
Goblin,Goblin
Skeleton,Kostlivec
Vampire,Upír
Lich King,Lichý král
Equipment,Výbava
Inventory,Inventář
Weapon,Zbraň
Armor,Zbroj
Shield,Štít
Potion,Lektvar
Scroll,Svitek
Spell,Kouzlo
Magic,Magie
Temple,Chrám
Inn,Hospoda
Village,Vesnice
City,Město
```

### Jak používat glosář v DeepL Pro:

1. Při překladu dokumentu **vyber svůj glosář** z dropdown menu
2. DeepL **automaticky aplikuje** tvoji terminologii
3. **Kontroluj konzistenci** po překladu

---

## 🎯 Workflow krok za krokem

### Krok 1: Příprava

```bash
# Máš už připraveno:
cd /home/brux/projekty/flail-srd

# Zdrojové soubory:
source/FLAIL_pravidla.pdf              # Anglický PDF originál (56MB)
source/FLAIL_original_english.txt      # Extrahovaný text (239KB)

# Cílové soubory:
docs/cs/*.md                           # České překlady
```

### Krok 2: Vytvoř glosář

1. Otevři https://www.deepl.com/translator
2. Přejdi na **Glossary** → **Create glossary**
3. Pojmenuj: **"FLAIL RPG Czech"**
4. Jazyk: **EN → CS**
5. Zkopíruj termíny z `FLAIL_glossary.csv` výše
6. **Ulož**

### Krok 3: Přelož dokument

#### Pro PDF:

1. Otevři https://www.deepl.com/translator
2. Klikni na **"Upload a document"**
3. Vyber `source/FLAIL_pravidla.pdf`
4. **Vyber glosář:** "FLAIL RPG Czech"
5. **Translate**
6. Počkaj ~2-5 minut (56MB soubor)
7. **Stáhni** přeložený PDF

#### Pro TXT:

1. Otevři `source/FLAIL_original_english.txt`
2. **Zkopíruj sekci** (např. "CHARACTER CREATION")
3. Vlož do DeepL Pro translatoru
4. **Vyber glosář:** "FLAIL RPG Czech"
5. **Translate**
6. **Zkopíruj výsledek** do příslušného `docs/cs/*.md` souboru
7. **Opakuj** pro další sekce

### Krok 4: Edituj a formátuj

```bash
# Otevři přeložený soubor
vim docs/cs/player/classes/bard.md

# Zkontroluj:
# ✓ Diakritika správně
# ✓ Terminologie konzistentní (podle glosáře)
# ✓ Markdown formátování zachováno
# ✓ Tabulky správně
# ✓ Odkazy fungují

# Lokální test
mkdocs serve
# → http://127.0.0.1:8000
```

### Krok 5: Commit

```bash
git add docs/cs/player/classes/bard.md
git commit -m "Překlad Bard pomocí DeepL Pro

Použit glosář pro konzistenci terminologie.
Manuálně zkontrolováno a upraveno formátování.
"
git push origin master
```

---

## 💡 Tipy a triky

### 1. Překládej po sekcích, ne celé

**Proč:** Lepší kontrola, snadnější úpravy

```
✅ DOBŘE: Přelož "Character Creation" → vlož do player/classes/*.md
❌ ŠPATNĚ: Přelož celé PDF najednou → ztráta struktury
```

### 2. Vždy používej glosář

**Konzistence terminologie je nejdůležitější!**

Podle [Allcorrect Games](https://allcorrectgames.com/insights/localization-glossaries-what-they-are-and-why-they-matter/):
> Nekonzistence ničí imerzi a frustruje hráče

### 3. Edituj výstup ručně

**DeepL je super, ale není dokonalý**

Kontroluj:
- [ ] České idiomy (DeepL někdy překládá doslovně)
- [ ] Herní slang (např. "push your luck" → "riskuj" ne "tlač své štěstí")
- [ ] Formální/neformální tón (FLAIL je neformální)
- [ ] Kulturní odkazy (ponechej, pokud jsou univerzální)

### 4. Využij kontextové poznámky

V DeepL Pro můžeš přidat poznámky k překladu:
- "Bard = nezměnit (vlastní název třídy)"
- "Flail = nezměnit (název hry)"

### 5. Kombinuj s učením angličtiny

**Pro každou sekci:**

1. **Přečti anglický text** → porozumění
2. **Přelož v DeepL** → technická práce
3. **Porovnej** → zjisti, jak DeepL překládá konstrukce
4. **Zapiš si** zajímavé fráze do `LEARNING_NOTES.md`

Příklad:
```markdown
## "Push your luck"
- Doslovný překlad: "tlač své štěstí" ❌
- DeepL překlad: "riskuj" ✅
- Context: idiomatic expression for gambling/risk-taking
```

---

## 🔧 Řešení problémů

### DeepL překládá názvy tříd

**Problém:** "Cutthroat" → "Zabiják" (místo "Hrdlořez")

**Řešení:**
1. Přidej do glosáře: `Cutthroat → Hrdlořez`
2. Nebo: V PDF nahraď `Cutthroat` za `[CLASS: Cutthroat]` před překladem

### Tabulky se rozbijí

**Problém:** Markdown tabulky nejsou správně formátované

**Řešení:**
1. Přelož text BEZ tabulek
2. Vlož anglické tabulky
3. Přelož jen obsah buněk ručně

### DeepL je moc doslovný

**Problém:** "This thing is Mausritter meets DCC!" → "Tahle věc je Mausritter potkává DCC!"

**Řešení:**
1. Edituj ručně: "Tohle je Mausritter meets DCC!"
2. Zachovej anglické názvy her v originále

### PDF překlad trvá příliš dlouho

**Problém:** 56MB PDF se překládá 10+ minut

**Řešení:**
1. Rozděl PDF na menší části (Adobe Acrobat, pdftk)
2. Nebo použij extrahovaný TXT soubor (rychlejší)

---

## 📊 Tracking progress s DeepL

### Vytvoř checklist v TRANSLATION_STATUS.md

```markdown
# Translation Progress (DeepL Pro)

## 🔄 In Progress - DeepL translation

### Frontmatter & Introduction
- [x] Foreword (použit DeepL + glosář) ✅
- [ ] Table of Contents (v procesu) 🔄
- [ ] Philosophy (čeká) ⏸️

### Player Rules
- [x] Character Creation intro (hotovo) ✅
- [ ] Bard class (překlad 50%) 🔄
- [ ] Wizard class (čeká) ⏸️
...

## ✅ Completed - Manual review done
- [x] index.md ✅
- [x] player/saves.md ✅
...
```

### Status legendy:
- ✅ = Přeloženo + zkontrolováno + commitnuto
- 🔄 = V procesu překladu
- ⏸️ = Čeká na překlad
- ❌ = Problém (opravit)

---

## 🌐 Užitečné odkazy

### DeepL dokumentace:
- **DeepL Pro:** https://www.deepl.com/en/pro
- **PDF Translation:** https://www.deepl.com/en/features/document-translation/pdf
- **Glossary Feature:** https://www.deepl.com/en/features/glossary
- **API Documentation:** https://developers.deepl.com/docs
- **Help Center:** https://support.deepl.com/hc/en-us

### Best practices:
- [IGDA Localization Best Practices (PDF)](https://igda-website.s3.us-east-2.amazonaws.com/wp-content/uploads/2021/04/09142137/Best-Practices-for-Game-Localization-v22.pdf)
- [LCP - Glossaries in Game Localization](https://lcplocalizations.com/the-importance-of-style-guides-and-glossaries-in-game-localization/)
- [Allcorrect - Why Glossaries Matter](https://allcorrectgames.com/insights/localization-glossaries-what-they-are-and-why-they-matter/)
- [GameTyrant - Mastering Game Localization 2026](https://gametyrant.com/news/mastering-game-localization-proven-strategies-for-success-in-2026)

---

## 🎓 Doporučený workflow pro učení + překlad

### 1. Angličtina first (15 min)

```bash
# Přečti anglickou sekci
cat source/FLAIL_original_english.txt | grep -A 50 "CHARACTER CREATION"

# Podtrhni neznámá slova
# Vyhledej v online slovníku
# Zapiš si do LEARNING_NOTES.md
```

### 2. DeepL překlad (5 min)

```bash
# Zkopíruj sekci do DeepL Pro
# Použij glosář
# Stáhni překlad
```

### 3. Porovnání (10 min)

```bash
# Porovnej:
# - Jak překládá idiomy?
# - Jak řeší složité konstrukce?
# - Kde používá formální/neformální?

# Zapiš poznatky do LEARNING_NOTES.md
```

### 4. Ruční editace (10 min)

```bash
# Uprav překlad:
# - Kontrola terminologie
# - Zlepši českou stylistiku
# - Zachovej markdown formátování
```

### 5. Commit (2 min)

```bash
git add docs/cs/player/classes/bard.md
git commit -m "Překlad Bard (DeepL Pro + manuální editace)"
git push
```

**Celkem: ~42 minut na jednu třídu/sekci**

---

## 📈 Statistiky a očekávání

### FLAIL SRD - rozsah projektu:

| Kategorie | Počet souborů | Odhadovaný čas s DeepL |
|-----------|---------------|------------------------|
| Třídy postav | 8 | 8 × 40 min = 5.3 hod |
| Pravidla hráčů | 5 | 5 × 30 min = 2.5 hod |
| GM nástroje | 6 | 6 × 45 min = 4.5 hod |
| Zdroje | 7 | 7 × 20 min = 2.3 hod |
| **CELKEM** | **26** | **~15 hodin** |

**Bez DeepL:** ~40-50 hodin
**S DeepL Pro:** ~15 hodin
**Úspora času:** **66%** ⚡

---

## 🏁 Checklist pro každou sekci

Před commitem zkontroluj:

- [ ] Text přeložen pomocí DeepL Pro s glosářem
- [ ] Terminologie konzistentní (zkontroluj GLOSSARY.md)
- [ ] Diakritika správně (háčky, čárky)
- [ ] Markdown formátování zachováno
- [ ] Tabulky správně formátované
- [ ] Odkazy fungují (relativní cesty)
- [ ] Lokální test OK (mkdocs serve)
- [ ] Commit message popisný
- [ ] Push na master

---

**Vytvořeno:** 2026-01-27
**Verze:** 1.0
**Status:** ✅ Ready to use

**Užij si překlad s DeepL Pro! 🚀**
