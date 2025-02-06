# (44°) Crie uma função que verifica se um número é par ou ímpar.

def par_impar(n):
    if n % 2 == 0: 
        print(f"O número {n} é par")
    else:
        print(f"O número {n} é ímpar")    

n = int(input("Digite um número: "))
par_impar(n)