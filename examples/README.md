# Environment Examples

This directory contains example environment configurations that you can use as templates for your own development environments.

## Available Examples

### 1. Python Data Science (`python-data-science.json`)

Complete Python environment for data science and machine learning.

**Includes:**
- pandas, numpy, matplotlib
- scikit-learn
- jupyter notebook

**Usage:**
```bash
# Generate installation scripts
mydevenv generate examples/python-data-science.json --output ./scripts

# Or run the generated script directly
bash scripts/install.sh
```

### 2. Node.js Full Stack (`nodejs-fullstack.json`)

Complete Node.js development environment with TypeScript.

**Includes:**
- TypeScript, ts-node
- ESLint, Prettier
- Nodemon for live reload

**Usage:**
```bash
mydevenv generate examples/nodejs-fullstack.json --output ./scripts
bash scripts/install.sh
```

### 3. Go Backend (`golang-backend.json`)

Complete Go development environment for backend services.

**Includes:**
- Go 1.21
- golangci-lint
- air for live reload

**Usage:**
```bash
mydevenv generate examples/golang-backend.json --output ./scripts
bash scripts/install.sh
```

## How to Use These Examples

### Method 1: Generate Scripts Locally

```bash
# Generate installation scripts
mydevenv generate examples/python-data-science.json --output ./my-scripts

# Run the installation script
bash my-scripts/install.sh
```

### Method 2: Customize for Your Needs

1. Copy an example file:
   ```bash
   cp examples/python-data-science.json my-environment.json
   ```

2. Edit the file to add/remove packages and configurations

3. Generate scripts:
   ```bash
   mydevenv generate my-environment.json --output ./scripts
   ```

### Method 3: Use with Docker

```bash
# Generate Dockerfile
mydevenv generate examples/python-data-science.json --type dockerfile --output .

# Build and run
docker build -t my-dev-env .
docker run -it my-dev-env
```

## Creating Your Own Environment

Start with a template:

```bash
mydevenv init --name "My Custom Environment" --description "My setup"
```

This creates a basic JSON file that you can customize with your preferred packages, environment variables, and configuration files.

## Configuration File Structure

Each environment configuration file follows this structure:

```json
{
  "name": "Environment Name",
  "description": "Description of the environment",
  "platform": "all|linux|macos|windows",
  "version": "1.0.0",
  "packages": [
    {
      "name": "package-name",
      "version": "1.0.0",
      "package_manager": "pip|npm|apt|brew|cargo",
      "description": "Package description",
      "is_global": true|false,
      "platform": "all|linux|macos|windows"
    }
  ],
  "environments": [
    {
      "key": "VARIABLE_NAME",
      "value": "variable_value",
      "description": "Variable description",
      "is_secret": false,
      "platform": "all"
    }
  ],
  "config_files": [
    {
      "name": "config-file-name",
      "file_path": "~/.config/file",
      "content": "file content here",
      "file_type": "text|json|yaml|toml",
      "platform": "all",
      "description": "File description"
    }
  ],
  "readme": "# Installation instructions\n\n..."
}
```

## Platform-Specific Notes

- **Linux**: Use `apt` or distribution-specific package managers
- **macOS**: Use `brew` for system packages
- **Windows**: Use `choco` or `scoop` for system packages
- **All**: Use language-specific package managers (pip, npm, cargo, etc.)

## Contributing

Have a useful environment configuration? Feel free to submit a PR with your example!
