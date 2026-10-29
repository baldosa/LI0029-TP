import os

import mysql.connector


def _conn():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "127.0.0.1"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASS", "root"),
        database=os.getenv("DB_NAME", "biblioteca"),
    )


def fetch(sql, params=()):
    c = _conn()
    try:
        cur = c.cursor(dictionary=True)
        cur.execute(sql, params)
        return cur.fetchall()
    finally:
        c.close()


def run(sql, params=()):
    """Ejecuta un INSERT/UPDATE/DELETE; devuelve (lastrowid, rowcount)."""
    c = _conn()
    try:
        cur = c.cursor()
        cur.execute(sql, params)
        c.commit()
        return cur.lastrowid, cur.rowcount
    finally:
        c.close()
