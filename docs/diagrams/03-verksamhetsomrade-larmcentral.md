# Verksamhetsområde: Larmcentral

## Översikt
Detta diagram visar alla system och integrationer specifikt för Larmcentral-verksamheten.

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
    subgraph "Larmcentral - Systemlandskap"
        direction TB
        
        subgraph "Inkommande Larm"
            Trygghetslarm[Trygghetslarm<br/>Neat]
            Personlarm[Personlarm]
            Inbrottslarm[Inbrottslarm]
        end
        
        subgraph "Larmmottagning"
            3CX[3CX<br/>Telefonväxel]
            ISM[Interview/ISM<br/>Larmmottagning<br/>MASTER]
        end
        
        subgraph "Larmhantering"
            CMP[CMP<br/>Trygghetslarm Admin]
            Guard[Guardtools<br/>Väktaraviseringar]
            Optinet[Optinet<br/>Ärendehantering]
        end
        
        subgraph "Bevakning & Tillsyn"
            Milestone[Milestone<br/>Kameralarm]
            Securecloud[Securecloud<br/>Securia]
        end
        
        subgraph "Stödjande System"
            Lime[Lime CRM<br/>Kunddatabas]
            EcoTech[EcoTech<br/>Kvalitet/Dokument]
        end
        
        Trygghetslarm -->|Larm| 3CX
        Personlarm -->|Larm| 3CX
        Inbrottslarm -->|Larm| 3CX
        
        3CX -->|Inkommande samtal<br/>Realtid| ISM
        ISM -->|Larmdata<br/>API| CMP
        ISM -->|Aviseringar<br/>API| Guard
        ISM -->|Ärenden<br/>API| Optinet
        
        Milestone -->|Alarm<br/>Meddelandekö| ISM
        Securecloud -->|Larmdata| ISM
        
        CMP -->|Administration| Trygghetslarm
        
        Lime -->|Kunddata| ISM
        EcoTech -->|Dokument| ISM
    end
    
    style ISM fill:#ffc6c6,stroke:#bd0909,stroke-width:4px
    style 3CX fill:#ff9999,stroke:#bd0909,stroke-width:2px
    style CMP fill:#ff9999,stroke:#bd0909,stroke-width:2px```

## System i Larmcentral

### Kärnsystem
1. **Interview/ISM** (Master)
   - Larmmottagningsystem
   - Tar emot larm från 3CX
   - Skickar vidare till CMP, Guardtools
   - Kontakt: Rasmus Svensson, Sten Möller, Jonas
   - Org: HVOF/SEF

2. **3CX** (Kritiskt)
   - Telefonväxel
   - Tar emot inkommande samtal från trygghetslarm
   - Skickar vidare till ISM
   - Kontakt: Patrik Wiren, Sten Möller
   - Org: HVOF

### Stödsystem
3. **CMP** - Remote administration trygghetslarm
4. **Guardtools** - Väktaraviseringar, larmorder
5. **Optinet** - Ärendehantering och bokning för tekniker
6. **Milestone** - Kameralarm, digital tillsyn
7. **Securecloud** - Securia (molntjänst)
8. **Lime CRM** - Kunddatabas för fastighetsägare
9. **EcoTech** - Kvalitet och dokumenthantering

## Processflöde

### Larmprocess
1. **Larm inkommer** → Trygghetslarm/Personlarm/Inbrottslarm
2. **3CX tar emot** → Telefonväxel dirigerar samtal
3. **ISM mottar** → Larmmottagningsystem registrerar
4. **CMP administrerar** → Remote administration av trygghetslarm
5. **Guardtools aviserar** → Väktare får order
6. **Optinet hanterar** → Ärendehantering för tekniker

### Bevakningsprocess
1. **Milestone detekterar** → Kameralarm triggas
2. **Alarm skickas** → Till ISM via meddelandekö
3. **ISM hanterar** → Larmmottagning och registrering

## Kontaktpersoner
- **Patrik Wiren** - Larmcentralen (3CX, CMP, Guardtools, Optinet, Lime CRM, EcoTech)
- **Rasmus Svensson** - Larmcentralen (ISM, Milestone, Securecloud)
- **Sten Möller** - Larmcentralen (3CX, ISM, Milestone)
- **Jonas** - Larmcentralen (ISM, Milestone, Securecloud)

## Kritikalitet
- **Kritiskt (24/7):** 3CX, Interview/ISM, CMP
- **Hög:** Guardtools, Milestone
- **Medel:** Optinet, Securecloud, Lime CRM, EcoTech

