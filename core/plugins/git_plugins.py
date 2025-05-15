# core/plugins/git_plugin.py
def suggest_git_commands(context: dict) -> list[str]:
    if context.get("in_git_repo"):
        return ["git status", "git log --oneline"]
    return []