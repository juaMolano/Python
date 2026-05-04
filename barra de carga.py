import time   # Librería que permite manejar pausas de tiempo

print("=" * 50)
print("SIMULADOR DE CARGA DE ARCHIVOS".center(50))
print("=" * 50)

# while True crea un ciclo infinito.
# El programa seguirá funcionando hasta que el usuario decida salir.
while True:


    # Solicita el tamaño total del archivo en MB
    tamaño = float(input("Ingrese el tamaño del archivo (MB): "))

    # Solicita el tiempo total que durará la carga
    tiempo_total = float(input("Ingrese el tiempo de carga (segundos): "))

    print("=" * 50)

    # La f delante del texto permite insertar variables dentro del print
    print(f"Iniciando subida de {tamaño} MB...")

    print("=" * 50)

   

    # La barra tendrá 20 espacios en total
    pasos = 20

    # Calcula cuánto tiempo debe esperar entre cada avance
    # Ejemplo: si son 10 segundos y 20 pasos:
    # 10 / 20 = 0.5 segundos por avance
    intervalo = tiempo_total / pasos


    
    # PROCESO DE CARGA
  

    # range(pasos + 1) va desde 0 hasta 20
    # Se usa +1 para que también llegue al 100%
    for i in range(pasos + 1):

        # Calcula el porcentaje actual
        porcentaje = int((i / pasos) * 100)

        # Parte llena de la barra con #
        llenos = "#" * i

        # Parte vacía de la barra con -
        vacios = "-" * (pasos - i)

        # Une todo en una sola variable
        barra = f"[{llenos}{vacios}] {porcentaje}%"

        # \r hace que se escriba en la misma línea
        # end="" evita salto de línea
        print("\r" + barra, end="")

        # Hace una pausa para simular la carga real
        time.sleep(intervalo)


    print(f"\n\n¡Archivo de {tamaño} MB subido con éxito!")
    print("=" * 50)


    repetir = input("¿Desea cargar otro archivo? (si/no): ").strip().lower()

    # strip() elimina espacios
    # lower() convierte a minúsculas

    # Si escribe algo diferente de "si", termina el programa
    if repetir != "si":
        print("=" * 50)
        print("Programa finalizado. ¡Hasta luego!".center(50))
        print("=" * 50)
        break   # Rompe el while y finaliza