# Utvärderingskriterier - RFI/RFP

## Översikt

Kriterier för att utvärdera leverantörer och system i RFI/RFP-processen.

## Syfte

Tydliga kriterier för att objektivt utvärdera svar och system.

## Utvärderingsprocess

1. **Insamling**: Samla in svar från leverantörer
2. **Utvärdering**: Utvärdera enligt kriterierna
3. **Poängsättning**: Ge poäng för varje kriterium
4. **Rangordning**: Rangordna leverantörer baserat på total poäng
5. **Beslut**: Välj leverantör för nästa steg

## Utvärderingskriterier

### 1. Funktionella krav (40%)

**Vikt**: 40%

**Beskrivning**: Hur väl systemet möter funktionella krav.

**Underskriterier**:
- Larmhantering (10%)
- Vårdhantering (15%)
- Personalhantering (10%)
- Rapporter och analyser (5%)

**Poängskala**: 0-5
- 5: Utmärkt - Överträffar alla krav
- 4: Mycket bra - Möter alla krav
- 3: Bra - Möter de flesta krav
- 2: Acceptabelt - Möter grundläggande krav
- 1: Otillräckligt - Möter få krav
- 0: Inte möjligt - Möter inga krav

### 2. Icke-funktionella krav (25%)

**Vikt**: 25%

**Beskrivning**: Säkerhet, prestanda, tillgänglighet.

**Underskriterier**:
- Säkerhet (10%)
- Prestanda (10%)
- Tillgänglighet (5%)

**Poängskala**: 0-5 (samma som ovan)

### 3. Integrationer (15%)

**Vikt**: 15%

**Beskrivning**: Hur väl systemet kan integreras med befintliga system.

**Underskriterier**:
- API:er (8%)
- Befintliga integrationer (4%)
- Integrationstöd (3%)

**Poängskala**: 0-5

### 4. Masterdata (10%)

**Vikt**: 10%

**Beskrivning**: Hur systemet hanterar masterdata.

**Underskriterier**:
- Masterdata-stöd (5%)
- Datakvalitet (3%)
- Validering (2%)

**Poängskala**: 0-5

### 5. Support och utveckling (10%)

**Vikt**: 10%

**Beskrivning**: Supportnivå och kontinuerlig utveckling.

**Underskriterier**:
- Support (5%)
- Utveckling (3%)
- Dokumentation (2%)

**Poängskala**: 0-5

## Poängberäkning

### Total poäng

```
Total poäng = (Funktionella krav × 0.40) + 
              (Icke-funktionella krav × 0.25) + 
              (Integrationer × 0.15) + 
              (Masterdata × 0.10) + 
              (Support × 0.10)
```

### Exempel

| Leverantör | Funktionella | Icke-funktionella | Integrationer | Masterdata | Support | Total |
|------------|--------------|-------------------|---------------|------------|---------|-------|
| Leverantör A | 4.5 | 4.0 | 4.5 | 4.0 | 4.5 | 4.3 |
| Leverantör B | 4.0 | 4.5 | 3.5 | 4.5 | 4.0 | 4.1 |
| Leverantör C | 3.5 | 4.0 | 4.0 | 3.5 | 3.5 | 3.7 |

## Beslutsmatris

### Måste ha (Must Have)

System som inte uppfyller dessa krav elimineras direkt:

- ✅ Stödjer Freja eID eller SITHS
- ✅ Följer GDPR
- ✅ Har API:er
- ✅ Stödjer grundläggande funktioner (larm, vård)

### Bör ha (Should Have)

Viktiga krav som påverkar poäng:

- Stödjer alla autentiseringsmetoder
- Utmärkt prestanda
- Bra integrationer
- Masterdata-stöd

### Skulle vilja ha (Nice to Have)

Önskvärda funktioner som ger bonuspoäng:

- Avancerade rapporter
- BI-integrationer
- Moderna användargränssnitt

## Nästa steg

Efter utvärdering:

1. **Top 3**: Välj de 3 bästa leverantörerna
2. **Demo**: Be om demo av systemen
3. **Referenser**: Kontakta referenskunder
4. **RFP**: Skicka RFP till top 3

## Relaterade dokument

- [RFI-material](rfi-material.md)
- [Kravlista](requirements-list.md)
- [Frågor till leverantörer](supplier-questions.md)

## Kontakt

För frågor om utvärdering, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

