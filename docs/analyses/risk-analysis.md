# 🔴 Riskanalys - Systemlandskap & Systembyte

## 🎯 Syfte

!!! danger "Riskhantering"
    Förstå risker för att kunna hantera dem proaktivt. Denna analys täcker både nuläge och risker vid systembyte.

**Metod**:
- 📋 Systemanalys
- 🎤 Intervjuer med verksamhet & IT
- 📊 Riskworkshop

---

## 🔴 Risker - Nuläge

### Risk 1️⃣: Systemberoenden

| Element | Värde |
|---------|-------|
| **Beschrivning** | Kritiska system är beroende av äldre system som kan bli ounderhållna |
| **Sannolikhet** | 🔴 Hög (60-80%) |
| **Påverkan** | 🔴 Hög (kritisk verksamhet) |
| **Risknivå** | 🔴 **KRITISK** |
| **Prioritet** | **1 - HÖGSTA** |

<div style="background-color: #FFEBEE; border-left: 4px solid #DC3545; padding: 12px; margin: 12px 0;">
<strong>⚠️ Exempel beroenden:</strong>
- Lifecare → Pascal (läkemedel)
- Kuben → Lifecare (schema)
- HRutan → Medvind (personal)
</div>

**Åtgärder**:
- ✅ Identifiera kritiska beroenden
- ✅ Planera ersättning/migrering
- ✅ Säkerställ leverantörsuppgift under övergång

---

### Risk 2️⃣: Datakvalitet

| Element | Värde |
|---------|-------|
| **Beskrivning** | Data är inkonsekvent eller felaktig p.g.a. manuell överföring |
| **Sannolikhet** | 🟡 Medel (40-60%) |
| **Påverkan** | 🔴 Hög (patientvård påverkas) |
| **Risknivå** | 🟠 **MEDEL-HÖG** |
| **Prioritet** | **2 - HÖG** |

**Problem**:
- 📊 8+ system överför data manuellt
- ❌ Ingen validering av data
- 🔄 Inkonsistens mellan system

**Åtgärder**:
- ✅ Implementera automatiserad överföring (API)
- ✅ Datakvalitetskontroll & validering
- ✅ Masterdata-principen

---

### Risk 3️⃣: Säkerhet

| Element | Värde |
|---------|-------|
| **Beskrivning** | Säkerhetsbrister i system och integrationer |
| **Sannolikhet** | 🟡 Medel (50%) |
| **Påverkan** | 🔴 Hög (GDPR, patientdata) |
| **Risknivå** | 🟠 **MEDEL-HÖG** |
| **Prioritet** | **2 - HÖG** |

**Identifierade brister**:
- 🔐 Många olika autentiseringsmetoder
- 🚫 Svaga lösenord
- ❌ Begränsat SSO-stöd
- 📊 Brist på tvåfaktorsauth

**Åtgärder**:
- ✅ Standardisera på Freja eID + SITHS
- ✅ Implementera tvåfaktorsautentisering
- ✅ Regelbundna säkerhetsgranskar

---

### Risk 4️⃣: Kunskapsförlust

| Element | Värde |
|---------|-------|
| **Beskrivning** | Kunskap om system försvinner när personal lämnar |
| **Sannolikhet** | 🟡 Medel (naturlig påverkan) |
| **Påverkan** | 🟡 Medel (kan leda till fel) |
| **Risknivå** | 🟡 **MEDEL** |
| **Prioritet** | **4 - MEDEL** |

**Åtgärder**:
- ✅ Dokumentera alla system (denna plattform)
- ✅ Kunskapsöverföring & mentorering
- ✅ Kontinuerlig uppdatering

---

## ⚠️ Risker - Vid Systembyte

### Risk 1️⃣: Datamigration

| Element | Värde |
|---------|-------|
| **Beskrivning** | Data går förlorad, korrupts eller blir inkonsekvent vid migration |
| **Sannolikhet** | 🟡 Medel (30-50%) |
| **Påverkan** | 🔴 Hög (verksamhet stannar) |
| **Risknivå** | 🟠 **MEDEL-HÖG** |
| **Prioritet** | **3 - HÖG** |

**Mitigering**:
- ✅ Tydlig, testerad migrationsplan
- ✅ Full backup före migrering
- ✅ Validering av migrerad data
- ✅ Rollback-procedur om fel uppstår

---

### Risk 2️⃣: Verksamhetsstopp

| Element | Värde |
|---------|-------|
| **Beskrivning** | Verksamheten stoppas under systembyte (larmhantering, vård påverkas) |
| **Sannolikhet** | 🟢 Låg (5-10% om planerat) |
| **Påverkan** | 🔴 Kritisk (patienter i fara) |
| **Risknivå** | 🟠 **MEDEL-HÖG** |
| **Prioritet** | **3 - HÖG** |

**Mitigering**:
- ✅ Parallel drift under övergång
- ✅ Stegvis migration per system
- ✅ Zero-downtime-arkitektur
- ✅ 24/7 support under implementering

---

### Risk 3️⃣: Integrationsproblem

| Element | Värde |
|---------|-------|
| **Beskrivning** | Integrationer fungerar inte med nytt system |
| **Sannolikhet** | 🟡 Medel (40-60%) |
| **Påverkan** | 🔴 Hög (många system påverkas) |
| **Risknivå** | 🟠 **MEDEL-HÖG** |
| **Prioritet** | **3 - HÖG** |

**Mitigering**:
- ✅ Kartlägg alla integrationer (redan gjort)
- ✅ Testa integrationer innan go-live
- ✅ Alternativa lösningar planerade
- ✅ API-first-princip

---

### Risk 4️⃣: Användaracceptans

| Element | Värde |
|---------|-------|
| **Beskrivning** | Användare accepterar inte eller motsätter sig nytt system |
| **Sannolikhet** | 🟡 Medel (40%) |
| **Påverkan** | 🟡 Medel (lägre produktivitet) |
| **Risknivå** | 🟡 **MEDEL** |
| **Prioritet** | **5 - MEDEL** |

**Mitigering**:
- ✅ Användarinvolvering från dag 1
- ✅ Omfattande utbildning
- ✅ Superanvändare & champions
- ✅ Kontinuerlig support

---

## 📊 Riskmatris - Prioritering

| Risk | Sannolikhet | Påverkan | Nivå | Prioritet | Status |
|------|-------------|----------|------|-----------|--------|
| 🔴 Systemberoenden | Hög | Hög | 🔴 Kritisk | **1** | 🔴 Öppen |
| 📊 Datakvalitet | Medel | Hög | 🟠 Medel-Hög | **2** | 🟡 Plan |
| 🔐 Säkerhet | Medel | Hög | 🟠 Medel-Hög | **2** | 🟡 Plan |
| 📦 Datamigration | Medel | Hög | 🟠 Medel-Hög | **3** | 🟡 Plan |
| 🔗 Integrationer | Medel | Hög | 🟠 Medel-Hög | **3** | 🟡 Plan |
| 💼 Kunskapsförlust | Medel | Medel | 🟡 Medel | **4** | ✅ Påbörjat |
| ⏸️ Verksamhetsstopp | Låg | Hög | 🟠 Medel-Hög | **3** | 🟡 Plan |
| 👥 Användaracceptans | Medel | Medel | 🟡 Medel | **5** | 🟡 Plan |

---

## 🎯 Åtgärdsplan per Prioritet

### 🔴 Prioritet 1: Systemberoenden (OMEDELBAR)

| Åtgärd | Tidslinje | Ansvarig | Resultat |
|--------|-----------|----------|----------|
| Kartlägg alla kritiska beroenden | Q1 | IT-arkitektur | 📋 Dokumenterat |
| Identifiera "slöa" system | Q1 | IT-drift | 📋 Klassificerat |
| Planera ersättning | Q2 | ITD-ledning | 🎯 Roadmap |
| Säkerställ leverantörsuppgift | Q2 | Upphandling | ✅ Kontrakt |

---

### 🟠 Prioritet 2: Datakvalitet & Säkerhet (HÖG)

| Åtgärd | Tidslinje | Ansvarig | Resultat |
|--------|-----------|----------|----------|
| Automatisera dataöverföring | Q2-Q3 | IT-arkitektur | ⚡ API-integrationer |
| Implementera datakvalitetskontroll | Q2 | IT-verksamhet | ✅ Validering |
| Expandera Freja eID | Q1-Q2 | IT-säkerhet | 🔐 SSO på flera system |
| Tvåfaktorsauth på känsliga system | Q3 | IT-säkerhet | 🔐 Skyddad access |

---

### 🟡 Prioritet 3-5: Migration & Övriga (MEDEL)

**Migrering, integrationer, användaracceptans**: Se migrationplan (separat dokument)

---

| Risk | Ägare | Monitor | Godkänd |
|------|-------|---------|---------|
| Systemberoenden | IT-ledning | IT-arkitektur | Director |
| Datakvalitet | IT-verksamhet | Qualitetsansvarig | Director |
| Säkerhet | IT-säkerhet | Säkerhetschef | CISO |
| Datamigration | Projektledare | Migrationsteam | Director |
| Verksamhetsstopp | Operationell ledning | On-call manager | Drift |
| Integrationer | IT-arkitektur | Integrationsteam | Director |
| Kunskapsförlust | HR + IT-drift | Kompetenscenter | HR-chef |
| Användaracceptans | Verksamhetsledning | Change manager | V-ledning |

---

## 🔗 Läs mer

- 📈 [Gap-analys](gap-analysis.md) - Vad behöver förbättras?
- 🚨 [Pain Points](pain-points.md) - Nuvarande problem
- 🗺️ [Systemlandskap](../systems/system-landscape.md) - Se alla system
- 🔗 [Integrationskarta](../systems/integrations.md) - Systemsamband
- 📊 [Masterdata](../systems/masterdata.md) - Datakvalitet

