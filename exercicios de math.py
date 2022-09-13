#crie um programa q leia um numero real e mostre na tela a sua porção inteira
#ex: 6.10 inteiro é 6
import math
import random
numero = float(input("digite um valor:"))

#o trunc corta a parte inteira de um número.

print(" o valor digitado foi {} e a sua porção inteira é {}".format(numero, math.trunc(numero)))
print(" ou da fazer usando o próprio python que fica {}".format(int(numero)))


print("\n--------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n\n programa q veja o comprimento do cateto oposto e do cateto adjacente de um triangulo, calcule o comprimento da hipotenusa.\n\n\n")


catetoadja = float(input("Qual o cateto adjacente?"))
catetoop = float(input("Qual o cateto oposto?"))
hipotenusa = (catetoop ** 2 + catetoadja ** 2) ** (1/2)
print(" a hipotenusa vai medir {}".format(hipotenusa))
print("ou")
hipo = math.hypot(catetoop, catetoadja)
print("A hipotenusa vai medir {:.2f}".format(hipo))



print("\n--------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n\n ex 3: faça um programa que leia um ângulo qualquer e mostre o seu seno, cosseno e tangente. \n\n\n")
#o math usa angulo em radianos
angulo = float(input("Qual o valor do seu ângulo?"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print ("o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.".format(seno, cosseno, tangente))


print("\n--------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n\n exercício 3: um professor quer sortear um de seus quatro alunos, tem q ler o nome delas e escrever o escolhido.\n\n\n")

nome1 = input("Qual o nome do primeiro aluno?")
nome2 = input("Qual o nome do segundo aluno?")
nome3 = input("Qual o nome do terceiro aluno?")
nome4 = input("Qual o nome do quarto aluno?")
lista = [nome1, nome2, nome3, nome4]
#uma lista se abre com []

sorteado = random.choice(lista)
print("O aluno escolhido para fazer a tarefa do professor é {}".format(sorteado))


print("\n--------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n\n exercício 4: o professor quer um programa que sortea a ordem de apresentação de trabalhos dos alunos. crie um programa que leia nome dos quatro alunos da questão passada e mostre a ordem sorteada\n\n\n")
#shuffle significa embaralhar
random.shuffle(lista)
print("A ordem de apresentação será:")
print(lista)


print("\n--------------------------------------------------------------------------------------------------------------------------------------\n")
print("\n\n\n faça um programa em python que abra e reproduza o áudio de um arquivo mp3\n\n\n")

