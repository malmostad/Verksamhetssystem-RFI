# Process: Vårdhantering

## Översikt
Detta diagram visar processflödet för hur vård hanteras från registrering till uppföljning.

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
    participant Brukare as Brukare
    participant Life as Lifecare-Procapita<br/>Journal/Vård
    participant NPÖ as NPÖ<br/>Patientöversikt
    participant Kuben as Kuben<br/>Tidsplanering
    participant Pascal as Pascal<br/>Läkemedel
    participant MCSS as MCSS<br/>Signering
    participant Phoniro as Phoniro Care<br/>Uppföljning
    
    Note over Brukare,Phoniro: Vårdprocess - Steg för steg
    
    Brukare->>Life: Registreras som brukare
    Life->>Life: Skapa journal<br/>(Master data)
    
    Life->>NPÖ: Synkronisera patientdata<br/>(API HL7)
    NPÖ-->>Life: Bekräfta synkronisering
    
    Life->>Kuben: Skapa vårdbehov
    Kuben->>Kuben: Planera tider
    Kuben->>Life: Uppdatera tidsplanering<br/>(API/Databas)
    
    Life->>Pascal: Beställ läkemedel<br/>(API)
    Pascal->>Pascal: Hantera beställning
    Pascal-->>Life: Bekräfta beställning
    
    Life->>MCSS: Skapa signeringsuppgift<br/>(API)
    MCSS->>MCSS: Digital signering
    MCSS-->>Life: Bekräfta signering
    
    Life->>Phoniro: Skicka tidsdata<br/>(Batch)
    Phoniro->>Phoniro: Uppföljning av insatser
    
    Note over Life: Vårdprocess slutförd```

## Processsteg

### Steg 1: Registrering
- **System:** Lifecare-Procapita
- **Aktivitet:** 
  - Brukare registreras i systemet
  - Journal skapas (Master data)
  - Grundläggande information registreras
- **Output:** Brukare registrerad, journal skapad

### Steg 2: Patientdata-synkronisering
- **System:** Lifecare-Procapita ↔ NPÖ
- **Aktivitet:** 
  - Patientdata synkroniseras med NPÖ
  - Nationell patientöversikt uppdateras
  - HL7-standard används
- **Output:** Patientdata synkroniserad

### Steg 3: Tidsplanering
- **System:** Kuben → Lifecare-Procapita
- **Aktivitet:** 
  - Vårdbehov identifieras
  - Tider planeras i Kuben
  - Tidsplanering uppdateras i Lifecare-Procapita
- **Output:** Tidsplanering skapad

### Steg 4: Läkemedelsbeställning
- **System:** Lifecare-Procapita ↔ Pascal
- **Aktivitet:** 
  - Läkemedel beställs från Pascal
  - Beställning hanteras i Pascal
  - Status uppdateras i Lifecare-Procapita
- **Output:** Läkemedel beställt

### Steg 5: Digital signering
- **System:** Lifecare-Procapita ↔ MCSS
- **Aktivitet:** 
  - Signeringsuppgift skapas i MCSS
  - Personal signerar digitalt
  - Signering bekräftas i Lifecare-Procapita
- **Output:** Läkemedel signerat

### Steg 6: Uppföljning
- **System:** Lifecare-Procapita → Phoniro Care
- **Aktivitet:** 
  - Tidsdata skickas till Phoniro Care
  - Insatser följs upp
  - Resultat dokumenteras
- **Output:** Uppföljning genomförd

## Roller och Ansvar

| Roll | System | Ansvar |
|------|--------|--------|
| **Sjuksköterska** | Lifecare-Procapita | Registrera brukare, skapa journal |
| **Läkare** | NPÖ, Pascal | Granska patientdata, beställa läkemedel |
| **Planerare** | Kuben | Planera tider och vårdbehov |
| **Personal** | MCSS | Signera läkemedel digitalt |
| **Uppföljare** | Phoniro Care | Följa upp insatser |

## Tidslinje

```
Dag 1 - Registrering och planering
  - Brukare registreras i Lifecare-Procapita
  - Patientdata synkroniseras med NPÖ
  - Tidsplanering skapas i Kuben

Dag 2-7 - Vårdgenomförande
  - Läkemedel beställs via Pascal
  - Signering genomförs i MCSS
  - Vård genomförs enligt plan

Dag 8+ - Uppföljning
  - Tidsdata skickas till Phoniro Care
  - Insatser följs upp
  - Resultat dokumenteras
```

## Kvalitetsmått

- **Registreringstid:** < 30 minuter
- **Synkronisering:** Realtid med NPÖ
- **Tidsplanering:** Planerad inom 24 timmar
- **Läkemedelsbeställning:** Hanterad inom 4 timmar
- **Signering:** Genomförd inom 2 timmar
- **Uppföljning:** Genomförd inom 7 dagar

## Integrationer i Processen

### Kritiska Integrationer
1. **Lifecare-Procapita ↔ NPÖ**
   - Typ: API HL7
   - Frekvens: Realtid
   - Kritikalitet: Hög

2. **Lifecare-Procapita ↔ Pascal**
   - Typ: API
   - Frekvens: On-demand
   - Kritikalitet: Hög

3. **Kuben → Lifecare-Procapita**
   - Typ: API/Databas
   - Frekvens: Realtid
   - Kritikalitet: Medel

### Stödintegrationer
4. **Lifecare-Procapita → MCSS**
   - Typ: API
   - Frekvens: On-demand
   - Kritikalitet: Medel

5. **Lifecare-Procapita → Phoniro Care**
   - Typ: Batch
   - Frekvens: Daglig
   - Kritikalitet: Låg

## Problem och Lösningar

### Problem 1: Synkroniseringsfel
- **Orsak:** Brist på standardiserad datamodell
- **Lösning:** Implementera HL7 FHIR standard

### Problem 2: Dubbel registrering
- **Orsak:** Manuell registrering i flera system
- **Lösning:** Automatisk synkronisering

### Problem 3: Brist på realtidsdata
- **Orsak:** Batch-integrationer
- **Lösning:** Överväg API-integrationer för kritiska flöden

