# (4°) Solicite um número ao usuário e verifique se ele é positivo, negativo ou zero.

n = int(input("Digite um número: "))

if n < 0:
    print(f"{n} é um valor negativo")
elif n > 0:
    print(f"{n} é um valor positivo")
else:
    print(f"{n} é nulo(0)")