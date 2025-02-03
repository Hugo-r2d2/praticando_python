# (23°) Peça três números e exiba o maior deles.

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Difite um número: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} é o maior valor!")
elif n2 > n1 and n2 > n3:
    print(f"{n2} é o maior valor!")
else:
    print(f"{n3} é o maior valor!")