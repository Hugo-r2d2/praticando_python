 # (30°) Verifique se um número digitado é primo.

n = int(input("Digite um número: "))

if n < 2:  # Números menores que 2 não são primos
    print("Não é número primo")
else:
    primo = True  # Suponhamos que seja primo
    for i in range(2, int(n**0.5) + 1):  # Verifica divisibilidade até a raiz quadrada de n
        if n % i == 0:
            primo = False
            break  # Se encontrou um divisor, pode parar

    if primo:
        print("Número primo")
    else:
        print("Não é número primo")
