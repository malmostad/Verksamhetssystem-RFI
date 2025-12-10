#!/usr/bin/env python3
"""
Improves all Mermaid diagrams to be more visual, larger, and better styled
"""

import re
from pathlib import Path

def improve_mermaid_diagram(content):
    """Improves Mermaid diagrams with better styling and larger size"""
    
    # Enhanced config with larger fonts, better colors, and more visual appeal
    enhanced_config = """%%{init: {
  'theme': 'default',
  'themeVariables': {
    'fontSize': '22px',
    'fontFamily': 'Arial, sans-serif',
    'primaryColor': '#2196F3',
    'primaryTextColor': '#ffffff',
    'primaryBorderColor': '#1976D2',
    'lineColor': '#1976D2',
    'secondaryColor': '#FFC107',
    'tertiaryColor': '#4CAF50',
    'background': '#FAFAFA',
    'mainBkgColor': '#FFFFFF',
    'secondBkgColor': '#F5F5F5',
    'tertiaryBkgColor': '#E8F5E9',
    'textColor': '#212121',
    'secondaryTextColor': '#424242',
    'tertiaryTextColor': '#616161',
    'lineColor': '#1976D2',
    'border1': '#1976D2',
    'border2': '#FFC107',
    'arrowheadColor': '#1976D2',
    'clusterBkg': '#E3F2FD',
    'clusterBorder': '#1976D2',
    'defaultLinkColor': '#1976D2',
    'titleColor': '#1976D2',
    'edgeLabelBackground': '#FFFFFF',
    'actorBorder': '#1976D2',
    'actorBkg': '#E3F2FD',
    'actorTextColor': '#212121',
    'actorLineColor': '#1976D2',
    'signalColor': '#1976D2',
    'signalTextColor': '#212121',
    'labelBoxBkgColor': '#E3F2FD',
    'labelBoxBorderColor': '#1976D2',
    'labelTextColor': '#212121',
    'loopTextColor': '#212121',
    'noteBorderColor': '#FFC107',
    'noteBkgColor': '#FFF9C4',
    'noteTextColor': '#212121',
    'activationBorderColor': '#1976D2',
    'activationBkgColor': '#E3F2FD',
    'sequenceNumberColor': '#FFFFFF',
    'sectionBkgColor': '#E3F2FD',
    'altBkgColor': '#FFF9C4',
    'altBkgColor2': '#E3F2FD',
    'excludeBkgColor': '#FFEBEE',
    'taskBorderColor': '#1976D2',
    'taskBkgColor': '#E3F2FD',
    'taskTextLightColor': '#FFFFFF',
    'taskTextColor': '#212121',
    'taskTextDarkColor': '#212121',
    'taskTextOutsideColor': '#212121',
    'taskTextClickableColor': '#1976D2',
    'activeTaskBorderColor': '#4CAF50',
    'activeTaskBkgColor': '#C8E6C9',
    'gridColor': '#E0E0E0',
    'doneTaskBkgColor': '#C8E6C9',
    'doneTaskBorderColor': '#4CAF50',
    'critBorderColor': '#F44336',
    'critBkgColor': '#FFCDD2',
    'todayLineColor': '#FFC107'
  },
  'flowchart': {
    'nodeSpacing': 60,
    'rankSpacing': 80,
    'curve': 'basis',
    'padding': 20,
    'htmlLabels': true,
    'useMaxWidth': true
  },
  'gantt': {
    'leftPadding': 75,
    'gridLineStartPadding': 35,
    'fontSize': 18,
    'fontFamily': 'Arial, sans-serif',
    'numberSectionStyles': 4,
    'axisFormat': '%Y-%m-%d',
    'topAxis': false,
    'bottomAxis': true,
    'topPadding': 50,
    'bottomPadding': 50
  }
}}%%
"""
    
    # Pattern to find mermaid code blocks
    pattern = r'```mermaid\n(?:%%\{init:.*?%%\})?\n?'
    
    # Replace with enhanced config
    def replace_func(match):
        return f'```mermaid\n{enhanced_config}'
    
    # Only replace if not already using enhanced config
    if 'fontSize: \'22px\'' not in content:
        content = re.sub(pattern, replace_func, content, flags=re.DOTALL)
    
    return content

def improve_all_diagrams():
    """Improves all diagram files"""
    diagrams_dir = Path("docs/diagrams")
    
    if not diagrams_dir.exists():
        print("❌ Diagrams directory not found")
        return
    
    improved_count = 0
    for md_file in diagrams_dir.glob("*.md"):
        if md_file.name == "README.md":
            continue
        
        try:
            content = md_file.read_text(encoding="utf-8")
            improved = improve_mermaid_diagram(content)
            
            if content != improved:
                md_file.write_text(improved, encoding="utf-8")
                improved_count += 1
                print(f"✅ Improved: {md_file.name}")
        except Exception as e:
            print(f"⚠️  Error processing {md_file.name}: {e}")
    
    print(f"\n✅ Improved {improved_count} diagram files with enhanced styling")

if __name__ == "__main__":
    improve_all_diagrams()

