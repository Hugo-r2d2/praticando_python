# (45°) Escreva uma função que recebe uma lista e retorna o maior número.

def maior(lista):
    n_maior = lista[0]
    for num in lista:
        if num > n_maior:
            n_maior = num
    print(f"O maior número é: {n_maior}")

numeros = []

for i in range(1, 6):
    n = int(input("Digite um número: "))
    numeros.append(n)

maior(numeros)