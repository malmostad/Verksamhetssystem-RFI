# Kravlista - RFI/RFP

## Översikt

Detaljerade krav för nytt verksamhetssystem.

## Syfte

Specificera vad ett nytt system måste kunna göra för att möta HVOF:s behov.

## Kravkategorier

### 1. Funktionella krav

#### 1.1 Larmhantering

- [ ] **KRAV-001**: Systemet ska kunna ta emot larm från flera källor (telefon, trygghetslarm, kameralarm)
- [ ] **KRAV-002**: Systemet ska kunna prioritera larm baserat på typ och allvarlighetsgrad
- [ ] **KRAV-003**: Systemet ska kunna skicka larm vidare till rätt resurs (väktare, personal)
- [ ] **KRAV-004**: Systemet ska logga alla larm och åtgärder

#### 1.2 Vårdhantering

- [ ] **KRAV-005**: Systemet ska kunna hantera vårdplaner och vårddokumentation
- [ ] **KRAV-006**: Systemet ska kunna integrera med NPÖ för patientöversikt
- [ ] **KRAV-007**: Systemet ska kunna hantera läkemedelsbeställningar (Pascal)
- [ ] **KRAV-008**: Systemet ska stödja signering (MCSS)

#### 1.3 Personalhantering

- [ ] **KRAV-009**: Systemet ska kunna hantera personaldata
- [ ] **KRAV-010**: Systemet ska kunna integrera med HRutan för personaldata
- [ ] **KRAV-011**: Systemet ska kunna hantera tidsplanering

### 2. Icke-funktionella krav

#### 2.1 Säkerhet

- [ ] **KRAV-012**: Systemet ska stödja Freja eID för SSO
- [ ] **KRAV-013**: Systemet ska stödja SITHS för vårddata
- [ ] **KRAV-014**: Systemet ska följa GDPR
- [ ] **KRAV-015**: Systemet ska logga alla åtgärder

#### 2.2 Prestanda

- [ ] **KRAV-016**: Systemet ska hantera minst 1000 användare samtidigt
- [ ] **KRAV-017**: Systemet ska ha svarstid < 2 sekunder
- [ ] **KRAV-018**: Systemet ska ha 99.9% tillgänglighet

#### 2.3 Integrationer

- [ ] **KRAV-019**: Systemet ska exponera REST API:er
- [ ] **KRAV-020**: Systemet ska kunna ta emot data via API
- [ ] **KRAV-021**: Systemet ska stödja HL7 för vårddata
- [ ] **KRAV-022**: Systemet ska kunna integrera med befintliga system

### 3. Masterdata

- [ ] **KRAV-023**: Systemet ska kunna vara master för sin datadomän
- [ ] **KRAV-024**: Systemet ska kunna ta emot masterdata från andra system
- [ ] **KRAV-025**: Systemet ska validera data vid mottagande

### 4. Rapporter och analyser

- [ ] **KRAV-026**: Systemet ska kunna generera rapporter
- [ ] **KRAV-027**: Systemet ska exponera data för BI-system
- [ ] **KRAV-028**: Systemet ska stödja export av data

## Prioritering

### Måste ha (Must Have)

- KRAV-001 till KRAV-011 (Funktionella krav)
- KRAV-012 till KRAV-015 (Säkerhet)
- KRAV-019 till KRAV-022 (Integrationer)

### Bör ha (Should Have)

- KRAV-016 till KRAV-018 (Prestanda)
- KRAV-023 till KRAV-025 (Masterdata)

### Skulle vilja ha (Nice to Have)

- KRAV-026 till KRAV-028 (Rapporter)

## Utvärderingskriterier

Se [Utvärderingskriterier](evaluation-criteria.md) för hur krav ska utvärderas.

## Relaterade dokument

- [RFI-material](rfi-material.md)
- [Frågor till leverantörer](supplier-questions.md)
- [Systemlandskap](../systems/system-landscape.md)

## Kontakt

För frågor om krav, kontakta IT-avdelningen.

## Uppdaterad

Senast uppdaterad: 2024-01-XX
Uppdaterad av: [Namn]

