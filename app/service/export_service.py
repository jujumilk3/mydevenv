"""Export/Import service for development environments"""

import json
from typing import Any

import yaml

from app.util.script_generator import ScriptGenerator


class ExportService:
    """Service for exporting development environments"""

    @staticmethod
    def export_to_json(bucket_data: dict[str, Any]) -> str:
        """Export bucket data to JSON format"""
        return json.dumps(bucket_data, indent=2, ensure_ascii=False)

    @staticmethod
    def export_to_yaml(bucket_data: dict[str, Any]) -> str:
        """Export bucket data to YAML format"""
        return yaml.dump(bucket_data, allow_unicode=True, sort_keys=False)

    @staticmethod
    def generate_install_script(bucket_data: dict[str, Any], script_type: str = "bash") -> str:
        """Generate installation script"""
        if script_type == "bash":
            return ScriptGenerator.generate_bash_script(bucket_data)
        elif script_type == "powershell":
            return ScriptGenerator.generate_powershell_script(bucket_data)
        elif script_type == "dockerfile":
            return ScriptGenerator.generate_dockerfile(bucket_data)
        elif script_type == "docker-compose":
            return ScriptGenerator.generate_docker_compose(bucket_data)
        else:
            raise ValueError(f"Unsupported script type: {script_type}")

    @staticmethod
    def export_complete_package(bucket_data: dict[str, Any]) -> dict[str, str]:
        """Export complete package with all formats"""
        return {
            "metadata.json": ExportService.export_to_json(bucket_data),
            "metadata.yaml": ExportService.export_to_yaml(bucket_data),
            "install.sh": ExportService.generate_install_script(bucket_data, "bash"),
            "install.ps1": ExportService.generate_install_script(bucket_data, "powershell"),
            "Dockerfile": ExportService.generate_install_script(bucket_data, "dockerfile"),
            "docker-compose.yml": ExportService.generate_install_script(bucket_data, "docker-compose"),
            "README.md": bucket_data.get("readme", ""),
        }


class ImportService:
    """Service for importing development environments"""

    @staticmethod
    def import_from_json(json_data: str) -> dict[str, Any]:
        """Import bucket data from JSON"""
        return json.loads(json_data)

    @staticmethod
    def import_from_yaml(yaml_data: str) -> dict[str, Any]:
        """Import bucket data from YAML"""
        return yaml.safe_load(yaml_data)

    @staticmethod
    def validate_bucket_data(bucket_data: dict[str, Any]) -> bool:
        """Validate imported bucket data"""
        required_fields = ["name", "description"]
        return all(field in bucket_data for field in required_fields)
