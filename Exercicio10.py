nota1= int(input("Digite a primeira nota do aluno: "))
nota2= int(input("Digite a segunda nota do aluno: "))

media=(nota1 + nota2)/ 2

if media >= 7 :
  print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")