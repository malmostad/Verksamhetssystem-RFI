# Pain Points - Nuvarande problem

## Översikt

Identifierade problem och utmaningar i nuvarande systemlandskap.

## Syfte

Förstå vad som fungerar dåligt idag för att kunna prioritera förbättringar och ställa rätt krav vid systembyte.

## Metod

- Intervjuer med användare
- Systemanalys
- Supportstatistik

## Pain Points

### 1. Många olika inloggningar

**Problem**: Användare måste logga in i många olika system med olika metoder.

**Påverkan**:
- Tidskrävande
- Användare glömmer lösenord
- Säkerhetsrisk (svaga lösenord)

**System påverkade**: Alla system

**Prioritet**: Hög

### 2. Manuell dataöverföring

**Problem**: Data måste kopieras manuellt mellan system.

**Påverkan**:
- Felrisker
- Tidskrävande
- Inkonsekvent data

**System påverkade**: HRutan → Medvind, Ekot → Koll-Qlikview

**Prioritet**: Hög

### 3. Saknad integration

**Problem**: System är inte integrerade trots att de borde vara det.

**Påverkan**:
- Dubbelarbete
- Felrisker
- Begränsad funktionalitet

**Exempel**: Visma och HRutan, Kuben och Lifecare-Procapita

**Prioritet**: Medel

### 4. Begränsad API-täckning

**Problem**: Många system saknar API:er eller har begränsade API:er.

**Påverkan**:
- Svårt att integrera
- Begränsade möjligheter
- Kostsamma speciallösningar

**System påverkade**: Många system

**Prioritet**: Medel

### 5. Ouppdaterad dokumentation

**Problem**: Dokumentation är spridd och ouppdaterad.

**Påverkan**:
- Svårt att hitta information
- Felaktig information
- Tidskrävande att hitta rätt person

**Prioritet**: Låg (löses med denna plattform)

### 6. Komplex systemlandskap

**Problem**: Många system gör det svårt att förstå helheten.

**Påverkan**:
- Svårt att förstå flöden
- Svårt att planera systembyte
- Risk för missade integrationer

**Prioritet**: Medel

## Prioritering

| Pain Point | Prioritet | Påverkan | Lösbarhet |
|------------|-----------|----------|-----------|
| Många inloggningar | Hög | Hög | Medel |
| Manuell dataöverföring | Hög | Hög | Medel |
| Saknad integration | Medel | Medel | Medel |
| Begränsad API-täckning | Medel | Medel | Hög |
| Ouppdaterad dokumentation | Låg | Medel | Låg |
| Komplex systemlandskap | Medel | Medel | Låg |

## Rekommendationer

### Kort sikt

1. **Standardisera autentisering**
   - Utöka Freja eID till fler system
   - Implementera SSO där möjligt

2. **Förbättra dokumentationen**
   - Använd denna plattform
   - Uppdatera kontinuerligt

### Medellång sikt

1. **Automatisera dataöverföring**
   - Implementera API:er
   - Etablera automatiska integrationer

2. **Förbättra integrationer**
   - Prioritera kritiska integrationer
   - Standardisera integrationstyper

### Lång sikt

1. **Förenkla systemlandskapet**
   - Konsolidera system där möjligt
   - Ersätt äldre system

## Relaterade dokument

- [Gap-analys](gap-analysis.md)
- [Systemlandskap](../systems/system-landscape.md)
- [Arkitekturprinciper](../overview/architecture-principles.md)

## Kontakt

För frågor om pain points, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

