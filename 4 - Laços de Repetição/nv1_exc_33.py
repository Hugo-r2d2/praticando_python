# (33°) Peça um número e exiba sua tabuada de 1 a 10.
import os

os.system('cls' if os.name == 'nt' else 'clear')

print("======== TABUADA ========".center(40))
n = int(input("Digite um número:".center(40)))

contador = 1
os.system('cls' if os.name == 'nt' else 'clear')

print("=========================".center(40), "=========================".center(40), "=========================".center(40), "=========================".center(40))
print("========= SOMA ==========".center(40), "======= Subtração =======".center(40), "===== Multiplicação =====".center(40), "======== Divisão ========".center(40))

while contador <= 10:
    soma = f"{contador} + {n} = {contador + n}"
    subtracao = f"{contador + n} - {n} = {(contador + n)- n}"
    multiplicacao = f"{contador} x {n} = {contador * n}"
    divisao = f"{contador * n} / {n} = {(contador * n) / n}"
    print(soma.center(40), subtracao.center(40), multiplicacao.center(40), divisao.center(40))
    contador += 1


