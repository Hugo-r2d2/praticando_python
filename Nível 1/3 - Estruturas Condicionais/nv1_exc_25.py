# (25°) Peça um número e informe se ele é múltiplo de 3 e de 5 ao mesmo tempo.

n = int(input("Digite um número: "))

if n%3 == 0 and n%5 == 0: 
    print(f"O número '{n}' é divisível por 3 e por 5")
elif n%3 == 0: 
    print(f"O número '{n}' é múltiplo de 3 e não de 5")
elif n%5 == 0:
    print(f"O número '{n}' é múltiplo de 5 e não de 3")
else:
    print(f"O número não é múltiplo nem de 5 e nem de 3") 
