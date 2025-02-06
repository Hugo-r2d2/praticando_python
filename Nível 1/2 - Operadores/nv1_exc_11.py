# (11°) Peça dois números ao usuário e mostre a soma, subtração, multiplicação e divisão.

n1 = int(input("Digite um valor: "))
n2 = int(input("Diigte um valor: "))

soma = n1 + n1

if n1 > n2:
    subtracao = n1 - n2
else:
    subtracao = n2 - n1

multiplicacao = n1 * n2

divisao = n1 / n2

print(f'O valor da soma é: {soma}')
print(f'O valor da subtração é: {subtracao}')
print(f'O valor da multiplicação é: {multiplicacao}')
print(f'O valor da divisão é: {divisao}')