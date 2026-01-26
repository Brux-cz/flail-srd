# FLAIL - Cesky preklad a SRD

Preklad OSR fantasy RPG FLAIL od Games Omnivorous do cestiny.

## Struktura projektu

```
flail-srd/
├── docs/
│   ├── cs/              # Cesky preklad (publikovano)
│   │   ├── index.md
│   │   ├── player/      # Pravidla pro hrace
│   │   ├── gm/          # Pravidla pro GM
│   │   └── resources/   # Zdroje (mesta, NPC, jmena...)
│   ├── en/              # Anglicky original (TODO)
│   └── assets/          # Sdilene obrazky
├── source/              # Zdrojove PDF
├── scripts/             # Pomocne skripty
├── cards/               # Data karet
├── glosar.csv           # Glosar terminu
├── translation_source.md # Kompletni preklad (jedna velka MD)
└── mkdocs.yml           # Konfigurace MkDocs
```

## Lokalni vyvoj

```bash
cd /home/brux/projekty/flail-srd
source venv/bin/activate
mkdocs serve   # http://127.0.0.1:8000
```

## Workflow prekladu

1. **Uprav** soubory v `docs/cs/`
2. **Testuj** lokalne: `mkdocs serve`
3. **Commitni** a **pushni**: zmeny se automaticky deployi na GitHub Pages

## Verzovani

- Verze prekladu odpovida verzi originalu
- Tagy: `v1.0-cs`, `v1.1-cs`, atd.
- Branch `master` = aktualni publikovana verze

## Glosar

Pred prekladem novych terminu VZDY konzultuj `glosar.csv`.

Klicove terminy:
| EN | CS |
|----|----|
| Bone Whisperer | Septac kosti |
| Cutthroat | Hrdlorez |
| Tinkerer | Kutilek |
| Push-your-luck | Riskovaci mechanika |

## Pridani anglicke verze (TODO)

1. Vytvor `docs/en/` se stejnou strukturou jako `docs/cs/`
2. Odkomentuj `en` locale v `mkdocs.yml`
3. Web pak bude mit prepinac jazyku

## Odkazy

- **Web:** https://brux-cz.github.io/flail-srd
- **Originalni hra:** [Games Omnivorous](https://gamesomnivorous.com)
