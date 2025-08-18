#!/usr/bin/env python3
"""
Script to test YAML validation for all stack files
"""

import yaml
import os
import glob
from pathlib import Path

def test_yaml_file(file_path):
    """Test if a YAML file is valid"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        print(f"✅ VALID: {file_path}")
        return True
    except yaml.YAMLError as e:
        print(f"❌ INVALID: {file_path}")
        print(f"   Error: {e}")
        return False
    except Exception as e:
        print(f"❌ ERROR: {file_path}")
        print(f"   Error: {e}")
        return False

def main():
    """Test all YAML files in the stacks directory"""
    stacks_dir = Path("stacks")
    yaml_files = list(stacks_dir.glob("*.yaml"))
    
    print("🧪 Testing YAML validation for all stack files...")
    print("=" * 60)
    
    valid_count = 0
    invalid_count = 0
    
    for yaml_file in yaml_files:
        if test_yaml_file(yaml_file):
            valid_count += 1
        else:
            invalid_count += 1
        print()
    
    print("=" * 60)
    print(f"📊 Results:")
    print(f"   ✅ Valid files: {valid_count}")
    print(f"   ❌ Invalid files: {invalid_count}")
    print(f"   📁 Total files: {len(yaml_files)}")
    
    if invalid_count > 0:
        print("\n⚠️  Some files have YAML syntax errors!")
        return 1
    else:
        print("\n🎉 All YAML files are valid!")
        return 0

if __name__ == "__main__":
    exit(main())
