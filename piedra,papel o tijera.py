import random
import time

print("=" * 50)
print("BIENVENIDO A PIEDRA, PAPEL O TIJERA".center(50))
print("=" * 50)

opciones = ["piedra", "papel", "tijera"]

while True:
	print("Escribe piedra, papel o tijera (o 'salir' para terminar).")
	usuario = input("Tu elección: ").strip().lower()

	# Salir del juego
	if usuario == "salir":
		print("=" * 50)
		print("Finalizaste. ¡Hasta luego!".center(50))
		print("=" * 50)
		break

	# Validación de entrada
	if usuario not in opciones:
		print("Opción no válida. Intenta de nuevo.")
		continue

	print("La computadora está eligiendo...")
	time.sleep(0.7)

	pc = random.choice(opciones)
    # la f se usa para llamar a las variables dentro del print y mostrar su valor.
	print(f"Tú: {usuario}")
	print(f"PC: {pc}")

	# 1) Empate
	if usuario == pc:
		print("Resultado: EMPATE")
	# 2) Victoria del usuario
	elif (
		(usuario == "piedra" and pc == "tijera") or
		(usuario == "tijera" and pc == "papel") or
		(usuario == "papel" and pc == "piedra")
	):
		print("Resultado: ¡GANASTE!")
	# 3) Derrota del usuario (gana la PC)
	else:
		print("Resultado: PERDISTE")

	print("=" * 50)