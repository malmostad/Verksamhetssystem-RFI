# HVOF Systemarkitektur

Systemarkitekturdokumentation för Hälsa, Vård och Omsorgsförvaltningen (HVOF) i Malmö stad.

## Översikt

Detta repository innehåller komplett dokumentation av HVOF:s systemlandskap, processer och systemarkitektur. Dokumentationen är byggd med MkDocs och Material Theme.

## Snabbstart

### 1. Installera dependencies

```bash
pip install -r requirements.txt
```

### 2. Generera dokumentation

```bash
# Generera utökad systemdata
python3 generate_extended_data.py

# Generera webbplatsstruktur
python3 generate_website.py
```

### 3. Starta lokal server

```bash
mkdocs serve
```

Öppna http://127.0.0.1:8000 i webbläsaren.

### 4. Bygg statisk sida

```bash
mkdocs build
```

Skapar `site/` med statiska filer.

### 5. Deploy till GitHub Pages

```bash
mkdocs gh-deploy
```

## Struktur

```
docs/
├── overview/          # Översikt, organisation, principer
├── processes/         # Processer
├── systems/           # Systemlandskap och systemdokumentation
├── diagrams/          # Visuella diagram
├── analyses/          # Analyser
├── rfi-rfp/           # RFI/RFP-material
├── templates/         # Mallar för dokumentation
└── images/            # Bilder och logotyper
```

## Färgschema

**Stadsgrön (Malmö stad)**:
- HEX: `#01351C`
- PANTONE: 3435 C
- CMYK: 93 / 24 / 85 / 68
- RGB: 1 / 53 / 28

## Logotyp

- **Navigation**: Vit logotyp (`malmo-stad-logo.png`)
- **Startsida**: Färgad logotyp (`malmo-stad-logo-colour.png`)

## Systemdata

- **Master source**: `systems_data.py`
- **Extended data**: `systems_data_extended.json` (single source of truth)

## Bidra

1. Redigera `systems_data.py` eller Markdown-filer
2. Kör `python3 generate_extended_data.py` och `python3 generate_website.py`
3. Testa lokalt med `mkdocs serve`
4. Commit och push till Git

## Kontakt

För frågor om systemarkitekturen, kontakta IT-avdelningen.

## Licens

Malmö stad
