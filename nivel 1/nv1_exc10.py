# (10°) Peça para o usuário digitar um número e mostre o tipo da variável usando type().

entrada = input("Digite qualquer coisa: ")

try: 
    valor = int(entrada)
    print("Você digitou um númmero inteiro: ", valor)
    print("Tipo: ", type(valor))
except ValueError:
    try:
        valor = float(entrada)
        print("Você digitou um número decimal: ", valor)
        print("Tipo: ", type(valor))
    except ValueError:
        print("Você digitou um valor não numérico: ", entrada)
        print("Tipo: ", type(entrada))