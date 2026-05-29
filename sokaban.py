# sokoban.py

import os

# =========================
# NIVELES DEL JUEGO
# =========================

niveles = [

    # Nivel 1 (OBLIGATORIO)
    [
        list("#######"),
        list("#     #"),
        list("#  $  #"),
        list("# .@  #"),
        list("#     #"),
        list("#######")
    ],

    # Nivel 2
    [
        list("########"),
        list("#   .  #"),
        list("#  $$  #"),
        list("#   @  #"),
        list("#      #"),
        list("########")
    ],

    # Nivel 3
    [
        list("########"),
        list("#  .   #"),
        list("#  $   #"),
        list("#  $   #"),
        list("#  @   #"),
        list("########")
    ],

    # Nivel 4
    [
        list("#########"),
        list("#   .   #"),
        list("#  $$   #"),
        list("#   @   #"),
        list("#       #"),
        list("#########")
    ],

    # Nivel 5
    [
        list("#########"),
        list("# .   . #"),
        list("# $$ $$ #"),
        list("#   @   #"),
        list("#       #"),
        list("#########")
    ],

    # Nivel 6
    [
        list("##########"),
        list("# .      #"),
        list("# $$     #"),
        list("#   @    #"),
        list("#     .  #"),
        list("##########")
    ],

    # Nivel 7
    [
        list("##########"),
        list("# . .    #"),
        list("# $$ $   #"),
        list("#   @    #"),
        list("#        #"),
        list("##########")
    ],

    # Nivel 8
    [
        list("###########"),
        list("# .     . #"),
        list("# $$$     #"),
        list("#    @    #"),
        list("#         #"),
        list("###########")
    ],

    # Nivel 9
    [
        list("###########"),
        list("# . . .   #"),
        list("# $$$     #"),
        list("#    @    #"),
        list("#         #"),
        list("###########")
    ],

    # Nivel 10
    [
        list("############"),
        list("# .      . #"),
        list("# $$ $$    #"),
        list("#    @     #"),
        list("#          #"),
        list("############")
    ],

    # Nivel 11
    [
        list("############"),
        list("# . . .    #"),
        list("# $$$$$    #"),
        list("#    @     #"),
        list("#          #"),
        list("############")
    ],

    # Nivel 12
    [
        list("#############"),
        list("# . . . .   #"),
        list("# $$$$$$    #"),
        list("#     @     #"),
        list("#           #"),
        list("#############")
    ]
]

# =========================
# FUNCIONES
# =========================

def limpiar_pantalla():
    os.system("cls" if os.name == "nt" else "clear")


def dibujar_mapa(matriz):
    for fila in matriz:
        print("".join(fila))

    print("\nCONTROLES:")
    print("W = Arriba")
    print("A = Izquierda")
    print("S = Abajo")
    print("D = Derecha")
    print("Q = Salir")


def obtener_posicion_jugador(matriz):
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == "@":
                return fila, columna

    return None, None


def es_meta_original(fila, columna):
    return (fila, columna) in metas


def mover(direccion):
    global mapa

    fila, columna = obtener_posicion_jugador(mapa)

    movimientos = {
        "W": (-1, 0),
        "S": (1, 0),
        "A": (0, -1),
        "D": (0, 1)
    }

    if direccion not in movimientos:
        return

    df, dc = movimientos[direccion]

    nueva_fila = fila + df
    nueva_columna = columna + dc

    # Evitar errores fuera de límites
    if nueva_fila < 0 or nueva_columna < 0:
        return

    if nueva_fila >= len(mapa) or nueva_columna >= len(mapa[0]):
        return

    destino = mapa[nueva_fila][nueva_columna]

    # =========================
    # PARED
    # =========================
    if destino == "#":
        return

    # =========================
    # MOVIMIENTO NORMAL
    # =========================
    if destino == " " or destino == ".":

        if es_meta_original(fila, columna):
            mapa[fila][columna] = "."
        else:
            mapa[fila][columna] = " "

        mapa[nueva_fila][nueva_columna] = "@"

    # =========================
    # EMPUJAR CAJA
    # =========================
    elif destino == "$" or destino == "*":

        caja_nueva_fila = nueva_fila + df
        caja_nueva_columna = nueva_columna + dc

        # Evitar errores fuera de límites
        if caja_nueva_fila < 0 or caja_nueva_columna < 0:
            return

        if caja_nueva_fila >= len(mapa):
            return

        if caja_nueva_columna >= len(mapa[0]):
            return

        siguiente = mapa[caja_nueva_fila][caja_nueva_columna]

        # Solo mover si el espacio está libre
        if siguiente == " " or siguiente == ".":

            # Mover caja
            if siguiente == ".":
                mapa[caja_nueva_fila][caja_nueva_columna] = "*"
            else:
                mapa[caja_nueva_fila][caja_nueva_columna] = "$"

            # Restaurar posición anterior de la caja
            if es_meta_original(nueva_fila, nueva_columna):
                mapa[nueva_fila][nueva_columna] = "."
            else:
                mapa[nueva_fila][nueva_columna] = " "

            # Restaurar posición anterior del jugador
            if es_meta_original(fila, columna):
                mapa[fila][columna] = "."
            else:
                mapa[fila][columna] = " "

            # Mover jugador
            mapa[nueva_fila][nueva_columna] = "@"


def nivel_completado():
    for fila in mapa:
        if "$" in fila:
            return False

    return True


# =========================
# INICIO DEL JUEGO
# =========================

print("===== SOKOBAN EN TERMINAL =====")

for numero_nivel in range(len(niveles)):

    mapa = [fila[:] for fila in niveles[numero_nivel]]

    metas = set()

    for f in range(len(mapa)):
        for c in range(len(mapa[f])):
            if mapa[f][c] == ".":
                metas.add((f, c))

    while True:

        limpiar_pantalla()

        print(f"===== NIVEL {numero_nivel + 1} =====\n")

        dibujar_mapa(mapa)

        if nivel_completado():
            print("\n¡Nivel completado!")
            input("Presiona ENTER para continuar...")
            break

        tecla = input("\nMovimiento: ").upper()

        if tecla == "Q":
            print("Juego terminado.")
            exit()

        mover(tecla)

limpiar_pantalla()
print("¡FELICIDADES! COMPLETASTE TODOS LOS NIVELES.")

## Cómo ejecutar el programa

