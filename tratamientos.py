from database import conectar

def crear_tratamiento():
    paciente_id = int(input("ID del paciente: "))
    descripcion = input("Descripción: ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO tratamientos (paciente_id, descripcion, estado)
    VALUES (?, ?, ?)
    """, (paciente_id, descripcion, "En proceso"))

    conn.commit()
    conn.close()
    print("✅ Tratamiento creado")

def ver_tratamientos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT pacientes.nombre, tratamientos.descripcion, tratamientos.estado
    FROM tratamientos
    JOIN pacientes ON pacientes.id = tratamientos.paciente_id
    """)

    datos = cursor.fetchall()

    print("\n--- TRATAMIENTOS ---")
    for d in datos:
        print(d)

    conn.close()