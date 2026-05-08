import sqlite3

def conectar():
    return sqlite3.connect("ortodoncia.db")

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pacientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT,
        edad INTEGER
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tratamientos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        paciente_id INTEGER,
        descripcion TEXT,
        estado TEXT,
        FOREIGN KEY (paciente_id) REFERENCES pacientes(id)
    )
    """)

    conn.commit()
    conn.close()