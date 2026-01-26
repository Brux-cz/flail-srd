# 🔄 Translation Workflow - NÁVOD PRO AKTUALIZACI VERZÍ

> **⚠️ DŮLEŽITÉ:** Tento soubor použij, až ti přijde **nová verze FLAIL od autora**!

---

## 📋 Kdy použít tento workflow?

✅ Když dostaneš novou verzi PDF od Andre Novoa
✅ Když chceš aktualizovat překlad na novou verzi hry
✅ Když potřebuješ porovnat změny mezi verzemi

❌ Ne pro běžné úpravy překladu (ty dělej přímo na master)

---

## 🚀 Quick Start - Základní příkazy

```bash
# 1. Vytvořit test branch pro simulaci nové verze
git checkout staging
git checkout -b test/v1.1-simulation

# 2. Udělat změny v souborech (upravit MD soubory podle nové verze)
# ... editace docs/cs/*.md ...

# 3. Commit a zjistit co se změnilo
git add docs/cs/
git commit -m "Simulate v1.1 changes"
git diff staging --stat           # Přehled změn
git diff staging docs/cs/         # Detailní změny

# 4. Lokální test
mkdocs build --clean
mkdocs serve    # Otevři http://127.0.0.1:8000

# 5. Deploy na staging pro testování
git checkout staging
git merge test/v1.1-simulation
git push origin staging

# 6. Zkontroluj web: https://brux-cz.github.io/flail-srd

# 7. Pokud OK → nasaď na production
git checkout master
git merge staging
git tag -a v1.1-cs -m "v1.1 Release"
git push origin master --tags

# 8. Cleanup
git branch -d test/v1.1-simulation
```

---

## 📝 Krok za krokem - Detailní návod

### Krok 1: Příprava

```bash
# Ujisti se, že jsi na stagingu
git checkout staging
git pull origin staging

# Vytvoř test branch
git checkout -b test/v1.1-simulation
```

### Krok 2: Udělej změny podle nové verze

Edituj soubory v `docs/cs/` podle nové verze PDF:

- **Nové třídy/sekce** → vytvoř nové `.md` soubory
- **Upravené sekce** → uprav existující `.md` soubory
- **Smazané sekce** → smaž části nebo celé soubory
- **Aktualizuj** `mkdocs.yml` pokud je třeba

### Krok 3: Zjisti co se změnilo

```bash
# Commit změn
git add docs/cs/
git commit -m "Simulate v1.X changes"

# Přehled - kolik souborů, řádků
git diff staging --stat

# Které soubory se změnily?
git diff staging --name-status

# Detail - co přesně v souborech?
git diff staging docs/cs/player/combat.md     # Konkrétní soubor
git diff staging docs/cs/                     # Celá složka
```

**Vytvoř TODO list pro překlad:**

```bash
cat > TRANSLATION_TODO.md << 'EOF'
# Translation TODO: v1.0 → v1.1

## HIGH PRIORITY (NOVÉ)
- [ ] Nový soubor: docs/cs/xxx.md (X řádků)

## MEDIUM PRIORITY (ZMĚNĚNO)
- [ ] Upraveno: docs/cs/yyy.md (+X řádků)

## LOW PRIORITY (SMAZÁNO)
- [ ] Smazáno: docs/cs/zzz.md
EOF
```

### Krok 4: Lokální testování

```bash
# Build (ověř, že není chyba)
source venv/bin/activate
mkdocs build --clean

# Spusť local server
mkdocs serve

# Otevři prohlížeč: http://127.0.0.1:8000
# Zkontroluj:
# ✓ Nové stránky se zobrazují
# ✓ Upravené stránky vypadají OK
# ✓ Žádné broken links
# ✓ Search funguje
```

**Pro automatické testování řekni Claudeovi:**
> "Otestuj web pomocí Playwright - zkontroluj navigaci, nové stránky a search"

### Krok 5: Staging deployment

```bash
# Merge test změn do staging
git checkout staging
git merge test/v1.1-simulation

# Push (spustí automatický deploy)
git push origin staging

# Počkej ~30 sekund

# Zkontroluj deployment
gh run list --limit 1 --branch staging

# Otevři web: https://brux-cz.github.io/flail-srd
# Zkontroluj, že vše funguje
```

### Krok 6: Production deployment

**Pouze pokud je staging OK!**

```bash
# Merge do master
git checkout master
git merge staging --no-ff -m "Merge staging: v1.1 translation update"

# Vytvoř tag
git tag -a v1.1-cs -m "v1.1 Czech translation

New features:
- XXX
- YYY

Changes:
- ZZZ
"

# Push
git push origin master --tags

# Zkontroluj deployment
gh run list --limit 1 --branch master
```

### Krok 7: Cleanup

```bash
# Smaž test branch
git branch -d test/v1.1-simulation

# Ověř stav
git branch -a

# Hotovo! 🎉
```

---

## 🎯 Tipy a triky

### Jak zjistit, co se změnilo mezi verzemi?

```bash
# Porovnej dva tagy
git diff v0.1-cs v1.0-cs

# Porovnej s určitým datem
git diff --since="2026-01-01" docs/cs/

# Najdi všechny nové soubory
git diff --name-status staging | grep "^A"

# Najdi všechny smazané soubory
git diff --name-status staging | grep "^D"
```

### Jak testovat jen určitou stránku?

```bash
# Build jen pro kontrolu chyb
mkdocs build

# Najdi built soubor
ls -la site/player/classes/

# Otevři přímo v prohlížeči
open site/player/classes/artificer/index.html
```

### Jak vrátit změny, když něco pokazím?

```bash
# Vrať změny v jednom souboru (před commitem)
git restore docs/cs/player/combat.md

# Vrať všechny změny (před commitem)
git restore docs/cs/

# Vrať poslední commit (už commitnuto)
git reset --soft HEAD~1

# Hard reset (POZOR: ztratíš změny!)
git reset --hard HEAD
```

### Jak nasadit opravu na production rychle?

```bash
# Hotfix přímo na master (jen pro malé opravy!)
git checkout master
# ... uprav soubor ...
git add docs/cs/xxx.md
git commit -m "Fix: oprava preklepu v XXX"
git push origin master
```

---

## 📊 Checklist pro deployment

Před merge do master zkontroluj:

- [ ] Všechny změny jsou commitnuty
- [ ] `mkdocs build --clean` bez chyb
- [ ] Lokální test OK (mkdocs serve)
- [ ] Staging deployment úspěšný
- [ ] Web na staging funguje správně
- [ ] Žádné broken links
- [ ] Search funguje
- [ ] Nové stránky jsou v navigaci
- [ ] Upravené stránky vypadají OK

---

## 🆘 Když něco nejde

### MkDocs build selhává

```bash
# Zkontroluj Python závislosti
pip list | grep mkdocs

# Reinstaluj
pip install --upgrade mkdocs-material mkdocs-static-i18n

# Zkus clean build
rm -rf site/
mkdocs build --clean
```

### GitHub Actions fail

```bash
# Podívej se na logy
gh run list --limit 1
gh run view <run-id> --log

# Často stačí re-run
gh run rerun <run-id>
```

### Web se nenačte

```bash
# Počkej ~1 minutu na GitHub Pages propagaci

# Zkontroluj, že branch existuje
git ls-remote --heads origin

# Force deploy
git commit --allow-empty -m "Trigger rebuild"
git push origin master
```

---

## 📁 Důležité soubory

| Soubor | Účel |
|--------|------|
| `WORKFLOW.md` | Tento návod (čti ho!) |
| `TEST_REPORT.md` | Detailní dokumentace testu workflow |
| `TRANSLATION_TODO.md` | Vytvoř si ho při každé aktualizaci |
| `.github/workflows/deploy.yml` | GitHub Actions config |
| `mkdocs.yml` | MkDocs konfigurace |
| `docs/cs/` | České překlady |

---

## 🔗 Odkazy

- **Production web:** https://brux-cz.github.io/flail-srd
- **GitHub repo:** https://github.com/Brux-cz/flail-srd
- **GitHub Actions:** https://github.com/Brux-cz/flail-srd/actions
- **MkDocs dokumentace:** https://www.mkdocs.org/
- **Material theme:** https://squidfunk.github.io/mkdocs-material/

---

## 💡 Poznámky

- **Staging branch** je trvalý - nemazat!
- **Test branches** smaž po merge
- **TRANSLATION_TODO.md** vytvoř při každé aktualizaci
- **Tagy** používej pro verzování (v1.0-cs, v1.1-cs, ...)
- **Production** vždy přes staging, ne přímo!

---

**Poslední test:** 2026-01-26
**Test status:** ✅ 100% úspěšný
**Workflow ready:** ✅ Ano

---

> 💬 **Tip:** Pokud nevíš, co dělat, řekni Claudeovi:
> *"Potřebuji aktualizovat FLAIL SRD na novou verzi. Otevři WORKFLOW.md a pomoz mi s tím."*
