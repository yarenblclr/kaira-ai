import sqlite3
from flask import current_app, g


def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(
            current_app.config["DATABASE_URL"]
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(error=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    db = get_db()

    db.execute("""
        CREATE TABLE IF NOT EXISTS leads (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            isim TEXT NOT NULL,
            telefon TEXT NOT NULL,
            firma TEXT,
            urun_ilgisi TEXT,
            mesaj TEXT,
            tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    db.commit()


def lead_ekle(isim, telefon, firma=None, urun_ilgisi=None, mesaj=None):
    db = get_db()

    db.execute("""
        INSERT INTO leads
        (isim, telefon, firma, urun_ilgisi, mesaj)
        VALUES (?, ?, ?, ?, ?)
    """, (isim, telefon, firma, urun_ilgisi, mesaj))

    db.commit()


def tum_leadler():
    db = get_db()

    kayitlar = db.execute("""
        SELECT *
        FROM leads
        ORDER BY tarih DESC
    """).fetchall()

    return [dict(kayit) for kayit in kayitlar]