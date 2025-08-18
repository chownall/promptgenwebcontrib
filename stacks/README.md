# Tech Stacks Repository

Ce dossier contient les tech stacks disponibles pour l'extension PromptWebGen, suivant un schéma standardisé basé sur les normes de l'industrie.

## 📋 Formats supportés

### 🟢 **YAML (Recommandé pour l'édition)**
- **Plus facile à éditer** manuellement
- **Syntaxe claire** et lisible
- **Moins d'erreurs** de syntaxe
- **Fichiers** : `*.yaml`

### 🔵 **JSON (Pour l'API)**
- **Format standard** pour les APIs
- **Validation automatique** avec le schéma
- **Fichiers** : `*.json`

## 🔄 Conversion automatique

Utilisez le script Python pour convertir YAML → JSON :
```bash
python convert-yaml-to-json.py stacks/*.yaml
```

## 📋 Schéma JSON Standardisé

Chaque tech stack suit le schéma défini dans `schema.json` qui respecte les standards suivants :

### Structure obligatoire :
- **id** : Identifiant unique
- **name** : Nom lisible de la stack
- **description** : Description technique concise
- **category** : Catégorie (Frontend/Backend/Full-Stack/Mobile/DevOps/Data/AI/ML)
- **technologies** : Technologies structurées par catégorie
- **setup** : Instructions d'installation et configuration

### Technologies structurées :
```yaml
technologies:
  core:
    - name: "Technology Name"
      version: "1.0.0"
      category: "Language|Framework|Library|Database|Tool|Service"
  build_tools: [...]
  testing: [...]
  quality: [...]
```

### Setup automatisé :
```yaml
setup:
  prerequisites:
    - "Node.js 18+"
    - "npm"
  installation:
    - "npm install"
    - "npm run dev"
  configuration:
    - filename: "config.js"
      content: "// Configuration content"
      description: "Description du fichier"
```

## 🚀 Ajout d'un nouveau tech stack

### Méthode recommandée (YAML) :
1. **Copier le template** : `cp template.yaml ma-nouvelle-stack.yaml`
2. **Éditer le fichier YAML** avec vos données
3. **Convertir en JSON** : `python convert-yaml-to-json.py ma-nouvelle-stack.yaml`
4. **Valider** que le JSON est conforme au schéma

### Méthode directe (JSON) :
1. **Créer un nouveau fichier JSON** dans ce dossier
2. **Suivre le schéma** défini dans `schema.json`
3. **Inclure toutes les sections obligatoires**
4. **Structurer les technologies** par catégorie
5. **Fournir des instructions d'installation** complètes
6. **Ajouter les fichiers de configuration** nécessaires

## ✅ Validation

Les tech stacks sont validés contre le schéma JSON et analysés automatiquement par le système MCP (Model Context Protocol) lors de la soumission via Pull Request.

## 🎯 Avantages du schéma standardisé

- **Installation automatisée** par IA
- **Validation automatique** des données
- **Structure claire** et maintenable
- **Instructions complètes** d'installation
- **Fichiers de configuration** inclus
- **Compatibilité** avec les standards de l'industrie
- **Édition facile** en YAML
- **Conversion automatique** vers JSON
