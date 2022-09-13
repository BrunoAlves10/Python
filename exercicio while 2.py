'''
Fazer um programa que leia um número indeterminado de números inteiros representando a idade de uma pessoa. 
A repetição da entrada de dados deve ser interrompida quando for digitado ZERO para a idade. Calcular e imprimir a idade média do conjunto de idades lidos.              
'''
'''
idadegeral = 0
idade = int(input("Qual a idade da pessoa?"))

while idade >= 0:
    if idade > 0:
        idade = int(input("Qual a idade da pessoa?"))
    idadegeral = idade + idade
    if idade == 0:
        print("Programa encerrado")
        break
    else:
        media = idade/idadegeral
print("Programa encerrado e a média de pessoas foi: {}".format(media))
'''

print('-'*40)
print('\n CALCULO DA IDADE MÉDIA DE UM CONJUNTO DE IDADES LIDAS\n')
print('-'*40)
soma_idades = 0
total_lido = 0
idade = 1
print("<< Digite as Idades (zero para parar) >>")
while idade != 0:
    idade = int(input('Idade: '))
    if idade == 0: 
        break
soma_idades+=idade
total_lido+=1
print(f'\n Idade média: {soma_idades/total_lido:.1f}')