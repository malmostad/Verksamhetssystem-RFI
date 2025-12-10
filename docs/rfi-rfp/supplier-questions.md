# Frågor till leverantörer - RFI

## Översikt

Frågor som ska ställas till leverantörer i RFI-processen.

## Syfte

Få svar på viktiga frågor för att kunna utvärdera leverantörer och system.

## Processer

### 1. Hur stödjer ert system larmhantering?

**Kontext**: HVOF har en larmcentral som tar emot larm från flera källor.

**Frågor**:
- Hur tar systemet emot larm från olika källor (telefon, trygghetslarm, kameralarm)?
- Hur prioriterar systemet larm?
- Hur skickar systemet larm vidare till rätt resurs?
- Hur loggar systemet larm och åtgärder?

**Relaterade krav**: KRAV-001 till KRAV-004

### 2. Hur stödjer ert system vårdhantering?

**Kontext**: HVOF behöver hantera vårdplaner, vårddokumentation och integrera med vårdtjänster.

**Frågor**:
- Hur hanterar systemet vårdplaner och vårddokumentation?
- Hur integrerar systemet med NPÖ för patientöversikt?
- Hur hanterar systemet läkemedelsbeställningar (Pascal)?
- Hur stödjer systemet signering (MCSS)?

**Relaterade krav**: KRAV-005 till KRAV-008

### 3. Hur hanterar ni masterdata?

**Kontext**: HVOF följer masterdata-principen där varje datadomän har ett master system.

**Frågor**:
- Kan ert system vara master för sin datadomän?
- Hur tar systemet emot masterdata från andra system?
- Hur validerar systemet data vid mottagande?
- Hur säkerställer ni datakvalitet?

**Relaterade krav**: KRAV-023 till KRAV-025

### 4. Hur fungerar era API:er?

**Kontext**: HVOF behöver integrera med många befintliga system.

**Frågor**:
- Vilka API:er exponerar systemet?
- Vilken API-standard använder ni (REST, SOAP, GraphQL)?
- Finns API-dokumentation?
- Stödjer systemet HL7 för vårddata?
- Hur hanterar ni API-versionering?

**Relaterade krav**: KRAV-019 till KRAV-022

### 5. Hur säkerställer ni GDPR i kommunal verksamhet?

**Kontext**: HVOF hanterar känslig person- och vårddata.

**Frågor**:
- Hur säkerställer ni GDPR-efterlevnad?
- Var lagras data (Sverige, EU)?
- Hur hanterar ni rätt till radering?
- Hur loggar ni dataåtkomst?
- Har ni certifieringar (ISO 27001, etc.)?

**Relaterade krav**: KRAV-012 till KRAV-015

### 6. Hur stödjer ni autentisering?

**Kontext**: HVOF använder Freja eID och SITHS för inloggning.

**Frågor**:
- Stödjer systemet Freja eID för SSO?
- Stödjer systemet SITHS för vårddata?
- Stödjer systemet Active Directory?
- Hur hanterar ni rollbaserad åtkomst (RBAC)?

**Relaterade krav**: KRAV-012, KRAV-013

### 7. Hur fungerar integrationer?

**Kontext**: HVOF har många befintliga system som måste integreras.

**Frågor**:
- Hur integrerar systemet med befintliga system?
- Vilka integrationer har ni redan implementerat?
- Hur lång tid tar det att implementera en integration?
- Vilken support erbjuder ni för integrationer?

**Relaterade krav**: KRAV-019 till KRAV-022

### 8. Hur hanterar ni rapporter och analyser?

**Kontext**: HVOF behöver rapporter och data för BI-system.

**Frågor**:
- Vilka rapporter kan systemet generera?
- Hur exponerar systemet data för BI-system?
- Stödjer systemet export av data?
- Vilka analysverktyg ingår?

**Relaterade krav**: KRAV-026 till KRAV-028

### 9. Vad är er prestanda och tillgänglighet?

**Kontext**: HVOF har 10 000+ användare och kritiska system.

**Frågor**:
- Hur många användare kan systemet hantera samtidigt?
- Vad är systemets svarstid?
- Vad är systemets tillgänglighet (SLA)?
- Hur hanterar ni hög belastning?

**Relaterade krav**: KRAV-016 till KRAV-018

### 10. Hur ser er support och utveckling ut?

**Kontext**: HVOF behöver långsiktig support och kontinuerlig utveckling.

**Frågor**:
- Vilken supportnivå erbjuder ni?
- Hur ofta uppdateras systemet?
- Hur hanterar ni buggar och förbättringar?
- Vad ingår i supportavtalet?

## Svarformat

Leverantörer bör svara med:
- Tydliga svar på varje fråga
- Exempel och skärmdumpar där lämpligt
- Referenser till dokumentation
- Kontaktperson för uppföljning

## Utvärdering

Svar kommer att utvärderas enligt [Utvärderingskriterier](evaluation-criteria.md).

## Relaterade dokument

- [RFI-material](rfi-material.md)
- [Kravlista](requirements-list.md)
- [Systemlandskap](../systems/system-landscape.md)

## Kontakt

För frågor om dessa frågor, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

