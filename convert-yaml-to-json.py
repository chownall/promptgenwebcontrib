#!/usr/bin/env python3
"""
Script pour convertir les fichiers YAML en JSON
Usage: python convert-yaml-to-json.py stacks/*.yaml
"""

import yaml
import json
import sys
import os
from pathlib import Path

def yaml_to_json(yaml_file):
    """Convertit un fichier YAML en JSON"""
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Créer le nom du fichier JSON
    json_file = yaml_file.replace('.yaml', '.json')
    
    # Écrire le JSON formaté
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    print(f"✅ Converti: {yaml_file} → {json_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python convert-yaml-to-json.py stacks/*.yaml")
        sys.exit(1)
    
    for yaml_file in sys.argv[1:]:
        if yaml_file.endswith('.yaml'):
            yaml_to_json(yaml_file)
        else:
            print(f"⚠️  Ignoré: {yaml_file} (pas un fichier .yaml)")

if __name__ == "__main__":
    main()
