# Setup - HVOF Systemarkitektur Webbplats

## Snabbstart

### 1. Installera Dependencies

```bash
pip install -r requirements.txt
```

### 2. Generera Dokumentation

```bash
python3 generate_extended_data.py
python3 generate_website.py
python3 generate_docs.py
```

### 3. Starta Lokal Server

```bash
mkdocs serve
```

Öppna webbläsaren på: http://127.0.0.1:8000

### 4. Bygg för Produktion

```bash
mkdocs build
```

Detta skapar en `site/` mapp med den färdiga webbplatsen.

## Deployment

### GitHub Pages (Rekommenderat)

```bash
mkdocs gh-deploy
```

Detta publicerar automatiskt till GitHub Pages.

### Intern Server

1. Bygg webbplatsen: `mkdocs build`
2. Kopiera `site/` mappen till webbservern
3. Konfigurera webbservern att serva `site/` mappen

### Docker (Alternativ)

```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
RUN mkdocs build
CMD ["mkdocs", "serve", "--dev-addr=0.0.0.0:8000"]
```

## Uppdatera Dokumentation

### Lägg till/Redigera System

1. Redigera `systems_data.py` eller `systems_data_extended.json`
2. Kör `python3 generate_website.py`
3. Commit och push

### Redigera Manuellt

1. Redigera Markdown-filer i `docs/`
2. Commit och push
3. Webbplatsen uppdateras automatiskt (om CI/CD är konfigurerat)

## Funktioner

### Sök
- Tryck `S` eller klicka på sökikonen
- Sök på systemnamn, beskrivningar, kontakter, etc.

### Filtrering
- Filtrera på kategori
- Filtrera på kritikalitet
- Filtrera på kostnad
- Filtrera på användare

### Interaktiva Diagram
- Klicka på diagram för att interagera
- Zoom och pan
- Exportera som PNG/SVG

### Responsiv Design
- Fungerar på desktop, tablet och mobil
- Touch-vänlig navigation

## Best Practices

### För Redaktörer

1. **Använd Markdown** - Enkelt att lära sig
2. **Följ mallar** - Se befintliga systemdokumentation
3. **Validera data** - Kör `python3 generate_extended_data.py` för att validera
4. **Commit ofta** - Små, logiska commits

### För Administratörer

1. **Backup regelbundet** - Git är backup, men extra backup rekommenderas
2. **Övervaka kostnader** - Uppdatera kostnader regelbundet
3. **Granska ändringar** - Använd Git history för att se ändringar
4. **Kommunikera ändringar** - Informera användare om större ändringar

## Support

För frågor eller problem:
- Se dokumentationen i `docs/`
- Kontakta ITD
- Öppna issue på GitHub

