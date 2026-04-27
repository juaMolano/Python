
import random, time
print("=*50")
print("bienvenido al simulador de la ruleta rusa")
print("=*50")

input("poner bala en el tambor (presiona enter)")
bala= random.randint(1, 6)
print("girar el tambor...")
time.sleep(0.5)

disparos = 0 #variable para contar disparos realizados

while True:
    input("girar el tambor (presiona enter)")
    disparos += 1
    recamara = random.randint(1, 6)

    input("apuntar y disparar (precione enter)")
    
    time.sleep(1)

    if recamara == bala:
        print("!bang! has perdido. la bala estaba en la recamara " \
              "número", bala)
    else:
        print("sobreviviste al disparo.")
        print("disparos ", disparos)
    if disparos == 5:
        print("!felicidades! has ganado al sobrevivir 5 intentos")
        break
    print("="*50)
    print("finalizaste")
    print("=*50")