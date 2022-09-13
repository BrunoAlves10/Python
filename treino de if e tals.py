from sys import excepthook

checkerror = True
try:
    while checkerror:
        print("Calculador de notas de alunos.")

        nota1 = float(input("Qual a nota da prova 1 do aluno? "))
        peso1 = float(input("Qual o peso da prova 1? "))
        nota2 = float(input("Qual a nota da prova 2 do aluno? "))
        peso2 = float(input("Qual o peso da prova 2? "))

        notafinal = ((nota1 * peso1) + (nota2 * peso2))

        if notafinal >= 7:
            print("O aluno está aprovado, com a média no boletim de {}".format(notafinal))
        elif notafinal < 7:
            print("O aluno está reprovado, com a média com a nota no boletim de {}".format(notafinal))
        elif notafinal ==10:
            print("O aluno foi aprovado com distinção com a média no boletim de 10")
except:
    print("fLAMENGO MELHOR DO MUNDO.")