# Design Style Guide

## Översikt

Denna guide definierar standarder för visuell design, färger, ikoner och diagramtyper i dokumentationen.

## Färger

### Primära färger

| Färg | Hex | Användning |
|------|-----|------------|
| **Stadsgrön** | `#01351C` | Primär färg, Malmö stad, centrala system |
| **Grön** | `#4CAF50` | Vård & Omsorg, framgång, aktiv |
| **Orange** | `#FF9800` | Ekonomi, varningar |
| **Röd** | `#F44336` | Kritiska system, fel, stopp |
| **Lila** | `#9C27B0` | IT-system, molntjänster |
| **Gul** | `#FFC107` | Autentisering, viktig information |

**Stadsgrön (Malmö stad)**:
- PANTONE: 3435 C
- CMYK: 93 / 24 / 85 / 68
- RGB: 1 / 53 / 28
- HEX: `#01351C`
- RAL: 6009
- NCS: 8010-G10Y

### Färgkodning per kategori

#### Systemkategorier

```mermaid
graph LR
    A[Centrala System<br/>#01351C] 
    B[Vård & Omsorg<br/>#4CAF50]
    C[Ekonomi<br/>#FF9800]
    D[Larm<br/>#F44336]
    E[IT<br/>#9C27B0]
    F[Autentisering<br/>#FFC107]
```

#### Kritikalitet

- **Kritisk** (Röd `#D32F2F`): 24/7 drift, nedtid < 1 timme
- **Hög** (Orange `#F57C00`): Daglig drift, nedtid < 4 timmar
- **Medel** (Gul `#FBC02D`): Viktiga stödsystem, nedtid < 24 timmar
- **Låg** (Grå `#9E9E9E`): Stödsystem, nedtid < 48 timmar

## Ikoner

### Systemikoner

| Ikon | Användning |
|------|------------|
| 🔐 | Autentisering, säkerhet |
| 🏥 | Vård & Omsorg |
| 💰 | Ekonomi |
| 🚨 | Larm, kritiska system |
| 👥 | Personal, HR |
| 💻 | IT-system |
| 📞 | Telefoni, kommunikation |
| 📊 | Data, rapporter |
| ⏰ | Tidsplanering |
| 🔔 | Aviseringar |
| 📋 | Dokumentation, listor |
| 💊 | Läkemedel |
| ✍️ | Signering |
| 📹 | Video, övervakning |
| 👮 | Säkerhet, väktare |

### Processikoner

| Ikon | Användning |
|------|------------|
| ▶️ | Start |
| ⏹️ | Stopp |
| ⚠️ | Varning |
| ✅ | Framgång, klar |
| ❌ | Fel, misslyckad |
| 🔄 | Loop, upprepning |
| ➡️ | Flöde, nästa steg |

## Diagramtyper

### 1. Systemlandskap (System Landscape)

**Syfte**: Översikt över alla system och deras relationer.

**Mall:**
```mermaid
graph TB
    subgraph "Kategori"
        A[System A]
        B[System B]
    end
    A -->|Integration| B
```

### 2. Processflöde (Process Flow)

**Syfte**: Visa steg i en process.

**Mall:**
```mermaid
flowchart TD
    Start([Start]) --> Steg1[Steg 1]
    Steg1 --> Steg2{Beslut?}
    Steg2 -->|Ja| Steg3[Steg 3]
    Steg2 -->|Nej| Slut([Slut])
```

### 3. Dataflöde (Data Flow)

**Syfte**: Visa hur data flödar mellan system.

**Mall:**
```mermaid
graph LR
    Master[Master System] -->|Data| System1[System 1]
    Master -->|Data| System2[System 2]
```

### 4. Integration (Integration Diagram)

**Syfte**: Detaljerad bild av integrationer.

**Mall:**
```mermaid
graph TB
    A[System A] -->|API| B[System B]
    A -->|Batch| C[System C]
    B -.->|SSO| D[System D]
```

### 5. Kritikalitet (Criticality)

**Syfte**: Visa systemprioritering.

**Mall:**
```mermaid
graph TB
    subgraph Kritisk["🔴 KRITISKT"]
        K1[System 1]
        K2[System 2]
    end
    subgraph Hog["🟠 HÖG"]
        H1[System 3]
    end
```

## Typografi

### Rubriker

- **H1** (`#`): Sidsrubrik
- **H2** (`##`): Huvudsektion
- **H3** (`###`): Undersektion
- **H4** (`####`): Detaljer

### Textstil

- **Fetstil** (`**text**`): Viktig information
- *Kursiv* (`*text*`): Betoning
- `Kod` (`` `text` ``): Systemnamn, tekniska termer

## Layout och struktur

### Dokumentstruktur

Varje dokument ska ha:

1. **Rubrik** (H1)
2. **Översikt** (H2) - Kort beskrivning
3. **Huvudinnehåll** (H2-H4)
4. **Relaterade länkar** (H2) - Till andra dokument

### Tabeller

Använd tabeller för strukturerad information:

```markdown
| Kolumn 1 | Kolumn 2 | Kolumn 3 |
|----------|----------|----------|
| Data 1   | Data 2   | Data 3   |
```

### Listor

**Punktlista** för icke-ordnade:
```markdown
- Punkt 1
- Punkt 2
```

**Numrerad lista** för steg:
```markdown
1. Steg 1
2. Steg 2
```

## Mermaid-styling

### Standard init-block

```mermaid
%%{init: {
  'theme': 'default',
  'themeVariables': {
    'fontSize': '22px',
    'fontFamily': 'Arial, sans-serif',
    'primaryColor': '#01351C',
    'primaryTextColor': '#ffffff',
    'primaryBorderColor': '#01351C',
    'lineColor': '#01351C',
    'secondaryColor': '#FFC107',
    'tertiaryColor': '#4CAF50',
    'background': '#FAFAFA',
    'mainBkgColor': '#FFFFFF',
    'textColor': '#212121',
    'clusterBkg': '#E8F5E9',
    'clusterBorder': '#01351C'
  },
  'flowchart': {
    'nodeSpacing': 60,
    'rankSpacing': 80,
    'curve': 'basis',
    'padding': 20,
    'htmlLabels': true,
    'useMaxWidth': true
  }
}}%%
```

### Färgstyling för noder

```mermaid
style SystemA fill:#01351C,stroke:#012414,stroke-width:4px,color:#FFFFFF
style SystemB fill:#4CAF50,stroke:#2E7D32,stroke-width:4px,color:#FFFFFF
```

## Exempel

### Exempel 1: Systemlandskap

```mermaid
graph TB
    subgraph Central["🏢 Centrala System"]
        HR["👥 HRutan<br/>Personal"]
        Life["🏥 Lifecare-Procapita<br/>Journal/Vård"]
    end
    HR -->|Personaldata| Life
    
    style HR fill:#01351C,stroke:#012414,stroke-width:4px,color:#FFFFFF
    style Life fill:#4CAF50,stroke:#2E7D32,stroke-width:4px,color:#FFFFFF
    style Central fill:#E8F5E9,stroke:#01351C,stroke-width:3px
```

### Exempel 2: Processflöde

```mermaid
flowchart TD
    Start([▶️ Start]) --> Steg1[📋 Steg 1: Förbered]
    Steg1 --> Steg2{⚠️ Beslut?}
    Steg2 -->|✅ Ja| Steg3[✅ Steg 3: Genomför]
    Steg2 -->|❌ Nej| Slut([⏹️ Slut])
    Steg3 --> Slut
```

## Checklista

Innan du publicerar ett dokument, kontrollera:

- [ ] Följer färgschema
- [ ] Använder rätt ikoner
- [ ] Diagram är tillräckligt stora
- [ ] Tydliga rubriker och struktur
- [ ] Länkar fungerar
- [ ] Stavning och grammatik korrekt
- [ ] Följer mall för dokumenttyp

## Uppdateringar

Denna guide uppdateras kontinuerligt. För förslag på förbättringar, kontakta IT-avdelningen.

