# Kärnprocesser - Översikt

## Översikt

Kärnprocesser är de huvudsakliga processerna som stödjer HVOF:s primära uppdrag.

# 🔄 Kärnprocesser - Översikt

## 📌 Vad är kärnprocesser?

!!! note "Definition"
    Kärnprocesser är de huvudsakliga processerna som stödjer HVOF:s primära uppdrag för äldre och personer med funktionsnedsättning.

---

## 📋 Processöversikt

| # | Process | Syfte | System | Detaljer |
|---|---------|-------|--------|----------|
| 🚨 | **Larmhantering** | Ta emot och hantera akuta larm | Interview/ISM, 3CX, CMP, Guardtools, Milestone | [Se detaljer](case-management.md) |
| 🏥 | **Vårdhantering** | Planera och genomföra vård & omsorg | Lifecare-Procapita, NPÖ, Pascal, MCSS, Kuben | [Se detaljer](follow-up.md) |
| 👥 | **Personalhantering** | Hantera personal och schema | HRutan, Medvind, Visma, Vikariebanken | [Se detaljer](onboarding.md) |

---

## 🔄 Processflöden

```mermaid
graph TB
    subgraph "Kärnprocesser i HVOF"
        Larm["🚨 Larmhantering<br/>(Akut respons)"]
        Vard["🏥 Vårdhantering<br/>(Långsiktig vård)"]
        Personal["👥 Personalhantering<br/>(Resursplanering)"]
    end
    
    Larm -->|Utlöser| Vard
    Personal -->|Resurser| Vard
    Personal -->|Beredskap| Larm
    
    style Larm fill:#EF5350,stroke:#C62828,stroke-width:3px,color:#FFFFFF
    style Vard fill:#66BB6A,stroke:#2E7D32,stroke-width:3px,color:#FFFFFF
    style Personal fill:#42A5F5,stroke:#1565C0,stroke-width:3px,color:#FFFFFF
```

---

## 🚨 Larmhantering

**Ansvar**: Mottagning och hantering av akuta larm från äldre och personer med behov

| Element | Detalj |
|---------|--------|
| **Huvudsystem** | Interview/ISM (larmmottagning) |
| **Integrerat med** | 3CX (telefoni), CMP (sensorer), Milestone (kamera), Guardtools (smartklockor) |
| **Tidskritisk** | Ja - måste hålla <5 min svarstid |
| **Operatörer** | ~15 personer i larmnav |
| **Volymer** | 200-500 larm/dag under säsong |

!!! info "Kritisk process"
    Detta är en kritisk process för patienternas säkerhet. Systembyte kräver noll-downtime-migrering.

[🔍 Läs mer om larmhantering →](case-management.md)

---

## 🏥 Vårdhantering

**Ansvar**: Planering, genomförande och uppföljning av vård och omsorgstjänster

| Element | Detalj |
|---------|--------|
| **Huvudsystem** | Lifecare-Procapita (journalföring) |
| **Integrerat med** | NPÖ (patientöversikt), Pascal (läkemedel), MCSS (hemtjänst), Kuben (schemaläggning) |
| **Användargrupper** | Sjuksköterskor, undersköterskor, rehabiliterare |
| **Antal användare** | ~200 aktiva |
| **Komplexitet** | Mycket hög - många integrationer |

<div style="background-color: #E3F2FD; border-left: 4px solid #1976D2; padding: 12px; margin: 12px 0;">
<strong>💡 Viktigt:</strong> Denna process är helt beroende av nätverk och pålitliga integrationer.
</div>

[🔍 Läs mer om vårdhantering →](follow-up.md)

---

## 👥 Personalhantering

**Ansvar**: Rekrytering, anställning, schemaläggning och HR-administration

| Element | Detalj |
|---------|--------|
| **Huvudsystem** | HRutan (HR-administration) |
| **Integrerat med** | Medvind (tidrapportering), Visma (löner), Vikariebanken (vikarier) |
| **HR-personal** | ~8 personer |
| **Omfattning** | ~350 anställda + vikarier |
| **Typ** | Icke-kritisk men affärsväsentlig |

[🔍 Läs mer om personalhantering →](onboarding.md)

---

## 🎯 Stödprocesser

!!! tip "Relaterade processer"
    Utöver kärnprocesserna finns också viktiga stödprocesser:
    - **Ärendehantering** (MSM/Marval)
    - **Ekonomihantering** (Ekot)
    - **Masterdata-hantering** (HR-data, patientdata)
    - **IT-drift** (Nätverk, säkerhet, backup)

---

## 📊 Systemintegrationer per process

```mermaid
graph LR
    subgraph "Larmhantering"
        ISM["Interview/ISM<br/>(Kärna)"]
        CX["3CX<br/>(Tel)"]
        CMP["CMP<br/>(Sensorer)"]
        ISM --> CX
        ISM --> CMP
    end
    
    subgraph "Vårdhantering"
        LC["Lifecare<br/>(Kärna)"]
        NPO["NPÖ<br/>(Pat.översikt)"]
        Pascal["Pascal<br/>(Läk)"]
        Kuben["Kuben<br/>(Schema)"]
        LC --> NPO
        LC --> Pascal
        LC --> Kuben
    end
    
    subgraph "Personalhantering"
        HR["HRutan<br/>(Kärna)"]
        Medvind["Medvind<br/>(Tider)"]
        Visma["Visma<br/>(Löner)"]
        HR --> Medvind
        HR --> Visma
    end
    
    style ISM fill:#EF5350,color:#FFF
    style LC fill:#66BB6A,color:#FFF
    style HR fill:#42A5F5,color:#FFF
```

---

## 🔗 Relaterade dokument

- 🗺️ [Systemlandskap](../../systems/system-landscape.md)
- 📊 [Processdiagram](../../diagrams/process/)
- 🏗️ [Arkitekturprinciper](../../overview/architecture-principles.md)
- 📈 [Integrationskarta](../../systems/integrations.md)

