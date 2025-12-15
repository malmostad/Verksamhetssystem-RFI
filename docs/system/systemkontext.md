# Systemkontext
## Malmö stad | Hälsa, Vård och Omsorg (HVOF)

Systemet ska fungera som centralt verksamhetssystem för vårdhantering, journalföring och verksamhetsstöd. Det ska integrera med befintliga system och stödja alla verksamhetsområden inom HVOF.

## Systemkontext

```mermaid
%%{init: {
  "flowchart": {
    "curve": "basis",
    "rankSpacing": 60,
    "nodeSpacing": 40
  }
}}%%
flowchart LR
    subgraph Users["Användare"]
        direction TB
        SK["Sjuksköterskor"]
        AT["Arbetsterapeuter"]
        FT["Fysioterapeuter"]
        P["Brukare/Patient"]
    end
    
    VS["Nytt Verksamhetssystem<br/>Centralt verksamhetssystem"]
    
    subgraph Right["Externa System"]
        direction TB
        
        subgraph Nat["Nationella System"]
            direction TB
            NPO["NPÖ"]
            PAS["Pascal"]
            FK["Förskrivningskollen"]
        end
        
        subgraph Reg["Regionala System"]
            direction TB
            MP["Mina Planer"]
            KR["Kvalitetsregister"]
        end
        
        subgraph Lok["Lokala System"]
            direction TB
            MCSS["MCSS<br/>Digital signering av läkemedelslistan"]
            WS["WebSESAM"]
            J["Journalföringssystem"]
            EK["Ekonomisystem"]
            HR["HR-system"]
        end
        
        subgraph Auth["Autentisering"]
            direction TB
            SITHS["SITHS eID"]
            FREJA["Freja eID"]
        end
        
        subgraph Larm["Larmcentral"]
            LS["Larmsystem"]
        end
    end
    
    SK --> VS
    AT --> VS
    FT --> VS
    P --> VS
    VS -->|"Primär"| NPO
    VS -->|"Primär"| PAS
    VS --> FK
    VS -->|"Sekundär"| MP
    VS -->|"Sekundär"| KR
    VS -->|"Primär"| MCSS
    VS --> WS
    VS -->|"Datamigration"| J
    VS --> EK
    VS --> HR
    VS -->|"Möjlig"| LS
    VS --> SITHS
    VS --> FREJA
```

Systemet ska fungera som central hub för vårddata och integrera med kritiska externa system för patientöversikt, läkemedel och digital signering av läkemedelslistan (MCSS). Integration med ekonomisystem och HR-system är nödvändig för kostnadsdata och personaladministration.

---

## Integrationer

Systemet måste integrera med ett stort antal befintliga system. Integrationerna är prioriterade enligt verksamhetskritiska behov.

### Integrationer per prioritet

| Prioritet | System | Syfte |
|-----------|--------|-------|
| **Primär** | NPÖ | Nationell patientöversikt |
| **Primär** | Pascal | Läkemedelshantering |
| **Primär** | MCSS | Digital signering av läkemedelslistan |
| **Sekundär** | Kvalitetsregister | Kvalitetssäkring |
| **Sekundär** | Mina Planer | Samordnad vårdplan |
| **Sekundär** | Tid- och insatsuppföljning | Planering och uppföljning |
| **Sekundär** | Välfärdsteknik | Trygghetslarm och välfärdsteknik |
| **Möjlig** | Larmcentral | Larmhantering |

**Totalt**: 30+ huvudintegrationer, 170+ tekniska kopplingar. Se [Behov och frågor](../rfi-material/behov-och-fragor.md#vara-behov-teknik-och-integration) för komplett lista.

---

## System som kommer att bytas

Flera system i nuvarande systemlandskap kommer att bytas ut. Detta påverkar planeringen för ett nytt verksamhetssystem och integrationsmöjligheter.

```mermaid
flowchart TB
    subgraph Byts["System som kommer att bytas"]
        Journal["Journalföringssystem"]
        Economy["Ekonomisystem"]
        Larm["Larmsystem"]
    end
    
    subgraph Behalls["System som behålls"]
        NPO["NPÖ"]
        Pascal["Pascal"]
        MCSS["Digital signering"]
        Planer["Mina Planer"]
        Kvalitet["Kvalitetsregister"]
        HR["HR-system"]
        WebSESAM["WebSESAM"]
    end
    
    System["Nytt Verksamhetssystem"]
    
    System -->|"Datamigration"| Journal
    System -->|"Integration"| Economy
    System -->|"Möjlig"| Larm
    System -->|"Primär"| NPO
    System -->|"Primär"| Pascal
    System -->|"Primär"| MCSS
    System -->|"Sekundär"| Planer
    System -->|"Sekundär"| Kvalitet
    System --> HR
    System --> WebSESAM
```

---

**Malmö stad | Hälsa, Vård och Omsorg (HVOF)**


