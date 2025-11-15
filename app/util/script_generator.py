"""Script generator for environment setup"""

from typing import Any


class ScriptGenerator:
    """Generate installation scripts for different platforms"""

    @staticmethod
    def generate_bash_script(bucket_data: dict[str, Any]) -> str:
        """Generate bash installation script"""
        script_lines = [
            "#!/bin/bash",
            "set -e",
            "",
            f"# {bucket_data.get('name', 'Development Environment')} Installation Script",
            f"# {bucket_data.get('description', '')}",
            "",
            "echo '================================'",
            f"echo 'Installing {bucket_data.get('name', 'environment')}...'",
            "echo '================================'",
            "",
        ]

        # Install packages
        packages = bucket_data.get("packages", [])
        if packages:
            script_lines.append("# Install packages")
            script_lines.append("echo 'Installing packages...'")

            # Group by package manager
            pkg_managers = {}
            for pkg in packages:
                manager = pkg.get("package_manager", "")
                if manager not in pkg_managers:
                    pkg_managers[manager] = []
                pkg_managers[manager].append(pkg)

            # Generate install commands
            for manager, pkgs in pkg_managers.items():
                if manager == "apt":
                    script_lines.append("sudo apt-get update")
                    for pkg in pkgs:
                        cmd = pkg.get("install_command") or f"sudo apt-get install -y {pkg['name']}"
                        script_lines.append(cmd)
                elif manager == "brew":
                    for pkg in pkgs:
                        cmd = pkg.get("install_command") or f"brew install {pkg['name']}"
                        script_lines.append(cmd)
                elif manager == "pip":
                    for pkg in pkgs:
                        global_flag = "--user" if not pkg.get("is_global") else ""
                        version = pkg.get("version", "latest")
                        version_spec = f"=={version}" if version != "latest" else ""
                        cmd = pkg.get("install_command") or f"pip install {global_flag} {pkg['name']}{version_spec}"
                        script_lines.append(cmd)
                elif manager == "npm":
                    for pkg in pkgs:
                        global_flag = "-g" if pkg.get("is_global") else ""
                        version = pkg.get("version", "latest")
                        version_spec = f"@{version}" if version != "latest" else ""
                        cmd = (
                            pkg.get("install_command") or f"npm install {global_flag} {pkg['name']}{version_spec}"
                        )
                        script_lines.append(cmd)
                else:
                    # Custom package manager
                    for pkg in pkgs:
                        cmd = pkg.get("install_command") or f"{manager} install {pkg['name']}"
                        script_lines.append(cmd)

            script_lines.append("")

        # Set environment variables
        environments = bucket_data.get("environments", [])
        if environments:
            script_lines.append("# Set environment variables")
            script_lines.append("echo 'Setting environment variables...'")
            for env in environments:
                key = env.get("key", "")
                value = env.get("value", "")
                is_secret = env.get("is_secret", False)
                if is_secret:
                    script_lines.append(f"# {key}=<SECRET> (please set manually)")
                else:
                    script_lines.append(f"export {key}='{value}'")
            script_lines.append("")

        # Create config files
        config_files = bucket_data.get("config_files", [])
        if config_files:
            script_lines.append("# Create config files")
            script_lines.append("echo 'Creating config files...'")
            for config in config_files:
                file_path = config.get("file_path", "")
                content = config.get("content", "")
                script_lines.append(f"cat > {file_path} << 'EOF'")
                script_lines.append(content)
                script_lines.append("EOF")
                script_lines.append("")

        script_lines.extend(
            [
                "echo '================================'",
                "echo 'Installation completed!'",
                "echo '================================'",
            ]
        )

        return "\n".join(script_lines)

    @staticmethod
    def generate_powershell_script(bucket_data: dict[str, Any]) -> str:
        """Generate PowerShell installation script for Windows"""
        script_lines = [
            "# PowerShell Installation Script",
            f"# {bucket_data.get('name', 'Development Environment')}",
            f"# {bucket_data.get('description', '')}",
            "",
            "Write-Host '================================'",
            f"Write-Host 'Installing {bucket_data.get('name', 'environment')}...'",
            "Write-Host '================================'",
            "",
        ]

        # Install packages
        packages = bucket_data.get("packages", [])
        if packages:
            script_lines.append("# Install packages")
            script_lines.append("Write-Host 'Installing packages...'")

            for pkg in packages:
                manager = pkg.get("package_manager", "")
                if manager == "choco":
                    cmd = pkg.get("install_command") or f"choco install {pkg['name']} -y"
                    script_lines.append(cmd)
                elif manager == "npm":
                    global_flag = "-g" if pkg.get("is_global") else ""
                    version = pkg.get("version", "latest")
                    version_spec = f"@{version}" if version != "latest" else ""
                    cmd = pkg.get("install_command") or f"npm install {global_flag} {pkg['name']}{version_spec}"
                    script_lines.append(cmd)
                elif manager == "pip":
                    global_flag = "" if pkg.get("is_global") else "--user"
                    version = pkg.get("version", "latest")
                    version_spec = f"=={version}" if version != "latest" else ""
                    cmd = pkg.get("install_command") or f"pip install {global_flag} {pkg['name']}{version_spec}"
                    script_lines.append(cmd)
                else:
                    cmd = pkg.get("install_command", "")
                    if cmd:
                        script_lines.append(cmd)

            script_lines.append("")

        # Set environment variables
        environments = bucket_data.get("environments", [])
        if environments:
            script_lines.append("# Set environment variables")
            script_lines.append("Write-Host 'Setting environment variables...'")
            for env in environments:
                key = env.get("key", "")
                value = env.get("value", "")
                is_secret = env.get("is_secret", False)
                if is_secret:
                    script_lines.append(f"# {key}=<SECRET> (please set manually)")
                else:
                    script_lines.append(f"[Environment]::SetEnvironmentVariable('{key}', '{value}', 'User')")
            script_lines.append("")

        # Create config files
        config_files = bucket_data.get("config_files", [])
        if config_files:
            script_lines.append("# Create config files")
            script_lines.append("Write-Host 'Creating config files...'")
            for config in config_files:
                file_path = config.get("file_path", "").replace("~", "$env:USERPROFILE")
                content = config.get("content", "")
                script_lines.append(f"@'\n{content}\n'@ | Out-File -FilePath {file_path} -Encoding UTF8")
                script_lines.append("")

        script_lines.extend(
            [
                "Write-Host '================================'",
                "Write-Host 'Installation completed!'",
                "Write-Host '================================'",
            ]
        )

        return "\n".join(script_lines)

    @staticmethod
    def generate_dockerfile(bucket_data: dict[str, Any]) -> str:
        """Generate Dockerfile"""
        lines = [
            "FROM ubuntu:22.04",
            "",
            f"# {bucket_data.get('name', 'Development Environment')}",
            f"# {bucket_data.get('description', '')}",
            "",
            "ENV DEBIAN_FRONTEND=noninteractive",
            "",
        ]

        # Set environment variables
        environments = bucket_data.get("environments", [])
        if environments:
            lines.append("# Environment variables")
            for env in environments:
                if not env.get("is_secret", False):
                    lines.append(f"ENV {env.get('key', '')}={env.get('value', '')}")
            lines.append("")

        # Install system packages
        packages = bucket_data.get("packages", [])
        apt_packages = [pkg for pkg in packages if pkg.get("package_manager") == "apt"]
        if apt_packages:
            lines.append("# Install system packages")
            lines.append("RUN apt-get update && apt-get install -y \\")
            for i, pkg in enumerate(apt_packages):
                suffix = " \\" if i < len(apt_packages) - 1 else ""
                lines.append(f"    {pkg.get('name', '')}{suffix}")
            lines.append("    && rm -rf /var/lib/apt/lists/*")
            lines.append("")

        # Install other packages
        other_packages = [pkg for pkg in packages if pkg.get("package_manager") != "apt"]
        if other_packages:
            lines.append("# Install additional packages")
            for pkg in other_packages:
                manager = pkg.get("package_manager", "")
                if manager in ["pip", "npm", "cargo"]:
                    cmd = pkg.get("install_command") or f"{manager} install {pkg.get('name', '')}"
                    lines.append(f"RUN {cmd}")
            lines.append("")

        # Copy config files
        config_files = bucket_data.get("config_files", [])
        if config_files:
            lines.append("# Copy config files")
            for config in config_files:
                file_path = config.get("file_path", "")
                lines.append(f"COPY {config.get('name', 'config')} {file_path}")
            lines.append("")

        lines.append("WORKDIR /workspace")
        lines.append('CMD ["/bin/bash"]')

        return "\n".join(lines)

    @staticmethod
    def generate_docker_compose(bucket_data: dict[str, Any]) -> str:
        """Generate docker-compose.yml"""
        lines = [
            "version: '3.8'",
            "",
            "services:",
            f"  {bucket_data.get('path', 'devenv')}:",
            "    build: .",
            "    container_name: ${PROJECT_NAME:-devenv}",
            "    volumes:",
            "      - ./workspace:/workspace",
            "    environment:",
        ]

        # Add environment variables
        environments = bucket_data.get("environments", [])
        for env in environments:
            if not env.get("is_secret", False):
                lines.append(f"      - {env.get('key', '')}={env.get('value', '')}")

        lines.extend(["    stdin_open: true", "    tty: true"])

        return "\n".join(lines)
