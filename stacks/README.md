# Tech Stacks Repository

This directory contains the tech stacks available for the PromptWebGen extension, following a standardized schema based on industry standards.

## 📋 YAML Format

All tech stacks are stored in YAML format for easy editing and maintenance:

### 🟢 **YAML (Recommended)**
- **Easy to edit** manually
- **Clear syntax** and readable
- **Fewer syntax errors**
- **Files**: `*.yaml`

## 📋 Standardized Schema

Each tech stack follows a standardized schema with the following structure:

### Required structure:
- **id**: Unique identifier
- **name**: Readable stack name
- **description**: Concise technical description
- **category**: Category (Frontend/Backend/Full-Stack/Mobile/DevOps/Data/AI/ML)
- **technologies**: Technologies structured by category
- **setup**: Installation and configuration instructions

### Structured technologies:
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

### Automated setup:
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
      description: "File description"
```

## 🚀 Adding a new tech stack

### Recommended method (YAML):
1. **Copy the template**: `cp template.yaml my-new-stack.yaml`
2. **Edit the YAML file** with your data
3. **Validate** that the structure is correct
4. **Test** the installation instructions

### Direct method:
1. **Create a new YAML file** in this directory
2. **Follow the schema** defined in the template
3. **Include all required sections**
4. **Structure technologies** by category
5. **Provide complete installation instructions**
6. **Add necessary configuration files**

## ✅ Validation

Tech stacks are automatically analyzed by the MCP (Model Context Protocol) system when submitted via Pull Request.

## 🎯 Advantages of the standardized schema

- **Automated installation** by AI
- **Automatic validation** of data
- **Clear structure** and maintainable
- **Complete installation instructions**
- **Configuration files included**
- **Industry standards compatibility**
- **Easy editing** in YAML
- **Simple maintenance**
