print("Questão 5 tarefa if")
from math import sqrt
# ax²+bx+c
#sqrt
# O programa ta certo, só tem que corrigir esse j.
a = float(input("Qual o valor de A? "))
b = float(input("Qual o valor de B? "))
c = float(input("Qual o valor de C? "))

delta = b**2 - 4 * a * c
print("O delta é {}\n".format(delta))

delta = sqrt(delta)
print("raiz é {}".format(delta))

baska1 = ((-b) + sqrt( ( b**2 ) -4 * a * c) ) / 2 * a
baska2 = ((b) - sqrt( (b ** 2) -4 * a * c )) / 2 * a
print("As Raizes dessa equação são: {} e {}".format(baska1, baska2))