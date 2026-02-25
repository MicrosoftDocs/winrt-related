#!/usr/bin/env python3
"""Additional validation: check git diff stats for anomalies."""

import subprocess
from pathlib import Path

def main():
    print("Checking git diff statistics...\n")
    
    # Get diff stats
    result = subprocess.run(
        ['git', 'diff', '--stat', 'main'],
        capture_output=True,
        text=True,
        check=True
    )
    
    lines = result.stdout.strip().split('\n')
    
    # Parse the summary line
    summary = lines[-1]
    print(f"Overall: {summary}\n")
    
    # Look for anomalies: files with excessive deletions relative to additions
    anomalies = []
    
    for line in lines[:-1]:
        if 'element-' not in line:
            continue
        
        parts = line.split('|')
        if len(parts) < 2:
            continue
        
        filename = parts[0].strip()
        stats = parts[1].strip()
        
        # Parse +/- counts
        additions = stats.count('+')
        deletions = stats.count('-')
        
        # Flag if deletions are way more than additions (could indicate content loss)
        # But hierarchy updates should have more deletions, so allow for that
        if deletions > 50 and additions < 10:
            anomalies.append({
                'file': Path(filename).name,
                'additions': additions,
                'deletions': deletions
            })
    
    if anomalies:
        print(f"WARNING: Files with unusual diff patterns ({len(anomalies)}):")
        for item in anomalies[:10]:
            print(f"  {item['file']}: +{item['additions']} -{item['deletions']}")
        print("\nNote: These may be normal if they had long hierarchies")
    else:
        print("OK: No unusual diff patterns detected")
    
    # Check that we only touched element files
    print("\nChecking modified file types...")
    non_element_files = []
    
    for line in lines[:-1]:
        parts = line.split('|')
        if len(parts) < 1:
            continue
        
        filename = parts[0].strip()
        if 'uapmanifestschema' in filename and not filename.endswith('element-*.md'):
            filepath = Path(filename)
            if filepath.suffix == '.md' and not filepath.name.startswith('element-'):
                non_element_files.append(filepath.name)
    
    if non_element_files:
        print(f"WARNING: Modified non-element files: {non_element_files}")
    else:
        print("OK: Only element files were modified")
    
    print("\n" + "="*60)
    print("Git diff validation complete!")

if __name__ == '__main__':
    main()
