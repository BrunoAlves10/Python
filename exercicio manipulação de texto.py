#programa que le o nome completo e mostra td com letra maiuscula, minuscula, qunatas letras(sem espaço) quantas letras no primeiro nome.
nome = input("digite o seu nome completo: ").strip()#pra tirar os espaços do inicio q a pessoa coloca sem querer.
print("analisando os seus dados...")
print("O seu nome em letra maiúscula é {}".format(nome.upper()))
print("seu nome em letra minúscula é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome))) #assim ele conta o espaço.
print("Seu nome tem ao todo {} letras".format(len(nome) - nome.count(' ')))

separa = nome.split()
print("seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))

nome = (input("Digite o seu nome completo: ")).strip()
nomee = nome.split()
print("O seu primeiro nome é {}".format(nomee[0]))
print("Seu último nome é {}".format(nomee[len(nome)-1]))