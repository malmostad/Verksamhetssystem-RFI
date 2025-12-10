# Detaljerad Integrationskarta

## Översikt
Detta diagram visar alla kända integrationer mellan system med integrationstyp och dataströmmar.

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
graph LR
    subgraph "Larmcentral - Kritiska Integrationer"
        direction TB
        3CX[3CX<br/>Telefonväxel]
        ISM[Interview/ISM<br/>Larmmottagning]
        CMP[CMP<br/>Trygghetslarm]
        Guard[Guardtools<br/>Väktare]
        Milestone[Milestone<br/>Kameralarm]
        
        3CX -->|Realtid<br/>API| ISM
        ISM -->|Larmdata<br/>API/Batch| CMP
        ISM -->|Aviseringar<br/>API| Guard
        Milestone -->|Alarm<br/>Meddelandekö| ISM
    end
    
    subgraph Vard["🏥 Vård & Omsorg - Kritiska Integrationer"]
        direction TB
        Life["🏥 Lifecare-Procapita<br/>━━━━━━━━━━<br/>Journal/Vård"]
        NPÖ["📋 NPÖ<br/>━━━━━━━━━━<br/>Patientöversikt"]
        Pascal["💊 Pascal<br/>━━━━━━━━━━<br/>Läkemedel"]
        MCSS["✍️ MCSS<br/>━━━━━━━━━━<br/>Signering"]
        Kuben["⏰ Kuben<br/>━━━━━━━━━━<br/>Tidsplanering"]
        Phoniro["⏰ Phoniro Care<br/>━━━━━━━━━━<br/>Uppföljning"]
        
        Life <==>|"👤 Patientdata<br/>API HL7"| NPÖ
        Life <==>|"💊 Läkemedel<br/>API"| Pascal
        Life ==>|"✍️ Signering<br/>API"| MCSS
        Kuben ==>|"📅 Tidsplanering<br/>API/Databas"| Life
        Life ==>|"⏰ Tidsdata<br/>Batch"| Phoniro
    end
    
    subgraph Personal["👥 Personal & HR - Integrationer"]
        direction TB
        HR["👥 HRutan<br/>━━━━━━━━━━<br/>Personal"]
        Medvind["👥 Medvind<br/>━━━━━━━━━━<br/>Personal"]
        Visma["💼 Visma<br/>━━━━━━━━━━<br/>Rekrytering"]
        
        HR ==>|"📊 Personaldata<br/>Batch/Fil"| Medvind
        Visma ==>|"💼 Rekrytering<br/>API"| HR
    end
    
    subgraph Ekonomi["💰 Ekonomi - Integrationer"]
        direction TB
        Ekot["💰 Ekot<br/>━━━━━━━━━━<br/>Ekonomi"]
        Koll["📈 Koll-Qlikview<br/>━━━━━━━━━━<br/>Business Intelligence"]
        Stratsys["📊 Stratsys<br/>━━━━━━━━━━<br/>Statistik"]
        
        Ekot ==>|"📊 Ekonomidata<br/>Batch/Daglig"| Koll
        Ekot ==>|"📊 Ekonomidata<br/>Batch/Daglig"| Stratsys
    end
    
    subgraph Security["🔐 Säkerhet - Inloggning"]
        direction TB
        Freja["🔑 Freja eID<br/>━━━━━━━━━━<br/>SSO (Inloggningsmetod)"]
        SITHS["🆔 SITHS<br/>━━━━━━━━━━<br/>Kort (Inloggningsmetod)"]
        
        Freja -.->|"🔐 SSO/API"| HR
        Freja -.->|"🔐 SSO/API"| Life
        SITHS -.->|"🔐 Inloggning"| NPÖ
        SITHS -.->|"🔐 Inloggning"| Pascal
        SITHS -.->|"🔐 Inloggning"| MCSS
    end
    
    style ISM fill:#F44336,stroke:#C62828,stroke-width:4px,color:#FFFFFF
    style Life fill:#4CAF50,stroke:#2E7D32,stroke-width:4px,color:#FFFFFF
    style HR fill:#01351C,stroke:#01351C,stroke-width:4px,color:#FFFFFF
    style Ekot fill:#FF9800,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style Freja fill:#FFC107,stroke:#F57C00,stroke-width:3px,color:#000000
    style SITHS fill:#FF6F00,stroke:#E65100,stroke-width:3px,color:#FFFFFF
    
    style Larm fill:#FFEBEE,stroke:#F44336,stroke-width:3px
    style Vard fill:#E8F5E9,stroke:#4CAF50,stroke-width:3px
    style Personal fill:#E8F5E9,stroke:#01351C,stroke-width:3px
    style Ekonomi fill:#FFF3E0,stroke:#FF9800,stroke-width:3px
    style Security fill:#FFF9C4,stroke:#FFC107,stroke-width:3px```

## Integrationstyper och Teknologi

### API-integrationer (REST/SOAP)
- **Freja eID** → HRutan, Lifecare-Procapita (SSO/API)
- **NPÖ** ↔ Lifecare-Procapita (API HL7)
- **Pascal** ↔ Lifecare-Procapita (API)
- **MCSS** ↔ Lifecare-Procapita (API)
- **3CX** → Interview/ISM (Realtid API)
- **Interview/ISM** → CMP, Guardtools (API)

### Batch/Filöverföringar
- **Ekot** → Koll-Qlikview (Ekonomidata, daglig batch)
- **Ekot** → Stratsys (Ekonomidata, daglig batch)
- **HRutan** → Medvind (Personaldata, daglig batch)
- **Lifecare-Procapita** → Phoniro Care (Tidsdata, batch)

### Direkta databaslänkar
- **Interview/ISM** → CMP (Larmdata, direkt databas)
- **Kuben** → Lifecare-Procapita (Tidsplanering, direkt databas)

### Meddelandeköer
- **3CX** → Interview/ISM (Samtal, meddelandekö)
- **Milestone** → Interview/ISM (Alarm, meddelandekö)

## Kritikalitet per Integration

### Hög Kritikalitet (24/7, Realtid)
- 3CX → Interview/ISM
- Interview/ISM → CMP
- Lifecare-Procapita ↔ NPÖ
- Lifecare-Procapita ↔ Pascal
- Freja eID → HRutan, Lifecare-Procapita

### Medel Kritikalitet (Daglig, Batch)
- HRutan → Medvind
- Ekot → Koll-Qlikview
- Ekot → Stratsys
- Lifecare-Procapita → Phoniro Care

### Låg Kritikalitet (On-demand)
- Visma → HRutan
- Interview/ISM → Guardtools

