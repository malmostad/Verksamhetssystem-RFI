# Verksamhetsområde: Vård & Omsorg

## Översikt
Detta diagram visar alla system och integrationer specifikt för Vård & Omsorg-verksamheten.

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
    'secondBkgColor': '#F5F5F5',
    'tertiaryBkgColor': '#E8F5E9',
    'textColor': '#212121',
    'secondaryTextColor': '#424242',
    'tertiaryTextColor': '#616161',
    'lineColor': '#01351C',
    'border1': '#01351C',
    'border2': '#FFC107',
    'arrowheadColor': '#01351C',
    'clusterBkg': '#E8F5E9',
    'clusterBorder': '#01351C',
    'defaultLinkColor': '#01351C',
    'titleColor': '#01351C',
    'edgeLabelBackground': '#FFFFFF',
    'actorBorder': '#01351C',
    'actorBkg': '#E8F5E9',
    'actorTextColor': '#212121',
    'actorLineColor': '#01351C',
    'signalColor': '#01351C',
    'signalTextColor': '#212121',
    'labelBoxBkgColor': '#E8F5E9',
    'labelBoxBorderColor': '#01351C',
    'labelTextColor': '#212121',
    'loopTextColor': '#212121',
    'noteBorderColor': '#FFC107',
    'noteBkgColor': '#FFF9C4',
    'noteTextColor': '#212121',
    'activationBorderColor': '#01351C',
    'activationBkgColor': '#E8F5E9',
    'sequenceNumberColor': '#FFFFFF',
    'sectionBkgColor': '#E8F5E9',
    'altBkgColor': '#FFF9C4',
    'altBkgColor2': '#E8F5E9',
    'excludeBkgColor': '#FFEBEE',
    'taskBorderColor': '#01351C',
    'taskBkgColor': '#E8F5E9',
    'taskTextLightColor': '#FFFFFF',
    'taskTextColor': '#212121',
    'taskTextDarkColor': '#212121',
    'taskTextOutsideColor': '#212121',
    'taskTextClickableColor': '#01351C',
    'activeTaskBorderColor': '#4CAF50',
    'activeTaskBkgColor': '#C8E6C9',
    'gridColor': '#E0E0E0',
    'doneTaskBkgColor': '#C8E6C9',
    'doneTaskBorderColor': '#4CAF50',
    'critBorderColor': '#F44336',
    'critBkgColor': '#FFCDD2',
    'todayLineColor': '#FFC107'
  },
  'flowchart': {
    'nodeSpacing': 60,
    'rankSpacing': 80,
    'curve': 'basis',
    'padding': 20,
    'htmlLabels': true,
    'useMaxWidth': true
  },
  'gantt': {
    'leftPadding': 75,
    'gridLineStartPadding': 35,
    'fontSize': 18,
    'fontFamily': 'Arial, sans-serif',
    'numberSectionStyles': 4,
    'axisFormat': '%Y-%m-%d',
    'topAxis': false,
    'bottomAxis': true,
    'topPadding': 50,
    'bottomPadding': 50
  }
}}%%
graph TB
    subgraph "Vård & Omsorg - Systemlandskap"
        direction TB
        
        subgraph "Kärnsystem - Master"
            Life[Lifecare-Procapita<br/>Journal/Vård<br/>MASTER]
        end
        
        subgraph "Externa Vårdtjänster"
            NPÖ[NPÖ<br/>Nationell Patientöversikt<br/>Inera]
            Pascal[Pascal<br/>Läkemedel<br/>Inera]
            MCSS[MCSS<br/>Digital Signering]
            MinaPlaner[Mina planer<br/>Vårdplanering<br/>KFSK]
            KomKat[KomKat<br/>HSA Katalog<br/>KFSK]
        end
        
        subgraph "Tidsplanering & Uppföljning"
            Kuben[Kuben<br/>Tidsplanering]
            Phoniro[Phoniro Care<br/>Tid/Insatsuppföljning]
        end
        
        subgraph "Trygghet & Sensorer"
            Sensio[Sensio<br/>Trygghetssensorer]
            Smooth[Smooth lite<br/>Trygghetssensorer]
            Viser[Viser<br/>Larmsystem säbo]
        end
        
        subgraph "Stödjande System"
            Mateo[Mateo<br/>Kostdata]
            Senior[Senior alert<br/>Kvalitetsregister]
        end
        
        Life <-->|Patientdata<br/>API HL7| NPÖ
        Life <-->|Läkemedel<br/>API| Pascal
        Life -->|Signering<br/>API| MCSS
        Life -->|Vårdplan<br/>API| MinaPlaner
        Life -->|HSA-data<br/>API| KomKat
        
        Kuben -->|Tidsplanering<br/>API/Databas| Life
        Life -->|Tidsdata<br/>Batch| Phoniro
        
        Sensio -->|Sensorlarm| Life
        Smooth -->|Sensorlarm| Life
        Viser -->|Larmdata| Life
        
        Mateo -->|Kostdata| Life
        Senior -->|Kvalitetsdata| Life
    end
    
    subgraph "Autentisering"
        Freja[Freja eID]
        SITHS[SITHS]
        
        Freja -->|Inloggning| Life
        SITHS -->|Inloggning| NPÖ
        SITHS -->|Inloggning| Pascal
        SITHS -->|Inloggning| MCSS
        SITHS -->|Inloggning| MinaPlaner
        SITHS -->|Inloggning| KomKat
    end
    
    style Life fill:#adf0c7,stroke:#087429,stroke-width:4px
    style NPÖ fill:#90ee90,stroke:#087429,stroke-width:2px
    style Pascal fill:#90ee90,stroke:#087429,stroke-width:2px
    style MCSS fill:#90ee90,stroke:#087429,stroke-width:2px```

## System i Vård & Omsorg

### Kärnsystem
1. **Lifecare-Procapita** (Master)
   - Journal och vårdsystem
   - Master för all vårddata
   - Integrerar med NPÖ, Pascal, MCSS
   - Kontakt: ÖSA, FSF
   - Org: FSF

### Externa Vårdtjänster
2. **NPÖ** - Nationell patientöversikt (Inera)
3. **Pascal** - Beställning läkemedel (Inera)
4. **MCSS** - Digital signering läkemedel
5. **Mina planer** - Samordnad vårdplanering (KFSK)
6. **KomKat** - HSA katalog (KFSK)

### Tidsplanering & Uppföljning
7. **Kuben** - Tidsplanering vårdbehov
8. **Phoniro Care** - Tid och insatsuppföljning

### Trygghet & Sensorer
9. **Sensio trygghetssensorer** - Trygghetssensorer (Säbo)
10. **Smooth lite trygghetssensorer** - Trygghetssensorer (Säbo)
11. **Viser** - Larmsystem säbo

### Stödjande System
12. **Mateo** - Kostdataprogram
13. **Senior alert** - Kvalitetsregister

## Processflöden

### Vårdprocess
1. **Brukare registreras** → Lifecare-Procapita
2. **Vårdplan skapas** → Mina planer (KFSK)
3. **Tidsplanering** → Kuben → Lifecare-Procapita
4. **Läkemedel beställs** → Pascal ↔ Lifecare-Procapita
5. **Signering** → MCSS ↔ Lifecare-Procapita
6. **Uppföljning** → Phoniro Care ← Lifecare-Procapita

### Patientdata-flöde
1. **Lifecare-Procapita** (Master) → Patientdata
2. **NPÖ** ↔ Lifecare-Procapita (Synkronisering)
3. **Externa system** läser från NPÖ eller Lifecare-Procapita

## Kontaktpersoner
- **ÖSA** - Vård och omsorg (Lifecare-Procapita, NPÖ, Pascal, MCSS, Mina planer)
- **FSF** - Familj och socialförvaltning (Lifecare-Procapita, Phoniro Care)
- **KFSK** - Kommunföbundet Skåne (Mina planer, KomKat)
- **Inera** - NPÖ, Pascal
- **Ubejd Shala** - Sensorer (Sensio, Smooth lite)
- **Jens Klemedsson** - Viser

## Kritikalitet
- **Kritiskt (24/7):** Lifecare-Procapita, NPÖ, Pascal
- **Hög:** MCSS, Kuben
- **Medel:** Phoniro Care, Mina planer, KomKat
- **Låg:** Sensio, Smooth lite, Viser, Mateo, Senior alert

## Autentisering
- **Freja eID** → Lifecare-Procapita (SSO)
- **SITHS-kort** → NPÖ, Pascal, MCSS, Mina planer, KomKat

