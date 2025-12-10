# Systemlandskap - RFI-fokus

## Översikt

Detta dokument fokuserar på system som är mest direkt kopplade till vård/omsorg, larm, planering och kvalitet - de system som är viktigast i RFI inför verksamhetssystems-byte.

## Systemdomäner

### 1. Kärnverksamhet Omsorg

Detta är kärnsystemen för vård och omsorgsverksamheten.

#### Lifecare/Procapita
**Leverantör**: Tietoevry Care  
**Typ**: Verksamhetssystem för socialtjänst & vård/omsorg (SoL, LSS, HSL)

**Användning**:
- Dokumentation, handläggning, beslut, verkställighet, journal, uppföljning
- Hemtjänst, särskilt boende, LSS, myndighetsutövning

**Integrationer**:
- Phoniro Care (tid/insats)
- MCSS (signering)
- Mina Planer (vårdplanering)
- NPÖ (patientöversikt)
- Pascal (läkemedel)
- Senior Alert (kvalitetsregister)
- Ekot/Raindance (ekonomi)
- Koll/QlikView, Stratsys (BI)
- Open e-plattformen (e-tjänster)

**RFI-betydelse**: Detta är idag "core" omsorgssystemet. Tydlig beskrivning av processer, roller, integrationer och datadomäner är utgångspunkt för verksamhetssystems-byte.

#### Phoniro Care
**Leverantör**: Phoniro (Assa Abloy/Tunstall)  
**Typ**: Tid- och insatsuppföljning + nyckel- och låshantering

**Användning**:
- Personal kvitterar besök och insatser hos brukare
- Data för uppföljning, debitering, kvalitet
- Integration med digitala lås (Phoniro Lock)

**Integrationer**:
- Lifecare (beställning/insatsplan) → Phoniro (utförande/tid) → ekonomi/BI

**RFI-betydelse**: Behöver tydlig strategi - ska nytt verksamhetssystem ha inbyggd funktion eller fortsätta använda Phoniro via integration?

#### MCSS - HVOF
**Typ**: Digital signering av läkemedel och HSL-uppgifter

**Användning**:
- Sjuksköterska dokumenterar ordination och delegering
- Undersköterska signerar utförd läkemedelshantering digitalt (SITHS/Freja)

**Integrationer**:
- Lifecare (ordinerade insatser)
- Pascal (läkemedel)

**RFI-betydelse**: Krav på elektronisk signeringsfunktion för delegerade HSL-insatser eller integration mot MCSS.

#### Kuben
**Typ**: Planeringssystem för vårdbehov/tider

**Användning**:
- Planera insatser i Säbo/hemsjukvård utifrån vårdtyngd och personalresurser

**Integrationer**:
- Lifecare (beslut/insatser)
- Medvind (schemaläggning)

#### Mina Planer
**Leverantör**: Region Skåne + Skånes Kommuner  
**Typ**: IT-stöd för samordnad vårdplanering (SVU) och Samordnad Individuell Plan (SIP)

**Användning**:
- Utskrivningsklara patienter
- Planering mellan sjukhus, primärvård och kommun

**Integrationer**:
- Regionens system → Mina Planer → Lifecare

**RFI-betydelse**: Nytt system måste kunna ta emot/visa information från Mina Planer och dokumentera SIP/planer.

#### NPÖ (Nationell patientöversikt)
**Leverantör**: Inera  
**Typ**: Nationell tjänst för att dela journalinformation mellan vårdgivare

**Användning**:
- Hälso- och sjukvårdspersonal kan läsa journalinformation från regioner och andra vårdgivare

**Integrationer**:
- Lifecare/MCSS → NPÖ (publicering)
- NPÖ → kliniska arbetsflöden (konsumtion)

**RFI-betydelse**: Nytt system måste stödja NPÖ (både konsumera och publicera).

#### Pascal
**Leverantör**: Inera  
**Typ**: Nationellt IT-stöd för ordination och beställning av dosdispenserade läkemedel

**Användning**:
- Ordna dospåsar och läkemedelslistor för patienter

**Integrationer**:
- Lifecare/MCSS ↔ Pascal ↔ Apotek/dosleverantör

**RFI-betydelse**: Krav på integrationsstöd (direktlänk/SSO, strukturerad läkemedelslista).

#### Senior Alert
**Leverantör**: CPUA Region Jönköpings län  
**Typ**: Nationellt kvalitetsregister för vårdprevention

**Användning**:
- Riskbedömningar, åtgärdsplaner och uppföljning för äldre
- Fall, trycksår, nutrition, munhälsa, blåsdysfunktion

**Integrationer**:
- Lifecare (riskbedömning/åtgärder) → Senior Alert (rapportering)

**RFI-betydelse**: Krav på stöd för registrering och export till nationella kvalitetsregister.

#### Webb SESAM
**Typ**: Hjälpmedelssystem för beställning/administration av hjälpmedel

### 2. Larm & Välfärdsteknik

System för trygghetslarm, välfärdsteknik och larmhantering.

#### 3CX
**Leverantör**: 3CX  
**Typ**: Mjukvarubaserad IP-PBX / kommunikationsplattform (VoIP, telefoni, video, chatt)

**Användning**:
- Telefonväxel i larmcentralen för samtal från trygghetslarm
- Köer, hänvisning, inspelning, statistik

**Integrationer**:
- Interview/ISM (larmmottagning)
- CMP (trygghetslarm)
- GuardTools (väktare)
- Lime CRM (kunddata)

**RFI-betydelse**: Placera i kommunikationslagret. Krav på hög tillgänglighet, redundans, SIP-trunkar, loggning, statistik, API/CTI-integration.

#### Interview/ISM
**Typ**: Larmmottagningssystem för trygghets-, person- och inbrottslarm

**Användning**:
- Core i larmkedjan
- Mottagning och hantering av larm

**Integrationer**:
- 3CX (telefoni)
- CMP (trygghetslarm)
- Milestone (kameralarm)
- GuardTools (väktare)

**RFI-betydelse**: Kritiskt system i larmkedjan. Beskriv integrationer och krav på redundans.

#### CMP (Neat - Care Management Portal)
**Leverantör**: Legrand Care / Neat Group  
**Typ**: Webbportal för fjärradministration och övervakning av trygghetstelefoner/trygghetslarm

**Användning**:
- Administrera trygghetstelefoner i hemmen
- Firmware-uppdateringar, larmprofiler, felövervakning
- Larmhistorik, status på larmterminaler

**Integrationer**:
- Trygghetslarm → CMP/Neat → Interview/3CX/GuardTools

**RFI-betydelse**: Krav på integration mellan framtida verksamhetssystem och välfärdsteknikplattform för larmstatus på brukarnivå.

#### GuardTools
**Typ**: Mjukvarusvit för bevakningsbranschen

**Användning**:
- Larmhantering, patruller, väktaruppdrag, rapportering

**Integrationer**:
- Interview/ISM
- 3CX
- CMP

#### Milestone
**Leverantör**: Milestone Systems  
**Typ**: Video management system (VMS) för kamerabevakning

**Användning**:
- Kameralarm och digital tillsyn nattetid från larmcentralen

**Integrationer**:
- Interview/ISM (larmcentral)
- Säbo/hemtjänst

**RFI-betydelse**: Krav på hantering av kameralarm som del av trygghetskedjan, med loggning, sekretess och integration.

#### Viser & Sensio trygghetssensorer / Smooth Lite
**Leverantör**: SensioCare (Viser) och Great Security (Smooth Lite)  
**Typ**: Trygghetssensorer och larmsystem i särskilt boende

**Användning**:
- Övervakar nattaktivitet, fall, frånvaro ur säng
- Sängsensorer, rörelsesensorer

**Integrationer**:
- Sensorer → Viser/Skyresponse → personalens mobiler
- Verksamhetssystem (journal/larmnotering)
- Milestone (kamera vid larm)

**RFI-betydelse**: Beskriv arkitektur för välfärdsteknik - flera leverantörer, behov av sammanhållen larm- och eventplattform.

#### Phoniro Lock systems / digitala lås
**Leverantör**: Phoniro / Assa Abloy  
**Typ**: Digitala dörrlås för hemtjänstbrukare

**Användning**:
- Omvårdnadspersonal låser upp med mobil/Säker delad mobil
- Kvittens kopplas till tidsregistrering

**Integrationer**:
- Phoniro Care (primär)
- Lifecare (indirekt via planerade insatser)

**RFI-betydelse**: Krav på stöd för digitala lås, mobil åtkomst, öppna API:er, säkerhetsnivå (Freja/SITHS).

### 3. Kvalitet & Ledning

System för kvalitetsledning, avvikelsehantering och rapportering.

#### EcoTech
**Leverantör**: EcoTech  
**Typ**: Molnbaserat ledningssystem för kvalitet/miljö/arbetsmiljö

**Användning**:
- Policyer, rutiner, egenkontroller, avvikelseflöden
- Dokumenthantering, lagbevakning

**Integrationer**:
- Främst via dokumentlänkar och export (ingen hård realtidsintegration)

**RFI-betydelse**: Fundera om EcoTech ska fortsätta vara "source of truth" för rutiner, eller om leverantören ska integrera mot eller ersätta det.

#### Agera (incidentrapportering)
**Leverantör**: Flexite  
**Typ**: Avvikelse-/incidenthanteringssystem (arbetsmiljö, säkerhet, kvalitet)

**Användning**:
- Rapportering av tillbud, olycksfall och avvikelser
- Arbetsmiljö och patientsäkerhet
- Utredning, följa upp, analysera mönster

**Integrationer**:
- HRutan/Medvind (personalsystem)
- EcoTech (kvalitetssystem)
- Stratsys/BI (rapporter)

**RFI-betydelse**: Krav på statistik, analys, integration med personalsystem och kvalitetssystem.

#### Avvikelse-/synpunktssystem (Selfpoint-plattform)
**Leverantör**: Selfpoint  
**Typ**: Plattform för avvikelse- och synpunktshantering

**Användning**:
- Personal: registrera avvikelser (fall, läkemedel, bemötande, arbetsmiljö)
- Medborgare: lämna synpunkter/klagomål via e-tjänster

**Integrationer**:
- Lifecare/Phoniro (ärendenummer)
- Koll/QlikView, Stratsys (BI)

**RFI-betydelse**: Fundera om detta ska ersättas, integreras eller leva kvar - många leverantörer erbjuder inbyggd avvikelsehantering. Krav på API, export, strukturerade avvikelsetyper.

#### Stratsys
**Typ**: Mål- och uppföljnings/rapportverktyg

**Användning**:
- Kopplat till ekonomi och kvalitetsuppföljning

**Integrationer**:
- Ekot (ekonomi)
- Agera (avvikelser)

#### Koll - QlikView
**Typ**: BI-lösning (QlikView-appar)

**Användning**:
- Ekonomirapportering
- Analys och rapporter

**Integrationer**:
- Ekot (ekonomidata)
- Lifecare (vårddata)

### 4. HR & Personal

System för personalhantering och HR-processer.

#### HRutan
**Typ**: HR-/självservice-portal för Malmö stad

**Användning**:
- Personalinfo, självservice
- Arbetsrelaterade uppgifter

**Integrationer**:
- Medvind (schema)
- Adato (rehab)

**RFI-betydelse**: Omsorgssystemet behöver utbyta uppgifter om personal, behörigheter, vikarier. HR-systemen är typiskt egna "core system" som inte ersätts vid omsorgs-RFI.

#### Medvind
**Typ**: Centralt personalsystem för schema och tidrapportering

**Användning**:
- Schema och tidrapportering i Malmö stad

**Integrationer**:
- HRutan (personaldata)
- Kuben (planering)

#### Vikariebanken
**Typ**: System för hantering av timvikarier

**Användning**:
- Hantering av timvikarier

**Integrationer**:
- HRutan (personaldata)

#### Visma Recruit
**Typ**: Rekryteringsverktyg för HR

**Användning**:
- Rekrytering

**Integrationer**:
- HRutan (anställningsdata)

#### Adato
**Leverantör**: Miljödata AB  
**Typ**: Rehabiliterings- och sjukfrånvarosystem

**Användning**:
- Dokumentation av rehabärenden och sjukfrånvaro
- Stödjer arbetsgivarens skyldigheter och rehabprocess

**Integrationer**:
- HRutan/Medvind (anställdas data)

**RFI-betydelse**: Om rehabfunktionalitet ska in i nytt verksamhetssystem eller HR-plattform: krav på stöd för rehabprocess, GDPR-säker dokumentation, behörighetsstyrning, statistik.

### 5. Säkerhet & Access

System för säkerhet, passerkontroll och accesshantering.

#### ARX passagesystem
**Leverantör**: ASSA ABLOY  
**Typ**: Passer- och larmsystem för dörrar/fastigheter

**Användning**:
- Passerkontroll i boenden, kontor, larmcentral, serverrum
- Kopplas till inbrottslarm och andra säkerhetssystem

**Integrationer**:
- KeyWin/Traka (nyckelskåp)
- Phoniro Lock, Sensio, Smooth (digitala lås)
- GuardTools (väktarsystem)

**RFI-betydelse**: Beskriv beroenden till omsorgssystem (schema/behörighet via AD), loggning, säkerhet, öppna API:er för passersystemdata.

#### KeyWin / Traka
**Typ**: Nyckelskåpssystem (nyckeladministration, loggning)

**Användning**:
- Nyckeladministration och loggning

**Integrationer**:
- ARX (passersystem)
- Omsorgsverksamhet

#### Stanley Unizon, RCO, SoliCard
**Typ**: Passer- och säkerhetssystem

**Användning**:
- Passerkontroll och säkerhet

### 6. Infrastruktur/IT-förvaltning

System för IT-infrastruktur och förvaltning.

#### MSM/Marval
**Typ**: IT-ärendehanteringssystem

**Användning**:
- IT-support och ärenden

#### Snipe-IT
**Typ**: Open source inventariesystem för IT-utrustning

**Användning**:
- Inventering av IT-utrustning

#### EasyApp
**Leverantör**: Secure & Safe  
**Typ**: Molnbaserat inventarie- och märkningssystem

**Användning**:
- Inventering av IT-utrustning, välfärdsteknik, hjälpmedel
- Spårbarhet av trygghetssensorer, nyckelskåp, terminaler

**Integrationer**:
- CMP, Sensio, Smooth, Traka/KeyWin (logisk koppling)

**RFI-betydelse**: Krav på att nytt verksamhetssystem ska kunna referera till utrustning/ID eller att inventariesystemet fortsätter fristående med rapportexport.

#### Intune
**Leverantör**: Microsoft  
**Typ**: MDM/MEM för mobil- och klienthantering

**Användning**:
- Säkerhet, appar, mobilhantering

#### IFacts
**Typ**: IT-förvaltningssystem

#### KomKat / HSA
**Leverantör**: KFSK  
**Typ**: Administration av HSA-katalogen (identiteter och behörigheter i vård/omsorg)

**Användning**:
- Identitets- och behörighetshantering

**Integrationer**:
- Vård/omsorgssystem (behörigheter)

#### Imprivata
**Typ**: Lösningar för Single Sign-On och klinisk åtkomst

**Användning**:
- Snabb inloggning, kort-inloggning
- Relevanta för journalsystem, MCSS

### 7. Övriga System

#### Open e-plattformen
**Leverantör**: Malmö stad (byggd på Ineras/Open ePlatform)  
**Typ**: E-tjänsteplattform

**Användning**:
- Skapa digitala tjänster som kan kopplas mot verksamhetssystem

**Integrationer**:
- Lifecare (verksamhetssystem)

#### Platina
**Typ**: Dokument- och ärendehanteringssystem

**Användning**:
- Nämndsärenden, beslut

#### Maskeringstjänsten (Atea)
**Typ**: AI-tjänst för att maskera personuppgifter

**Användning**:
- Maskera personuppgifter i handlingar inför utlämning

#### Lime CRM
**Typ**: CRM-system (svensk leverantör)

**Användning**:
- Kund- och avtalsdata för fastighetsägare/e-lås

**Integrationer**:
- 3CX (kunddata vid larm)

#### Ekot/Raindance
**Typ**: Ekonomisystem

**Användning**:
- Ekonomi och budget

**Integrationer**:
- Lifecare (debitering)
- Koll/QlikView, Stratsys (rapporter)

**RFI-betydelse**: Omsorgssystemet behöver integrera för debitering, men ekonomisystemet ersätts typiskt inte vid omsorgs-RFI.

## Smärtpunkter

### Dubbel dokumentation
- Mellan Lifecare, Phoniro, Senior Alert, Mina Planer
- Behov av minskad dubbel dokumentation

### Integrationer
- Många olika system som behöver integreras
- Olika integrationstyper (API, batch, manuell)

### Välfärdsteknik
- Flera leverantörer (Sensio, Great Security, Neat)
- Behov av sammanhållen larm- och eventplattform

### Nationella tjänster
- Krav på integration med NPÖ, Pascal, Mina Planer, Senior Alert
- Dubbel dokumentation mellan system

## RFI-fokus

För RFI bör följande beskrivas tydligt:

1. **Vilken roll systemet har idag** - Vad gör systemet i verksamheten?
2. **Vilken information det är master för** - Var är datan auktoritativ?
3. **Vilka externa tjänster som är "must have" integrationer** - NPÖ, Pascal, Mina Planer, Senior Alert, digitala lås, trygghetssensorer, tid- & insatsuppföljning
4. **Vilka smärtpunkter verksamheten upplever** - Dubbel dokumentation, integrationer, välfärdsteknik

## Nästa steg

1. Uppdatera integrationskarta med dessa kopplingar
2. Skapa detaljerade RFI-krav per system
3. Identifiera kritiska integrationer
4. Dokumentera smärtpunkter och förbättringsmöjligheter

