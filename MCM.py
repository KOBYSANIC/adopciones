def mcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mcm(a, b):
    return abs(a * b) // mcd(a, b)

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
print(f"El MCM de {numero1} y {numero2} es {mcm(numero1, numero2)}")