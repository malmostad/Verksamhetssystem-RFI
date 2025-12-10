# Kritikalitet - Systemprioritering

## Översikt
Detta diagram visar systemens kritikalitet baserat på verksamhetspåverkan och driftkrav.

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
    subgraph Kritisk["KRITISKT - 24/7 Drift"]
        direction LR
        K1["3CX<br/>Telefonväxel<br/>Nedtid: mindre än 1 timme"]
        K2["Interview-ISM<br/>Larmmottagning<br/>Nedtid: mindre än 1 timme"]
        K3["Lifecare-Procapita<br/>Journal-Vård<br/>Nedtid: mindre än 1 timme"]
        K4["CMP<br/>Trygghetslarm<br/>Nedtid: mindre än 1 timme"]
    end
    
    subgraph Hog["HÖG PRIORITET - Daglig drift"]
        direction LR
        H1["HRutan<br/>Personal<br/>Nedtid: mindre än 4 timmar"]
        H2["Ekot<br/>Ekonomi<br/>Nedtid: mindre än 4 timmar"]
        H3["Freja eID<br/>Inloggningsmetod<br/>Nedtid: mindre än 4 timmar"]
        H4["NPÖ<br/>Patientöversikt<br/>Nedtid: mindre än 4 timmar"]
        H5["Pascal<br/>Läkemedel<br/>Nedtid: mindre än 4 timmar"]
    end
    
    subgraph Medel["MEDEL PRIORITET - Viktiga stödsystem"]
        direction LR
        M1["MSM-Marval<br/>IT-ärenden<br/>Nedtid: mindre än 24 timmar"]
        M2["Kuben<br/>Tidsplanering<br/>Nedtid: mindre än 24 timmar"]
        M3["Milestone<br/>Kameralarm<br/>Nedtid: mindre än 24 timmar"]
        M4["Guardtools<br/>Väktare<br/>Nedtid: mindre än 24 timmar"]
        M5["MCSS<br/>Signering<br/>Nedtid: mindre än 24 timmar"]
    end
    
    subgraph Lag["LÅG PRIORITET - Stödsystem"]
        direction LR
        L1["Optinet<br/>Ärendehantering<br/>Nedtid: mindre än 48 timmar"]
        L2["Phoniro Care<br/>Uppföljning<br/>Nedtid: mindre än 48 timmar"]
        L3["Lime CRM<br/>Kunddatabas<br/>Nedtid: mindre än 48 timmar"]
        L4["EcoTech<br/>Kvalitet<br/>Nedtid: mindre än 48 timmar"]
        L5["Medvind<br/>Personal<br/>Nedtid: mindre än 48 timmar"]
    end
    
    style K1 fill:#D32F2F,stroke:#B71C1C,stroke-width:5px,color:#FFFFFF
    style K2 fill:#D32F2F,stroke:#B71C1C,stroke-width:5px,color:#FFFFFF
    style K3 fill:#D32F2F,stroke:#B71C1C,stroke-width:5px,color:#FFFFFF
    style K4 fill:#D32F2F,stroke:#B71C1C,stroke-width:5px,color:#FFFFFF
    
    style H1 fill:#F57C00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style H2 fill:#F57C00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style H3 fill:#F57C00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style H4 fill:#F57C00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style H5 fill:#F57C00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    
    style M1 fill:#FBC02D,stroke:#F57F17,stroke-width:3px,color:#000000
    style M2 fill:#FBC02D,stroke:#F57F17,stroke-width:3px,color:#000000
    style M3 fill:#FBC02D,stroke:#F57F17,stroke-width:3px,color:#000000
    style M4 fill:#FBC02D,stroke:#F57F17,stroke-width:3px,color:#000000
    style M5 fill:#FBC02D,stroke:#F57F17,stroke-width:3px,color:#000000
    
    style L1 fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    style L2 fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    style L3 fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    style L4 fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    style L5 fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    
    style Kritisk fill:#FFEBEE,stroke:#D32F2F,stroke-width:4px
    style Hog fill:#FFF3E0,stroke:#F57C00,stroke-width:3px
    style Medel fill:#FFFDE7,stroke:#FBC02D,stroke-width:2px
    style Lag fill:#FAFAFA,stroke:#9E9E9E,stroke-width:2px
```

## Kritikalitetsdefinitioner

### KRITISKT (Röd) - 24/7 Drift
System som måste vara tillgängliga dygnet runt. Nedtid påverkar verksamheten omedelbart.

**System:**
- **3CX** - Telefonväxel (Larmcentral)
- **Interview/ISM** - Larmmottagning (Master)
- **Lifecare-Procapita** - Journal/Vård (Master)
- **CMP** - Trygghetslarm administration

**Krav:**
- 99.9% tillgänglighet
- Realtid monitoring
- Automatisk redundans
- Snabb återställning (< 1 timme)

### HÖG PRIORITET (Orange) - Daglig drift
System som används dagligen och påverkar verksamheten vid nedtid.

**System:**
- **HRutan** - Personal (Master)
- **Ekot** - Ekonomi (Master)
- **Freja eID** - Säker inloggning
- **NPÖ** - Patientöversikt
- **Pascal** - Läkemedel

**Krav:**
- 99% tillgänglighet
- Daglig monitoring
- Återställning inom 4 timmar

### MEDEL PRIORITET (Gul) - Viktiga stödsystem
System som är viktiga men kan hanteras med begränsad funktionalitet.

**System:**
- **MSM/Marval** - IT-ärenden
- **Kuben** - Tidsplanering
- **Milestone** - Kameralarm
- **Guardtools** - Väktare
- **MCSS** - Signering

**Krav:**
- 95% tillgänglighet
- Veckovis monitoring
- Återställning inom 24 timmar

### LÅG PRIORITET (Beige) - Stödsystem
System som kan vara nere utan omedelbar verksamhetspåverkan.

**System:**
- **Optinet** - Ärendehantering
- **Phoniro Care** - Uppföljning
- **Lime CRM** - Kunddatabas
- **EcoTech** - Kvalitet
- **Medvind** - Personal

**Krav:**
- 90% tillgänglighet
- Månadsvis monitoring
- Återställning inom 48 timmar

## Nedtidspåverkan

| Kritikalitet | Max Nedtid | Verksamhetspåverkan | Återställning |
|--------------|------------|---------------------|---------------|
| **Kritiskt** | < 1 timme | Omedelbar | < 1 timme |
| **Hög** | < 4 timmar | Daglig verksamhet | < 4 timmar |
| **Medel** | < 24 timmar | Begränsad funktionalitet | < 24 timmar |
| **Låg** | < 48 timmar | Minimal påverkan | < 48 timmar |

## Beroenden

### Kritiska Beroenden
- **3CX** → Interview/ISM (Kritisk integration)
- **Interview/ISM** → CMP (Kritisk integration)
- **Lifecare-Procapita** ↔ NPÖ, Pascal (Kritiska integrationer)
- **Freja eID** → HRutan, Lifecare-Procapita (Kritisk inloggning)

### Kaskadeffekter
Om ett kritiskt system faller:
- **3CX nere** → Interview/ISM kan inte ta emot samtal
- **Interview/ISM nere** → CMP kan inte administrera larm
- **Lifecare-Procapita nere** → NPÖ, Pascal kan inte synkronisera
- **Freja eID nere** → Användare kan inte logga in

