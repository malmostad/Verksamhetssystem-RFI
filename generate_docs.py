#!/usr/bin/env python3
"""
Automatiserad dokumentationsgenerering för HVOF Systemarkitektur
Genererar systemdokumentation, diagram och RFI-underlag
"""

import json
import os
import sys
from pathlib import Path

# Import systems_data
from systems_data import systems_data

def create_system_doc(system):
    """Skapar individuell systemdokumentation"""
    doc = f"""# {system['name']}

## Översikt
**Typ:** {system['type']}  
**Kategori:** {system['category']}  
**Ägare:** {system['owner']}  
**Organisation:** {system['org'] if system['org'] else 'Ej angivet'}  
**Avdelning:** {system['department'] if system['department'] else 'Ej angivet'}

## Beskrivning
{system['description'] if system['description'] else 'Beskrivning saknas'}

## Kontaktpersoner
"""
    if system['contacts']:
        for contact in system['contacts']:
            doc += f"- {contact}\n"
    else:
        doc += "- Ej angivet\n"
    
    doc += f"""
## Autentisering
{system['auth'] if system['auth'] else 'Ej angivet'}

## Integrationer
*Kompletteras med faktiska integrationer*

## Användningsområden
*Kompletteras med faktiska användningsområden*

## Volymer
*Kompletteras med faktiska volymer*

## Kritikalitet
*Kompletteras med faktisk kritikalitet*

## Utmaningar och Förbättringsbehov
*Kompletteras med faktiska utmaningar*

## Framtida Planer
*Kompletteras med framtida planer*
"""
    return doc

def generate_system_docs():
    """Genererar dokumentation för alla system"""
    base_path = Path("docs/02-system")
    
    # Skapa kategorimappar
    categories = {
        "Central Systems": "centrala-system",
        "Cloud Services": "molntjanster",
        "Applications": "applikationer",
        "Services": "tjanster",
        "Other": "ovriga-system"
    }
    
    for category, folder in categories.items():
        category_path = base_path / folder
        category_path.mkdir(parents=True, exist_ok=True)
        
        # Skapa README för kategorin
        readme = f"""# {category}

Detta är dokumentationen för system i kategorin {category}.

## System i denna kategori
"""
        systems_in_category = [s for s in systems_data if s['category'] == category]
        for system in systems_in_category:
            filename = system['name'].lower().replace(' ', '-').replace('/', '-')
            readme += f"- [{system['name']}](./{filename}.md)\n"
        
        (category_path / "README.md").write_text(readme, encoding='utf-8')
        
        # Skapa dokumentation för varje system
        for system in systems_in_category:
            filename = system['name'].lower().replace(' ', '-').replace('/', '-')
            doc = create_system_doc(system)
            (category_path / f"{filename}.md").write_text(doc, encoding='utf-8')

def generate_system_overview_mermaid():
    """Genererar Mermaid-diagram för systemöversikt"""
    diagram = """```mermaid
graph TB
    subgraph "Centrala System"
"""
    central_systems = [s for s in systems_data if s['category'] == 'Central Systems'][:10]
    for sys in central_systems:
        diagram += f"        {sys['id']}[{sys['name']}]\n"
    diagram += """    end
    
    subgraph "Molntjänster"
"""
    cloud_systems = [s for s in systems_data if s['category'] == 'Cloud Services'][:10]
    for sys in cloud_systems:
        diagram += f"        {sys['id']}[{sys['name']}]\n"
    diagram += """    end
    
    subgraph "Tjänster"
"""
    services = [s for s in systems_data if s['category'] == 'Services'][:10]
    for sys in services:
        diagram += f"        {sys['id']}[{sys['name']}]\n"
    diagram += """    end
```"""
    return diagram

def generate_integration_diagram():
    """Genererar integrationsdiagram"""
    # Identifiera kända integrationer baserat på systembeskrivningar
    integrations = []
    
    # Larmcentral integrationer
    ism = next((s for s in systems_data if 'Interview' in s['name']), None)
    c3x = next((s for s in systems_data if s['name'] == '3CX'), None)
    cmp = next((s for s in systems_data if s['name'] == 'CMP'), None)
    
    if ism and c3x:
        integrations.append((c3x['id'], ism['id'], 'Samtal'))
    if ism and cmp:
        integrations.append((ism['id'], cmp['id'], 'Larmdata'))
    
    # Vårdintegrationer
    lifecare = next((s for s in systems_data if 'Lifecare' in s['name']), None)
    npo = next((s for s in systems_data if s['name'] == 'NPÖ'), None)
    pascal = next((s for s in systems_data if s['name'] == 'Pascal'), None)
    kuben = next((s for s in systems_data if s['name'] == 'Kuben'), None)
    
    if lifecare and npo:
        integrations.append((lifecare['id'], npo['id'], 'Patientdata'))
    if lifecare and pascal:
        integrations.append((lifecare['id'], pascal['id'], 'Läkemedel'))
    if kuben and lifecare:
        integrations.append((kuben['id'], lifecare['id'], 'Tidsplanering'))
    
    diagram = """```mermaid
graph LR
"""
    for source_id, target_id, label in integrations:
        source = next((s for s in systems_data if s['id'] == source_id), None)
        target = next((s for s in systems_data if s['id'] == target_id), None)
        if source and target:
            diagram += f"    {source['name'].replace(' ', '').replace('-', '')} -->|{label}| {target['name'].replace(' ', '').replace('-', '')}\n"
    
    diagram += "```"
    return diagram

def generate_rfi_summary():
    """Genererar RFI-sammanfattning"""
    summary = f"""# RFI-underlag - Sammanfattning

## Systemöversikt
Totalt antal system: **{len(systems_data)}**

### Fördelning per kategori
"""
    categories = {}
    for system in systems_data:
        cat = system['category']
        categories[cat] = categories.get(cat, 0) + 1
    
    for cat, count in sorted(categories.items()):
        summary += f"- **{cat}**: {count} system\n"
    
    summary += """
## Kritiska System
*Kompletteras med faktisk kritikalitet*

## Masterdata
*Kompletteras med faktiska masters*

## Integrationer
*Kompletteras med faktiska integrationer*

## Utmaningar
*Kompletteras med faktiska utmaningar*

## Målbild
*Kompletteras med målbild*
"""
    return summary

def main():
    """Huvudfunktion för dokumentationsgenerering"""
    print("Genererar systemdokumentation...")
    generate_system_docs()
    
    print("Genererar diagram...")
    diagrams_path = Path("docs/diagrams")
    diagrams_path.mkdir(parents=True, exist_ok=True)
    
    # Systemöversikt
    overview = generate_system_overview_mermaid()
    (diagrams_path / "system-overview.md").write_text(overview, encoding='utf-8')
    
    # Integrationer
    integration = generate_integration_diagram()
    (diagrams_path / "integration-overview.md").write_text(integration, encoding='utf-8')
    
    # RFI-sammanfattning
    rfi_path = Path("docs/05-rfi")
    rfi_path.mkdir(parents=True, exist_ok=True)
    rfi_summary = generate_rfi_summary()
    (rfi_path / "rfi-summary.md").write_text(rfi_summary, encoding='utf-8')
    
    print(f"✅ Dokumentation genererad för {len(systems_data)} system")
    print(f"📁 Dokumentation finns i: docs/")
    print(f"📊 Diagram finns i: docs/diagrams/")
    print(f"📋 RFI-underlag finns i: docs/05-rfi/")

if __name__ == "__main__":
    main()

