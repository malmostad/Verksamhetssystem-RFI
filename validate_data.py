#!/usr/bin/env python3
"""
Validates systems data for completeness and correctness
"""

import json
from pathlib import Path

def validate_system(system, system_ids):
    """Validates a single system"""
    errors = []
    warnings = []
    
    # Required fields
    required_fields = ["id", "name", "type", "category", "description"]
    for field in required_fields:
        if field not in system or not system[field]:
            errors.append(f"{system.get('name', 'Unknown')}: Missing required field '{field}'")
    
    # Validate ID is unique
    if system["id"] in system_ids:
        errors.append(f"{system.get('name', 'Unknown')}: Duplicate ID {system['id']}")
    system_ids.add(system["id"])
    
    # Validate cost
    if "cost" in system:
        cost = system["cost"]
        if not isinstance(cost.get("annual", 0), (int, float)):
            errors.append(f"{system.get('name')}: Invalid annual cost")
        if not isinstance(cost.get("license", 0), (int, float)):
            errors.append(f"{system.get('name')}: Invalid license cost")
    
    # Validate users
    if "users" in system:
        users = system["users"]
        if not isinstance(users.get("total", 0), (int, float)):
            errors.append(f"{system.get('name')}: Invalid user count")
    
    # Validate criticality
    valid_criticalities = ["Critical", "High", "Medium", "Low"]
    if "criticality" in system and system["criticality"] not in valid_criticalities:
        warnings.append(f"{system.get('name')}: Invalid criticality '{system['criticality']}'")
    
    # Validate status
    valid_statuses = ["Active", "Planned", "Retired", "Deprecated"]
    if "status" in system and system["status"] not in valid_statuses:
        warnings.append(f"{system.get('name')}: Invalid status '{system['status']}'")
    
    # Check for missing cost data
    if "cost" in system and system["cost"].get("annual", 0) == 0:
        warnings.append(f"{system.get('name')}: Missing cost data")
    
    # Check for missing user data
    if "users" in system and system["users"].get("total", 0) == 0:
        warnings.append(f"{system.get('name')}: Missing user data")
    
    return errors, warnings

def validate_data():
    """Validates all systems data"""
    # Load from single source of truth: systems_data_extended.json (generated from systems_data.py)
    try:
        data_file = Path("systems_data_extended.json")
        if data_file.exists():
            with open(data_file, "r", encoding="utf-8") as f:
                systems = json.load(f)
        else:
            # Fallback to systems_data.py if JSON doesn't exist
            from systems_data import systems_data
            systems = systems_data
    except Exception as e:
        print(f"❌ Error loading data: {e}")
        return False
    
    all_errors = []
    all_warnings = []
    system_ids = set()
    
    for system in systems:
        errors, warnings = validate_system(system, system_ids)
        all_errors.extend(errors)
        all_warnings.extend(warnings)
    
    # Report results
    print(f"Validating {len(systems)} systems...")
    print()
    
    if all_errors:
        print(f"❌ Found {len(all_errors)} errors:")
        for error in all_errors:
            print(f"  - {error}")
        print()
    
    if all_warnings:
        print(f"⚠️  Found {len(all_warnings)} warnings:")
        for warning in all_warnings[:10]:  # Show first 10
            print(f"  - {warning}")
        if len(all_warnings) > 10:
            print(f"  ... and {len(all_warnings) - 10} more warnings")
        print()
    
    if not all_errors and not all_warnings:
        print("✅ All data is valid!")
        return True
    elif not all_errors:
        print("✅ No errors found, but some warnings (data may be incomplete)")
        return True
    else:
        print("❌ Validation failed. Please fix errors before proceeding.")
        return False

if __name__ == "__main__":
    success = validate_data()
    exit(0 if success else 1)

