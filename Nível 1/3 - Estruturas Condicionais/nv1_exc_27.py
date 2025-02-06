# (27°) Crie um sistema simples de login que verifica nome de usuário e senha.
import os

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela    

print("======================================")
print("=========== Crie sua conta ===========")

usuário = input("Digite um nome para login: ")
senha = input("Digite uma senha para login: ")

print("======================================")

login_usuario = None
login_senha = None

os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela    

while login_usuario != usuário or login_senha != senha:    
    print("======================================")
    print("=========== Faça seu login ===========")
    login_usuario = input("Digite seu usuário: ")
    login_senha = input("Digite sua senha: ")

    os.system('cls' if os.name == 'nt' else 'clear') # Limpa a tela    

    if login_usuario != usuário or login_senha != senha:
        print("\n!! Usuário ou senha incorretos. Tente novamente. !!")

    

print("======================================")

print("Cadastro e Login feito com sucesso!")
