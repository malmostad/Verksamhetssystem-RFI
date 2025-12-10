# Diagram - Översikt

Denna mapp innehåller fokuserade diagram för olika syften och aspekter av HVOFs systemlandskap.

## Diagramlista

### 1. Masterdata-flöde
**Fil:** `01-masterdata-flow.md`  
**Syfte:** Visar hur masterdata flödar mellan system och vilka system som är master för olika datadomäner.  
**Användning:** Förstå dataägaransvar och dataströmmar.

### 2. Detaljerad Integrationskarta
**Fil:** `02-integration-detailed.md`  
**Syfte:** Visar alla kända integrationer mellan system med integrationstyp och dataströmmar.  
**Användning:** Förstå systemberoenden och integrationstyper.

### 3. Verksamhetsområde: Larmcentral
**Fil:** `03-verksamhetsomrade-larmcentral.md`  
**Syfte:** Visar alla system och integrationer specifikt för Larmcentral-verksamheten.  
**Användning:** Förstå larmcentralens systemlandskap och processer.

### 4. Verksamhetsområde: Vård & Omsorg
**Fil:** `04-verksamhetsomrade-vard.md`  
**Syfte:** Visar alla system och integrationer specifikt för Vård & Omsorg-verksamheten.  
**Användning:** Förstå vårdens systemlandskap och processer.

### 5. Kritikalitet
**Fil:** `05-kritikalitet.md`  
**Syfte:** Visar systemens kritikalitet baserat på verksamhetspåverkan och driftkrav.  
**Användning:** Prioritera system vid incidenter och planering.

### 6. Autentiseringsflöde
**Fil:** `06-autentisering.md`  
**Syfte:** Visar hur användare autentiserar sig till olika system och vilka metoder som används.  
**Användning:** Förstå säkerhetsarkitekturen och inloggningsflöden.

### 7. Process: Larmhantering
**Fil:** `07-process-larm.md`  
**Syfte:** Visar processflödet för hur larm hanteras från inkommande larm till uppföljning.  
**Användning:** Förstå larmprocessen steg för steg.

### 8. Process: Vårdhantering
**Fil:** `08-process-vard.md`  
**Syfte:** Visar processflödet för hur vård hanteras från registrering till uppföljning.  
**Användning:** Förstå vårdprocessen steg för steg.

## Användning

### För RFI-processen
1. **Masterdata-flöde** - Visa leverantörer vilka system som är kritiska
2. **Integrationskarta** - Förklara systemberoenden
3. **Verksamhetsområden** - Visa system per verksamhet
4. **Kritikalitet** - Prioritera system vid systembyte

### För systembyte
1. **Processdiagram** - Förstå verksamhetsflöden
2. **Integrationskarta** - Identifiera påverkade system
3. **Masterdata-flöde** - Planera datamigration
4. **Kritikalitet** - Prioritera migrationsordning

### För förståelse
1. **Autentiseringsflöde** - Förstå säkerhetsarkitekturen
2. **Verksamhetsområden** - Se system i kontext
3. **Processdiagram** - Förstå verksamhetsflöden

## Diagramtyper

Alla diagram använder **Mermaid** för att vara:
- Versionskontrollerade (i Git)
- Automatiserbart genererbara
- Visuellt tydliga
- Enkla att uppdatera

## Uppdatering

Diagrammen uppdateras när:
- Nya system läggs till
- Integrationer ändras
- Processer förändras
- Kritikalitet ändras

## Generering

Diagrammen kan genereras automatiskt med `generate_docs.py` eller uppdateras manuellt i Markdown-filerna.

