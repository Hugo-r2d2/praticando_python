# (47°) Escreva uma função que inverte uma string.

def invert(texto):
    invert_text = texto[::-1]
    print(f"O texto invertido é: {invert_text}")

texto = input("Digite uma palavra: ")
invert(texto)