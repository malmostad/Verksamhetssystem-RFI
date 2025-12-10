#!/usr/bin/env python3
"""
Removes duplicate Mermaid init blocks from diagram files
"""

import re
from pathlib import Path

def remove_duplicate_inits(content):
    """Removes duplicate Mermaid init blocks"""
    # Find all mermaid code blocks
    pattern = r'```mermaid\n(.*?)```'
    
    def process_block(match):
        block_content = match.group(1)
        
        # Count how many init blocks there are
        init_count = block_content.count('%%{init:')
        
        if init_count > 1:
            # Find the first complete init block
            init_pattern = r'%%\{init:.*?\}%%'
            inits = re.findall(init_pattern, block_content, re.DOTALL)
            
            if inits:
                # Keep only the first (most complete) init block
                # Remove all init blocks
                cleaned = re.sub(init_pattern, '', block_content, flags=re.DOTALL)
                # Add back the first one at the beginning
                cleaned = f'{inits[0]}\n{cleaned.strip()}'
                return f'```mermaid\n{cleaned}```'
        
        return match.group(0)
    
    return re.sub(pattern, process_block, content, flags=re.DOTALL)

def cleanup_all_diagrams():
    """Cleans up all diagram files"""
    diagrams_dir = Path("docs/diagrams")
    
    if not diagrams_dir.exists():
        print("❌ Diagrams directory not found")
        return
    
    cleaned_count = 0
    for md_file in diagrams_dir.glob("*.md"):
        if md_file.name == "README.md":
            continue
        
        try:
            content = md_file.read_text(encoding="utf-8")
            cleaned = remove_duplicate_inits(content)
            
            if content != cleaned:
                md_file.write_text(cleaned, encoding="utf-8")
                cleaned_count += 1
                print(f"✅ Cleaned: {md_file.name}")
        except Exception as e:
            print(f"⚠️  Error processing {md_file.name}: {e}")
    
    print(f"\n✅ Cleaned {cleaned_count} diagram files")

if __name__ == "__main__":
    cleanup_all_diagrams()

