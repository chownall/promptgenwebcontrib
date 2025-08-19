# Tech Stacks Repository

This directory contains the tech stacks available for the PromptWebGen extension. All stacks are stored in YAML format for easy editing and maintenance.

## 📁 Directory Structure

Place all your tech stack descriptions in the `/stacks` directory using the YAML format. Each stack should be a separate `.yaml` file.

## 📋 YAML Format

All tech stacks must be written in YAML format:

### ✅ **Why YAML?**
- **Easy to edit** manually
- **Clear syntax** and readable
- **Fewer syntax errors**
- **Human-friendly** format

### 📄 **File Naming**
- Use descriptive names: `my-stack-name.yaml`
- Use lowercase and hyphens
- Example: `html-js-css-minimal.yaml`

## 🔧 Template Usage

**Always use `template.yaml` as your starting point:**

1. **Copy the template**: `cp template.yaml my-new-stack.yaml`
2. **Edit the file** with your stack information
3. **Follow the structure** exactly as shown in the template
4. **Fill in all required fields**

## ✅ Validation

### **Automatic Validation**
The system is **error-proof (bulletproof)** and will handle most common issues automatically.

### **Manual Validation (Optional)**
Use the validation script to check your YAML files:

```bash
# Test all YAML files
python3 test-yaml-validation.py

# Test a specific file
python3 -c "import yaml; yaml.safe_load(open('stacks/my-stack.yaml'))"
```

### **What the validator checks:**
- ✅ YAML syntax correctness
- ✅ Required field presence
- ✅ Data type validation
- ❌ Reports any parsing errors

## 📋 Required Structure

Each tech stack must follow this structure:

```yaml
id: 1                    # Unique identifier
name: "Stack Name"       # Human-readable name
description: "..."       # Technical description
category: Frontend       # Frontend/Backend/Full-Stack/etc.

technologies:
  core:                  # Core technologies
    - name: "Tech Name"
      version: "1.0.0"
      category: "Language"
  
  build_tools: []        # Build tools (optional)
  testing: []           # Testing tools (optional)
  quality: []           # Quality tools (optional)

setup:
  prerequisites: []     # System requirements
  installation: []      # Installation steps
  configuration: []     # Config files (optional)

use_cases: []           # Use cases
tags: []               # Search tags
documentation: {}      # Documentation links
contributor: {}        # Contributor info
metadata: {}           # Stats and pricing
timestamps: {}         # Creation/update dates
```

## 🚀 Adding a New Stack

### **Step-by-Step Process:**

1. **Copy the template**:
   ```bash
   cp template.yaml my-awesome-stack.yaml
   ```

2. **Edit the file** with your stack details:
   - Replace placeholder values
   - Add your technologies
   - Include installation steps
   - Add configuration files

3. **Validate (optional)**:
   ```bash
   python3 test-yaml-validation.py
   ```

4. **Commit and push**:
   ```bash
   git add stacks/my-awesome-stack.yaml
   git commit -m "feat: Add my awesome stack"
   git push origin main
   ```

## 🎯 Best Practices

### **Do's:**
- ✅ Follow the template structure exactly
- ✅ Use descriptive names and descriptions
- ✅ Include all required fields
- ✅ Test your installation steps
- ✅ Use proper YAML syntax

### **Don'ts:**
- ❌ Don't skip required fields
- ❌ Don't use JSON format
- ❌ Don't ignore the template
- ❌ Don't forget to validate

## 🔍 Error Handling

The system is designed to be **error-proof**:
- **Graceful degradation** for minor issues
- **Automatic error recovery**
- **Clear error messages**
- **Fallback to default values**

## 📚 Examples

Check the existing stacks for examples:
- `html-js-css-minimal.yaml` - Ultra minimal stack
- `html-js-tailwind.yaml` - Complete frontend stack
- `php-mysql-wordpress.yaml` - CMS stack
- `ruby-on-rails.yaml` - Full-stack framework

## 🛠️ Tools

- **`template.yaml`** - Starting template for new stacks
- **`test-yaml-validation.py`** - Validation script
- **`README.md`** - This documentation

## 🎉 Ready to Start?

1. Copy `template.yaml`
2. Fill in your stack details
3. Validate with the script
4. Submit your contribution!

The system is **bulletproof** - just follow the template and you'll be fine! 🚀
