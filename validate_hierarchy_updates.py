#!/usr/bin/env python3
"""Validate that hierarchy updates didn't break any content."""

import re
from pathlib import Path
import subprocess

def get_file_from_main(filepath):
    """Get file content from main branch."""
    try:
        result = subprocess.run(
            ['git', 'show', f'main:{filepath}'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout
    except subprocess.CalledProcessError:
        return None

def extract_sections(content):
    """Extract all H2 sections from markdown content."""
    sections = {}
    current_section = None
    current_content = []
    
    for line in content.split('\n'):
        if line.startswith('## '):
            # Save previous section
            if current_section:
                sections[current_section] = '\n'.join(current_content)
            # Start new section
            current_section = line[3:].strip()
            current_content = []
        elif current_section:
            current_content.append(line)
    
    # Save last section
    if current_section:
        sections[current_section] = '\n'.join(current_content)
    
    return sections

def find_tables(content):
    """Find all markdown tables in content."""
    tables = []
    in_table = False
    table_lines = []
    
    for line in content.split('\n'):
        # Markdown tables have pipes
        if '|' in line and line.strip():
            if not in_table:
                in_table = True
                table_lines = [line]
            else:
                table_lines.append(line)
        else:
            if in_table:
                tables.append('\n'.join(table_lines))
                in_table = False
                table_lines = []
    
    # Don't forget last table
    if in_table and table_lines:
        tables.append('\n'.join(table_lines))
    
    return tables

def validate_file(filepath):
    """Validate a single file."""
    # Get current version
    full_path = Path(r'C:\winrt-related-pr') / filepath
    if not full_path.exists():
        return {'error': 'File not found in working tree'}
    
    with open(full_path, 'r', encoding='utf-8') as f:
        current_content = f.read()
    
    # Get main version
    main_content = get_file_from_main(filepath)
    if main_content is None:
        return {'error': 'File not found in main branch'}
    
    # Extract sections
    main_sections = extract_sections(main_content)
    current_sections = extract_sections(current_content)
    
    issues = []
    
    # Check that all sections (except Element hierarchy) are present
    for section in main_sections:
        if section == 'Element hierarchy':
            continue
        if section not in current_sections:
            issues.append(f"Missing section: {section}")
    
    # Check for new unexpected sections
    for section in current_sections:
        if section not in main_sections and section != 'Element hierarchy':
            issues.append(f"New section added: {section}")
    
    # Validate tables are intact
    main_tables = find_tables(main_content)
    current_tables = find_tables(current_content)
    
    if len(main_tables) != len(current_tables):
        issues.append(f"Table count mismatch: {len(main_tables)} -> {len(current_tables)}")
    
    # Check for code blocks
    main_code_blocks = main_content.count('```')
    current_code_blocks = current_content.count('```')
    
    if main_code_blocks != current_code_blocks:
        issues.append(f"Code block mismatch: {main_code_blocks} -> {current_code_blocks}")
    
    # Compare non-hierarchy sections for major content loss
    for section in main_sections:
        if section == 'Element hierarchy':
            continue
        if section in current_sections:
            main_len = len(main_sections[section])
            current_len = len(current_sections[section])
            # Allow for minor formatting differences, but flag major changes
            if current_len < main_len * 0.8:  # More than 20% reduction
                issues.append(f"Section '{section}' significantly shorter: {main_len} -> {current_len} chars")
    
    return {
        'issues': issues,
        'sections_main': list(main_sections.keys()),
        'sections_current': list(current_sections.keys()),
        'tables_main': len(main_tables),
        'tables_current': len(current_tables)
    }

def main():
    schema_dir = Path(r'winrt-related-src\schemas\appxpackage\uapmanifestschema')
    
    # Get list of modified files from git
    result = subprocess.run(
        ['git', 'diff', '--name-only', 'main', '--', str(schema_dir)],
        capture_output=True,
        text=True,
        check=True
    )
    
    modified_files = [f.strip() for f in result.stdout.split('\n') if f.strip()]
    
    print(f"Validating {len(modified_files)} modified files...\n")
    
    total_issues = 0
    files_with_issues = []
    
    for filepath in modified_files[:10]:  # Sample first 10 for quick check
        print(f"Checking {Path(filepath).name}...", end=' ')
        validation = validate_file(filepath)
        
        if 'error' in validation:
            print(f"ERROR: {validation['error']}")
            total_issues += 1
            files_with_issues.append(filepath)
        elif validation['issues']:
            print(f"⚠️  {len(validation['issues'])} issue(s)")
            for issue in validation['issues']:
                print(f"    - {issue}")
            total_issues += len(validation['issues'])
            files_with_issues.append(filepath)
        else:
            print("✓ OK")
    
    print(f"\n{'='*60}")
    print(f"Quick validation of first 10 files:")
    print(f"  Total issues: {total_issues}")
    print(f"  Files with issues: {len(files_with_issues)}")
    
    if total_issues == 0:
        print("\n✅ Validation PASSED - No issues found!")
        print("\nRunning full validation on all files...")
        
        # Run full validation
        all_issues = 0
        all_files_with_issues = []
        
        for filepath in modified_files:
            validation = validate_file(filepath)
            
            if 'error' in validation or validation['issues']:
                all_issues += len(validation.get('issues', []))
                all_files_with_issues.append(filepath)
        
        print(f"\n{'='*60}")
        print(f"Full validation of {len(modified_files)} files:")
        print(f"  Total issues: {all_issues}")
        print(f"  Files with issues: {len(all_files_with_issues)}")
        
        if all_issues == 0:
            print("\n✅ FULL VALIDATION PASSED!")
        else:
            print(f"\n⚠️  Found {all_issues} issues in {len(all_files_with_issues)} files")
            if len(all_files_with_issues) <= 20:
                print("\nFiles with issues:")
                for f in all_files_with_issues:
                    print(f"  - {Path(f).name}")
    else:
        print(f"\n⚠️  Found issues in quick check. Review before proceeding.")

if __name__ == '__main__':
    main()
