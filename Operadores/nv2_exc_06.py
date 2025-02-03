# (6°) Peça para o usuário inserir duas palavras e verifique se são iguais.

p1 = input("Digite uma palavra: ")
p2 = input("Digite uma palavra: ")

igual = p1 == p2

if igual == True:
    print("As duas palavras são iguais")
else:
    print("As duas palavras são diferentes")