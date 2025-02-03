# (3°) Compare dois números informados pelo usuário e exiba o maior.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))

if n1 > n2:
    print(f"{n1} é maior que {n2}")
elif n2 > n1:
    print(f"{n2} é maior que {n1}")
else:
    print("Números iguais")