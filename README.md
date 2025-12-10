# HVOF Systemarkitektur

Systemarkitekturdokumentation för Hälsa, Vård och Omsorgsförvaltningen (HVOF) i Malmö stad.

## Snabbstart

### 1. Installera dependencies

```bash
pip install -r requirements.txt
```

### 2. Starta lokal server

```bash
mkdocs serve
```

Öppna http://127.0.0.1:8000 i webbläsaren.

### 3. Deploy till GitHub Pages

```bash
mkdocs gh-deploy
```

> **Note**: Git måste vara installerat. Se [GITHUB_PAGES_DEPLOYMENT.md](GITHUB_PAGES_DEPLOYMENT.md) för detaljerade instruktioner.

## Struktur

```
docs/
 overview/          # Översikt, organisation, principer
 processes/         # Processer
 systems/           # Systemlandskap och systemdokumentation
 diagrams/          # Visuella diagram
 analyses/          # Analyser
 rfi-rfp/           # RFI/RFP-material
 templates/         # Mallar för dokumentation
 images/            # Bilder och logotyper
```

## Systemdata

- **Master source**: `systems_data.py`
- **Extended data**: `systems_data_extended.json`

## Licens

Malmö stad
