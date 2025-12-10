#!/usr/bin/env python3
"""
Generates complete website structure for HVOF System Architecture
Creates MkDocs-compatible documentation with interactive features
"""

import json
import os
from pathlib import Path
from systems_data import systems_data

def create_system_page(system, output_dir):
    """Creates a detailed page for each system"""
    category_dir = {
        "Central Systems": "centrala-system",
        "Cloud Services": "molntjanster",
        "Applications": "applikationer",
        "Services": "tjanster",
        "Other": "ovriga-system"
    }
    
    category_folder = category_dir.get(system["category"], "ovriga-system")
    system_dir = Path(output_dir) / "02-system" / category_folder
    system_dir.mkdir(parents=True, exist_ok=True)
    
    # Normalize filename - remove special chars and handle duplicates
    filename = system["name"].lower()
    filename = filename.replace(" ", "-")
    filename = filename.replace("/", "-")
    filename = filename.replace("(", "")
    filename = filename.replace(")", "")
    filename = filename.replace("---", "-")
    filename = filename.replace("--", "-")
    
    filepath = system_dir / f"{filename}.md"
    
    # Load extended data from JSON (single source of truth)
    try:
        with open("systems_data_extended.json", "r", encoding="utf-8") as f:
            extended_data = json.load(f)
        extended_system = next((s for s in extended_data if s["id"] == system["id"]), system)
    except FileNotFoundError:
        # Fallback to basic system data if extended doesn't exist
        extended_system = system
    
    cost = extended_system.get("cost", {})
    users = extended_system.get("users", {})
    technical = extended_system.get("technical", {})
    
    content = f"""# {system['name']}

## Översikt

**Typ:** {system['type']}  
**Kategori:** {system['category']}  
**Ägare:** {system['owner']}  
**Organisation:** {system['org'] if system['org'] else 'Ej angivet'}  
**Avdelning:** {system['department'] if system['department'] else 'Ej angivet'}  
**Status:** {extended_system.get('status', 'Active')}  
**Kritikalitet:** {extended_system.get('criticality', 'Medium')}

## Beskrivning

{system['description'] if system['description'] else 'Beskrivning saknas'}

## Kontaktpersoner

"""
    if system['contacts']:
        for contact in system['contacts']:
            content += f"- {contact}\n"
    else:
        content += "- Ej angivet\n"
    
    content += f"""
## Autentisering

{system['auth'] if system['auth'] else 'Ej angivet'}

## Kostnad

| Typ | Belopp | Valuta |
|-----|--------|--------|
| **Årlig kostnad** | {cost.get('annual', 0):,} SEK | {cost.get('currency', 'SEK')} |
| **Licenskostnad** | {cost.get('license', 0):,} SEK | {cost.get('currency', 'SEK')} |
| **Supportkostnad** | {cost.get('support', 0):,} SEK | {cost.get('currency', 'SEK')} |
| **Totalt** | {cost.get('annual', 0) + cost.get('license', 0) + cost.get('support', 0):,} SEK | {cost.get('currency', 'SEK')} |

*Kompletteras med faktiska kostnader*

## Användare

- **Totalt antal användare:** {users.get('total', 0):,}
- **Användargrupper:** {', '.join(users.get('groups', [])) if users.get('groups') else 'Ej angivet'}
- **Roller:** {', '.join(users.get('roles', [])) if users.get('roles') else 'Ej angivet'}

*Kompletteras med faktiska användarantal*

## Teknisk Information

| Fält | Värde |
|------|-------|
| **Deployment** | {technical.get('deployment', 'Ej angivet')} |
| **Leverantör** | {technical.get('vendor', 'Ej angivet')} |
| **Version** | {technical.get('version', 'Ej angivet')} |
| **Databas** | {technical.get('database', 'Ej angivet')} |

### API:er

"""
    if technical.get('apis'):
        for api in technical['apis']:
            content += f"- {api}\n"
    else:
        content += "- Ej angivet\n"
    
    content += f"""
### Integrationer

"""
    if technical.get('integrations'):
        for integration in technical['integrations']:
            content += f"- {integration}\n"
    else:
        content += "- Ej angivet\n"
    
    content += f"""
## Integrationer

*Kompletteras med faktiska integrationer*

## Användningsområden

*Kompletteras med faktiska användningsområden*

## Volymer

*Kompletteras med faktiska volymer*

## Kritikalitet

**Nivå:** {extended_system.get('criticality', 'Medium')}

*Kompletteras med faktisk kritikalitet och nedtidspåverkan*

## Utmaningar och Förbättringsbehov

*Kompletteras med faktiska utmaningar*

## Framtida Planer

"""
    if extended_system.get('retirement_date'):
        content += f"**Planerad utfasning:** {extended_system['retirement_date']}\n\n"
    
    content += "*Kompletteras med framtida planer*\n"
    
    if extended_system.get('notes'):
        content += f"\n## Anteckningar\n\n{extended_system['notes']}\n"
    
    filepath.write_text(content, encoding='utf-8')
    return filepath

def generate_system_index(output_dir):
    """Generates index pages for each category"""
    categories = {
        "Central Systems": ("Centrala System", "centrala-system"),
        "Cloud Services": ("Molntjänster", "molntjanster"),
        "Applications": ("Applikationer", "applikationer"),
        "Services": ("Tjänster", "tjanster"),
        "Other": ("Övriga System", "ovriga-system")
    }
    
    for category, (name, folder) in categories.items():
        systems_in_category = [s for s in systems_data if s['category'] == category]
        category_dir = Path(output_dir) / "02-system" / folder
        category_dir.mkdir(parents=True, exist_ok=True)
        
        readme = f"""# {name}

Detta är dokumentationen för system i kategorin {name}.

## System i denna kategori

Totalt: **{len(systems_in_category)} system**

"""
        # Group by criticality
        critical = [s for s in systems_in_category if any(kw in s['name'].lower() for kw in ['lifecare', 'interview', 'ism', 'hrutan', 'ekot', '3cx', 'cmp'])]
        high = [s for s in systems_in_category if s not in critical and 'freja' in s['name'].lower() or 'npo' in s['name'].lower() or 'pascal' in s['name'].lower()]
        others = [s for s in systems_in_category if s not in critical and s not in high]
        
        if critical:
            readme += "### Kritiska System\n\n"
            for system in critical:
                filename = system['name'].lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")
                readme += f"- [{system['name']}](./{filename}.md) - {system['description'][:60]}...\n"
            readme += "\n"
        
        if high:
            readme += "### Hög Prioritet\n\n"
            for system in high:
                filename = system['name'].lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")
                readme += f"- [{system['name']}](./{filename}.md) - {system['description'][:60]}...\n"
            readme += "\n"
        
        if others:
            readme += "### Övriga System\n\n"
            for system in others:
                filename = system['name'].lower().replace(" ", "-").replace("/", "-").replace("(", "").replace(")", "")
                readme += f"- [{system['name']}](./{filename}.md) - {system['description'][:60]}...\n"
        
        (category_dir / "README.md").write_text(readme, encoding='utf-8')

def generate_statistics_page(output_dir):
    """Generates statistics and overview page"""
    stats_dir = Path(output_dir) / "statistics"
    stats_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        from systems_data_extended import systems_data as extended_data
    except:
        extended_data = systems_data
    
    # Calculate statistics
    total_cost = sum(s.get("cost", {}).get("annual", 0) for s in extended_data)
    total_users = sum(s.get("users", {}).get("total", 0) for s in extended_data)
    
    categories = {}
    criticality = {}
    deployment = {}
    
    for system in extended_data:
        cat = system['category']
        categories[cat] = categories.get(cat, 0) + 1
        
        crit = system.get('criticality', 'Medium')
        criticality[crit] = criticality.get(crit, 0) + 1
        
        dep = system.get('technical', {}).get('deployment', 'Unknown')
        deployment[dep] = deployment.get(dep, 0) + 1
    
    content = f"""# Statistik och Översikt

## Systemöversikt

- **Totalt antal system:** {len(extended_data)}
- **Totalt antal användare:** {total_users:,}
- **Total årlig kostnad:** {total_cost:,} SEK

## Fördelning per Kategori

```mermaid
pie title System per Kategori
"""
    for cat, count in sorted(categories.items()):
        content += f'    "{cat}" : {count}\n'
    content += "```\n\n"
    
    content += "## Fördelning per Kritikalitet\n\n"
    content += "```mermaid\npie title System per Kritikalitet\n"
    for crit, count in sorted(criticality.items()):
        content += f'    "{crit}" : {count}\n'
    content += "```\n\n"
    
    content += "## Deployment-typer\n\n"
    content += "```mermaid\npie title Deployment-typer\n"
    for dep, count in sorted(deployment.items()):
        content += f'    "{dep}" : {count}\n'
    content += "```\n\n"
    
    content += "## Tabeller\n\n"
    content += "### System per Kategori\n\n"
    content += "| Kategori | Antal System |\n"
    content += "|----------|---------------|\n"
    for cat, count in sorted(categories.items()):
        content += f"| {cat} | {count} |\n"
    
    (stats_dir / "overview.md").write_text(content, encoding='utf-8')

def main():
    """Main function to generate website"""
    output_dir = Path("docs")
    output_dir.mkdir(exist_ok=True)
    
    print("Generating website structure...")
    
    # Generate system pages
    print("Creating system pages...")
    for system in systems_data:
        create_system_page(system, output_dir)
    
    # Generate category indexes
    print("Creating category indexes...")
    generate_system_index(output_dir)
    
    # Generate statistics
    print("Generating statistics...")
    generate_statistics_page(output_dir)
    
    print(f"✅ Website structure generated!")
    print(f"📁 Documentation in: docs/")
    print(f"\n🚀 To build website:")
    print(f"   1. Install MkDocs: pip install mkdocs mkdocs-material mkdocs-mermaid2-plugin")
    print(f"   2. Build: mkdocs build")
    print(f"   3. Serve locally: mkdocs serve")
    print(f"   4. Deploy: mkdocs gh-deploy")

if __name__ == "__main__":
    main()

