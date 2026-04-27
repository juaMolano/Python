import random

import time


def pausa(segundos: float) -> None:
    time.sleep(segundos)


def juego_ruleta() -> None:
    print("=== Sistema de azar: Revólver de 6 recámaras ===")
    pausa(0.7)

    # Inicialización: recámara con bala aleatoria entre 1 y 6
    bala = random.randint(1, 6)

    intentos_supervividos = 0
    MAX_INTENTOS_VICTORIA = 5

    print("Cargando el revólver...")
    pausa(1.0)
    print("Listo. Si sobrevives 5 intentos, ganas.\n")

    # Bucle de juego: el usuario interactúa manualmente
    while True:
        print(f"Intento {intentos_supervividos + 1} de {MAX_INTENTOS_VICTORIA}")

        input("Pulsa ENTER para GIRAR el tambor...")
        print("Girando...")
        pausa(0.8)

        # Mecánica de azar: en cada turno, recámara al frente aleatoria
        recamara = random.randint(1, 6)
        print("Tambor detenido.")
        pausa(0.5)

        input("Pulsa ENTER para DISPARAR...")
        print("Apuntando...")
        pausa(0.7)
        print("¡Click!")
        pausa(0.5)

        # Condición de derrota
        if recamara == bala:
            print("\nBANG. La recámara coincidió con la bala. PERDISTE.")
            return  # termina inmediatamente

        # Si no pierde, sobrevivió el intento
        intentos_supervividos += 1
        print("Te salvaste.\n")
        pausa(0.6)

        # Condición de victoria: sobrevivir 5 intentos
        if intentos_supervividos == MAX_INTENTOS_VICTORIA:
            print("¡GANASTE! Sobreviviste 5 intentos. (El sexto sería fatal).")
            return


if __name__ == "__main__":
    juego_ruleta()