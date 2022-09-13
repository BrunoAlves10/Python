#1 lb (libra) equivale a 0,454 kg.
#imprimir uma tabela q vai de 1 a 100 libras, de 5 em 5 libras , iniciando de 1 até 5, 10,15, 20... 100.
'''
valor = 1
while valor <=100:
    print("O valor é {}".format(valor))
    valor = valor + 1
print("Programa encerrado.")
'''
print("\tLibra é 1 q equivale a 0.454")
libra = 5
kg = 0.454
while libra <=100:
    print(f"{libra}      {libra*kg} ")
    libra = libra + 5
print("Programa acabou e ta certo.\n\n\n\n\n")

'''
RESOLUÇÃO DA PROFESSORA.
 Exercício 1 - Tabela converter libra em quilogramas
print(' <<< CONVERSOR (lb) --> (kg) >>>')
print('='*33)
print('\tLibra | Quilograma')
print('='*33)
#imprimir a 1a linha
print('\t  1   |    0.45')
k = 5
while k <=100:
    print(f'\t{k:3}   |   {k*0.454:5.2f}')
    k=k+5
print('='*33)
'''