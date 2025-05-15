import typer
from core import parser, executor, explainer

app = typer.Typer()

@app.command()
def dummy():
    typer.echo("dummy command")

@app.command()
def run(
    query: str = typer.Argument(..., help="Natural language command"),
    dry_run: bool = True
):
    """
    Translates a natural language command into a shell command, explains it,
    and optionally executes it.
    """
    # Step 1: Translate the query to a shell command
    command = parser.translate(query)

    # Step 2: Explain what the command does
    explanation = explainer.explain(command)
    typer.echo(f"🔍 Explanation: {explanation}")
    typer.echo(f"💻 Command: {command}")

    # Step 3: Execute if not a dry run
    if dry_run:
        typer.echo("🚫 Dry-run mode. Command not executed.")
    else:
        executor.execute(command)

if __name__ == "__main__":
    app()
