# OPERACIONES BÁSICAS 

def sumar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print("Resultado:", a + b)


def restar():
    a = float(input("Ingrese el primer valor: "))
    b = float(input("Ingrese el segundo valor: "))
    print("Resultado:", a - b)


def multiplicar():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo número: "))
    print("Resultado:", a * b)


def dividir():
    a = float(input("Ingrese el primer número: "))
    b = float(input("Ingrese el segundo numero: "))
    
    if b == 0:
        print("Error: No se puede dividir entre cero")
    else:
        print("Resultado:", a / b)


#  FACTORIAL 

def factorial_calculo(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial_calculo(n - 1)


def factorial():
    n = int(input("Ingrese un número: "))
    
    if n < 0:
        print("Error: El número debe ser positivo")
    else:
        print("Resultado:", factorial_calculo(n))


#  POTENCIA 

def potencia_calculo(base, exp):
    if exp == 0:
        return 1
    return base * potencia_calculo(base, exp - 1)


def potencia():
    base = float(input("Ingrese la base: "))
    exp = int(input("Ingrese el exponente: "))
    
    print("Resultado:", potencia_calculo(base, exp))


#  MENÚ PRINCIPAL

def mostrar_menu():
    print("""
 ═══════════════════════════
║      CALCULADORA PRO      ║
║═══════════════════════════║
║ 1. Sumar                  ║
║═══════════════════════════║                      
║ 2. Restar                 ║    
║═══════════════════════════║
║ 3. Multiplicar            ║
║═══════════════════════════║
║ 4. Dividir                ║
║═══════════════════════════║
║ 5. Factorial              ║
║═══════════════════════════║
║ 6. Potencia               ║
║═══════════════════════════║
║ 7. Salir                  ║ 
 ═══════════════════════════
""")


def calculadora():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            sumar()
        elif opcion == "2":
            restar()
        elif opcion == "3":
            multiplicar()
        elif opcion == "4":
            dividir()
        elif opcion == "5":
            factorial()
        elif opcion == "6":
            potencia()
        elif opcion == "7":
            print("Saliendo de la calculadora...")
            break
        else:
            print("Opción inválida")

        input("\nPresione Enter para continuar...")


# EJECUCIÓN 

calculadora()