'''
Fazer um programa que faz a leitura consecutiva de N números inteiros x. 
Construir um programa que identifica e imprime o MAIOR e o MENOR número 
entre os números digitados. O valor de N também deve ser digitado e deve 
ser maior ou igual a 10
'''
print('-'*40)
print('\n MAIOR E MENOR ENTRE NUMEROS DIGITADOS\n')
print('-'*40)
print("<< Entrada de Dados >>")
print(' Quantos números serão digitados? (maior do que 10): ')
while True:
    N = int(input('(maior do que 10): '))
    if N>10: 
        print(f'Digite os {N} números:')
        k=1
    while k <= N:
        x = int(input(f'{k}o. : '))
    if k==1:
        maior = menor = x
    else:
        if x > maior: maior = x
        if x < menor: menor = x
        k+=1
    print(f'  Maior = {maior}  Menor = {menor}')