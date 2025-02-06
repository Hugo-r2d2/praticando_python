# (48°) Crie uma função que recebe um número e verifica se ele é primo.

def primo(n):
    if n < 2:
        print("Não é número primo")
    else:
        primo = True
        for i in range(2, int(n**0.5) + 1): 
            if n % i == 0:
                primo = False
                break  

        if primo:
            print("Número primo")
        else:
            print("Não é número primo")
            
n = int(input("Digite um número: "))
primo(n)