# (40°) Peça um número ao usuário e exiba seu fatorial.

n = int(input("Digite um número: "))

f = 1

for i in range(1, n + 1):
    f *= i
print(f)