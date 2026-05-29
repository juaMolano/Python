import os 
def limpiar_pantalla():
    os,system('cls' if os.name == 'nt' else 'clear')

    def dibujar_torres(torres, n):
        #dibuja el estado actual de las torres
        limpiar_pantalla()
        print("\n"+"=="*15)
        print("torre de hanoi".center(45))
        print("=="*15+"\n")


        # Ancho maximo de la torre
        ancho_columna = n * 2 + 3

        #dibujar desde arriba hacia abajo
        for i in range(n - 1, -1, -1):
            fila=""
            for poste in ['A','B','C']:
                if i <len(torres[poste]):
                    tamaño_disco = torres[poste][i]
                    #crea el dibujo del disco [==]
                    disco_str="[" + "=" *((tamaño_disco * 2) -1) +"]"
                    #centrar el disco en la columna
                    fila += disco_str.center(ancho_columna)
                else:
                    #si no hay disco, dibuja una columna vacia
                    fila += "|".center(ancho_columna)
                print(fila)
        #dibujar la base de las torres
        print("-" * (ancho_columna * 3))
        print("A".center(ancho_columna)+"B".center(ancho_columna)+"C".center(ancho_columna))
    def jugar_hanoi():
    torres =