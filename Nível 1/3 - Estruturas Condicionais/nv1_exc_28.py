# (28°) Pergunte a idade do usuário e informe a categoria: Criança (0-12), Adolescente (13-17), Adulto (18+).

idade = int(input("Diga sua idade: "))

if idade in range(0, 13):  
    print("Categoria - Criança")
elif idade in range(13, 18):
    print("Categoria - Adolescente")
else:  
    print("Categoria - Adulto")
   