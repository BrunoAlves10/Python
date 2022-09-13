print("exercícios if 2\n\n\n")
print("Desenvolver um algoritmo para ler um número “x” e calcular e imprimir o valor de “y” de acordo com as condições abaixo")
print(" y = x , se x < 1;")
print("y = 0 , se x = 1;")
print("y = x² , se x > 1;\n\n")

X = float(input("Qual o valor X? "))

if X < 1:
    print("O valor de y é {}".format(X))
elif X == 1:
    print("O valor de y é 0")
elif X > 1:
    x2 = X ** 2
    print("O valor de y é {}".format(x2))

print("\n\n\n_____________________________________")
print("Exercício de if 3\n\n\n")
print("Ler 3 valores X, Y, Z representando os comprimentos dos lados de um triângulo. Verificar se eles podem ser os comprimentos dos lados de um triangulo e, se forem, verificar se é um triângulo equilátero, isósceles ou escaleno. Se eles não formarem um triângulo, imprimir uma mensagem.")

x = float(input("Qual o valor do lado x? "))
y = float(input("Qual o valor do lado y? "))
z = float(input("Qual o valor do lado z? "))

soma= x + y + z

if x == y == z:
    print("Esse é um triângulo equilatero, poís possui os 3 lados iguais.")
elif x==y or y==z or x==z:
    print("Esse é um triângulo isósceles, poís tem o compromento de 2 lados iguais.")
elif x != y != z:
    print("Esse é um triângulo escaleno, poís tem o comprimento de 3 lados diferentes.")
elif x >= soma or y >= soma or z >= soma:
    print("Esse triângulo não existe, poís o comprimento de algum lado desse triângulo é maior que a soma de todos os seus lados.")

print("Exercícios de if 4 \n\n\n")

x = input("Qual o valor de x? ")
y = input("Qual o valor de y? ")

if x < y:
    z = input("Qual o valor de z? ")
    if z >= x and z <= y:
        print("Z pertence ao intervalo")
    elif z == y:
        print("Z pertence ao intervalo e é o limite superior")
    elif z == x:
        print("O z pertence ao intervalo é o limite inferior")
    elif z > y:
        print("Z está fora do intervalo e é maior que o limite superior")
    elif z < x:
        print("Z está fora do intervalo e é menor que o limite inferior")
elif x >= y:
    print("O x tem que ser menor que o y")