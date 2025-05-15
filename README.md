🚀 Quick Start

Clone the repository from GitHub and navigate into the project directory.

Set up a Python virtual environment using python3 -m venv venv, activate it, and install the required dependencies with pip install -r requirements.txt.

Create a .env file in the project root and paste your OpenAI API key inside:

OPENAI_API_KEY=your-api-key-here

You can get your API key by logging into https://platform.openai.com/account/api-keys

Run the setup script by executing python setup_alias.py.

On macOS/Linux, you’ll be asked to choose between adding a shell alias or installing a wrapper script. The alias is added to your .bashrc or .zshrc, while the wrapper installs a command in /usr/local/bin or falls back to ~/.local/bin if permissions are restricted.

On Windows, a PowerShell function named ai will be added to your profile automatically.

You can now use the assistant by typing something like ai "list all mp4 files in Downloads" into your terminal.

💡 Features

Translates natural language into shell commands using OpenAI

Provides explanations and optional dry-run mode before executing

Cross-platform setup support for Unix and Windows

Designed to be modular with plugin support (e.g., for Git and Docker)

📁 Project Structure

The project is organized with modular components under a core/ directory, including:

main.py – entry point for the CLI

setup_alias.py – script to configure alias or wrapper

.env – file where your OpenAI API key is stored (not committed to Git)

core/parser.py – handles natural language translation

core/executor.py – handles dry-run and execution

core/explainer.py – explains shell commands

core/plugins/ – future support for plugin commands

🛠️ Requirements

Python 3.8 or higher

An OpenAI API key

🙌 Contributing

Feel free to open issues, suggest improvements, or submit pull requests to contribute to this project.

📄 License

This project is licensed under the MIT License.

