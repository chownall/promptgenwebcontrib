# Tech Stacks Repository

Ce dossier contient les tech stacks disponibles pour l'extension PromptWebGen, suivant un schéma JSON standardisé basé sur les normes de l'industrie.

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
```json
"technologies": {
  "core": [
    {
      "name": "Technology Name",
      "version": "1.0.0",
      "category": "Language|Framework|Library|Database|Tool|Service"
    }
  ],
  "build_tools": [...],
  "testing": [...],
  "quality": [...]
}
```

### Setup automatisé :
```json
"setup": {
  "prerequisites": ["Node.js 18+", "npm"],
  "installation": ["npm install", "npm run dev"],
  "configuration": [
    {
      "filename": "config.js",
      "content": "// Configuration content",
      "description": "Description du fichier"
    }
  ]
}
```

## 🚀 Ajout d'un nouveau tech stack

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
- **Compatibilité** avec les standards de l'industrie
- **Documentation claire** et structurée
- **Facilité de maintenance** et d'évolution
