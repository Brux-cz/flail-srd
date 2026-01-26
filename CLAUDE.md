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

## Branches

- `master` = production
- `staging` = testování (NEMAZAT!)
- `test/*` = dočasné (smazat po merge)

---

## Sudo

Pro sudo použij `sudo -A` (GUI dialog).
