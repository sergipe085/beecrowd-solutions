def main():
    notes = input().split(" ")

    n1 = float(notes[0])
    n2 = float(notes[1])
    n3 = float(notes[2])
    n4 = float(notes[3])

    avarage = (n1 * 2 + n2 * 3 + n3 * 4 + n4) / 10

    print(f"Media: {avarage:.1f}")

    if (avarage < 5.0):
        print("Aluno reprovado.")
        return

    if (avarage >= 7.0):
        print("Aluno aprovado.")
        return

    print("Aluno em exame.")

    exam = float(input())

    print(f"Nota do exame: {exam}")

    avarage = (avarage + exam) / 2

    if (avarage >= 5.0):
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")

    print(f"Media final: {avarage:.1f}")

main()