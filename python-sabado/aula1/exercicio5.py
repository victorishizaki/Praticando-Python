n1= int(input("digite o numero 1"))
n2= int(input("digite outro numero2"))

for y in range(n1, n2 + 1):
    if y % 2 == 0:
        print("o numero é par: ", y)