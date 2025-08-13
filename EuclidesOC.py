x = int(input("Insira o primeiro número: "))
y = int(input("Insira o segundo número: "))
Maior = max (x, y)
Menor = min (x, y) 

while Maior != Menor:
    z = Maior - Menor
    if z <= Menor:
        Maior = Menor
        Menor = z
    else:
        Maior = z

print (Maior) 