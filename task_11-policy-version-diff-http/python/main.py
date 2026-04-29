from fastapi import FastAPI, HTTPException

from db import get_connection
from repository import get_policy_content
from diff_engine import compare_versions

app = FastAPI()

@app.get("/diff")
def diff_policy(name: str, v1: int, v2: int):
    conn = get_connection()

    try:
        old = get_policy_content(conn, name, v1)
        new = get_policy_content(conn, name, v2)
    finally:
        conn.close()

    if old is None or new is None:
        raise HTTPException(
            status_code=404,
            detail="One or both policy versions not found"
        )

    result = compare_versions(old, new)

    return {
        "policy": name,
        "from_version": v1,
        "to_version": v2,
        "result": result
    }