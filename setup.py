# setup_alias.py
import os
import platform
from pathlib import Path
from dotenv import load_dotenv

def get_shell_profile():
    shell = os.environ.get("SHELL", "")
    home = Path.home()
    if "zsh" in shell:
        return home / ".zshrc"
    elif "bash" in shell:
        return home / ".bashrc"
    else:
        return None

def ensure_local_bin_in_path():
    profile = get_shell_profile()
    if not profile:
        return
    local_bin_line = 'export PATH="$HOME/.local/bin:$PATH"'
    with open(profile, "r") as f:
        lines = f.readlines()
    if any(local_bin_line in line for line in lines):
        return
    with open(profile, "a") as f:
        f.write(f"\n{local_bin_line}\n")
    print(f"\u2705 Added ~/.local/bin to PATH in {profile}. Run `source {profile}` or restart your terminal.")

def add_alias_to_shell(alias_command):
    profile = get_shell_profile()
    if not profile:
        print("\u274c Unsupported shell. Please manually add this alias.")
        return
    line = f'\nalias ai=\"{alias_command}\"\n'
    with open(profile, "a") as f:
        f.write(line)
    print(f"\u2705 Alias added to {profile}. Run `source {profile}` or restart your terminal.")

def create_wrapper_script(script_path):
    wrapper_code = f"""#!/bin/bash
python3 \"{script_path}\" run \"$@\"
"""
    preferred_path = Path("/usr/local/bin/ai")
    fallback_path = Path.home() / ".local/bin/ai"

    try:
        preferred_path.write_text(wrapper_code)
        preferred_path.chmod(0o755)
        print(f"\u2705 Wrapper script installed to {preferred_path}")
    except PermissionError:
        print("\u26a0\ufe0f Permission denied for /usr/local/bin. Falling back to ~/.local/bin...")
        fallback_path.parent.mkdir(parents=True, exist_ok=True)
        fallback_path.write_text(wrapper_code)
        fallback_path.chmod(0o755)
        print(f"\u2705 Wrapper script installed to {fallback_path}")
        ensure_local_bin_in_path()

def main():
    load_dotenv()  # Load variables from .env

    # Confirm OpenAI key presence
    if not os.getenv("OPENAI_API_KEY"):
        print("\u274c OPENAI_API_KEY not found in environment. Please create a .env file with your key:")
        print("OPENAI_API_KEY=your-api-key")
        return

    project_path = Path(__file__).resolve().parent
    script_path = project_path / "main.py"

    if platform.system() == "Windows":
        profile = Path.home() / "Documents/PowerShell/Microsoft.PowerShell_profile.ps1"
        profile.parent.mkdir(parents=True, exist_ok=True)
        command = f'function ai {{ python \"{script_path}\" run $args }}\n'
        with open(profile, "a") as f:
            f.write("\n" + command)
        print(f"\u2705 Function added to PowerShell profile: {profile}")
    else:
        choice = input("Add alias or wrapper script? [a/w]: ").strip().lower()
        if choice == "a":
            add_alias_to_shell(f'python3 \"{script_path}\" run')
        elif choice == "w":
            create_wrapper_script(script_path)
        else:
            print("\u274c Invalid choice.")

if __name__ == "__main__":
    main()