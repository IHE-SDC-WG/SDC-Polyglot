#!/usr/bin/env python3
"""
Compare SDC Schema elements/attributes with documentation in SDCSchema.ipynb
"""
import json
import re
import xml.etree.ElementTree as ET
from pathlib import Path
from collections import defaultdict

def extract_schema_elements_and_attributes(schema_dir):
    """Extract all element names and attribute names from XSD files"""
    elements = set()
    attributes = set()
    element_attrs = defaultdict(set)  # element -> set of attributes
    
    schema_files = list(Path(schema_dir).glob("*.xsd"))
    
    for schema_file in schema_files:
        try:
            tree = ET.parse(schema_file)
            root = tree.getroot()
            
            # Define namespace
            ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}
            
            # Find all element definitions
            for elem in root.findall('.//xs:element', ns):
                elem_name = elem.get('name')
                elem_type = elem.get('type', '')
                if elem_name:
                    elements.add(elem_name)
                    
                    # Try to find the type definition to get attributes
                    if elem_type:
                        # Remove namespace prefix if present
                        type_name = elem_type.split(':')[-1]
                        # Find complexType with this name
                        for ct in root.findall(f'.//xs:complexType[@name="{type_name}"]', ns):
                            # Find all attributes in this type
                            for attr in ct.findall('.//xs:attribute', ns):
                                attr_name = attr.get('name')
                                if attr_name:
                                    attributes.add(attr_name)
                                    element_attrs[elem_name].add(attr_name)
            
            # Find all attribute definitions
            for attr in root.findall('.//xs:attribute', ns):
                attr_name = attr.get('name')
                if attr_name:
                    attributes.add(attr_name)
            
            # Find all complexTypes and their attributes
            for ct in root.findall('.//xs:complexType', ns):
                ct_name = ct.get('name')
                if ct_name:
                    # Find elements that use this type
                    for elem in root.findall(f'.//xs:element[@type="{ct_name}"]', ns):
                        elem_name = elem.get('name')
                        if elem_name:
                            # Get attributes from this complexType
                            for attr in ct.findall('.//xs:attribute', ns):
                                attr_name = attr.get('name')
                                if attr_name:
                                    attributes.add(attr_name)
                                    element_attrs[elem_name].add(attr_name)
                    
                    # Also check attributeGroups
                    for ag in ct.findall('.//xs:attributeGroup', ns):
                        ag_ref = ag.get('ref', '').split(':')[-1]
                        # Find the attributeGroup definition
                        for ag_def in root.findall(f'.//xs:attributeGroup[@name="{ag_ref}"]', ns):
                            for attr in ag_def.findall('.//xs:attribute', ns):
                                attr_name = attr.get('name')
                                if attr_name:
                                    attributes.add(attr_name)
        except Exception as e:
            print(f"Error processing {schema_file}: {e}")
            continue
    
    return elements, attributes, element_attrs

def extract_notebook_content(notebook_path):
    """Extract all element and attribute names mentioned in the notebook"""
    with open(notebook_path, 'r') as f:
        nb = json.load(f)
    
    elements_mentioned = set()
    attributes_mentioned = set()
    
    for cell in nb['cells']:
        content = ''.join(cell.get('source', []))
        
        # Find XML element tags
        # Pattern: <ElementName or </ElementName
        elem_pattern = r'<([A-Z][a-zA-Z0-9]*)\b'
        elements_mentioned.update(re.findall(elem_pattern, content))
        
        # Find attribute names in XML
        # Pattern: attributeName=" or @attributeName
        attr_pattern = r'([a-zA-Z][a-zA-Z0-9]*)=\"|@([a-zA-Z][a-zA-Z0-9]*)'
        matches = re.findall(attr_pattern, content)
        for match in matches:
            attr = match[0] or match[1]
            if attr:
                attributes_mentioned.add(attr)
        
        # Find mentions in markdown text (capitalized words that might be elements)
        # Look for patterns like "Question", "Section", etc.
        text_elements = re.findall(r'\b([A-Z][a-z]+(?:[A-Z][a-z]*)*)\b', content)
        # Filter to likely element names (2+ chars, not common words)
        common_words = {'The', 'This', 'When', 'That', 'These', 'There', 'They', 
                       'Some', 'Each', 'All', 'Any', 'For', 'From', 'With', 'Which'}
        elements_mentioned.update(e for e in text_elements if e not in common_words and len(e) > 2)
    
    return elements_mentioned, attributes_mentioned

def main():
    schema_dir = Path("SDC-Schema-Packages")
    notebook_path = Path("Schema/SDCSchema.ipynb")
    
    print("Extracting schema elements and attributes...")
    schema_elements, schema_attributes, element_attrs = extract_schema_elements_and_attributes(schema_dir)
    
    print("Extracting notebook content...")
    nb_elements, nb_attributes = extract_notebook_content(notebook_path)
    
    # Filter schema elements to likely SDC elements (capitalized, reasonable names)
    schema_elements = {e for e in schema_elements if e and e[0].isupper() and len(e) > 1}
    schema_attributes = {a for a in schema_attributes if a and len(a) > 1}
    
    # Find missing elements
    missing_elements = schema_elements - nb_elements
    missing_attributes = schema_attributes - nb_attributes
    
    print(f"\n{'='*60}")
    print(f"SCHEMA ANALYSIS")
    print(f"{'='*60}")
    print(f"Total schema elements: {len(schema_elements)}")
    print(f"Total schema attributes: {len(schema_attributes)}")
    print(f"Elements mentioned in notebook: {len(nb_elements)}")
    print(f"Attributes mentioned in notebook: {len(nb_attributes)}")
    print(f"\nMissing elements: {len(missing_elements)}")
    print(f"Missing attributes: {len(missing_attributes)}")
    
    # Write detailed report
    with open("schema_comparison_report.md", "w") as f:
        f.write("# SDC Schema Comparison Report\n\n")
        f.write("This report compares elements and attributes defined in the SDC schema files ")
        f.write("with those documented in SDCSchema.ipynb.\n\n")
        
        f.write("## Summary\n\n")
        f.write(f"- **Total schema elements**: {len(schema_elements)}\n")
        f.write(f"- **Total schema attributes**: {len(schema_attributes)}\n")
        f.write(f"- **Elements documented**: {len(nb_elements)}\n")
        f.write(f"- **Attributes documented**: {len(nb_attributes)}\n")
        f.write(f"- **Missing elements**: {len(missing_elements)}\n")
        f.write(f"- **Missing attributes**: {len(missing_attributes)}\n\n")
        
        if missing_elements:
            f.write("## Missing Elements\n\n")
            f.write("The following elements are defined in the schema but not documented in the notebook:\n\n")
            for elem in sorted(missing_elements):
                f.write(f"- `{elem}`\n")
            f.write("\n")
        
        if missing_attributes:
            f.write("## Missing Attributes\n\n")
            f.write("The following attributes are defined in the schema but not documented in the notebook:\n\n")
            for attr in sorted(missing_attributes):
                f.write(f"- `{attr}`\n")
            f.write("\n")
        
        # Also list documented but not in schema (might be typos or deprecated)
        extra_elements = nb_elements - schema_elements
        extra_attributes = nb_attributes - schema_attributes
        
        if extra_elements:
            f.write("## Elements Mentioned But Not in Schema\n\n")
            f.write("These might be typos, deprecated elements, or references to external schemas:\n\n")
            for elem in sorted(extra_elements):
                if len(elem) > 2:  # Filter out very short matches
                    f.write(f"- `{elem}`\n")
            f.write("\n")
    
    print("\nDetailed report written to: schema_comparison_report.md")
    print(f"\nTop 20 missing elements:")
    for elem in sorted(list(missing_elements))[:20]:
        print(f"  - {elem}")
    
    print(f"\nTop 20 missing attributes:")
    for attr in sorted(list(missing_attributes))[:20]:
        print(f"  - {attr}")

if __name__ == "__main__":
    main()






