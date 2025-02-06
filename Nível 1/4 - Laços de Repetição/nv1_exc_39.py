# (39°) Gere os primeiros 10 números da sequência de Fibonacci.

a, b = 0, 1

cont = 0

while cont != 10:
    print(a)
    a, b = b, a + b
    cont += 1