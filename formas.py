print("=" * 50)
print("GEOMETRÍA CON BUCLES (ARTE ASCII)".center(50))
print("=" * 50)

# while True mantiene el programa funcionando
# hasta que el usuario decida salir
while True:

    print("\nMENÚ DE FIGURAS")
    print("1. Triángulo")
    print("2. Cuadrado")
    print("3. Rectángulo")
    print("4. Círculo")
    print("5. Pentágono")
    print("6. Salir")

    opcion = input("Elige una opción: ")

    # Si elige salir
    if opcion == "6":
        print("=" * 50)
        print("Programa finalizado. ¡Hasta luego!".center(50))
        print("=" * 50)
        break

    # Tamaño general para las figuras
    tamaño = int(input("Ingrese el tamaño para sus figuras: "))

    # =====================================
    # TRIÁNGULO
    # =====================================
    if opcion == "1":
        print("\n--- TRIÁNGULO ---")

        for fila in range(1, tamaño + 1):
            for columna in range(fila):
                print("#", end=" ")
            print()

    # =====================================
    # CUADRADO
    # =====================================
    elif opcion == "2":
        print("\n--- CUADRADO ---")

        for fila in range(tamaño):
            for columna in range(tamaño):
                print("#", end=" ")
            print()

    # =====================================
    # RECTÁNGULO
    # =====================================
    elif opcion == "3":
        print(f"\n--- RECTÁNGULO ({tamaño}x{tamaño*2}) ---")

        for fila in range(tamaño):
            for columna in range(tamaño * 2):
                print("#", end=" ")
            print()

    # =====================================
    # CÍRCULO
    # =====================================
    elif opcion == "4":
        print(f"\n--- CÍRCULO (Radio {tamaño}) ---")

        radio = tamaño

        for y in range(-radio, radio + 1):
            for x in range(-radio, radio + 1):

                # Fórmula del círculo:
                # x² + y² <= r²
                if x*x + y*y <= radio*radio:
                    print("#", end=" ")
                else:
                    print(" ", end=" ")
            print()

    # =====================================
    # PENTÁGONO
    # =====================================
    elif opcion == "5":
        print("\n--- PENTÁGONO ---")

        # Parte superior (techo)
        espacios = tamaño

        for i in range(1, tamaño + 1):
            print(" " * espacios, end="")
            for j in range(i * 2 - 1):
                print("#", end=" ")
            print()
            espacios -= 1

        # Parte inferior (base)
        for i in range(tamaño):
            print(" " * 2, end="")
            for j in range(tamaño * 2):
                print("#", end=" ")
            print()

    # =====================================
    # OPCIÓN INVÁLIDA
    # =====================================
    else:
        print("Opción no válida.")
