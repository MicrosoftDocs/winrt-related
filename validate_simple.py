#!/usr/bin/env python3
"""Quick validation that hierarchy updates didn't break content."""

from pathlib import Path
import re

def validate_file_structure(filepath):
    """Check that file has expected markdown structure."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    issues = []
    
    # Check for required sections
    if '## Syntax' not in content:
        issues.append("Missing '## Syntax' section")
    
    # Count tables
    table_lines = [line for line in content.split('\n') if '|' in line and line.strip()]
    
    # Count code blocks (should be even - opening and closing)
    code_block_count = content.count('```')
    if code_block_count % 2 != 0:
        issues.append(f"Unmatched code blocks: {code_block_count}")
    
    # Check hierarchy section format
    if '## Element hierarchy' in content:
        hierarchy_section = content.split('## Element hierarchy')[1].split('##')[0]
        
        # Should have tree characters if updated, OR just the element itself for root elements
        has_tree = '└─' in hierarchy_section
        has_nbsp = '&nbsp;' in hierarchy_section
        has_element = '**`<' in hierarchy_section or '**[`<' in hierarchy_section
        
        if not has_tree and not has_nbsp and not has_element:
            issues.append("Element hierarchy section appears empty")
        
        # Check for broken links
        broken_link_pattern = r'\]\(\s*\)|\]\(\.md\)'
        if re.search(broken_link_pattern, hierarchy_section):
            issues.append("Broken links in hierarchy section")
    
    # Check for mangled markdown
    # Look for common issues
    if '`<`<' in content or '>`>`' in content:
        issues.append("Doubled angle brackets detected")
    
    if '[``' in content or '``]' in content:
        issues.append("Malformed inline code")
    
    return issues

def main():
    schema_dir = Path(r'C:\winrt-related-pr\winrt-related-src\schemas\appxpackage\uapmanifestschema')
    
    # Get all element files
    element_files = list(schema_dir.glob('element-*.md'))
    
    print(f"Quick validation of {len(element_files)} element files...\n")
    
    files_with_issues = []
    total_issues = 0
    
    for md_file in element_files:
        issues = validate_file_structure(md_file)
        
        if issues:
            print(f"⚠️  {md_file.name}")
            for issue in issues:
                print(f"    - {issue}")
            files_with_issues.append(md_file.name)
            total_issues += len(issues)
    
    print(f"\n{'='*60}")
    print(f"Validation Summary:")
    print(f"  Files checked: {len(element_files)}")
    print(f"  Files with issues: {len(files_with_issues)}")
    print(f"  Total issues: {total_issues}")
    
    if total_issues == 0:
        print("\n✅ VALIDATION PASSED - No structural issues detected!")
    else:
        print(f"\n⚠️  Found {total_issues} potential issues")
        print("\nSample files with issues:")
        for f in files_with_issues[:10]:
            print(f"  - {f}")

if __name__ == '__main__':
    main()
