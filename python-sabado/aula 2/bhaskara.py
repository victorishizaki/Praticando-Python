print("Iremos calcular a fórmula de Bhaskara:")
print("")

print("Digite o valor de A: ")
a = float(input("A: "))
print("")

print("Digite o valor de B: ")
b = float(input("B: "))
print("")

print("Digite o valor de C: ")
c = float(input("C: "))
print("")

delta = b**2 - 4*a*c
print("Delta: ", delta)
print("")

bhaskaraX1 = (-b + delta ** (1 / 2)) / (2 * a)

bhaskaraX2 = (-b - delta ** (1 / 2)) / (2 * a)

print("x1: ", bhaskaraX1, ";", "x2: ", bhaskaraX2)
print("")

print("Fim do programa")