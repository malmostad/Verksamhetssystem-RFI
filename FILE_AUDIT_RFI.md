# Verksamhetssystem-RFI - Filgranskning & Reorganiseringsplan

**Datum:** 2024  
**Syfte:** Analysera alla befintliga filer och organisera för optimal RFI-fokus  
**Status:** Granskning slutförd - Rekommendationer klara

---

## 📊 Sammanfattning

**Totalt antal markdown-filer:** 157  
**Organiserade i:** 13 huvudkategorier  
**Navigationspunkter (mkdocs.yml):** 6 toppnivåsektioner

### Kvalitetsmetriker
- ✅ **Refererade filer:** 65 (filer som är länkade i mkdocs.yml nav)
- ⚠️ **Ej refererade filer:** 92 (orphaned files - inte i huvudnavigation)
- 🔴 **Filnamn med kodningsproblem:** 12 (special characters)

---

## 1. HUVUDKATEGORIER OCH FILÖVERSIKT

### A. RFI-MATERIAL (5 filer - KÄRNKRITISKA)
**Syfte:** Direktstöd för RFI-processen - högsta prioritet  
**Navigationsstatus:** ✅ Alla länkade

```
rfi-rfp/
├── rfi-material.md              ✅ RFI-dokumentation (huvudenterepunkt)
├── requirements-list.md         ✅ Kravspecifikation
├── supplier-questions.md        ✅ Frågor till leverantörer
├── evaluation-criteria.md       ✅ Utvärderingskriterier
└── 05-rfi/                      ❌ Underkatalog (inte refererad)
    ├── rfi-overview.md          ⚠️ Duplicerad innehål
    └── rfi-summary.md           ⚠️ Duplicerad innehål
```

**Rekommendation:** Konsolidera rfi-rfp/05-rfi/ innehål till huvudnivå - ta bort duplicering.

---

### B. VERKSAMHET (9 filer - OPERATIV KONTEXT)
**Syfte:** Beskriva verksamheten, organisation och processer  
**Navigationsstatus:** ✅ Alla länkade

```
overview/
├── verksamhetsbeskrivning.md    ✅ Verksamhetsbeskrivning (länkad)
├── organisation.md              ✅ Organisationsstruktur (länkad)
├── introduction.md              ⚠️ INTE LÄNKAD (potentiell startseite)
├── 00-overview/
│   └── verksamhetsbeskrivning.md ⚠️ DUPLICERAD

processes/core-processes/
├── overview.md                  ✅ Processer - Översikt (länkad)
├── case-management.md           ✅ Larmhantering (länkad)
├── follow-up.md                 ✅ Vårdhantering (länkad)
└── onboarding.md                ✅ Personalhantering (länkad)
```

**Rekommendation:** Ta bort duplicering i overview/00-overview/. Överväg introduction.md för frontpage-innehål.

---

### C. TEKNIK & INTEGRATION (18 filer - SYSTEMLANDSKAP)
**Syfte:** System, integationer, masterdata, diagram  
**Navigationsstatus:** ⚠️ Partiell (många orphaned diagram)

```
systems/
├── systemkatalog.md             ✅ Systemkatalog (länkad) - NYTT!
├── digitaliseringsstrategi.md   ✅ Digitaliseringsstrategi (länkad) - NYTT!
├── system-landscape.md          ✅ Systemöversikt (länkad)
├── system-landscape-rfi.md      ✅ Systemlandskap RFI (länkad)
├── integrations.md              ✅ Integrationer (länkad)
├── masterdata.md                ✅ Masterdata (länkad)
└── 02-system/                   [Se nedan - 57 systemfiler]

diagrams/
├── architecture/                ✅ 3 filer länkade
│   ├── kritikalitet.md
│   ├── autentisering.md
│   └── integration-detailed.md
├── data-flows/                  ✅ 1 fil länkad
│   └── masterdata-flow.md
├── process/                     ❌ 2 filer INTE länkade
│   ├── larmcentral.md
│   └── vard-omsorg.md
├── system-overview.md           ❌ INTE länkad
├── integration-overview.md      ❌ INTE länkad
├── README.md                    ⚠️ Metadata
└── 6 övriga diagramfiler        ❌ INTE länkade
```

**Rekommendation:** Länka processo-diagram i navigation. Konsolidera duplicerade system-overview filer.

---

### D. SYSTEMDOKUMENTATION (57 filer - DETALJERADE SYSTEM)
**Syfte:** Individuell dokumentation för varje system  
**Status:** ✅ Finns, men ej länkade individuellt (länkas via kategorilista)

```
systems/02-system/
├── centrala-system/              [25 system + README.md]
│   ├── 3cx.md, adato.md, agera.md, ...
│   └── README.md                 ✅ Länkad som kategorisida
├── molntjanster/                 [15 system + README.md]
│   └── README.md                 ✅ Länkad som kategorisida
├── applikationer/                [3 system + README.md]
│   └── README.md                 ✅ Länkad som kategorisida
├── tjanster/                     [10 system + README.md]
│   └── README.md                 ✅ Länkad som kategorisida
└── ovriga-system/                [4 system + README.md]
    └── README.md                 ✅ Länkad som kategorisida
```

**Kodningsproblem:** 12 systemfiler har specialtecken i filnamn:
- `keywin-nyckelskäp.md` → `keywin-nyckelskalp.md` (ä → a)
- `lärkan.md` → `larkan.md` (ä → a)
- `maskeringstjänsten.md` → `maskeringstjansten.md` (ä → a)
- `npoé.md` → `npoe.md` (é → e)
- `phoniro-lock-systems-phoniro-pi-digitala-låses.md` (lång fil, innehåller å)

**Rekommendation:** Byt namn på alla filer för att ta bort specialtecken (UTF-8 issue).

---

### E. ANALYSER (3 filer - SUPPORTMATERIAL)
**Syfte:** Underlags- och riskanalyser  
**Navigationsstatus:** ✅ Alla länkade

```
analyses/
├── gap-analysis.md              ✅ Gap-analys (länkad)
├── pain-points.md               ✅ Pain Points (länkad)
└── risk-analysis.md             ✅ Riskanalys (länkad)
```

**Status:** OK - alla är länkade och serverar sitt syfte.

---

### F. REFERENS & METADATA (6 filer - NAVIGATIONAL SUPPORT)
**Syfte:** Glossary, principer, kontakt, dokumentation  
**Navigationsstatus:** ⚠️ Partiell

```
overview/
├── glossary.md                  ✅ Ordlista (länkad)
├── architecture-principles.md   ✅ Arkitekturprinciper (länkad)
├── how-to-work.md               ❌ INTE LÄNKAD (instruktioner för redigerare)
├── design-style-guide.md        ❌ INTE LÄNKAD (style guide)

about/
├── contact.md                   ✅ Kontakt (länkad)
└── documentation.md             ❌ INTE LÄNKAD (documentation guide)
```

**Rekommendation:** Länka how-to-work.md i en "Redaktörguide" sektion. Behåll dokumentation.md för intern referens.

---

### G. STATISTIK & ÖVRIGA (2 filer)
**Syfte:** Verksamhetsöversikt  
**Navigationsstatus:** ⚠️ Partiell

```
statistics/
└── overview.md                  ⚠️ INTE LÄNKAD (överväg integrering)

Toppnivå:
├── index.md                     ✅ Startsida (länkad)
├── README.md                    ⚠️ Repo README (ej länkad - för GitHub)

templates/
├── analysis-template.md         ❌ Templatefiler (inte för webbsidan)
├── process-template.md          ❌ (interna resurser)
└── system-template.md           ❌
```

---

### H. IMAGES & OVERRIDES (Infrastruktur)
**Syfte:** Tillgångar och tema-anpassning  
**Status:** ✅ I bruk

```
images/
└── malmo-stad-logo-*.png        ✅ I bruk (theme)

overrides/
└── main.html                    ✅ I bruk (custom styling)
```

---

## 2. FILREFERENSANALYS

### ✅ VÄLDEFINERADE & LÄNKADE (65 filer)
Dessa filer är explicit länkade i mkdocs.yml navigation och serverar tydligt syfte.

**Kategorier:**
- RFI-Material (4)
- Verksamhet (8)
- Teknik & Integration (18)
- System categories (5 README + ~25)
- Analyser (3)
- Referens (2)
- Statistik/Hemmet (1)

---

### ⚠️ ORPHANED FILES (92 filer) - OELÄNDIGA FILER

Dessa finns i filsystemet men är inte länkade i huvudnavigation:

**Underkategorier:**

1. **Duplicerad innehål (2)**
   - `overview/00-overview/verksamhetsbeskrivning.md` ← duplicerad av `overview/verksamhetsbeskrivning.md`
   - `rfi-rfp/05-rfi/rfi-overview.md` ← duplicerad av `rfi-rfp/rfi-material.md`
   - `rfi-rfp/05-rfi/rfi-summary.md` ← duplicerad innehål

2. **Processdiagram (2) - BORDE LÄNKAS**
   - `diagrams/process/larmcentral.md`
   - `diagrams/process/vard-omsorg.md`

3. **Systemöversiktdiagram (2)**
   - `diagrams/system-overview.md`
   - `diagrams/integration-overview.md`
   - `diagrams/architecture/system-landscape-rfi.md` ← duplicerad?

4. **Gamla överskriftsdiagram (6)**
   - `diagrams/03-verksamhetsomrade-larmcentral.md`
   - `diagrams/04-verksamhetsomrade-vard.md`
   - `diagrams/06-autentisering.md`
   - Dessa verkar vara från tidigare struktur

5. **Dokumentation för redigerare (2)**
   - `overview/how-to-work.md` - Instruktioner för att arbeta med dokumentation
   - `about/documentation.md` - Guide för dokumentstruktur

6. **Mallar (3)**
   - `templates/analysis-template.md`
   - `templates/process-template.md`
   - `templates/system-template.md`

7. **README-filer (5)**
   - `diagrams/README.md`
   - `systems/02-system/centrala-system/README.md` ✅ LÄNKAD
   - `systems/02-system/molntjanster/README.md` ✅ LÄNKAD
   - `systems/02-system/applikationer/README.md` ✅ LÄNKAD
   - `systems/02-system/tjanster/README.md` ✅ LÄNKAD

8. **System-individuella filer (57)**
   - Dessa är ej individuellt länkade men är tillgängliga via kategori-sidor
   - Alla 57 systemfiler är organiserade och funktionella

---

## 3. TEKNISKA PROBLEM IDENTIFIERADE

### 🔴 KRITISKA PROBLEM

#### 1. **Filnamnsproblemet (UTF-8 Encoding)**
**Påverkat:** 12 systemfiler  
**Problem:** Filnamn innehåller specialtecken (å, ä, ö, é) som orsakar länkproblem

**Berörda filer:**
```
keywin-nyckelskäp.md          → keywin-nyckelskalp.md
lärkan.md                     → larkan.md
maskeringstjänsten.md         → maskeringstjansten.md
npoé.md                       → npoe.md
phoniro-lock-systems-phoniro-pi-digitala-låses.md (×2 variantier)
```

**Åtgärd:** Byt namn på alla filer för ASCII-kompatibilitet

---

#### 2. **Duplicerad innehål**
**Problem:** Samma information finns på flera ställen

**Exempel:**
- `overview/verksamhetsbeskrivning.md` vs `overview/00-overview/verksamhetsbeskrivning.md`
- RFI-material finns både under `rfi-rfp/` och `rfi-rfp/05-rfi/`

**Åtgärd:** Slå ihop och ta bort duplicering

---

#### 3. **Orphaned Diagram**
**Problem:** 8+ diagram-filer är inte länkade i navigation

**Påverkade diagram:**
- Process-diagram (larmcentral, vård-omsorg)
- Gamla väsentlighets-diagram
- Integration-overview

**Åtgärd:** Länka eller ta bort relevanta diagram

---

### 🟡 VARNINGSVÄRD PROBLEM

#### 4. **Otydlig katalogstruktur**
**Problem:** Flera katalogkombinationer (overview/00-overview/, rfi-rfp/05-rfi/) är förvirrande

**Åtgärd:** Standardisera namngivning - ta bort nummer-prefix från katalognamn

---

#### 5. **Ej länkade instruktionsfiler**
**Problem:** Redaktörer kan inte hitta how-to-work.md och documentation.md

**Åtgärd:** Skapa "För redigerare" sektion i navigation eller länka under "Om"

---

## 4. OPTIMERINGSREKOMMENDATIONER FÖR RFI

### 🎯 PRIORITET 1: KRITISKA ÅTGÄRDER (gör först)

#### Action 1.1: Åtgärda filnamnsproblemet
```bash
# Byt namn på alla filer med specialtecken
cd systems/02-system/molntjanster/
mv "keywin-nyckelskäp.md" "keywin-nyckelskalp.md"
mv "lärkan.md" "larkan.md"
mv "maskeringstjänsten.md" "maskeringstjansten.md"
mv "npoé.md" "npoe.md"
# etc.
```

**Uppdatering krävs i:**
- mkdocs.yml (om någon länkad direkt)
- systemkatalog.md (om länkad därifrån)
- Alla interna länkningar

---

#### Action 1.2: Konsolidera duplicerad RFI-innehål
**Ta bort:** `rfi-rfp/05-rfi/` katalog  
**Orsak:** Duplicerad innehål från `rfi-rfp/`

```bash
# Verifiera innehål först
diff rfi-rfp/rfi-material.md rfi-rfp/05-rfi/rfi-overview.md

# Om duplicerad - ta bort katalog
rm -r rfi-rfp/05-rfi/
```

---

#### Action 1.3: Konsolidera duplicerad verksamhet-innehål
**Ta bort:** `overview/00-overview/` katalog  
**Orsak:** Duplicerad innehål från `overview/`

```bash
# Verifiera innehål först
diff overview/verksamhetsbeskrivning.md overview/00-overview/verksamhetsbeskrivning.md

# Om duplicerad - ta bort katalog
rm -r overview/00-overview/
```

---

### 🎯 PRIORITET 2: NAVIGATIONSFÖRBÄTTRINGAR (gör näst)

#### Action 2.1: Länka processdiagram
**Lägg till i mkdocs.yml under "Teknik & Integration" → "Processöversikter":**

```yaml
- Processöversikter:
  - Larmcentral-process: diagrams/process/larmcentral.md
  - Vård & Omsorg-process: diagrams/process/vard-omsorg.md
```

---

#### Action 2.2: Länka instruktionsfiler
**Lägg till i mkdocs.yml under "Referens" eller ny "Admin" sektion:**

```yaml
- För redigerare:
  - Hur man arbetar: overview/how-to-work.md
  - Dokumentationsguide: about/documentation.md
  - Design Style Guide: overview/design-style-guide.md
```

---

#### Action 2.3: Överväg introduction.md för RFI-kontext
**Möjligt:** Använd `overview/introduction.md` för RFI-introduktion på hemmet eller första steg

---

### 🎯 PRIORITET 3: STÄDNING (gör sist)

#### Action 3.1: Ta bort gamla diagram
**Ta bort:** Dessa gamla diagram från tidigare struktur
```
diagrams/03-verksamhetsomrade-larmcentral.md
diagrams/04-verksamhetsomrade-vard.md
diagrams/06-autentisering.md
```

**Orsak:** Ersatta av bättre strukturerade filer under `diagrams/architecture/` och `diagrams/process/`

---

#### Action 3.2: Konsolidera diagram-översikter
**Rekommendation:** Slå samman `system-overview.md` och `integration-overview.md` till systemöversiktsfiler under `systems/` istället för `diagrams/`

---

#### Action 3.3: Template-filer
**Rekommendation:** Flytta templatefiler till en separat `_templates` eller `admin` katalog för att inte störa dokumentationen

---

## 5. FÖRESLAGEN NY FILSTRUKTUR

### FÖRE (NUVARANDE)
```
docs/
├── rfi-rfp/
│   ├── *.md
│   └── 05-rfi/                    ❌ Duplicerad
├── overview/
│   ├── *.md
│   └── 00-overview/               ❌ Duplicerad
├── diagrams/
│   ├── *.md (många orphaned)
│   ├── architecture/
│   ├── process/                   ⚠️ Inte länkad
│   └── data-flows/
└── systems/
    ├── systemkatalog.md
    ├── digitaliseringsstrategi.md
    └── 02-system/
```

### EFTER (REKOMMENDERAD)
```
docs/
├── rfi-rfp/
│   ├── rfi-material.md            ✅ Konsoliderad
│   ├── requirements-list.md
│   ├── supplier-questions.md
│   └── evaluation-criteria.md
├── overview/
│   ├── verksamhetsbeskrivning.md  ✅ Konsoliderad
│   ├── introduction.md
│   ├── organisation.md
│   ├── glossary.md
│   ├── architecture-principles.md
│   ├── how-to-work.md
│   └── design-style-guide.md
├── processes/
│   └── core-processes/
├── systems/
│   ├── systemkatalog.md
│   ├── digitaliseringsstrategi.md
│   ├── system-landscape.md
│   ├── integrations.md
│   ├── masterdata.md
│   └── 02-system/                 ✅ Filnamn fixade
└── diagrams/                       ✅ Länkade & städade
    ├── architecture/
    ├── process/
    └── data-flows/
```

---

## 6. NAVIGATIONÖVERSIKT (REKOMMENDERAD)

Nuvarande struktur är **bra** - fokus på dessa ändringar:

### Tillägg 1: Processöversikter-sektion
```yaml
- Teknik & Integration:
  - ...
  - Processöversikter:              ← NYT
    - Larmcentral: diagrams/process/larmcentral.md
    - Vård & Omsorg: diagrams/process/vard-omsorg.md
```

### Tillägg 2: För redigerare-sektion (valfritt)
```yaml
- Admin:                            ← NYT (valfritt - bara visa internt)
  - Hur man arbetar: overview/how-to-work.md
  - Dokumentationsguide: about/documentation.md
```

---

## 7. KODNINGSPLAN & PRIORITET

| Priority | Action | Filer | Tidsest. | Beroenden |
|----------|--------|-------|----------|-----------|
| **P1** | Byt namn på UTF-8 filer | 12 | 15 min | Uppdatera interna länk |
| **P1** | Ta bort `05-rfi/` dublett | 3 | 5 min | Verifiera ingen länkar |
| **P1** | Ta bort `00-overview/` dublett | 2 | 5 min | Verifiera ingen länkar |
| **P2** | Länka processdiagram | mkdocs.yml | 10 min | P1 slutförd |
| **P2** | Länka instruktionsfiler | mkdocs.yml | 10 min | P1 slutförd |
| **P2** | Överväg introduction.md | review | 5 min | Ingen |
| **P3** | Ta bort gamla diagram | 3 | 5 min | Verifiera ingen länkar |
| **P3** | Konsolidera diagram-översikter | move & update | 10 min | P2 slutförd |

**Total tidsuppskattning:** ~50 minuter

---

## 8. VALIDERING EFTER REORGANISERING

```bash
# 1. Bygga lokalt
mkdocs build --verbose

# 2. Kontrollera för varningar
mkdocs serve

# 3. Testa alla link
# - Manuellt klicka genom navigation
# - Säkerställ inga 404-sidor

# 4. Git commit
git add -A
git commit -m "Reorganisera filer för RFI - ta bort dubletter, länka diagram"
```

---

## AVSLUTANDE SAMMANFATTNING

| Metrik | Värde | Status |
|--------|-------|--------|
| Länkade filer | 65 | ✅ OK |
| Orphaned filer | 92 | ⚠️ De flesta är OK, några borde länkas |
| Duplicerad innehål | 3 katalog-par | 🔴 Måste fixas |
| UTF-8 filnamn | 12 | 🔴 Måste fixas |
| Processdiagram | 2 | ⚠️ Borde länkas |

**Rekommendation:** Genomför Priority 1 och Priority 2 åtgärder för att optimera RFI-fokus och städa upp filstrukturen. Priority 3 kan göras senare eller spridas över tid.

---

*Denna granskning genomfördes för att optimera Verksamhetssystem-RFI-dokumentationen för maximal RFI-fokus och användarvänlighet.*
