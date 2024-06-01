def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
print(f"El MCD de {numero1} y {numero2} es {mcd(numero1, numero2)}")
