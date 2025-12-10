# Dokumentation - Guide

## Hur dokumentationen fungerar

Denna systemarkitektur-dokumentation är byggd med **best practices** för stora organisationer:

### 1. Single Source of Truth
- All systemdata finns i `systems_data.py` eller `systems_data_extended.json`
- Dokumentation genereras automatiskt från datan
- Inga duplicerade data

### 2. Kodbaserad Dokumentation
- Markdown-filer (lätt att redigera)
- Mermaid-diagram (automatiskt renderade)
- Versionskontrollerad i Git

### 3. Automatiserad Generering
- `generate_website.py` - Genererar webbplats
- `generate_docs.py` - Genererar dokumentation
- `generate_extended_data.py` - Utökar data

### 4. Interaktiv Webbplats
- Sökbar
- Filtrerbar
- Responsiv (fungerar på alla enheter)

## Struktur

```
HVOF-system/
├── systems_data.py              # Single source of truth
├── systems_data_extended.json    # Utökad data (kostnad, användare, etc.)
├── generate_website.py          # Genererar webbplats
├── generate_docs.py             # Genererar dokumentation
├── mkdocs.yml                   # Webbplats-konfiguration
├── docs/                        # Dokumentation (Markdown)
│   ├── index.md                 # Startsida
│   ├── 00-overview/            # Översikt
│   ├── 01-nulage/              # Nulägesanalys
│   ├── 02-system/              # Systemdokumentation
│   ├── diagrams/               # Diagram
│   └── 05-rfi/                 # RFI-underlag
└── site/                        # Genererad webbplats (efter mkdocs build)
```

## Uppdatera Dokumentation

### Lägg till Nytt System

1. Öppna `systems_data_extended.json`
2. Lägg till nytt system med följande struktur:

```json
{
  "id": 58,
  "name": "Nytt System",
  "type": "System",
  "owner": "Ägare",
  "department": "Avdelning",
  "description": "Beskrivning",
  "contacts": ["Kontakt"],
  "org": "Organisation",
  "auth": "Autentisering",
  "category": "Central Systems",
  "cost": {
    "annual": 100000,
    "license": 50000,
    "support": 50000,
    "currency": "SEK"
  },
  "users": {
    "total": 500,
    "groups": ["Grupp 1", "Grupp 2"],
    "roles": ["Roll 1", "Roll 2"]
  },
  "technical": {
    "deployment": "Cloud",
    "vendor": "Leverantör",
    "version": "1.0",
    "database": "PostgreSQL",
    "apis": ["REST API"],
    "integrations": ["System 1", "System 2"]
  },
  "criticality": "High",
  "status": "Active",
  "retirement_date": null,
  "notes": "Anteckningar"
}
```

3. Kör `python3 generate_website.py`
4. Commit och push

### Uppdatera Befintligt System

1. Öppna `systems_data_extended.json`
2. Hitta systemet (sök på ID eller namn)
3. Uppdatera fälten
4. Kör `python3 generate_website.py`
5. Commit och push

### Redigera Manuellt

1. Redigera Markdown-filer i `docs/`
2. Commit och push
3. Webbplatsen uppdateras automatiskt

## Validering

Kör validering för att säkerställa att all data är korrekt:

```bash
python3 validate_data.py
```

Detta kontrollerar:
- Alla system har obligatoriska fält
- Kostnader är numeriska
- Användarantal är numeriska
- Integrationer refererar till befintliga system

## Backup

- **Git** - Automatisk backup vid varje commit
- **Manuell backup** - Kopiera `systems_data_extended.json` regelbundet
- **Webbplats** - Backup av `site/` mappen efter build

## Best Practices

### Datahantering
- ✅ Uppdatera kostnader kvartalsvis
- ✅ Uppdatera användarantal årligen
- ✅ Dokumentera alla integrationer
- ✅ Uppdatera status vid systemändringar

### Dokumentation
- ✅ Använd tydliga beskrivningar
- ✅ Inkludera kontakter
- ✅ Dokumentera integrationer
- ✅ Uppdatera vid ändringar

### Underhåll
- ✅ Granska dokumentationen månadsvis
- ✅ Validera data regelbundet
- ✅ Uppdatera diagram vid ändringar
- ✅ Kommunikera större ändringar

