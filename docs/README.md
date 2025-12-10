# HVOF Systemarkitektur - Dokumentation

Denna dokumentation är strukturerad för att stödja RFI-processen och ge leverantörer en tydlig förståelse av HVOFs systemlandskap, processer och behov.

## 📁 Dokumentationsstruktur

```
docs/
├── README.md                          # Denna fil
├── 00-overview/                       # Översikt och målbild
│   ├── verksamhetsbeskrivning.md
│   ├── organisationsstruktur.md
│   └── målbild-arkitektur.md
├── 01-nulage/                        # Nulägesanalys
│   ├── systemkarta.md
│   ├── integrationskarta.md
│   ├── informationsmodell.md
│   └── processkartor.md
├── 02-system/                        # Detaljerad systemdokumentation
│   ├── centrala-system/
│   ├── molntjanster/
│   ├── applikationer/
│   └── tjanster/
├── 03-integrationer/                 # Integrationsdokumentation
│   ├── integrationskatalog.md
│   └── api-oversikt.md
├── 04-processer/                     # Processdokumentation
│   ├── karnprocesser.md
│   └── stodprocesser.md
├── 05-rfi/                           # RFI-underlag
│   ├── rfi-overview.md
│   ├── kravspecifikation.md
│   └── fragor-till-leverantorer.md
└── diagrams/                         # Diagram (genererade)
    ├── systemkarta/
    ├── integrationskarta/
    └── processkartor/
```

## 🎯 Syfte

Denna dokumentation ska:
- Ge leverantörer en tydlig förståelse av HVOFs organisation och processer
- Dokumentera nuläget (system, integrationer, processer)
- Beskriva målbild och principer
- Underlätta RFI-processen

## 🛠️ Verktyg

- **VS Code** - Huvudverktyg för dokumentation
- **Mermaid** - Diagramgenerering i Markdown
- **PlantUML** - Avancerade arkitekturdiagram
- **Miro** - Visuell presentation för verksamheten
- **Python scripts** - Automatiserad dokumentationsgenerering

## 📊 Diagramtyper

1. **Systemkarta** - Översikt över alla system och deras relationer
2. **Integrationskarta** - Systemintegrationer och dataströmmar
3. **Processkartor** - Verksamhetsprocesser och arbetsflöden
4. **Informationsmodell** - Datadomäner och relationer
5. **Målarkitektur** - Framtida systemlandskap

## 🚀 Snabbstart

1. Läs `00-overview/verksamhetsbeskrivning.md` för kontext
2. Granska `01-nulage/systemkarta.md` för systemöversikt
3. Se `05-rfi/rfi-overview.md` för RFI-underlag

## 📝 Uppdatering

Dokumentationen uppdateras kontinuerligt. Se `CHANGELOG.md` för ändringar.

