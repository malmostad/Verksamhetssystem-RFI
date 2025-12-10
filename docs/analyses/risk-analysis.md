# Riskanalys

## Översikt

Identifierade risker i nuvarande systemlandskap och vid systembyte.

## Syfte

Förstå risker för att kunna hantera dem proaktivt.

## Metod

- Systemanalys
- Intervjuer
- Riskworkshop

## Risker - Nuläge

### 1. Systemberoenden

**Risk**: Kritiska system är beroende av äldre system.

**Sannolikhet**: Hög
**Påverkan**: Hög
**Risknivå**: 🔴 Hög

**Beskrivning**: Många system är beroende av äldre system som kan bli ounderhållna.

**Åtgärder**:
- Identifiera kritiska beroenden
- Planera ersättning
- Säkerställ support

### 2. Datakvalitet

**Risk**: Data är inkonsekvent eller felaktig.

**Sannolikhet**: Medel
**Påverkan**: Hög
**Risknivå**: 🟠 Medel-Hög

**Beskrivning**: Manuell dataöverföring leder till fel.

**Åtgärder**:
- Automatiserad dataöverföring
- Validering av data
- Masterdata-princip

### 3. Säkerhet

**Risk**: Säkerhetsbrister i system och integrationer.

**Sannolikhet**: Medel
**Påverkan**: Hög
**Risknivå**: 🟠 Medel-Hög

**Beskrivning**: Många olika autentiseringsmetoder och begränsad säkerhet.

**Åtgärder**:
- Standardisera autentisering
- Tvåfaktorsautentisering
- Säkerhetsgranskningar

### 4. Kunskapsförlust

**Risk**: Kunskap om system försvinner när personal lämnar.

**Sannolikhet**: Medel
**Påverkan**: Medel
**Risknivå**: 🟡 Medel

**Beskrivning**: Begränsad dokumentation och kunskap.

**Åtgärder**:
- Dokumentera system
- Kunskapsöverföring
- Uppdatera dokumentation

## Risker - Vid systembyte

### 1. Datamigration

**Risk**: Data går förlorad eller korrupts vid migration.

**Sannolikhet**: Medel
**Påverkan**: Hög
**Risknivå**: 🟠 Medel-Hög

**Åtgärder**:
- Tydlig migrationsplan
- Testning
- Backup och återställning

### 2. Verksamhetsstopp

**Risk**: Verksamheten stoppas under systembyte.

**Sannolikhet**: Låg
**Påverkan**: Hög
**Risknivå**: 🟡 Medel

**Åtgärder**:
- Parallel drift
- Stegvis migration
- Rollback-plan

### 3. Integrationer

**Risk**: Integrationer fungerar inte med nytt system.

**Sannolikhet**: Medel
**Påverkan**: Hög
**Risknivå**: 🟠 Medel-Hög

**Åtgärder**:
- Kartlägg integrationer
- Testa integrationer
- Alternativa lösningar

### 4. Användaracceptans

**Risk**: Användare accepterar inte nytt system.

**Sannolikhet**: Medel
**Påverkan**: Medel
**Risknivå**: 🟡 Medel

**Åtgärder**:
- Användarinvolvering
- Utbildning
- Support

## Riskmatris

| Risk | Sannolikhet | Påverkan | Risknivå | Prioritet |
|------|-------------|----------|----------|-----------|
| Systemberoenden | Hög | Hög | 🔴 Hög | 1 |
| Datakvalitet | Medel | Hög | 🟠 Medel-Hög | 2 |
| Säkerhet | Medel | Hög | 🟠 Medel-Hög | 2 |
| Datamigration | Medel | Hög | 🟠 Medel-Hög | 3 |
| Integrationer | Medel | Hög | 🟠 Medel-Hög | 3 |
| Kunskapsförlust | Medel | Medel | 🟡 Medel | 4 |
| Verksamhetsstopp | Låg | Hög | 🟡 Medel | 5 |
| Användaracceptans | Medel | Medel | 🟡 Medel | 6 |

## Åtgärdsplan

### Prioritet 1: Systemberoenden

- [ ] Identifiera kritiska beroenden
- [ ] Planera ersättning
- [ ] Säkerställ support

### Prioritet 2: Datakvalitet och Säkerhet

- [ ] Automatiserad dataöverföring
- [ ] Standardisera autentisering
- [ ] Säkerhetsgranskningar

### Prioritet 3: Systembyte

- [ ] Tydlig migrationsplan
- [ ] Kartlägg integrationer
- [ ] Testning

## Relaterade dokument

- [Gap-analys](gap-analysis.md)
- [Pain Points](pain-points.md)
- [Systemlandskap](../systems/system-landscape.md)

## Kontakt

För frågor om risker, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

