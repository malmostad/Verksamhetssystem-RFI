# Process: Larmhantering

## Översikt
Detta diagram visar processflödet för hur larm hanteras från inkommande larm till uppföljning.

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
sequenceDiagram
    participant T as Trygghetslarm<br/>(Neat)
    participant 3CX as 3CX<br/>Telefonväxel
    participant ISM as Interview/ISM<br/>Larmmottagning
    participant CMP as CMP<br/>Administration
    participant Guard as Guardtools<br/>Väktare
    participant Optinet as Optinet<br/>Ärendehantering
    participant Lime as Lime CRM<br/>Kunddatabas
    
    Note over T,Lime: Larmprocess - Steg för steg
    
    T->>3CX: Larm aktiveras<br/>(Realtid)
    3CX->>ISM: Inkommande samtal<br/>(Realtid API)
    
    ISM->>ISM: Registrera larm<br/>(Master data)
    
    ISM->>CMP: Skicka larmdata<br/>(API/Batch)
    CMP->>CMP: Administrera trygghetslarm
    
    ISM->>Guard: Avisera väktare<br/>(API)
    Guard->>Guard: Skapa larmorder
    
    ISM->>Optinet: Skapa ärende<br/>(API)
    Optinet->>Optinet: Boka tekniker
    
    ISM->>Lime: Hämta kunddata<br/>(API)
    Lime-->>ISM: Returnera kundinfo
    
    Note over ISM: Larm hanterat och registrerat```

## Processsteg

### Steg 1: Larm aktiveras
- **System:** Trygghetslarm (Neat)
- **Aktivitet:** Brukare aktiverar larm
- **Output:** Larm skickas till 3CX

### Steg 2: Telefonväxel tar emot
- **System:** 3CX
- **Aktivitet:** Telefonväxel tar emot inkommande samtal
- **Output:** Samtal dirigeras till ISM

### Steg 3: Larmmottagning
- **System:** Interview/ISM
- **Aktivitet:** 
  - Mottar larm från 3CX
  - Registrerar larm i systemet (Master)
  - Identifierar larmtyp (trygghetslarm, personlarm, inbrottslarm)
- **Output:** Larm registrerat, data skickas vidare

### Steg 4: Administration
- **System:** CMP
- **Aktivitet:** 
  - Tar emot larmdata från ISM
  - Administrerar trygghetslarm
  - Uppdaterar status
- **Output:** Larm administrerat

### Steg 5: Väktaravisering
- **System:** Guardtools
- **Aktivitet:** 
  - Tar emot avisering från ISM
  - Skapar larmorder
  - Aviserar väktare
- **Output:** Väktare aviserad

### Steg 6: Ärendehantering
- **System:** Optinet
- **Aktivitet:** 
  - Tar emot ärende från ISM
  - Bokar tekniker
  - Planerar åtgärd
- **Output:** Ärende skapat, tekniker bokade

### Steg 7: Kunddata
- **System:** Lime CRM
- **Aktivitet:** 
  - ISM hämtar kunddata
  - Visar fastighetsinformation
  - Visar avtal och kontaktuppgifter
- **Output:** Kunddata tillgänglig

## Roller och Ansvar

| Roll | System | Ansvar |
|------|--------|--------|
| **Larmoperatör** | Interview/ISM | Ta emot och registrera larm |
| **Administratör** | CMP | Administrera trygghetslarm |
| **Väktare** | Guardtools | Ta emot larmorder och agera |
| **Tekniker** | Optinet | Hantera tekniska ärenden |
| **Kundservice** | Lime CRM | Hantera kundinformation |

## Tidslinje

```
0:00 - Larm aktiveras (Trygghetslarm)
0:05 - 3CX tar emot samtal
0:10 - ISM registrerar larm
0:15 - CMP administrerar
0:20 - Guardtools aviserar väktare
0:25 - Optinet skapar ärende
0:30 - Lime CRM hämtar kunddata
```

## Kvalitetsmått

- **Svarstid:** < 30 sekunder från larm till registrering
- **Hanteringstid:** < 5 minuter från registrering till åtgärd
- **Uppföljning:** Alla larm följs upp inom 24 timmar

## Problem och Lösningar

### Problem 1: Lång svarstid
- **Orsak:** Brist på integration mellan system
- **Lösning:** Förbättra API-integrationer

### Problem 2: Dubbel registrering
- **Orsak:** Manuell registrering i flera system
- **Lösning:** Automatisk synkronisering

### Problem 3: Brist på kunddata
- **Orsak:** Lime CRM inte alltid tillgänglig
- **Lösning:** Cachning av kunddata i ISM

