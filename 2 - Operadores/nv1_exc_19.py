# (19°) Calcule a média de três notas e verifique se o aluno foi aprovado (média ≥ 7).

nota1 = float(input("Digite sua primeira nota: "))
nota2 = float(input("Digite sua segunda nota: "))
nota3 = float(input("Digite sua terceira nota: "))

media = (nota3 + nota2 + nota1) / 3

media = round(media, 2)

if media >= 7:
    print(f"Você está aprovado, sua média final foi: {media}")
else:
    print(f"Você está reprovado, sua média final foi: {media}")