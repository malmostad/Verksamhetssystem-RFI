# Lagkrav som styr HVOF:s vård och omsorg (översikt)

Denna RFI ger en översikt över lagkrav som påverkar utformningen av verksamhetssystemet. Texten är förenklad för att ge leverantörer en tydlig bild av kontexten – inte en fullständig juridisk genomgång.

Systemet ska stödja intentionerna i lagstiftningen och möjliggöra efterlevnad genom bra funktioner, spårbarhet och säkerhet.

## Snabböversikt: Tre lagstiftningar – en arkitektur

!!! info "Tre lagar – ett verksamhetssystem"
    Verksamhetssystemet behöver uppfylla krav från **cybersäkerhet**, **offentlighet och sekretess** och **dataskydd** samtidigt.  
    Det påverkar både teknik (arkitektur, säkerhet) och hur funktioner för dokumentation, åtkomst och uppföljning utformas.

| Lag | Verkningsområde | Huvudkrav på lösningen | Leverantörens roll |
|-----|-----------------|------------------------|--------------------|
| **Cybersäkerhetslagen (NIS 2)** | Säkerhet i kritisk verksamhet och IT‑tjänster | Struktur för incidenthantering, kontinuitet, sårbarhetshantering, loggning och kryptering | Visa hur er tjänst uppfyller säkerhetskraven och hur ni arbetar med risker och incidenter |
| **Offentlighet- och sekretesslagen (OSL 10 kap. 2a §)** | Hantering av sekretessbelagd information (t.ex. journaler) | Malmö stad ska ha kontroll över data och nycklar, leverantören är teknisk databearbetare | Säkerställa att arkitektur, åtkomst och underleverantörer följer principen om teknisk databearbetning |
| **Dataskyddsförordningen (GDPR)** | All personuppgiftsbehandling | Stödja registrerades rättigheter, laglig grund, gallring och spårbarhet | Vara personuppgiftsbiträde med tydliga avtal, processer och tekniskt stöd i systemet |

Nedan följer korta avsnitt per lagområde samt hur de påverkar verksamhetssystemet.

## Sammanfattning: Centrala lagkrav och systemarkitektur

Mindmappen nedan fokuserar på de tre tvärgående regelverken **NIS 2**, **OSL 10 kap. 2a §** och **GDPR** som i första hand styr den tekniska arkitekturen. **SoL**, **HSL** och **Patientlagen** beskrivs i efterföljande avsnitt som verksamhetsnära bakgrund och kontext.

```mermaid
--8<-- "diagrams/lagkrav-mindmap.mmd"
```

## Socialtjänstlagen (SoL)

SoL syftar till att skapa trygghet och goda levnadsförhållanden för HVOF:s målgrupper, bland annat äldre och personer med funktionsnedsättning.  
För verksamhetssystemet innebär det stöd för en rättssäker handläggningskedja – från utredning och beslut till verkställighet och uppföljning – där varje steg är dokumenterat och spårbart. Systemet behöver också kunna ta fram underlag för uppföljning och rapportering på individ- och verksamhetsnivå.

## Hälso- och sjukvårdslagen (HSL)

HSL ställer krav på god vård, hög patientsäkerhet och samverkan mellan olika vårdgivare.  
Systemet behöver därför erbjuda tydlig och strukturerad journalföring, uppdaterade vårdplaner och funktioner som gör säker informationsdelning möjlig. Behörighetsstyrning och loggning ska säkerställa att endast behörig personal kan ta del av känsliga uppgifter.

## Patientlagen

Patientlagen stärker patientens ställning och rätt till information och delaktighet.  
Verksamhetssystemet ska kunna hantera informerat samtycke och val, göra relevant information lätt tillgänglig för behöriga användare och samtidigt ge full spårbarhet kring vem som har läst eller ändrat uppgifter om patienten.

## Cybersäkerhetslagen (NIS 2) – cybersäkerhet i praktiken

Malmö stad kommer att omfattas av Cybersäkerhetslagen genom införandet av NIS 2‑direktivet. Som verksamhet inom vård och omsorg ses HVOF som kritisk verksamhet, vilket innebär höga krav på informationssäkerhet.

De viktigaste kraven för verksamhetssystemet handlar om hur säkerhetsarbetet är organiserat. Systemet behöver stödja effektiv incidenthantering och ha tydliga lösningar för backup, återläsning och drift vid störningar. Leverantören ska ha etablerade rutiner för sårbarhetshantering och kunna visa hur brister identifieras, åtgärdas och kommuniceras.

Åtkomst till känsliga uppgifter ska styras genom stark autentisering (t.ex. SITHS, Freja eID) och rollbaserad behörighet (RBAC). All åtkomst till patient- och brukaruppgifter ska loggas och kunna följas upp. Data ska skyddas både i transit och i vila med moderna, välkända krypteringslösningar.
För verksamhetssystemet innebär detta bland annat att Malmö stad ska ha kontroll över data och, där det är möjligt, över krypteringsnycklar. Det ska vara tydligt vilka roller hos leverantören och eventuella underleverantörer som kan nå uppgifter, och dessa personer ska omfattas av lagstadgad eller avtalsreglerad tystnadsplikt. Samma krav på säkerhet och sekretess ska gälla genom hela leveranskedjan.


Leverantören förväntas kunna beskriva sin säkerhetsorganisation, sina processer och relevanta certifieringar eller rapporter (t.ex. ISO 27001, SOC 2).

## Offentlighet- och sekretesslagen (OSL 10 kap. 2a §) – datakontroll

HVOF hanterar stora mängder sekretessbelagd information, bland annat patientjournaler och känsliga personuppgifter. OSL tillåter att sådan information lämnas till en leverantör endast om leverantören fungerar som **teknisk databearbetare** utan eget inflytande över data.

För verksamhetssystemet innebär detta bland annat:

- **Datakontroll** – Malmö stad ska behålla kontroll över data och, där det är möjligt, krypteringsnycklar.
- **Åtkomst till data** – Det ska vara tydligt vilka roller hos leverantören och eventuella underleverantörer som kan komma åt data.
- **Tystnadsplikt** – Personal som kan ta del av sekretessbelagda uppgifter ska vara bunden av lagstadgad eller avtalsreglerad tystnadsplikt.
- **Underleverantörer** – Samma krav på säkerhet och sekretess ska gälla för alla parter i leveranskedjan.

## Dataskyddsförordningen (GDPR) – dataskydd och rättigheter

Malmö stad är personuppgiftsansvarig för behandling av personuppgifter inom HVOF. En leverantör av verksamhetssystem blir personuppgiftsbiträde.

Systemet behöver därför kunna ta fram och vid behov korrigera all relevant persondata om en brukare eller patient, hantera gallring, arkivering och radering enligt gällande regler och erbjuda export av data i strukturerat, maskinläsbart format vid exempelvis systembyte. En tydlig beskrivning av informationsflöden, lagring och åtkomst underlättar arbetet med integritetskonsekvensbedömningar (DPIA) och löpande tillsyn.

## Tekniska säkerhetskrav i korthet

För att möta kraven ovan behöver verksamhetssystemet stödja modern kryptering både i transit (t.ex. TLS 1.2 eller högre) och i vila (t.ex. AES‑256 eller motsvarande), gärna med lösningar där Malmö stad kan ha egen eller delad kontroll över nycklar. Stöd för stark autentisering och etablerade identitetslösningar kombineras med en rollbaserad behörighetsmodell anpassad till HVOF:s olika yrkesroller. Loggar över åtkomst och viktiga händelser ska gå att analysera och exportera vid behov.

En central fråga till leverantörer är hur lösningen kan utformas så att Malmö stad har tillräcklig **teknisk kontroll** över data och kryptering för att uppfylla OSL, NIS 2 och GDPR, utan att det försvårar användarvänligheten i vardagen.


