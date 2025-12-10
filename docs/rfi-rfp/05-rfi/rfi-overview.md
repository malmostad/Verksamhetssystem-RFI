# RFI-underlag - Översikt

## Syfte

Detta dokument sammanfattar HVOFs systemlandskap, processer och behov för att underlätta leverantörers förståelse inför RFI-processen.

## Innehåll

1. [Verksamhetsbeskrivning](../00-overview/verksamhetsbeskrivning.md)
2. [Systemkarta - Nuläge](../01-nulage/systemkarta.md)
3. [Integrationskarta](../01-nulage/integrationskarta.md)
4. [Informationsmodell](../01-nulage/informationsmodell.md)
5. [Systemdokumentation](../02-system/)
6. [Kravspecifikation](./kravspecifikation.md)
7. [Frågor till leverantörer](./fragor-till-leverantorer.md)

## Snabböversikt

### Systemlandskap
- **Totalt antal system:** 57
- **Centrala System:** 25 system
- **Molntjänster:** 15 system
- **Applikationer:** 3 system
- **Tjänster:** 10 system
- **Övriga System:** 3 system

### Kritiska System
- **3CX** - Telefonväxel (Larmcentral)
- **Interview/ISM** - Larmmottagning
- **Lifecare-Procapita** - Journal/Vård (Master för vårddata)
- **HRutan** - Personal (Master för personaldata)
- **Ekot (Raindance)** - Ekonomi (Master för ekonomidata)
- **Freja eID** - Säker inloggning

### Masterdata
- **Personal:** HRutan (master)
- **Vårddata:** Lifecare-Procapita (master)
- **Ekonomi:** Ekot (Raindance) (master)
- **Larmdata:** Interview/ISM (master)

### Viktiga Integrationer
- **Larmcentral:** 3CX → Interview/ISM → CMP
- **Vård:** Lifecare-Procapita ↔ NPÖ, Pascal
- **Säkerhet:** Freja eID → HRutan, Lifecare-Procapita

## Utmaningar och Förbättringsbehov

### Identifierade Utmaningar
1. **Många system** - 57 system är svårt att hantera
2. **Blandade integrationstyper** - API, Batch, Direkt databas
3. **Brist på centraliserad integrationstjänst**
4. **Flera masters för samma data** - Risk för inkonsekvent data
5. **Brist på dokumentation** - Många integrationer saknar dokumentation

### Förbättringsbehov
1. **Standardisering** - API-first, standardiserade format
2. **Centraliserad integrationstjänst** - Eventuell API-gateway
3. **Datakvalitet** - Tydligt dataägaransvar och validering
4. **Dokumentation** - Alla integrationer dokumenterade
5. **Monitoring** - Övervakning av integrationer

## Målbild och Principer

### Strategiska Principer
1. **Standard före specialutveckling**
2. **API-first** - Öppna integrationer
3. **Datakvalitet** - Masterdata och datägaransvar
4. **Säkerhet** - Säker inloggning och dataskydd
5. **Användarcentrerat** - Enkelt för slutanvändare

### Framtida Mål
- Förenklad systemlandskap
- Standardiserade integrationer
- Tydligt dataägaransvar
- Förbättrad datakvalitet
- Bättre dokumentation

## Kontakt

För frågor om detta underlag, kontakta:
- **Systemarkitektur:** [Kontaktperson]
- **Verksamhet:** [Kontaktperson]
- **IT:** ITD

