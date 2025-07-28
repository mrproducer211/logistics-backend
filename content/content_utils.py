import json
import os
from typing import List, Dict, Optional

# Path to the content JSON file
CONTENT_FILE = os.path.join(os.path.dirname(__file__), 'content.json')

def load_content() -> List[Dict]:
    """Load all content from the JSON file"""
    try:
        with open(CONTENT_FILE, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_content(content: List[Dict]) -> bool:
    """Save content to the JSON file"""
    try:
        with open(CONTENT_FILE, 'w', encoding='utf-8') as f:
            json.dump(content, f, indent=2, ensure_ascii=False)
        return True
    except Exception as e:
        print(f"Error saving content: {e}")
        return False

def get_section(section_name: str) -> Optional[Dict]:
    """Get a specific section by name"""
    content = load_content()
    for item in content:
        if item.get('section') == section_name:
            return item
    return None

def update_section(section_name: str, new_data: Dict) -> bool:
    """Update a specific section"""
    content = load_content()
    
    # Find and update the section
    for item in content:
        if item.get('section') == section_name:
            item.update(new_data)
            return save_content(content)
    
    return False

def create_section(section_data: Dict) -> bool:
    """Create a new section"""
    content = load_content()
    
    # Check if section already exists
    for item in content:
        if item.get('section') == section_data.get('section'):
            return False  # Section already exists
    
    content.append(section_data)
    return save_content(content)

def delete_section(section_name: str) -> bool:
    """Delete a section"""
    content = load_content()
    content = [item for item in content if item.get('section') != section_name]
    return save_content(content) 