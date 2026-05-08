from database import crear_tablas
from pacientes import agregar_paciente, ver_pacientes
from tratamientos import crear_tratamiento, ver_tratamientos

def menu():
    crear_tablas()

    while True:
        print("\n=== SISTEMA ORTODONCIA ===")
        print("1. Agregar paciente")
        print("2. Ver pacientes")
        print("3. Crear tratamiento")
        print("4. Ver tratamientos")
        print("5. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_paciente()
        elif opcion == "2":
            ver_pacientes()
        elif opcion == "3":
            crear_tratamiento()
        elif opcion == "4":
            ver_tratamientos()
        elif opcion == "5":
            break
        else:
            print("❌ Opción inválida")

menu()