# RFI-material - Verksamhetssystems-byte

## Översikt

Detta dokument samlar material för Request for Information (RFI) inför byte av verksamhetssystem för HVOF. Fokus ligger på system som är mest direkt kopplade till vård/omsorg, larm, planering och kvalitet.

## Nuvarande situation

### Kärnsystem: Lifecare/Procapita

**Leverantör**: Tietoevry Care  
**Typ**: Verksamhetssystem för socialtjänst & vård/omsorg (SoL, LSS, HSL)

**Vad systemet gör idag**:
- Dokumentation, handläggning, beslut, verkställighet, journal, uppföljning
- Hemtjänst, särskilt boende, LSS, myndighetsutövning
- Master för vårddata och omsorgsdokumentation

**Kritiska integrationer**:
- Phoniro Care (tid/insatsuppföljning)
- MCSS (digital signering)
- Mina Planer (vårdplanering)
- NPÖ (patientöversikt)
- Pascal (läkemedel)
- Senior Alert (kvalitetsregister)
- Ekot/Raindance (ekonomi/debitering)
- Koll/QlikView, Stratsys (BI/rapporter)
- Open e-plattformen (e-tjänster)

**Processer som stöds**:
- Handläggning av ärenden (SoL, LSS)
- Vårdplanering och dokumentation
- Journalföring
- Beslut och verkställighet
- Uppföljning och kvalitetssäkring

**Roller**:
- Handläggare
- Sjuksköterskor
- Undersköterskor
- Chefer
- Ekonomi

## Kritiska integrationer - Must Have

### Nationella e-hälsotjänster

#### NPÖ (Nationell patientöversikt)
**Krav**: Nytt system måste stödja NPÖ (både konsumera och publicera)

**Användning**:
- Läsa journalinformation från regioner och andra vårdgivare
- Publicera journalinformation för andra vårdgivare

**Integrationstyp**: API, HL7

#### Pascal
**Krav**: Integrationsstöd (direktlänk/SSO, strukturerad läkemedelslista)

**Användning**:
- Ordination och beställning av dosdispenserade läkemedel
- Koppling till Nationella Läkemedelslistan

**Integrationstyp**: API, SSO

#### Senior Alert
**Krav**: Stöd för registrering och export till nationella kvalitetsregister

**Användning**:
- Riskbedömningar (fall, trycksår, nutrition, munhälsa, blåsdysfunktion)
- Åtgärdsplaner och uppföljning

**Integrationstyp**: Export, API

### Regionala tjänster

#### Mina Planer
**Krav**: Ta emot/visa information från Mina Planer, dokumentera SIP/planer

**Användning**:
- Samordnad vårdplanering (SVU)
- Samordnad Individuell Plan (SIP)
- Utskrivningsklara patienter

**Integrationstyp**: API, dokumentutbyte

### Välfärdsteknik

#### CMP (Neat - Care Management Portal)
**Krav**: Integration för larmstatus på brukarnivå

**Användning**:
- Fjärradministration av trygghetstelefoner
- Larmhistorik och status

**Integrationstyp**: API

#### Phoniro Lock / digitala lås
**Krav**: Stöd för digitala lås, mobil åtkomst, öppna API:er, säkerhetsnivå (Freja/SITHS)

**Användning**:
- Digitala dörrlås för hemtjänstbrukare
- Mobil åtkomst med kvittens

**Integrationstyp**: API, mobilapp

#### Viser/Sensio/Smooth (trygghetssensorer)
**Krav**: Sammanhållen larm- och eventplattform

**Användning**:
- Trygghetssensorer i särskilt boende
- Sängsensorer, rörelsesensorer
- Larm till personalens mobiler

**Integrationstyp**: API, eventplattform

### Tid- och insatsuppföljning

#### Phoniro Care
**Strategi**: Ska nytt system ha inbyggd funktion eller fortsätta använda Phoniro via integration?

**Användning**:
- Tid- och insatsuppföljning
- Kvittering av besök och insatser
- Data för uppföljning, debitering, kvalitet

**Integrationstyp**: API, databas

### Digital signering

#### MCSS - HVOF
**Krav**: Elektronisk signeringsfunktion för delegerade HSL-insatser eller integration mot MCSS

**Användning**:
- Digital signering av läkemedel och HSL-uppgifter
- Delegering och signering

**Integrationstyp**: API, SSO (SITHS/Freja)

### Larmcentral

#### Interview/ISM
**Krav**: Integration för larmmottagning och hantering

**Användning**:
- Larmmottagning för trygghets-, person- och inbrottslarm
- Core i larmkedjan

**Integrationstyp**: API, CTI

#### 3CX
**Krav**: Integration via API/CTI för telefonväxel

**Användning**:
- Telefoni i larmcentralen
- Köer, hänvisning, inspelning, statistik

**Integrationstyp**: API, CTI

#### Milestone
**Krav**: Hantering av kameralarm som del av trygghetskedjan

**Användning**:
- Kameralarm och digital tillsyn
- Video management system

**Integrationstyp**: API, eventplattform

### Personal och HR

#### HRutan/Medvind
**Krav**: Utbyte av uppgifter om personal, behörigheter, vikarier

**Användning**:
- Personaldata, schema, tidrapportering
- HR-processer

**Integrationstyp**: API, batch

**Notera**: HR-systemen är typiskt egna "core system" som inte ersätts vid omsorgs-RFI.

### Ekonomi

#### Ekot/Raindance
**Krav**: Integration för debitering

**Användning**:
- Ekonomi och budget
- Debitering

**Integrationstyp**: API, batch

**Notera**: Ekonomisystemet ersätts typiskt inte vid omsorgs-RFI.

### Planering

#### Kuben
**Krav**: Integration för planering av insatser

**Användning**:
- Planera insatser utifrån vårdtyngd och personalresurser

**Integrationstyp**: API, databas

## Smärtpunkter och förbättringsmöjligheter

### 1. Dubbel dokumentation
**Problem**: Dubbel dokumentation mellan:
- Lifecare och Phoniro
- Lifecare och Senior Alert
- Lifecare och Mina Planer

**Påverkan**:
- Tidskrävande
- Felrisker
- Inkonsekvent data

**Önskat**: Minskad dubbel dokumentation, enkel inmatning, automatisk synkronisering

### 2. Välfärdsteknik - flera leverantörer
**Problem**: Flera leverantörer för välfärdsteknik:
- Sensio (Viser)
- Great Security (Smooth Lite)
- Neat (CMP)
- Phoniro (digitala lås)

**Påverkan**:
- Komplex integration
- Olika plattformar
- Svårt att få sammanhållen bild

**Önskat**: Sammanhållen larm- och eventplattform, enhetlig integration

### 3. Integrationer
**Problem**: Många olika integrationstyper:
- API (realtid)
- Batch (daglig)
- Manuell (kopiering)

**Påverkan**:
- Komplexitet
- Felrisker
- Underhåll

**Önskat**: Standardiserade API:er, realtidsintegrationer där möjligt

### 4. Nationella tjänster
**Problem**: Krav på integration med många nationella tjänster:
- NPÖ
- Pascal
- Mina Planer
- Senior Alert

**Påverkan**:
- Komplex integration
- Dubbel dokumentation
- Olika standarder

**Önskat**: Enkel integration, automatisk synkronisering, minskad dubbel dokumentation

## Krav på nytt system

### Funktionella krav

#### Kärnfunktionalitet
- [ ] Stöd för SoL, LSS, HSL-processer
- [ ] Dokumentation, handläggning, beslut, verkställighet
- [ ] Journalföring
- [ ] Vårdplanering
- [ ] Uppföljning och kvalitetssäkring

#### Integrationer
- [ ] NPÖ (konsumera och publicera)
- [ ] Pascal (läkemedel)
- [ ] Senior Alert (kvalitetsregister)
- [ ] Mina Planer (vårdplanering)
- [ ] Phoniro Care eller inbyggd tid/insatsuppföljning
- [ ] MCSS eller inbyggd digital signering
- [ ] CMP (välfärdsteknik)
- [ ] Digitala lås (Phoniro Lock)
- [ ] Trygghetssensorer (Viser/Sensio/Smooth)
- [ ] Interview/ISM (larmcentral)
- [ ] 3CX (telefoni)
- [ ] Milestone (kameralarm)
- [ ] HRutan/Medvind (personal)
- [ ] Ekot (ekonomi/debitering)
- [ ] Kuben (planering)

#### Tid- och insatsuppföljning
- [ ] Kvittering av besök och insatser
- [ ] Tidsregistrering
- [ ] Uppföljning och debitering
- [ ] Koppling till digitala lås

#### Digital signering
- [ ] Signering av läkemedel
- [ ] Signering av HSL-uppgifter
- [ ] Delegering
- [ ] SITHS/Freja-autentisering

### Icke-funktionella krav

#### Säkerhet
- [ ] SITHS-autentisering för vårddata
- [ ] Freja eID för SSO
- [ ] GDPR-efterlevnad
- [ ] Loggning och spårbarhet

#### Prestanda
- [ ] Hantera 1000+ användare samtidigt
- [ ] Svarstid < 2 sekunder
- [ ] 99.9% tillgänglighet

#### Integrationer
- [ ] REST API:er
- [ ] HL7 för vårddata
- [ ] Realtidsintegrationer
- [ ] Batch-integrationer

#### Masterdata
- [ ] Master för vårddata
- [ ] Ta emot masterdata från andra system
- [ ] Validering av data

## Datamigration

### Kritiska datadomäner

1. **Vårddata** (från Lifecare/Procapita)
   - Journaler
   - Vårdplaner
   - Beslut
   - Uppföljningar

2. **Tids- och insatsdata** (från Phoniro Care)
   - Besök
   - Insatser
   - Tidsregistrering

3. **Läkemedelsdata** (från Pascal)
   - Ordinationer
   - Läkemedelslistor

4. **Kvalitetsdata** (från Senior Alert)
   - Riskbedömningar
   - Åtgärdsplaner

### Migrationkrav

- [ ] Migration av historik från Lifecare/Procapita
- [ ] Migration av tids- och insatsdata från Phoniro Care
- [ ] Bevarande av integrationer under migration
- [ ] Testning och validering
- [ ] Rollback-plan

## Processer som måste stödjas

### Vårdprocesser
1. Handläggning av ärenden (SoL, LSS)
2. Vårdplanering
3. Dokumentation
4. Beslut och verkställighet
5. Uppföljning

### Larmprocesser
1. Larmmottagning
2. Larmhantering
3. Aviseringar
4. Uppföljning

### Kvalitetsprocesser
1. Riskbedömningar
2. Avvikelsehantering
3. Kvalitetssäkring
4. Rapportering

### Personalprocesser
1. Schema
2. Tidsrapportering
3. Behörigheter
4. Vikarier

## Frågor till leverantörer

Se [Frågor till leverantörer](supplier-questions.md) för detaljerade frågor.

## Relaterade dokument

- [Systemlandskap - RFI-fokus](../systems/system-landscape-rfi.md)
- [Kravlista](requirements-list.md)
- [Frågor till leverantörer](supplier-questions.md)
- [Utvärderingskriterier](evaluation-criteria.md)

## Kontakt

För frågor om RFI-material, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-12-10
Uppdaterad av: [Namn]
