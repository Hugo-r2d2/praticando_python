# (43°) Escreva uma função que recebe três números e retorna a média deles.

def media(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    print(f"A média dos três números é: {media}")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

media(n1, n2, n3)