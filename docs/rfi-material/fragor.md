# Frågor till leverantörer
## Malmö stad | Hälsa, Vård och Omsorg (HVOF)

!!! info "RFI-format"
    Detta är en informationsinsamling. Svaren hjälper oss att bedöma er lösnings lämplighet för en framtida RFP.

---

## 1. Arkitektur och integration

**Våra behov**: Vi har ett komplext systemlandskap med många system och behöver standardiserade API:er för integration.

**Frågor**:

1. Beskriv er lösningsarkitektur – vilka komponenter och integrationspunkter ingår?
2. Vilka API:er exponerar systemet? (REST, SOAP, GraphQL, gRPC?)
3. Stödjer systemet HL7 FHIR-standard för vårddata?
4. Hur säkerställer ni datakvalité vid integrationspunkter?
5. Kan vi övervaka integrationer i realtid?
6. Vilka säkerhetsstandarder använder ni för API-kommunikation? (OAuth2, mTLS, etc.)

---

## 2. Datamigration från Lifecare-Procapita

**Våra behov**: Vi måste migrera historisk data från befintliga system med bibehållen datakvalitet.

**Frågor**:

1. Har ni erfarenhet av att migrera från verksamhetssystem för äldreomsorg?
2. Vilka datatyper kan systemet ta emot? (Journaler, vårddokument, tidsstämplar, relationer?)
3. Hur hanterar ni historiska data och ändringsloggar?
4. Kan ni bevara systemrelationer och kopplingar mellan data?
5. Vilken validering och datakvalitetskontroll gör ni under migration?
6. Ungefärlig tid för datamigration för vår datamängd?

---

## 3. Autentisering och åtkomstkontroll

**Våra behov**: Vi använder Freja eID och e-SITHS för autentisering av användare och sjukvårdspersonal.

**Frågor**:

1. Stödjer systemet Freja eID-inloggning via SSO?
2. Stödjer systemet e-SITHS för sjukvårdspersonal?
3. Hur hanterar systemet rollbaserad åtkomst (RBAC)?
4. Vilka andra autentiseringsmetoder stödjer ni? (LDAP, SAML, OAuth2?)
5. Hur loggar och granskar ni åtkomstförsök? (GDPR-spårning)

---

## 4. Säkerhet, dataskydd och regelefterlevnad

**Våra behov**: Vi hanterar känslig hälso- och personaldata. GDPR-efterlevnad, patientintegritet och datasäkerhet är kritiska.

**Frågor**:

1. Vilka säkerhetscertifieringar har systemet? (ISO 27001, SOC 2, annat?)
2. Var lagras data geografiskt? (Föredraget: Sverige eller EU)
3. Vilka backup- och disaster recovery-procedurer är etablerade?
4. Hur implementerar ni rätten till radering enligt GDPR?
5. Finns databehandlaravtal (DPA) tillgängliga för svenska kommuner?
6. Vilken kryptering använder systemet? (I transit och at rest)
7. Hur ofta genomför ni säkerhetsgranskning/penetrationstester?
8. Vilken process finns för rapportering av säkerhetshändelser?

---

## 5. Prestanda och skalbarhet

**Våra behov**: Systemet måste stödja vår verksamhets omfattning med flera samtidiga användare under toppbelastning.

**Frågor**:

1. Hur många samtidiga användare kan systemet hantera?
2. Vad är genomsnittlig svarstid för normala operationer?
3. Vad är systemets maximala belastningskapacitet?
4. Vilken tillgänglighet (SLA) erbjuder ni? (99,5%, 99,9%, 99,99%?)
5. Hur hanterar ni databasskalning vid växande användarantal?
6. Vilken redundans och failover-strategi har systemet? (Multi-region? Hot standby?)

---

## 6. Rapportering, affärsanalys och data

**Våra behov**: Vi behöver verksamhetsöversikt, statistik och möjlighet att koppla till nationella register.

**Frågor**:

1. Vilka rapporter kan systemet generera från starten?
2. Kan vi bygga egna rapporter? (Vilka verktyg och möjligheter?)
3. Hur exponerar systemet data för BI-system? (Vi använder idag Qlikview/Qlik)
4. Stödjer systemet dataexport? (CSV, Excel, API?)
5. Vilka verksamhetstal kan vi följa i realtid?
6. Kan systemet integrera med nationella register för Socialstyrelsens rapportering?

---

## 7. Support, underhåll och fortsatt utveckling

**Våra behov**: Systemet måste underhållas under många år med regelbundna uppdateringar, säkerhetsuppdateringar och ny funktionalitet.

**Frågor**:

1. Vilken supportnivå erbjuder ni? (24/7? Kontorstid?)
2. Vad är svarsnivåerna för kritiska problem? (1 timme? 4 timmar?)
3. Hur ofta uppdateras systemet? (Varje månad? Varje kvartal?)
4. Vilka nya funktioner är på er produktroadmap för nästa 2 år?
5. Hur garanterar ni backward-kompatibilitet vid systemuppdateringar?
6. Kan vi påverka er produktutveckling? (Feature requests och prioritering?)
7. Vilken produktsupport garanteras långsiktigt? (Till 2030? 2035?)

---

## 8. Implementeringstidsplan och projektöversikt

**Våra behov**: Vi behöver ungefärlig tidsplan för att planera internt.

**Frågor**:

1. Vilken totaltid uppskattar ni för implementering? (Från avtal till go-live)
2. Hur många resurser krävs från vår sida? (Antal personer och tidsomfattning)
3. Vilka huvudmilstolpar föreslår ni för projektet?
4. Vilken tid krävs för datamigration och testning?
5. Kan ni implementera enligt denna tidsplan parallellt med andra systembyte?
6. Vilka risker identifierar ni och hur mitigerar ni dem?
7. Kan vi göra en pilot/test innan full rollout?
8. Vilken parallell drifttid behövs? (Veckor? Månader?)

---

## 9. Molntjänster och hostingmodell (för SaaS-lösningar)

**Våra behov**: Vi behöver förstå molninfrastruktur, datalagring och kostnadsstruktur för SaaS-lösningar.

**Frågor**:

1. **Var lagras data geografiskt och under vilka juridiska ramverk?**
   - Fysisk datacentersplats: Vilka länder använder ni för datalagrering? (Vi kräver Sverige eller EU)
   - Redundans: Var befinner sig backups och disaster recovery-miljöer geografiskt?
   - Juridisk jurisdiktion: Under vilken jurisdiktion regleras databehandlingen?
   - Ägande av datacentret: Ägs datacentret av er eller av en tredjepartsoperatör?
   - Underleverantörer: Kan data hamna hos tredjepartsoperatörer eller molnleverantörer utanför EU?
   - Gränsövervakningsmöjlighet: Kan Malmö stad övervaka att data inte överförs till tredje länder?

2. **Vilken SaaS-modell använder ni och vad är licensieringsmodellen?**
   - Delning av data: Kan Malmö stads data komma att lagras tillsammans med andra kunders data?
   - Isolering: Vilka tekniska åtgärder säkerställer att våra data är åtskilda?
   - Kostnadsmodell: Licensering per användare, per system, per GB data, eller något annat?
   - Hidden costs: Vilka tilläggskostnader kan komma? (API-anrop, datalagring, support, uppdateringar)
   - Kostnadsövervakning: Kan vi se i realtid vad vi använder och vad som kommer att kosta?

3. **Tillgänglighet och Service Level Agreement (SLA)**
   - Systemtillgänglighet: Vad är er garanterad SLA? (Uptime procent, planerat underhåll)
   - Incidentrespons: Vad är er svarsprocedur när systemet är nere? (RTO, RPO)
   - Backup och disaster recovery: Hur ofta säkerhetskopieras data? Var lagras backups?
   - Eskalering: Hur hanteras kritiska problem? (Kontaktperson 24/7, supportlinjer på svenska)
   - Kompensation: Vad kompenserar ni om SLA-nivån missgynnas?

---

## 10. Cybersäkerhetslagen (NIS 2) - Obligatoriska säkerhetskrav

**Våra behov**: Cybersäkerhetslagen kräver att vi kan verifiera säkerheten. Vi behöver dokumenterat bevis från oberoende revisorer.

**Frågor**:

1. **Säkerhetscertifieringar och tredjepartsrapporter**
   - SOC 2 Type II: Har ni en aktuell rapport? (Max 12 månader gammal, från Big 4 rekommenderas)
   - ISO 27001: Är ni certifierade? Giltigt till när? Bifoga Statement of Applicability (SoA)
   - ISO 27018: Har ni certifiering för skydd av personuppgifter i molnet?
   - Personalsäkerhet: Genomgår all personal säkerhetsvetting? Finns sekretessavtal?
   - Penetrationstest: Utför ni årliga penetrationstester av externa säkerhetstestare?

2. **Kryptering enligt Cybersäkerhetslagen**
   - Kryptering i transit: Vilken protokoll använder ni? (TLS 1.2 minimum, helst 1.3)
   - Kryptering at rest: Är all patientdata krypterad vid lagring? (AES-256 rekommenderas)
   - Nyckelhantering: **Kan vi lagra och kontrollera våra egna krypteringsnycklar?** (KRITISK för OSL)
   - Prestanda: Märker användare någon prestandapåverkan från krypteringen?

3. **Incidenthantering och kontinuitetshantering**
   - Incidenthantering: Har ni en dokumenterad policy? Maximal tid till svar? (< 1 timme för kritiska)
   - Kontinuitetshantering: Vad är RTO och RPO? (Målvärde: RTO < 4 timmar, RPO < 1 timme)
   - Kommunikation vid incident: Vad är maximal tid före meddelande? (< 24 timmar)

---

## 11. Offentlighet- och Sekretesslagen (OSL) - Dataskyddskrav

**Våra behov**: OSL förbjuder att sekretessbelagd information delas med tredje parter om de inte är rent tekniska databearbetare utan eget inflytande.

**Frågor**:

1. **Åtkomst till data - vem kan läsa Malmö stads information?**
   - Direktanställda: Vilka anställda har åtkomst? Omfattas de av sekretessavtal?
   - Underleverantörer: Vilka underleverantörer har åtkomst? Lista namn, land, typ av tillgång
   - Moderbolag: Har moderbolaget åtkomst till våra data?
   - Geografisk spridning: I vilka länder kan personal läsa våra data? (Vi kräver endast Sverige eller EU)

2. **Datalagrering och dataisolering**
   - Samlokalisering: Lagras våra data tillsammans med andra kunders data i samma databas?
   - Dataisolering: Vilka tekniska åtgärder säkerställer att våra data är åtskilda?
   - Riskanalys: Finns risk att andra kunders administratörer kan läsa våra data?
   - Regulatory compliance: Omfattas er SaaS-miljö av granskning eller certifiering?

3. **Säkerhetsmål för OSL-kompatibilitet**
   - Kryptering vid lagring: AES-256 eller motsvarande?
   - Kryptering i transit: TLS 1.2+?
   - Åtkomstkontroll: Multi-factor autentisering?
   - Loggning av åtkomst: All åtkomst loggad?
   - Brandvägg och nätverk: IP-whitelist, VPN?
   - Personalsäkerhet: Säkerhetsvetting av personal?

---

## 12. GDPR och dataskydd

**Våra behov**: Vi är personuppgiftsansvarig enligt GDPR och behöver garantier för dataskydd.

**Frågor**:

1. Erbjuder ni ett Datbehandlaravtal (Data Processing Agreement)?
2. Godkänner ni att vi genomför en GDPR-konsekvensbedömning (DPIA)?
3. Godkänner ni att vi granskar er säkerhet regelbundet?
4. Hur implementerar ni rätten till radering enligt GDPR?
5. Hur implementerar ni rätten till dataportabilitet?

---

## 13. Integrationer och kostnadsmodell

**Våra behov**: Vi har många integrationer och behöver förstå er integrationsstrategi och kostnadsmodell.

**Frågor**:

1. Vilka API:er exponerar systemet? (REST? GraphQL? SOAP? HL7?)
2. Dokumentation tillgänglig? (Länk?)
3. Realtids-API eller endast batch-API?
4. Kostnadsmodell för integrationer: Ingår i baslicensen eller separat kostnadsmodell?
5. Begränsningar: Finns maximal gräns för API-anrop per dag/timme?
6. Kan ni ge exempel på kostnadsberäkning för vår integrationsmiljö?

---

## 14. Utdataplattform och BI-åtkomst

**Våra behov**: Vi använder idag Qlikview för BI och behöver kunna extrahera data från systemet.

**Frågor**:

1. Kan vi få åtkomst till data för rapportering? Via vilka metoder? (SQL-frågor? API? Export?)
2. I vilket format får vi data? (CSV? JSON? SQL-resultat?)
3. Hur aktuell är data? (Realtid? Daglig uppdatering?)
4. Ingår utdataplattformen i baslicensen eller finns separat kostnadsmodell?
5. Kan vi ansluta Qlikview direkt till er API/utdataplattform?

---

## 15. Sammanfattning - Kan ni uppfylla alla lagkrav?

**Frågor**:

1. **Cybersäkerhetslagen (NIS 2)**: Bekräfta att systemet kan uppfylla alla obligatoriska riskhanteringsåtgärder. Lista vilka ni redan uppfyller, vilka ni kan uppfylla med konfiguration, och vilka ni INTE kan uppfylla (om några).

2. **Offentlighet- och Sekretesslagen (OSL)**: Bekräfta att vi kan tillämpa 10 kap 2a § OSL med er tjänst. Bekräfta att vi kan dekryptera känslig data utan er hjälp. Bekräfta att okrypterad data INTE är tillgänglig för er personal eller underleverantörer.

3. **GDPR och dataskydd**: Erbjuder ni ett Datbehandlaravtal (Data Processing Agreement)? Godkänner ni att vi genomför en GDPR-konsekvensbedömning (DPIA)? Godkänner ni att vi granskar er säkerhet regelbundet?

4. **Övergripande lämplighet**: Baserat på denna informationsinsamling: Anser ni att er lösning passar för Malmö stad? Vilka är eventuella begränsningar eller utmaningar ni ser? Vad krävs från Malmö stad för att implementeringen ska lyckas?

---

## Svarformat - Obligatorisk information

Vi förväntar att er RFI-svar innehåller följande information:

| Element | Instruktion |
|---------|-------------|
| **Leverantörsnamn** | Organisationens officiella namn |
| **Kontaktperson** | Namn, e-postadress, telefon för uppföljning |
| **Svarsdatum** | Datum då svaret skickas |
| **Produktnamn och version** | Systemets officiella beteckning |
| **Följsamhetsstatus** | RFI-kompatibel (Ja / Nej / Delvis) |

**Instruktioner för svar per fråga**:
- Maximalt 2-5 stycken per fråga
- Använd tabeller och listor för tydlighet
- Bifoga gärna exempel, skärmdumpar och dokumentreferenser
- Ange källan eller referensen för varje påstående

---

## Dokumentation vi förväntar från leverantörer

Bifoga följande dokument tillsammans med svaren:

| Dokument | Förklaring |
|----------|-----------|
| **SOC 2 Type II-rapport** | Från oberoende revisor, max 12 mån gammal |
| **ISO 27001-certifikat** | Med Statement of Applicability (SoA) |
| **Datbehandlaravtal (DPA)** | Enligt GDPR |
| **Säkerhetspolicy** | Informationssäkerhetspolicy |
| **Incidenthanteringspolicy** | Dokumenterad process |
| **Kontinuitetsplan** | Med RTO/RPO-mål |
| **Prislista** | Transparent kostnadsmodell |
| **API-dokumentation** | För integrationer |
| **Teknisk arkitektur** | För kryptering, dataisolering, etc. |
| **Referenskunder** | Med kontaktuppgifter |

---

**Malmö stad | Hälsa, Vård och Omsorg (HVOF)**

