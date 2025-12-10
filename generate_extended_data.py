#!/usr/bin/env python3
"""
Extends systems_data.py with additional fields for complete system architecture
Adds: cost, users, technical details, etc.
"""

import json
from systems_data import systems_data

def extend_system_data(system):
    """Extends a system with additional architecture fields"""
    extended = system.copy()
    
    # Add default extended fields if not present
    if "cost" not in extended:
        extended["cost"] = {
            "annual": 0,  # Årlig kostnad i SEK
            "license": 0,  # Licenskostnad
            "support": 0,  # Supportkostnad
            "currency": "SEK"
        }
    
    if "users" not in extended:
        extended["users"] = {
            "total": 0,  # Totalt antal användare
            "groups": [],  # Användargrupper
            "roles": []  # Roller
        }
    
    if "technical" not in extended:
        extended["technical"] = {
            "deployment": "",  # On-premise, Cloud, Hybrid
            "vendor": "",  # Leverantör
            "version": "",  # Version
            "database": "",  # Databas
            "apis": [],  # API:er som systemet exponerar
            "integrations": []  # Integrationer
        }
    
    if "criticality" not in extended:
        # Set default criticality based on category
        if system["category"] == "Central Systems" and any(keyword in system["name"].lower() for keyword in ["lifecare", "interview", "ism", "hrutan", "ekot"]):
            extended["criticality"] = "Critical"
        elif system["category"] == "Central Systems":
            extended["criticality"] = "High"
        else:
            extended["criticality"] = "Medium"
    
    if "status" not in extended:
        extended["status"] = "Active"  # Active, Planned, Retired, Deprecated
    
    if "retirement_date" not in extended:
        extended["retirement_date"] = None
    
    if "notes" not in extended:
        extended["notes"] = ""
    
    return extended

def generate_extended_data():
    """Generates extended systems data"""
    extended_systems = [extend_system_data(system) for system in systems_data]
    
    # Save to JSON for easy editing (single source of truth for extended data)
    with open("systems_data_extended.json", "w", encoding="utf-8") as f:
        json.dump(extended_systems, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Extended data generated for {len(extended_systems)} systems")
    print(f"📁 JSON file: systems_data_extended.json (single source of truth)")
    
    return extended_systems

if __name__ == "__main__":
    generate_extended_data()

