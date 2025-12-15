# IT-miljö
## Malmö stad | Hälsa, Vård och Omsorg (HVOF)

HVOF:s IT-miljö kännetecknas av en komplex blandning av nationella, regionala och lokala applikationer som kräver olika inloggningsförfaranden och autentiseringsmetoder. Våra medarbetare använder många olika applikationer för delar av verksamhetsprocesser.

## Blandning av applikationstyper

Systemlandskapet består av en heterogen mix av applikationer från olika nivåer som används för olika delar av verksamhetsprocesser.

**Nationella system** kräver specifika autentiseringsmetoder och integrationer enligt nationella standarder. Dessa system är kritiska för verksamheten och måste integreras med verksamhetssystemet.

| System | Användargrupper | Inloggningsmetod | Förvaltare | Kommentar |
|--------|-----------------|------------------|------------|-----------|
| **NPÖ** (Nationella Patientöversikten) | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | SITHS | Inera | HSA-katalog, webb |
| **Pascal** (Läkemedelshantering) | Sjuksköterskor | SITHS | Inera | HSA-katalog |
| **Förskrivningskollen** | Sjuksköterskor | SITHS | Inera | Ej responsivt, kräver laptop, ej touch screen |

**Regionala system** används för samordning och kvalitetssäkring. Dessa system kräver API-integrationer och stöd för dokumentutbyte.

| System | Användargrupper | Inloggningsmetod | Förvaltare | Kommentar |
|--------|-----------------|------------------|------------|-----------|
| **Mina Planer** (Samordnad vårdplan) | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | SITHS eller Freja eID | Komin | Responsivt, webb |
| **Kvalitetsregister** | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | SITHS | | |

**Lokala system** utgör majoriteten av systemlandskapet. Dessa inkluderar verksamhetssystem, ekonomisystem, HR-system och specialiserade applikationer för olika verksamhetsområden.

| System | Användargrupper | Inloggningsmetod | Förvaltare | Kommentar |
|--------|-----------------|------------------|------------|-----------|
| **MCSS** (Digital signering) | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | SITHS eller Freja eID | Malmö stad | Avtal går ut 2026-09-01 |
| **Journalföringssystem** | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | SITHS | | Kommer att bytas |
| **WebSESAM** | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | Användarnamn + lösenord | | Responsivt |
| **Exorlive** | Arbetsterapeuter, Fysioterapeuter | Användarnamn + lösenord | | |
| **Kvalitetsavvikelser** (Selfpoint) | Sjuksköterskor, Arbetsterapeuter, Fysioterapeuter | Användarnamn + lösenord | | |

## Inloggningsförfaranden

Den nuvarande IT-miljön kräver att användare hanterar flera olika inloggningsmetoder. **SITHS** (Sjukvårdens IT-säkerhet) krävs för vårddata och används i de flesta nationella och regionala system. Idag används SITHS kort som inloggningsmetod, men målet är att använda **SITHS eID** för enklare och säkrare inloggning. **Freja eID** används för vissa system som MCSS och Mina Planer. Många lokala system använder fortfarande **användarnamn + lösenord** med olika krav på komplexitet och uppdateringsfrekvens.

## Systemegenskaper

Systemen i vår IT-miljö har olika tekniska egenskaper och krav. Vissa system är responsiva och kan användas på olika enheter, medan andra kräver specifika enheter eller konfigurationer. Till exempel kräver **Förskrivningskollen** hög upplösning (1920x1080 pixlar), stor fysisk skärmyta (14") samt mus eller pekplatta, vilket gör det svårt att använda på mobiltelefon eller surfplatta.

## Integrationer och tekniska krav

Systemen i vår IT-miljö har olika tekniska krav för integrationer. Nationella system kräver ofta HL7 FHIR-standard och specifika API:er. Regionala system kan ha olika krav på dokumentformat och datautbyte. Lokala system kan ha varierande stöd för API:er och integrationer.

## System vars avtal går ut

Flera system i nuvarande systemlandskap har avtal som går ut inom närmaste åren. Detta kan påverka planeringen för ett nytt verksamhetssystem och integrationsmöjligheter.

| System | Leverantör | Typ | Avtal går ut | Kommentar |
|--------|------------|-----|--------------|-----------|
| **iBinder** | iBinder Sverige AB | Fastighetsprogram | 2025-12-21 | Drift av förvaltningen |
| **TicTac Learn** | TicTac Learn AB | E-lärande verktyg | 2026-04-07 | Verktyg för e-lärande |
| **Optinet** | Optinet Data AB | Ärendehanteringssystem | 2026-06-10 | Ärendehantering |
| **TimeZynk** | TimeZynk AB | Planering och schemaläggning | 2026-07-31 | Planering-, beställnings- och schemaläggningssystem |
| **MCSS** | Vitec Appva AB | Digital signering | 2026-09-01 | IT-stöd för administration av omsorgsinsatser |
| **Inventariesystem** | Secure & Safe TechPrint AB | Inventariesystem | 2026-09-12 | Inventariehantering |
| **Procapita/Lifecare** | Tietoevry AB | Verksamhetssystem | 2028-12-30 | Support och underhåll av Procapita/Lifecare IFO VoO |

System vars avtal går ut inom närmaste åren kan påverka integrationsplaneringen för ett nytt verksamhetssystem.

---

**Malmö stad | Hälsa, Vård och Omsorg (HVOF)**


