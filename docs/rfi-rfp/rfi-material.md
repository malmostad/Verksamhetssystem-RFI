# RFI-material - Verksamhetssystemsbyte (översikt)

## Syfte & viktig princip

Detta dokument är en informationssamling för Request for Information (RFI) inför ett eventuellt byte av verksamhetssystem för HVOF. Viktigt: RFI-dokumentet innehåller inga bindande krav. Vi efterfrågar leverantörers information om kapabilitet, integrationserfarenhet, referenser och estimat — inte koncisa kravspecifikationer.

!!! note "RFI-princip"
    RFI innehåller *inte* krav. Be leverantörer beskriva hur deras lösning kan möta våra behov, vilka dataflöden de stöder, och ge exempel på tidigare leveranser.

## Snabböversikt (högnivå)

| Nyckel | Värde |
|---|---:|
| Antal system i landskapet | 57 |
| Fokusområden | Vård & omsorg, larm, planering, kvalitet |
| Viktigaste intressenter | Handläggare, sjuksköterskor, chefer, ekonomi |

## Nuvarande landskap (kort)

### Kärnsystem – Lifecare / Procapita

| Egenskap | Beskrivning |
|---|---|
| Leverantör | Tietoevry Care |
| Typ | Verksamhetssystem för SoL, LSS, HSL |
| Huvudfunktioner | Dokumentation, handläggning, vårdplanering, journalföring, uppföljning |

## Viktiga integrationsytor (översikt)

| Domän | System / Exempel | Typ av integration | Syfte |
|---|---|---|---|
| Nationella e‑hälsa | NPÖ | API / HL7 | Journalutbyte, delad patientinfo |
| Läkemedel | Pascal | API / SSO | Ordination, läkemedelslista |
| Kvalitetsregister | Senior Alert | Export / API | Riskbedömningar & uppföljning |
| Vårdplan | Mina Planer | API / dokumentutbyte | Samordnad vårdplanering (SIP) |
| Tid/insats | Phoniro Care | API / databas | Besökskvittering, uppföljning |
| Digital signering | MCSS | API / SSO | Elektronisk signering |
| Välfärdsteknik | CMP, Viser, Sensio | API / event | Larm & sensorhändelser |
| Larmcentral & telefoni | Interview/ISM, 3CX, Milestone | API / CTI | Larmmottagning, kameralarm, telefoni |

## Smärtpunkter & effekt (tabell)

| Problem | Konsekvens | Önskad förbättring |
|---|---|---|
| Dubbel dokumentation mellan system | Förlorad tid, fel, inkonsistens | Färre system-beroende manuella flöden, mer synkronisering |
| Många leverantörer för välfärdsteknik | Fragmenterad bild, integrationsarbete | Enhetlig eventplattform eller standardiserad integration |
| Blandade integrationstyper (API, batch, manuellt) | Komplex drift & underhåll | Standardiserade API:er, fler realtidsflöden |
| Nationella tjänster kräver stöd | Ökad integrationskostnad | Tydliga kopplingar till nationella gränssnitt |

## Scope för RFI (vad vi frågar om)

- Övergripande arkitektur och dataflöden
- Stöd för integrationsmönster (API, HL7, export/import)
- Erfarenhet av liknande kommun-/regionprojekt och referenser
- Förslag på migreringsstrategi och stöd för dataöverföring (högnivå)
- Drift- och säkerhetsmodeller (högnivå)

!!! tip "Observera"
    I detta RFI ber vi inte om en detaljerad kravlista eller bindande svar. Istället vill vi att leverantörer beskriver möjligheter, begränsningar och uppskattningar.

## Datamigration - högnivå (fokusområden)

| Domän | Vikt | Kommentar |
|---|---:|---|
| Vårddata | Hög | Journaler, vårdplaner och beslut kräver bevarande av historik |
| Tid/insats | Hög | Besöksdata från Phoniro bör migreras eller integreras under övergång |
| Läkemedel | Medel | Koppling till Pascal kräver strukturbevarande |
| Kvalitetsdata | Medel | Senior Alert export/import |

## Processöversikt (högnivå)

| Processområde | Viktiga flöden |
|---|---|
| Handläggning | Ärendehantering, beslut, dokumentation |
| Vårdplanering | Skapa, dela och följa upp planer (SIP, SVU) |
| Larm & trygghet | Sensorhändelser → aviseringar → åtgärd |
| Personal & HR | Scheman, tidrapportering, vikarier |

## Frågor till leverantörer (exempel - används i `supplier-questions.md`)

1. Beskriv er lösningsarkitektur och hur den hanterar integrationer mot nationella tjänster (NPÖ, Pascal, etc.).
2. Ge minst två referenser från kommunal vård/omsorg där ni levererat liknande integrationslösningar.
3. Hur hanterar ni datamigrering av journaler och historik? Ge en högnivåbeskrivning.
4. Vilka standarder och dataformat stödjer ni idag (API, HL7, FHIR etc.)?

## Relaterade dokument

- [Systemlandskap - RFI-fokus](../systems/system-landscape-rfi.md)
- [Frågor till leverantörer](supplier-questions.md)
- [Utvärderingskriterier](evaluation-criteria.md)

## Kontakt

För frågor om RFI-material, kontakta IT-avdelningen (se `about/contact.md`).

## Uppdaterad

Senast uppdaterad: 2024-12-10
Uppdaterad av: [Namn]
