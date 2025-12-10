# Gap-analys - Nuläge vs Målbild

## Översikt

Denna analys identifierar gap mellan nuvarande (AS-IS) och önskad (TO-BE) systemarkitektur.

## Syfte

Identifiera vad som saknas för att nå målbilden och prioritera förbättringar.

## Metod

- Systemanalys
- Intervjuer med verksamhet
- Jämförelse med målbild

## Gap-områden

### 1. Autentisering

**Nuläge (AS-IS)**:
- Många olika autentiseringsmetoder
- Användarnamn + lösenord i många system
- Begränsat SSO-stöd

**Målbild (TO-BE)**:
- Freja eID som primär metod
- SSO för alla system
- Tvåfaktorsautentisering där lämpligt

**Gap**:
- ❌ Många system saknar Freja eID-stöd
- ❌ Ingen central SSO-lösning
- ❌ Begränsat stöd för tvåfaktorsautentisering

**Prioritet**: Hög

### 2. Masterdata-hantering

**Nuläge (AS-IS)**:
- Masterdata definierat men inte konsekvent följt
- Manuell dataöverföring
- Data i flera system

**Målbild (TO-BE)**:
- Tydlig masterdata-princip
- Automatisk dataöverföring
- Ett master per datadomän

**Gap**:
- ❌ Saknar automatisk dataöverföring
- ❌ Data finns i flera system
- ❌ Ingen central masterdata-hantering

**Prioritet**: Hög

### 3. API-täckning

**Nuläge (AS-IS)**:
- Begränsad API-täckning
- Många batch-integrationer
- Saknade API:er för viktiga system

**Målbild (TO-BE)**:
- API-first-princip
- REST API:er för alla system
- Realtidsintegrationer

**Gap**:
- ❌ Många system saknar API:er
- ❌ För många batch-integrationer
- ❌ Begränsat stöd för realtidsintegrationer

**Prioritet**: Medel

### 4. Dokumentation

**Nuläge (AS-IS)**:
- Dokumentation spridd
- Ouppdaterad information
- Begränsad tillgänglighet

**Målbild (TO-BE)**:
- Centraliserad dokumentation
- Uppdaterad information
- Lättillgänglig för alla

**Gap**:
- ✅ Denna dokumentation löser detta
- ⚠️ Behöver uppdateras kontinuerligt

**Prioritet**: Låg (på väg att lösas)

## Prioritering

| Gap | Prioritet | Effekt | Ansträngning | Rekommendation |
|-----|-----------|--------|--------------|----------------|
| Autentisering | Hög | Hög | Medel | Implementera Freja eID för fler system |
| Masterdata | Hög | Hög | Hög | Etablera automatisk dataöverföring |
| API-täckning | Medel | Medel | Hög | Prioritera API:er för nya system |
| Dokumentation | Låg | Medel | Låg | Fortsätt med denna plattform |

## Nästa steg

1. **Kort sikt (0-6 månader)**
   - Utöka Freja eID till fler system
   - Förbättra dokumentationen

2. **Medellång sikt (6-18 månader)**
   - Implementera automatisk masterdata-överföring
   - Utveckla API:er för kritiska system

3. **Lång sikt (18+ månader)**
   - Full API-täckning
   - Centraliserad masterdata-hantering

## Relaterade dokument

- [Arkitekturprinciper](../overview/architecture-principles.md)
- [Systemlandskap](../systems/system-landscape.md)
- [Pain Points](pain-points.md)

## Kontakt

För frågor om denna analys, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

