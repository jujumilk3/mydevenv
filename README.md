# mydevenv - Development Environment Sharing Platform

> 개발 환경을 공유하고 저장하여 새로운 컴퓨터에서 쉽게 Import하고 설치할 수 있는 플랫폼

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.93.0-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🌟 Features

- **웹 인터페이스**: 모던한 React 기반 웹 UI로 환경을 쉽게 관리
- **환경 공유**: 개발 환경을 JSON/YAML로 내보내고 다른 사람과 공유
- **자동 설치 스크립트**: Bash, PowerShell, Dockerfile 자동 생성
- **패키지 관리**: pip, npm, brew, apt 등 다양한 패키지 매니저 지원
- **환경 변수 관리**: 환경 변수 템플릿 저장 및 배포
- **설정 파일 관리**: .bashrc, .gitconfig 등 설정 파일 백업 및 복원
- **CLI 도구**: 명령줄에서 쉽게 환경 관리
- **Docker 지원**: Docker 및 docker-compose로 환경 컨테이너화

## 📦 Installation

### Using Poetry (Recommended)

```bash
# Clone the repository
git clone https://github.com/jujumilk3/mydevenv.git
cd mydevenv

# Install dependencies
poetry install

# Activate virtual environment
poetry shell
```

### Using Docker (Recommended for Full Stack)

```bash
# Build and run with docker-compose (API + Frontend)
docker-compose up -d

# Services will be available at:
# - Frontend: http://localhost:3000
# - API: http://localhost:8000
# - API Docs: http://localhost:8000/docs
```

## 🚀 Quick Start

### 1. Start the Full Stack

```bash
# Using docker-compose (API + Frontend)
docker-compose up

# Or run separately:

# Backend (API)
poetry run uvicorn app.main:app --reload

# Frontend (in separate terminal)
cd frontend
npm install
npm run dev
```

### 2. Use the CLI Tool

```bash
# Initialize a new environment configuration
mydevenv init --name "My Dev Environment" --description "Python development setup"

# Scan current system packages
mydevenv scan --output ./my-current-env.json

# Generate installation scripts
mydevenv generate ./my-current-env.json --output ./scripts

# Export a bucket from API
mydevenv export 1 --format json --output ./bucket.json

# Download installation script
mydevenv install-script 1 --type bash --output ./install.sh

# Export all files for a bucket
mydevenv export-all 1 --output ./exported
```

## 📚 API Documentation

Once the server is running, visit:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

### Main Endpoints

#### Buckets (Development Environments)

- `GET /v1/bucket/{bucket_id}` - Get bucket details
- `POST /v1/bucket` - Create a new bucket
- `PATCH /v1/bucket/{bucket_id}` - Update bucket
- `DELETE /v1/bucket/{bucket_id}` - Delete bucket

#### Export/Import

- `GET /v1/bucket/{bucket_id}/export` - Export bucket (JSON/YAML)
- `GET /v1/bucket/{bucket_id}/install-script` - Generate installation script
- `GET /v1/bucket/{bucket_id}/export-all` - Export complete package

## 💡 Usage Examples

### Example 1: Create a Python Development Environment

```json
{
  "name": "Python Data Science Environment",
  "description": "Complete setup for data science with Python",
  "platform": "all",
  "packages": [
    {
      "name": "pandas",
      "version": "2.0.0",
      "package_manager": "pip",
      "description": "Data manipulation library"
    },
    {
      "name": "numpy",
      "version": "latest",
      "package_manager": "pip",
      "description": "Numerical computing library"
    }
  ],
  "environments": [
    {
      "key": "PYTHONPATH",
      "value": "/usr/local/lib/python3.10",
      "description": "Python path"
    }
  ],
  "config_files": [
    {
      "name": ".pylintrc",
      "file_path": "~/.pylintrc",
      "content": "[MASTER]\ninit-hook='import sys; sys.path.append(\"/path/to/root\")'"
    }
  ]
}
```

### Example 2: Node.js Development Environment

```json
{
  "name": "Node.js Full Stack Environment",
  "description": "Complete Node.js development setup",
  "platform": "all",
  "packages": [
    {
      "name": "typescript",
      "version": "latest",
      "package_manager": "npm",
      "is_global": true
    },
    {
      "name": "nodemon",
      "version": "latest",
      "package_manager": "npm",
      "is_global": true
    }
  ],
  "environments": [
    {
      "key": "NODE_ENV",
      "value": "development"
    }
  ]
}
```

## 🔧 CLI Commands

### `mydevenv init`
Initialize a new environment configuration file.

```bash
mydevenv init --name "My Environment" --description "Description" --output ./env.json
```

### `mydevenv scan`
Scan current system and generate environment configuration.

```bash
mydevenv scan --output ./current-env.json
```

### `mydevenv generate`
Generate installation scripts from a configuration file.

```bash
mydevenv generate ./env.json --output ./scripts --type all
```

### `mydevenv export`
Export a bucket from the API server.

```bash
mydevenv export 1 --format json --output ./bucket.json
```

### `mydevenv install-script`
Generate installation script for a bucket.

```bash
mydevenv install-script 1 --type bash --output ./install.sh
```

### `mydevenv export-all`
Export all files for a bucket.

```bash
mydevenv export-all 1 --output ./exported
```

## 🏗️ Architecture

```
mydevenv/
├── app/                     # Backend (FastAPI)
│   ├── api/v1/endpoint/     # API endpoints
│   ├── core/                # Core configurations
│   ├── model/               # Database models
│   │   ├── bucket.py        # Development environment
│   │   ├── package.py       # Package information
│   │   ├── environment.py   # Environment variables
│   │   └── config_file.py   # Configuration files
│   ├── service/             # Business logic
│   │   └── export_service.py # Export/Import services
│   ├── util/                # Utilities
│   │   └── script_generator.py # Script generation
│   ├── cli.py               # CLI tool
│   └── main.py              # Application entry point
├── frontend/                # Frontend (React + Vite)
│   ├── src/
│   │   ├── components/      # UI components
│   │   ├── pages/           # Page components
│   │   ├── services/        # API services
│   │   ├── types/           # TypeScript types
│   │   └── App.tsx          # Main app
│   ├── index.html
│   └── package.json
├── examples/                # Example environments
├── tests/                   # Tests
├── Dockerfile               # Backend Docker config
├── docker-compose.yml       # Full stack Docker config
└── pyproject.toml           # Backend dependencies
```

## 🛠️ Development

### Run Tests

```bash
poetry run pytest
```

### Code Formatting

```bash
# Format code
poetry run black .
poetry run isort .

# Lint code
poetry run ruff .
```

### Database Migrations

```bash
# Create migration
poetry run alembic revision --autogenerate -m "description"

# Apply migrations
poetry run alembic upgrade head
```

## 🌐 Environment Variables

Create a `.env` file in the root directory:

```dotenv
ENV=dev
JWT_SECRET_KEY=your-secret-key
DB_URL=sqlite+aiosqlite:///db.sqlite3
```

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 👨‍💻 Author

**jujumilk3** - [GitHub](https://github.com/jujumilk3)

## 🙏 Acknowledgments

- FastAPI for the awesome web framework
- SQLModel for the elegant ORM
- Typer for the CLI framework

## 📮 Support

If you have any questions or issues, please open an issue on GitHub.

---

Made with ❤️ by jujumilk3
