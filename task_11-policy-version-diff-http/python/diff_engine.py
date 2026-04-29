def compare_versions(old: str, new: str) -> dict:
    if old == new:
        return {
            "status": "no_change",
            "severity": "info",
            "message": "No difference between policy versions"
        }

    return {
        "status": "changed",
        "severity": "warning",
        "message": "Policy content has changed"
    }