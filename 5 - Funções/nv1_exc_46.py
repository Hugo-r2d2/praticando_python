# (46°) Faça uma função que calcula o fatorial de um número.

def fatorial(n):
    f = 1
    for i in range(1, n + 1):
        f *= i
    print(f"O fatorial é: {f}")

n = int(input("Digite um número: "))
fatorial(n)