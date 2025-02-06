# (29°) Peça uma nota e classifique: A (9-10), B (7-8.9), C (5-6.9), D (<5).

nota = float(input("Digite uma nota: "))

if nota >= 9 and nota <= 10:
    print("Nota A")
elif nota >= 7 and nota <= 8.9:
    print("Nota B")
elif nota >= 5 and nota <= 6.9:
    print("Nota C")
elif nota < 5:
    print("Nota D")