# Autentiseringsflöde

## Översikt
Detta diagram visar hur användare autentiserar sig till olika system och vilka autentiseringsmetoder som används.

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
    subgraph "Autentiseringsmetoder"
        Freja[Freja eID<br/>LOA 2/3<br/>SSO]
        SITHS[SITHS-kort<br/>+ PIN]
        AD[AD-inloggning<br/>Active Directory]
        UserPass[Användarnamn<br/>+ Lösenord]
        MSAuth[MS Authenticator<br/>+ Lösenord]
    end
    
    subgraph Central["🏢 Centrala System"]
        direction TB
        HR["👥 HRutan<br/>━━━━━━━━━━<br/>Personal"]
        Life["🏥 Lifecare-Procapita<br/>━━━━━━━━━━<br/>Journal/Vård"]
        Ekot["💰 Ekot<br/>━━━━━━━━━━<br/>Ekonomi"]
        ISM["🚨 Interview/ISM<br/>━━━━━━━━━━<br/>Larm"]
        MSM["💻 MSM/Marval<br/>━━━━━━━━━━<br/>IT-ärenden"]
    end
    
    subgraph Vard["🏥 Vårdtjänster"]
        direction TB
        NPÖ["📋 NPÖ<br/>━━━━━━━━━━<br/>Patientöversikt"]
        Pascal["💊 Pascal<br/>━━━━━━━━━━<br/>Läkemedel"]
        MCSS["✍️ MCSS<br/>━━━━━━━━━━<br/>Signering"]
        KomKat["📚 KomKat<br/>━━━━━━━━━━<br/>HSA Katalog"]
        MinaPlaner["📅 Mina planer<br/>━━━━━━━━━━<br/>Vårdplanering"]
    end
    
    subgraph Cloud["☁️ Molntjänster"]
        direction TB
        CMP["🔔 CMP<br/>━━━━━━━━━━<br/>Trygghetslarm"]
        Kuben["⏰ Kuben<br/>━━━━━━━━━━<br/>Tidsplanering"]
        Avvikelse["⚠️ Avvikelsehanteringssystem"]
    end
    
    Freja -.->|"🔐 SSO<br/>Enkel inloggning"| HR
    Freja -.->|"🔐 SSO<br/>Enkel inloggning"| Life
    Freja -.->|"🔐 SSO<br/>Enkel inloggning"| Medvind["👥 Medvind<br/>Personal"]
    
    SITHS -.->|"🆔 SITHS<br/>Kort + PIN"| NPÖ
    SITHS -.->|"🆔 SITHS<br/>Kort + PIN"| Pascal
    SITHS -.->|"🆔 SITHS<br/>Kort + PIN"| MCSS
    SITHS -.->|"🆔 SITHS<br/>Kort + PIN"| KomKat
    SITHS -.->|"🆔 SITHS<br/>Kort + PIN"| MinaPlaner
    
    AD -.->|"💼 AD<br/>Windows"| Avvikelse
    
    UserPass -.->|"🔓 Lösenord"| Ekot
    UserPass -.->|"🔓 Lösenord"| ISM
    UserPass -.->|"🔓 Lösenord"| MSM
    UserPass -.->|"🔓 Lösenord"| CMP
    UserPass -.->|"🔓 Lösenord"| Guardtools["👮 Guardtools<br/>Väktare"]
    UserPass -.->|"🔓 Lösenord"| Optinet["🔧 Optinet<br/>Ärendehantering"]
    
    MSAuth -.->|"📱 2FA<br/>Tvåfaktors"| CMP
    MSAuth -.->|"📱 2FA + AD"| Kuben
    
    style Freja fill:#FFC107,stroke:#F57C00,stroke-width:4px,color:#000000
    style SITHS fill:#FF6F00,stroke:#E65100,stroke-width:4px,color:#FFFFFF
    style AD fill:#9E9E9E,stroke:#616161,stroke-width:3px,color:#FFFFFF
    style UserPass fill:#E0E0E0,stroke:#9E9E9E,stroke-width:2px,color:#212121
    style MSAuth fill:#4CAF50,stroke:#388E3C,stroke-width:3px,color:#FFFFFF
    
    style Auth fill:#FFF9C4,stroke:#F57C00,stroke-width:3px
    style Central fill:#E8F5E9,stroke:#01351C,stroke-width:2px
    style Vard fill:#E8F5E9,stroke:#4CAF50,stroke-width:2px
    style Cloud fill:#F3E5F5,stroke:#9C27B0,stroke-width:2px```

## Autentiseringsmetoder

### 1. Freja eID (LOA 2/3) - SSO
**Säkerhetsnivå:** Hög  
**Används för:**
- HRutan (Personal)
- Lifecare-Procapita (Journal/Vård)
- Medvind (Personal)

**Fördelar:**
- Enkel inloggning (SSO)
- Hög säkerhet (LOA 2/3)
- Centraliserad hantering

### 2. SITHS-kort + PIN
**Säkerhetsnivå:** Mycket hög  
**Används för:**
- NPÖ (Patientöversikt)
- Pascal (Läkemedel)
- MCSS (Signering)
- KomKat (HSA Katalog)
- Mina planer (Vårdplanering)

**Fördelar:**
- Mycket hög säkerhet
- Krävs för vårddata
- Fysiskt kort + PIN

### 3. AD-inloggning (Active Directory)
**Säkerhetsnivå:** Medel  
**Används för:**
- Avvikelsehanteringssystem/Synpunktssystem

**Fördelar:**
- Integrerat med Windows
- Centraliserad användarhantering

### 4. Användarnamn + Lösenord
**Säkerhetsnivå:** Låg-Medel  
**Används för:**
- Ekot (Ekonomi)
- Interview/ISM (Larm)
- MSM/Marval (IT-ärenden)
- CMP (Trygghetslarm)
- Guardtools (Väktare)
- Optinet (Ärendehantering)
- Många fler system

**Fördelar:**
- Enkelt att använda
- Ingen extra hårdvara

**Nackdelar:**
- Lägre säkerhet
- Många olika lösenord

### 5. MS Authenticator + Lösenord
**Säkerhetsnivå:** Hög  
**Används för:**
- CMP (Trygghetslarm)
- Kuben (Tidsplanering) + AD

**Fördelar:**
- Tvåfaktorsautentisering
- App-baserad

## Autentiseringsflöden

### Flöde 1: Personal (HRutan)
```
Användare → Freja eID (SSO) → HRutan
```

### Flöde 2: Vård (Lifecare-Procapita)
```
Användare → Freja eID (SSO) → Lifecare-Procapita
```

### Flöde 3: Vårdtjänster (NPÖ, Pascal)
```
Användare → SITHS-kort + PIN → NPÖ/Pascal
```

### Flöde 4: Larmcentral (Interview/ISM)
```
Användare → Användarnamn + Lösenord → Interview/ISM
```

### Flöde 5: Trygghetslarm (CMP)
```
Användare → MS Authenticator + Lösenord → CMP
```

## Säkerhetsrekommendationer

### Förbättringar
1. **Standardisera autentisering**
   - Minska antalet olika metoder
   - Prioritera Freja eID för fler system

2. **Förbättra lösenordshanteringen**
   - Implementera lösenordshanterare
   - Kräv starka lösenord

3. **Tvåfaktorsautentisering**
   - Utöka MS Authenticator till fler system
   - Överväg SITHS för känslig data

4. **Centraliserad inloggning**
   - Utöka SSO (Freja eID) till fler system
   - Minska antalet separata inloggningar

## Användargrupper och Autentisering

| Användargrupp | Primär Metod | Sekundär Metod |
|---------------|--------------|----------------|
| **Personal/HR** | Freja eID | Användarnamn + Lösenord |
| **Vårdpersonal** | Freja eID, SITHS | Användarnamn + Lösenord |
| **Läkare** | SITHS | Freja eID |
| **Larmcentral** | Användarnamn + Lösenord | MS Authenticator |
| **IT** | AD, Användarnamn + Lösenord | - |
| **Administration** | Användarnamn + Lösenord | - |

