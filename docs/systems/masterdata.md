# 📊 Informationsmodell - Masterdata

## 🎯 Vad är masterdata?

!!! note "Definition"
    Masterdata är den auktoritativa källan för information inom varje domän. Denna modell beskriver viktiga informationsdomäner, deras relationer och ansvar i HVOFs systemlandskap.

Principen: **En master per datadomän** 👑

---

```mermaid
erDiagram
    PERSON ||--o{ VARDRELATION : har
    PERSON ||--o{ LARM : har
    PERSON ||--o{ TIDSREGISTRERING : har
    PERSON ||--o{ LAKEMEDEL : tar
    
    PERSON {
        string personnummer
        string namn
        string adress
        string telefon
    }
    
    VARDRELATION {
        string vardrelation_id
        string vardtyp
        date startdatum
        date slutdatum
    }
    
    LARM {
        string larm_id
        string larmtyp
        datetime tidpunkt
        string status
    }
    
    TIDSREGISTRERING {
        string registrering_id
        datetime starttid
        datetime sluttid
        string aktivitet
    }
    
    LAKEMEDEL {
        string lakemedel_id
        string namn
        string dos
        date startdatum
    }
    
    PERSONAL ||--o{ TIDSREGISTRERING : registrerar
    PERSONAL ||--o{ VARDRELATION : ansvarar
    
    PERSONAL {
        string personal_id
        string namn
        string roll
        string organisation
    }
    
    ARENDE ||--o{ DOKUMENT : innehaller
    ARENDE ||--o{ PERSON : relaterar
    
    ARENDE {
        string arende_id
        string arendetyp
        string status
        date skapad
    }
    
    DOKUMENT {
        string dokument_id
        string typ
        string innehall
        date skapad
    }
    
    EKONOMI ||--o{ ARENDE : relaterar
    
    EKONOMI {
        string ekonomi_id
        string kostnadsstalle
        decimal belopp
        date datum
    }
## 👥 Datadomäner - Översikt

| # | Domän | Master | Dataägare | Kritikalitet | Sekundära System |
|---|-------|--------|-----------|--------------|------------------|
| 1 | 👥 Personal | HRutan | HR/SEF | 🔴 Hög | Medvind, Visma, Lärkan |
| 2 | 🏥 Brukare/Patient | Lifecare | ÖSA/FSF | 🔴 Hög | NPÖ, Pascal, Kuben |
| 3 | 🩺 Vårddata | Lifecare | ÖSA/FSF | 🔴 Kritisk | Kuben, Phoniro Care |
| 4 | 🚨 Larmdata | Interview/ISM | Larmcentral | 🔴 Kritisk | 3CX, CMP, Guardtools |
| 5 | 💰 Ekonomi | Ekot | Ekonomi | 🟡 Medel | Koll-Qlikview, Stratsys |
| 6 | 📋 IT-ärenden | MSM/Marval | ITD | 🟡 Medel | — |
| 7 | 🏢 Fastigheter | Lime CRM | Larmcentral | 🟢 Låg | — |
| 8 | 📄 Dokument | Distribuerat | Varierande | 🟡 Medel | Platina, EcoTech |

!!! tip "Databeskyttning"
    Alla datadomäner innehåller känslig information (GDPR, säkerhet). Masterdatasystemen måste skyddas högt.

---

## 📐 Datarelationer - Modell

**Se ERDiagram ovan för relationerna mellan entiteterna.**

---

## 🎯 Datadomäner - Detaljer

### 1️⃣ Personal | 👥

### 1️⃣ Personal | 👥

| Element | Värde |
|---------|-------|
| **Master** | 🔑 HRutan |
| **Dataägare** | HR-avdelning / SEF |
| **Kritikalitet** | 🔴 Hög |
| **Volym** | ~350 aktiva + vikarier |

**Nyckeldata**:
- Personalnummer, namn, roll, organisation
- Kompetens, arbetsuppgifter, tidrapportering

**Sekundära system**:
- Medvind (tidsregistrering)
- Visma (rekrytering)
- Vikariebanken (timvikarier)
- Lärkan (utbildning)

---

### 2️⃣ Brukare/Patient | 🏥

| Element | Värde |
|---------|-------|
| **Master** | 🔑 Lifecare-Procapita |
| **Dataägare** | Äldreomsorg & Funktionsstöd (ÖSA/FSF) |
| **Kritikalitet** | 🔴 Kritisk |
| **Volym** | ~8000-10000 aktiva brukare |

**Nyckeldata**:
- Personnummer, namn, adress, kontaktuppgifter
- Vårdrelationer, vårdplan, behov

**Sekundära system**:
- NPÖ (patientöversikt)
- Pascal (läkemedel)
- Kuben (tidsplanering)

<div style="background-color: #E8F5E9; border-left: 4px solid #4CAF50; padding: 12px; margin: 12px 0;">
<strong>✅ Källa till sanning:</strong> Lifecare är enda källan för brukarinformation. Andra system är läsare.
</div>

---

### 3️⃣ Vårddata | 🩺

| Element | Värde |
|---------|-------|
| **Master** | 🔑 Lifecare-Procapita |
| **Dataägare** | Äldreomsorg & Funktionsstöd (ÖSA/FSF) |
| **Kritikalitet** | 🔴 Kritisk |
| **Standard** | HL7 FHIR, HSV-standarden |

**Nyckeldata**:
- Journalanteckningar, vårdplaner
- Insatser, tidsplanering, uppföljning
- Medicinering, undersökningar

**Sekundära system**:
- Kuben (tidsplanering)
- Phoniro Care (tid/insatsuppföljning)
- Mina planer (samordnad vårdplanering)

!!! warning "Säkerhetskritisk"
    Vårddata är känslig och ska bara lagras i Lifecare. Andra system får endast läsåtkomst via säkra API:er.

---

### 4️⃣ Läkemedel | 💊

| Element | Värde |
|---------|-------|
| **Masters** | 🔑 Pascal + MCSS (delat ansvar) |
| **Dataägare** | ÖSA/FSF |
| **Kritikalitet** | 🔴 Kritisk |
| **Regulation** | E-recept, SITHS-signering |

**Nyckeldata**:
- Läkemedelsbeställningar, dosering
- Digital signering, expedition
- Allergier, kontraindikationer

**Sekundära system**:
- Lifecare (patientjournal)
- MCSS (digital signering)

---

### 5️⃣ Larm & Trygghet | 🚨

| Element | Värde |
|---------|-------|
| **Master** | 🔑 Interview/ISM |
| **Dataägare** | Larmnav/Larmcentral |
| **Kritikalitet** | 🔴 Kritisk |
| **Volym** | 200-500 larm/dag |

**Nyckeldata**:
- Larmtyp, tidpunkt, status
- Hantering, uppföljning, sluttidpunkt

**Larmtyper**:
- 🚨 Personlarm (mobilt/armband)
- 🏠 Trygghetslarm (hemma)
- 🔒 Inbrottslarm (säkerhet)
- 📹 Kameralarm

**Sekundära system**:
- 3CX (telefoniöverföring)
- CMP (sensoröversikt)
- Guardtools (väktarsamordning)
- Milestone (kameralarm)

<div style="background-color: #FFEBEE; border-left: 4px solid #DC3545; padding: 12px; margin: 12px 0;">
<strong>🚨 Livskritisk:</strong> Denna system måste ha 99.9% tillgänglighet. Redundans och backup krävs.
</div>

---

### 6️⃣ Ekonomi | 💰

| Element | Värde |
|---------|-------|
| **Master** | 🔑 Ekot (Raindance) |
| **Dataägare** | Ekonomi-avdelning |
| **Kritikalitet** | 🟡 Medel |
| **Budget** | Årliga budgetar per kostnadsställe |

**Nyckeldata**:
- Kostnadsställen, budget, utgifter
- Fakturor, betalningar, rapportering

**Sekundära system**:
- Koll-Qlikview (BI & rapportering)
- Stratsys (statistik)

---

### 7️⃣ IT-Ärenden | 📋

| Element | Värde |
|---------|-------|
| **Master** | 🔑 MSM (Marval) |
| **Dataägare** | IT-avdelning (ITD) |
| **Kritikalitet** | 🟡 Medel |
| **Ärendetyper** | Support, förvaltning, projekt |

**Kopplade system**:
- Agera (incidentrapportering)
- Optinet (teknikerärenden)
- Avvikelsehanteringssystem

---

### 8️⃣ Dokument | 📄

| Element | Värde |
|---------|-------|
| **Master** | Distribuerat (inget centralt master) |
| **Dataägare** | Varierande per typ |
| **Kritikalitet** | 🟡 Medel |
| **Utmaning** | Fragmenterad, svår att hitta |

**System som hanterar**:
- Platina (nämndsfrågor)
- EcoTech (QMS & dokumenthantering)
- Adato (rehabärenden)
- Lifecare (journaldokument)

!!! danger "Problem"
    Dokumentation är fragmenterad över många system. Behöver standardiserad dokumenthantering.

---

## ⚠️ Datakvalitetsproblem

| Problem | Påverkan | Lösning | Prioritet |
|---------|----------|--------|----------|
| 🔴 Flera masters för samma data | Inkonsistens | Definiera ett master | 🔴 Hög |
| 📊 Brist på standardisering | Integreringsproblem | Adoptera standarder | 🔴 Hög |
| ✋ Manuell dataöverföring | Felrisker | Automatisera | 🔴 Hög |
| 🔍 Svag datakvalitetskontroll | Felaktig data | Implementera validering | 🟡 Medel |
| 📚 Distribuerad dokumentation | Svårfytt | Centralisera | 🟡 Medel |

---

## 🎯 Framtida målbild - Masterdata

### Principer

```mermaid
graph TB
    A["👑 En Master<br/>per Domän"] --> B["✅ Datakvalitet"]
    C["📊 Standardiserad<br/>Modell"] --> D["🔗 Enkel Integration"]
    E["✋ Automatiserad<br/>Överföring"] --> F["⏱️ Realtidsdata"]
    G["🔍 Quality Control<br/>Inbyggd"] --> H["🛡️ Säker Data"]
    
    B --> Resultat["🎉 Pålitlig Arkitektur"]
    D --> Resultat
    F --> Resultat
    H --> Resultat
```

### Migreringsplan

| Fas | Tidslinje | Fokus | Resultat |
|-----|-----------|-------|----------|
| **1. Definiera** | Q1 | Tydliga masters | 📋 Dokumenterat |
| **2. Standardisera** | Q2-Q3 | Datamodeller | 📊 Konsistent |
| **3. Automatisera** | Q4+ | API-överföringar | ⚡ Realtid |
| **4. Validera** | År 2+ | Kvalitetskontroll | ✅ Ren data |

---

## 🔗 Läs mer

- 🏗️ [Arkitekturprinciper](../overview/architecture-principles.md) - Masterdata-princip
- 🔗 [Integrationskarta](./integrations.md) - Dataflöden
- 🗺️ [Systemlandskap](./system-landscape.md) - Se alla system
- 🚨 [Pain Points](../analyses/pain-points.md) - Manuell överföring

