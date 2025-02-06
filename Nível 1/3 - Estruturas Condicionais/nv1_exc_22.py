# (22°) Crie um programa que verifica se um usuário pode votar (idade ≥ 16).

idade = int(input("Informe sua idade: "))

if idade >= 16:
    print("Parabéns, você tem idade o suficiente para votar!")
else:
    print("Infelizmente você é muito novo para que possa votar!")