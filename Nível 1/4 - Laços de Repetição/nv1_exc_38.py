# (38°) Leia números até o usuário digitar 0 e mostre a soma total.

n = 1
soma = 0

while n != 0:
    n = int(input("Digite um número: "))
    soma = soma + n
print(f'A soma de todos os números digitados é: {soma}')