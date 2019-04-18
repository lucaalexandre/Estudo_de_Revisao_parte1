lado1 = int(input("Digite o primeiro valor do lado do triângulo: "))
lado2 = int(input("Digite o segundo valor do lado do triângulo: "))
lado3 = int(input("Digite o terceiro valor do lado do triângulo: "))

soma = lado1 + lado2

if soma > lado3 :
    print("Esse não é considerado um triângulo")
elif lado1 == lado2 == lado3:
    print("Esse é considerado como um triângulo Equilátero")
elif lado2 == lado3 or lado2 == lado1 or lado1 == lado3 :
    print("Esse é considerado como um triângulo Isósceles")
elif lado1 != lado2 != lado3:
    print("Esse é considerado como um triângulo Escaleno")