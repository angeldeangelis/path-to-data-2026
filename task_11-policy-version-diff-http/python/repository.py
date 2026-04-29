import psycopg2

def get_policy_content(conn, name: str, version: int) -> str | None:
    with conn.cursor() as cur:
        cur.execute(
            """
            SELECT content
            FROM policies
            WHERE name = %s AND version = %s
            """,
            (name, version)
        )
        row = cur.fetchone()
        return row[0] if row else None