# Kärnprocesser - Översikt

## Översikt

Kärnprocesser är de huvudsakliga processerna som stödjer HVOF:s primära uppdrag.

## Processer

### 1. Larmhantering

**Beskrivning**: Processen för att ta emot, hantera och följa upp larm.

**System**: Interview/ISM, 3CX, CMP, Guardtools, Milestone

**Se**: [Larmhantering](case-management.md)

### 2. Vårdhantering

**Beskrivning**: Processen för att planera, genomföra och följa upp vård och omsorg.

**System**: Lifecare-Procapita, NPÖ, Pascal, MCSS, Kuben

**Se**: [Vårdhantering](follow-up.md)

### 3. Personalhantering

**Beskrivning**: Processen för att rekrytera, anställa och hantera personal.

**System**: HRutan, Medvind, Visma, Vikariebanken

**Se**: [Personalhantering](onboarding.md)

## Processkarta

```mermaid
graph TB
    subgraph "Kärnprocesser"
        Larm[🚨 Larmhantering]
        Vard[🏥 Vårdhantering]
        Personal[👥 Personalhantering]
    end
    
    Larm -->|Data| Vard
    Personal -->|Personaldata| Vard
    Personal -->|Personaldata| Larm
    
    style Larm fill:#F44336,stroke:#C62828,stroke-width:3px,color:#FFFFFF
    style Vard fill:#4CAF50,stroke:#2E7D32,stroke-width:3px,color:#FFFFFF
    style Personal fill:#01351C,stroke:#01351C,stroke-width:3px,color:#FFFFFF
```

## Relaterade dokument

- [Systemlandskap](../systems/system-landscape.md)
- [Processdiagram](../diagrams/process/)

