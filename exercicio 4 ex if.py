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