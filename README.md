# PromptWebGen Contrib

Welcome to the PromptWebGen contribution repository! This is where you can contribute tech stacks and prompts to the PromptWebGen Cursor extension.

## 🚀 What is PromptWebGen?

**PromptWebGen** is a powerful Cursor extension that provides ready-to-use prompts for creating website boilerplates, UX components, and business components. It helps developers quickly generate modern, production-ready web applications.

### ✨ Features

- **Pre-built Prompts**: Ready-to-use prompts for common web development tasks
- **Tech Stack Templates**: Complete technology stack definitions with installation instructions
- **UX Components**: Prompts for creating user interface components
- **Business Components**: Templates for common business logic patterns
- **AI-Powered Generation**: Leverages AI to generate code based on your specifications

## 🛠️ How It Works

1. **Install the Extension**: Add PromptWebGen to your Cursor editor
2. **Select a Tech Stack**: Choose from available technology stacks
3. **Use Pre-built Prompts**: Generate boilerplates, components, and features
4. **Customize**: Modify and extend the generated code for your needs

## 📁 Repository Structure

```
promptgenwebcontrib/
├── stacks/                    # Tech stack definitions
│   ├── template.yaml         # Template for new stacks
│   ├── html-js-css-minimal.yaml
│   ├── html-js-tailwind.yaml
│   ├── php-mysql-wordpress.yaml
│   ├── ruby-on-rails.yaml
│   └── README.md             # Stack documentation
├── prompts/                   # Pre-built prompts (coming soon)
├── components/               # Component templates (coming soon)
└── README.md                 # This file
```

## 🤝 How to Contribute

### Contributing Tech Stacks

1. **Fork this repository**
2. **Create a new tech stack**:
   ```bash
   cp stacks/template.yaml stacks/my-awesome-stack.yaml
   ```
3. **Edit the stack** following the YAML format
4. **Validate your stack**:
   ```bash
   python3 test-yaml-validation.py
   ```
5. **Submit a Pull Request**

### What Makes a Good Tech Stack?

- **Complete Setup Instructions**: Step-by-step installation guide
- **Configuration Files**: Ready-to-use config files
- **Clear Documentation**: Links to official docs
- **Real-world Use Cases**: Practical applications
- **Modern Technologies**: Up-to-date versions and best practices

### Contributing Prompts

Coming soon! You'll be able to contribute:
- **UX Component Prompts**: For creating UI components
- **Business Logic Prompts**: For common business patterns
- **Boilerplate Prompts**: For project scaffolding

## 📋 Tech Stack Format

All tech stacks are defined in YAML format with the following structure:

```yaml
id: 1
name: "Stack Name"
description: "Description of the stack"
category: Frontend  # Frontend/Backend/Full-Stack/etc.

technologies:
  core:
    - name: "Technology"
      version: "1.0.0"
      category: "Language"

setup:
  prerequisites: []
  installation: []
  configuration: []

use_cases: []
tags: []
contributor:
  name: "Your Name"
  email: "your@email.com"
```

See `stacks/template.yaml` for the complete template.

## 🔧 Development

### Prerequisites

- Python 3.8+
- Git
- Cursor editor

### Local Development

1. **Clone the repository**:
   ```bash
   git clone https://github.com/chownall/promptgenwebcontrib.git
   cd promptgenwebcontrib
   ```

2. **Validate existing stacks**:
   ```bash
   python3 test-yaml-validation.py
   ```

3. **Create your contribution**:
   ```bash
   cp stacks/template.yaml stacks/my-stack.yaml
   # Edit the file
   python3 test-yaml-validation.py
   ```

## 📝 Pull Request Process

1. **Fork the repository**
2. **Create a feature branch**:
   ```bash
   git checkout -b feature/my-awesome-stack
   ```
3. **Make your changes**
4. **Test your changes**:
   ```bash
   python3 test-yaml-validation.py
   ```
5. **Commit and push**:
   ```bash
   git add .
   git commit -m "feat: Add my awesome tech stack"
   git push origin feature/my-awesome-stack
   ```
6. **Create a Pull Request**

### PR Guidelines

- **Clear title**: Describe what you're adding
- **Detailed description**: Explain the tech stack and its use cases
- **Validation**: Ensure your YAML passes validation
- **Testing**: Test the installation steps yourself

## 🎯 Available Tech Stacks

### Frontend
- **HTML + JavaScript + CSS Minimal**: Ultra-minimal vanilla web stack
- **HTML + JavaScript + Tailwind CSS**: Modern frontend with utility-first CSS

### Full-Stack
- **PHP + MySQL + WordPress**: Classic CMS stack
- **Ruby on Rails + PostgreSQL + Hotwire**: Modern full-stack framework

### Coming Soon
- React + TypeScript + Vite
- Vue.js + Nuxt.js
- Next.js + Prisma
- Laravel + Inertia.js
- Django + PostgreSQL

## 🚀 Getting Your Stack in the Extension

1. **Submit a PR** with your tech stack
2. **Wait for review** from maintainers
3. **Address feedback** if needed
4. **Get merged** into the main repository
5. **Your stack appears** in the PromptWebGen extension!

## 📞 Support

- **Issues**: Report bugs or request features
- **Discussions**: Ask questions and share ideas
- **Discord**: Join our community (coming soon)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Thanks to all contributors who help make PromptWebGen better! Your tech stacks and prompts help developers around the world build amazing web applications faster.

---

**Ready to contribute?** Start by checking out the [stacks directory](stacks/) and creating your first tech stack! 🚀
