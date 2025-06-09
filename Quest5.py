##Quest-5
nota = float(input("Digite a nota: "))
if 0 <= nota <= 10:
    if nota >= 7:
        print("Aprovado")
    elif nota >= 5:
        print("Recuperação")
    else:
        print("Reprovado")
else:
    print("Nota inválida")