nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2)/ 2
if media >= 9.0 or media == 10.0 :
    print("Suas notas foram de {} e {}, sua media foi de {} conceito é A você foi APROVADO".format(nota1, nota2, media))

elif media >= 7.5 or media == 9.0:
    print("Suas notas foram de {} e {}, sua media foi de {} conceito é B você foi APROVADO".format(nota1, nota2, media))

elif media >= 6.0 or media == 7.5:
    print("Suas notas foram de {} e {}, sua media foi de {} conceito é C você foi APROVADO ".format(nota1, nota2, media))

elif media >= 4.0 or media == 6.0:
    print("Suas notas foram de {} e {}, sua media foi de {} conceito é D  você foi REPROVADO".format(nota1, nota2, media))

elif media >= 4.0 or media == 0.0:
    print("Suas notas foram de {} e {}, sua media foi de {} conceito é E você foi REPROVADO ".format(nota1, nota2, media))
