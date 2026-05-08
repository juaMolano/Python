from database import conectar

def agregar_paciente():
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO pacientes (nombre, edad) VALUES (?, ?)",
        (nombre, edad)
    )

    conn.commit()
    conn.close()
    print("✅ Paciente agregado")

def ver_pacientes():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM pacientes")
    pacientes = cursor.fetchall()

    print("\n--- PACIENTES ---")
    for p in pacientes:
        print(p)

    conn.close()