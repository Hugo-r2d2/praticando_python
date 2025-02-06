# (37°) Peça um número e exiba todos os números pares de 1 até ele.

n = int(input("Digite um número: "))

for i in range(1, n + 1):
    if i % 2 == 0:
        print(i)