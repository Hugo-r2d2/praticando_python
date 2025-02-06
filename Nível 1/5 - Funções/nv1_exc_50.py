# (50°) Faça uma função que conta quantas vogais existem em uma palavra.

def contar_vogais(palavra):
    vogais = "aeiouAEIOU"

    contador = sum(1 for letra in palavra if letra in vogais)
    return contador

palavra = input("Digite uma palavra: ")
print(f"Quantidade de vogais em '{palavra}' é: {contar_vogais(palavra)}")
