"""CLI tool for mydevenv - Development Environment Sharing Platform"""

import json
from pathlib import Path
from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.table import Table

app = typer.Typer(help="mydevenv - Development Environment Sharing Platform")
console = Console()

# Default API configuration
DEFAULT_API_URL = "http://localhost:8000/v1"


@app.command()
def export(
    bucket_id: int = typer.Argument(..., help="Bucket ID to export"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file path"),
    format: str = typer.Option("json", "--format", "-f", help="Export format (json, yaml)"),
    api_url: str = typer.Option(DEFAULT_API_URL, "--api-url", help="API server URL"),
):
    """Export a development environment bucket"""
    try:
        response = httpx.get(f"{api_url}/bucket/{bucket_id}/export", params={"format": format})
        response.raise_for_status()

        if output:
            output.write_text(response.text)
            console.print(f"[green]✓[/green] Exported to {output}")
        else:
            console.print(response.text)

    except httpx.HTTPError as e:
        console.print(f"[red]✗[/red] Error: {e}")
        raise typer.Exit(1)


@app.command()
def install_script(
    bucket_id: int = typer.Argument(..., help="Bucket ID"),
    output: Optional[Path] = typer.Option(None, "--output", "-o", help="Output file path"),
    script_type: str = typer.Option(
        "bash", "--type", "-t", help="Script type (bash, powershell, dockerfile, docker-compose)"
    ),
    api_url: str = typer.Option(DEFAULT_API_URL, "--api-url", help="API server URL"),
):
    """Generate installation script for a bucket"""
    try:
        response = httpx.get(
            f"{api_url}/bucket/{bucket_id}/install-script",
            params={"script_type": script_type},
        )
        response.raise_for_status()

        if output:
            output.write_text(response.text)
            console.print(f"[green]✓[/green] Installation script saved to {output}")
        else:
            console.print(response.text)

    except httpx.HTTPError as e:
        console.print(f"[red]✗[/red] Error: {e}")
        raise typer.Exit(1)


@app.command()
def export_all(
    bucket_id: int = typer.Argument(..., help="Bucket ID"),
    output_dir: Path = typer.Option("./exported", "--output", "-o", help="Output directory"),
    api_url: str = typer.Option(DEFAULT_API_URL, "--api-url", help="API server URL"),
):
    """Export all files for a bucket (scripts, configs, etc.)"""
    try:
        response = httpx.get(f"{api_url}/bucket/{bucket_id}/export-all")
        response.raise_for_status()

        files = response.json()
        output_dir.mkdir(parents=True, exist_ok=True)

        for filename, content in files.items():
            file_path = output_dir / filename
            file_path.write_text(content)
            console.print(f"[green]✓[/green] Created {file_path}")

        console.print(f"\n[green]✓[/green] All files exported to {output_dir}")

    except httpx.HTTPError as e:
        console.print(f"[red]✗[/red] Error: {e}")
        raise typer.Exit(1)


@app.command()
def init(
    name: str = typer.Option(..., "--name", "-n", help="Environment name"),
    description: str = typer.Option("", "--description", "-d", help="Environment description"),
    platform: str = typer.Option("all", "--platform", "-p", help="Target platform (linux, macos, windows, all)"),
    output: Path = typer.Option("./devenv.json", "--output", "-o", help="Output file path"),
):
    """Initialize a new development environment configuration"""
    config = {
        "name": name,
        "description": description,
        "platform": platform,
        "version": "1.0.0",
        "packages": [],
        "environments": [],
        "config_files": [],
        "readme": f"# {name}\n\n{description}\n\n## Installation\n\nRun the installation script:\n\n```bash\nbash install.sh\n```",
    }

    output.write_text(json.dumps(config, indent=2))
    console.print(f"[green]✓[/green] Initialized environment configuration at {output}")
    console.print("\nNext steps:")
    console.print("1. Edit the configuration file to add packages, environments, and config files")
    console.print("2. Use 'mydevenv generate' to create installation scripts")


@app.command()
def generate(
    config: Path = typer.Argument(..., help="Configuration file (JSON or YAML)"),
    output_dir: Path = typer.Option("./scripts", "--output", "-o", help="Output directory for scripts"),
    script_type: str = typer.Option(
        "all", "--type", "-t", help="Script type (bash, powershell, dockerfile, docker-compose, all)"
    ),
):
    """Generate installation scripts from a configuration file"""
    try:
        config_data = json.loads(config.read_text())
        output_dir.mkdir(parents=True, exist_ok=True)

        from app.util.script_generator import ScriptGenerator

        scripts = {}
        if script_type in ["bash", "all"]:
            scripts["install.sh"] = ScriptGenerator.generate_bash_script(config_data)
        if script_type in ["powershell", "all"]:
            scripts["install.ps1"] = ScriptGenerator.generate_powershell_script(config_data)
        if script_type in ["dockerfile", "all"]:
            scripts["Dockerfile"] = ScriptGenerator.generate_dockerfile(config_data)
        if script_type in ["docker-compose", "all"]:
            scripts["docker-compose.yml"] = ScriptGenerator.generate_docker_compose(config_data)

        for filename, content in scripts.items():
            file_path = output_dir / filename
            file_path.write_text(content)
            console.print(f"[green]✓[/green] Generated {file_path}")

        console.print(f"\n[green]✓[/green] Scripts generated in {output_dir}")

    except Exception as e:
        console.print(f"[red]✗[/red] Error: {e}")
        raise typer.Exit(1)


@app.command()
def scan(
    output: Path = typer.Option("./current-env.json", "--output", "-o", help="Output file path"),
):
    """Scan current system and generate environment configuration"""
    import platform
    import subprocess

    config = {
        "name": f"Environment for {platform.node()}",
        "description": f"Scanned from {platform.system()} {platform.release()}",
        "platform": platform.system().lower(),
        "version": "1.0.0",
        "packages": [],
        "environments": [],
        "config_files": [],
    }

    console.print("[yellow]⚠[/yellow] Scanning system packages...")

    # Scan pip packages
    try:
        result = subprocess.run(["pip", "freeze"], capture_output=True, text=True)
        if result.returncode == 0:
            for line in result.stdout.strip().split("\n"):
                if "==" in line:
                    name, version = line.split("==")
                    config["packages"].append(
                        {
                            "name": name,
                            "version": version,
                            "package_manager": "pip",
                            "description": f"Python package: {name}",
                            "is_global": False,
                            "platform": "all",
                        }
                    )
    except FileNotFoundError:
        console.print("[yellow]⚠[/yellow] pip not found")

    # Scan npm global packages
    try:
        result = subprocess.run(["npm", "list", "-g", "--depth=0", "--json"], capture_output=True, text=True)
        if result.returncode == 0:
            npm_data = json.loads(result.stdout)
            dependencies = npm_data.get("dependencies", {})
            for name, info in dependencies.items():
                config["packages"].append(
                    {
                        "name": name,
                        "version": info.get("version", "latest"),
                        "package_manager": "npm",
                        "description": f"NPM package: {name}",
                        "is_global": True,
                        "platform": "all",
                    }
                )
    except FileNotFoundError:
        console.print("[yellow]⚠[/yellow] npm not found")

    output.write_text(json.dumps(config, indent=2))
    console.print(f"\n[green]✓[/green] Environment configuration saved to {output}")
    console.print(f"Found {len(config['packages'])} packages")


@app.command()
def version():
    """Show version information"""
    console.print("mydevenv version 0.1.0")
    console.print("Development Environment Sharing Platform")


if __name__ == "__main__":
    app()
