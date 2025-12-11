# 🗂️ ORGANISERING FÖR RFI - ÅTGÄRDSLISTA

**Datum:** 2024  
**Mål:** Organisera alla filer för optimal RFI-fokus  
**Totalt åtgärder:** 11 åtgärdspunkter  

---

## ✅ ÅTGÄRDSLISTA - RFI REORGANISERING

### **PRIORITET 1: KRITISKA ÅTGÄRDER** (Gör först - 25 min)

#### [ ] 1.1 - Byt namn på 12 systemfiler med UTF-8 specialtecken

**Varför:** Filnamn med å, ä, ö, é orsakar länkproblem

**Filer att byta namn:**
```
systems/02-system/molntjanster/
  ✏️ keywin-nyckelskäp.md → keywin-nyckelskalp.md
  ✏️ lärkan.md → larkan.md
  ✏️ maskeringstjänsten.md → maskeringstjansten.md
  ✏️ npoé.md → npoe.md
  ✏️ phoniro-lock-systems-phoniro-pi-digitala-låses.md (×2 varianter)
  
systems/02-system/tjanster/
  ✏️ (fler specialteckensfiler)
```

**Steg:**
1. Gå till `systems/02-system/` katalog
2. Byt namn på varje fil med specialtecken
3. Uppdatera mkdocs.yml om något direkt länkat (är det inte)
4. Uppdatera systemkatalog.md om länkar finns

**Kommando (PowerShell):**
```powershell
# Kontrollera alla filer med UTF-8 problem
Get-ChildItem -Recurse "c:\...\systems\02-system\" -Filter "*.md" | 
  Where-Object { $_.Name -match "[åäöéè]" } | 
  Select-Object FullName, Name
```

---

#### [ ] 1.2 - Ta bort `rfi-rfp/05-rfi/` katalog (duplicerad innehål)

**Varför:** Samma innehål finns redan under `rfi-rfp/`

**Filer att ta bort:**
```
rfi-rfp/05-rfi/rfi-overview.md       ← duplicerad av rfi-material.md
rfi-rfp/05-rfi/rfi-summary.md        ← duplicerad innehål
```

**Steg:**
1. Verifiera innehål: `diff rfi-rfp/rfi-material.md rfi-rfp/05-rfi/rfi-overview.md`
2. Säkerställ ingen länkade dessa filer från mkdocs.yml
3. Ta bort katalog: `rm -r rfi-rfp/05-rfi/`
4. Git commit: `git add -A; git commit -m "Ta bort duplicerad RFI-innehål (05-rfi katalog)"`

**Påverkan:** ✅ Noll (ej länkad)

---

#### [ ] 1.3 - Ta bort `overview/00-overview/` katalog (duplicerad innehål)

**Varför:** Samma innehål finns redan under `overview/`

**Filer att ta bort:**
```
overview/00-overview/verksamhetsbeskrivning.md  ← duplicerad av overview/verksamhetsbeskrivning.md
```

**Steg:**
1. Verifiera innehål: `diff overview/verksamhetsbeskrivning.md overview/00-overview/verksamhetsbeskrivning.md`
2. Säkerställ ingen länkade dessa filer från mkdocs.yml
3. Ta bort katalog: `rm -r overview/00-overview/`
4. Git commit: `git add -A; git commit -m "Ta bort duplicerad verksamhet-innehål (00-overview katalog)"`

**Påverkan:** ✅ Noll (ej länkad)

---

### **PRIORITET 2: NAVIGATIONSFÖRBÄTTRINGAR** (Gör näst - 20 min)

#### [ ] 2.1 - Länka processdiagram i mkdocs.yml

**Varför:** 2 processdiagram är orphaned, borde länkas för att göra dem tillgängliga

**Nya filer att länka:**
- `diagrams/process/larmcentral.md`
- `diagrams/process/vard-omsorg.md`

**Steg:**
1. Öppna `mkdocs.yml`
2. Under `- Teknik & Integration:`, lägg till ny sektion:

```yaml
  - Teknik & Integration:
    - Systemöversikt: systems/system-landscape.md
    - ...befintliga...
    - Processöversikter:              # ← NYT
      - Larmcentral-process: diagrams/process/larmcentral.md
      - Vård & Omsorg-process: diagrams/process/vard-omsorg.md
```

3. Spara och testa: `mkdocs serve`
4. Git commit: `git add mkdocs.yml; git commit -m "Länka processdiagram i navigation"`

**Påverkan:** ✅ Gör 2 orphaned filer tillgängliga

---

#### [ ] 2.2 - Länka instruktionsfiler för redigerare

**Varför:** Redaktörer kan inte hitta dokumentation för att arbeta med sidan

**Nya filer att länka:**
- `overview/how-to-work.md` - Instruktioner för att arbeta med dokumentation
- `about/documentation.md` - Guide för dokumentstruktur
- `overview/design-style-guide.md` - Design guide

**Steg:**
1. Öppna `mkdocs.yml`
2. Under `- Referens:`, lägg till eller skapa ny sektion:

**Option A: Under Referens (rekommenderat)**
```yaml
  - Referens:
    - Ordlista: overview/glossary.md
    - ...befintliga...
    - För redigerare:              # ← NYT
      - Hur man arbetar: overview/how-to-work.md
      - Dokumentationsguide: about/documentation.md
      - Design Style Guide: overview/design-style-guide.md
```

**Option B: Ny "Admin" sektion (alternativ)**
```yaml
  - Admin:                          # ← NYT sektion
    - Hur man arbetar: overview/how-to-work.md
    - Dokumentationsguide: about/documentation.md
    - Design Style Guide: overview/design-style-guide.md
```

3. Spara och testa: `mkdocs serve`
4. Git commit: `git add mkdocs.yml; git commit -m "Länka instruktionsfiler för redigerare"`

**Påverkan:** ✅ Gör 3 orphaned filer tillgängliga för redigerare

---

#### [ ] 2.3 - Överväg introduction.md för RFI-kontext

**Varför:** `overview/introduction.md` är en bra introduktionstext men inte länkad

**Options:**
- **A: Länka under RFI-Material** (före övriga dokument)
- **B: Länka under Verksamhet** (för kontext)
- **C: Lämna ej länkad** (om innehål redan täcks av index.md)

**Steg:**
1. Läs `overview/introduction.md` för att förstå innehål
2. Avgör var det passar bäst i navigationen
3. Lägg till länk eller ta bort om duplicerad
4. Git commit: `git add mkdocs.yml; git commit -m "Länka introduction.md eller ta bort om duplicerad"`

**Påverkan:** ⚠️ Beroende på val

---

### **PRIORITET 3: STÄDNING** (Gör sist - 20 min)

#### [ ] 3.1 - Ta bort gamla diagram från tidigare struktur

**Varför:** Ersatta av bättre organiserade filer, skapar förvirring

**Filer att ta bort:**
```
diagrams/03-verksamhetsomrade-larmcentral.md     ← ersatt av diagrams/process/larmcentral.md
diagrams/04-verksamhetsomrade-vard.md            ← ersatt av diagrams/process/vard-omsorg.md
diagrams/06-autentisering.md                     ← ersatt av diagrams/architecture/autentisering.md
```

**Steg:**
1. Verifiera dessa är överflödiga (jämför med newer versioner)
2. Git check - säkerställ ingen länkade dem
3. Ta bort: `rm diagrams/03-*.md diagrams/04-*.md diagrams/06-*.md`
4. Git commit: `git add -A; git commit -m "Ta bort gamla diagram från tidigare struktur"`

**Påverkan:** ✅ Rengör 3 orphaned filer

---

#### [ ] 3.2 - Flytta templates till separat admin-katalog (valfritt)

**Varför:** Templatefiler räcker inte för dokumentationen, kan ställa till förvirring

**Filer att flytta:**
```
templates/analysis-template.md
templates/process-template.md
templates/system-template.md
```

**Alternativ 1: Flytta till `_templates/`**
```bash
mkdir _templates
mv templates/* _templates/
rm -r templates/
```

**Alternativ 2: Behåll men ta bort från docs (flytta till repo-rot)**
```bash
mv docs/templates/* .templates/ (utanför docs/)
```

**Alternativ 3: Lämna som är** (om de inte orsakar problem)

**Steg:**
1. Avgör om detta är nödvändigt (gör om du är säker)
2. Flytta om ja
3. Git commit

**Påverkan:** ⚠️ Liten - valfritt

---

### **PRIORITET 4: DOKUMENTATION** (Parallell med ovan - 10 min)

#### [ ] 4.1 - Uppdatera README.md med ny struktur

**Varför:** README bör reflektera slutlig struktur

**Steg:**
1. Öppna `README.md`
2. Uppdatera `## Struktur` avsnitt för att reflektera:
   - Ej längre `00-overview/`, `05-rfi/`
   - Nya länkade diagram
   - Uppdaterad kataloglista

3. Git commit: `git add README.md; git commit -m "Uppdatera README efter reorganisering"`

---

#### [ ] 4.2 - Lägg till denna åtgärdslista som intern referens (valfritt)

**Steg:**
1. Spara denna fil i repo under `REORGANISERING_PROGRESS.md`
2. Använd för att följa framsteg
3. Git add vid varje steg

**Påverkan:** ℹ️ Dokumentation endast

---

## 🎯 EXEKVERINGSPLAN

### VECKA 1
```
❑ Måndag: Gör P1 åtgärder (1.1-1.3) = 25 min
❑ Tisdag: Gör P2 åtgärder (2.1-2.3) = 20 min  
❑ Onsdag: Gör P3 åtgärder (3.1-3.2) = 20 min
❑ Torsdag: Gör P4 åtgärder (4.1-4.2) = 10 min
❑ Fredag: Testa fullständigt + Git push
```

### TESTNING VID VARJE STEG
```bash
# Efter varje åtgärd:
mkdocs build --verbose        # Kontrollera syntax
mkdocs serve                  # Testa lokalt på http://127.0.0.1:8000
# Klicka runt - verifiera inga 404-fel
```

---

## 📋 VALIDERING CHECKLISTA

Efter all reorganisering:

- [ ] **Alla P1-åtgärder slutförda**
- [ ] `mkdocs build` kör utan fel
- [ ] `mkdocs serve` startar utan fel
- [ ] Inga varningar om "unrecognized links"
- [ ] Alla navigationslänkningar fungerar
- [ ] Systemkatalog länkningar fungerar (57 system)
- [ ] Digitaliseringsstrategi länkningar fungerar
- [ ] Process-diagram är tillgängliga från navigation
- [ ] Instruktionsfiler är tillgängliga för redigerare
- [ ] Gamla diagram är borttagna/ersatta
- [ ] Git push utan konflikter
- [ ] GitHub Pages bygger utan fel

---

## 💡 TIPS & SNABBREFERENS

### PowerShell-kommandon för att kontrollera status

```powershell
# Se alla orphaned filer (ej i mkdocs.yml)
Get-ChildItem -Recurse -Filter "*.md" | 
  Where-Object { (Get-Content ...\mkdocs.yml) -notmatch $_.Name } |
  Select-Object Name

# Se alla filer med specialtecken
Get-ChildItem -Recurse -Filter "*.md" | 
  Where-Object { $_.Name -match "[åäöéè]" } | 
  Select-Object FullName

# Kontrollera mkdocs.yml syntax
python -m yaml mkdocs.yml
```

### Git-kommandon

```bash
# Se vilka filer som ändrats
git status

# Se diff för specifik fil
git diff mkdocs.yml

# Undo senaste commit (om något går fel)
git reset --soft HEAD~1
git reset HEAD mkdocs.yml  # Undo add
```

---

## ❓ VANLIGA FRÅGOR

**F: Vad händer om jag glömmer att uppdatera en länk?**  
S: `mkdocs serve` kommer att varna om broken links. Testa alltid lokalt först!

**F: Kan jag ångra detta?**  
S: Ja! Git har full historik. Du kan alltid göra `git reset` eller `git revert`.

**F: Måste jag göra alla åtgärder?**  
S: Nej. P1 är kritisk. P2 förbättrar UX. P3 är cleanup. P4 är dokumentation.

**F: Vad är skillnaden mellan orphaned filer och duplicerad filer?**  
S: **Orphaned** = finns men är inte länkad. **Duplicerad** = samma innehål på flera ställen.

---

**Status:** 🟡 Klar för aktivering  
**Nästa steg:** Starta med åtgärd 1.1 (UTF-8 filnamn)  
**Beräknad tid:** ~75 minuter totalt

*Denna åtgärdslista är en detaljerad guide för att reorganisera Verksamhetssystem-RFI för optimal RFI-fokus.*
