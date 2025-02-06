# (49°) Escreva uma função que recebe dois números e retorna o maior.

def maior(n1, n2):
    if n1 > n2:
        print(f"O maior número é: {n1}")
    else:
        print(f"O maior número é: {n2}")
        
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
maior(n1, n2)