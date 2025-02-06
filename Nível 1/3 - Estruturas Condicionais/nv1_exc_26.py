# (26°) Peça um dia da semana (1 a 7) e exiba o nome correspondente.

dict = {
    '1' : 'Segunda',
    '2' : 'Terça',
    '3' : 'Quarta',
    '4' : 'Quinta',
    '5' : 'Sexta',
    '6' : 'Sábado',
    '7' : 'Domingo'
}

dia = input("Digite um dia da semana entre 1 e 7: ")

print(f'O dia correspondente é: {dict[dia]}')