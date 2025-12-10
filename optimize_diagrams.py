#!/usr/bin/env python3
"""
Optimizes all Mermaid diagrams in docs/diagrams/ to be larger and more readable
"""

import re
from pathlib import Path

def optimize_mermaid_diagram(content):
    """Adds optimization config to Mermaid diagrams"""
    # Pattern to find mermaid code blocks
    pattern = r'```mermaid\n'
    
    # Replacement with optimized config
    replacement = r'```mermaid\n%%{init: {\'theme\':\'default\', \'themeVariables\': { \'fontSize\': \'18px\', \'primaryColor\': \'#2196F3\', \'primaryTextColor\': \'#fff\', \'primaryBorderColor\': \'#1976D2\', \'lineColor\': \'#1976D2\', \'fontFamily\': \'Arial, sans-serif\', \'nodeBkgColor\': \'#E3F2FD\', \'mainBkgColor\': \'#FAFAFA\', \'textColor\': \'#212121\'}}}%%\n'
    
    # Only replace if not already optimized
    if '%%{init:' not in content:
        content = re.sub(pattern, replacement, content)
    
    return content

def optimize_all_diagrams():
    """Optimizes all diagram files"""
    diagrams_dir = Path("docs/diagrams")
    
    if not diagrams_dir.exists():
        print("❌ Diagrams directory not found")
        return
    
    optimized_count = 0
    for md_file in diagrams_dir.glob("*.md"):
        if md_file.name == "README.md":
            continue
        
        try:
            content = md_file.read_text(encoding="utf-8")
            optimized = optimize_mermaid_diagram(content)
            
            if content != optimized:
                md_file.write_text(optimized, encoding="utf-8")
                optimized_count += 1
                print(f"✅ Optimized: {md_file.name}")
        except Exception as e:
            print(f"⚠️  Error processing {md_file.name}: {e}")
    
    print(f"\n✅ Optimized {optimized_count} diagram files")

if __name__ == "__main__":
    optimize_all_diagrams()

