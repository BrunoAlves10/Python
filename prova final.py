numeroeleitores = float(input("O número de eleitores é: "))
totalEleitores = numeroeleitores
voto = 0
joao = 0
maria = 0
branco = 0
nullo = 0
total = 0
senha = 0

while numeroeleitores != 0:
    print("========================================")
    print("Código   I   Candidato")
    print("11       I   João")
    print("45       I   Maria")
    print(" 0       I  Voto em Branco")
    print("Qualquer dígito além desses é voto nulo")
    print("========================================")

    voto = int(input("Digite o seu voto: "))
    
    valor = False
    if voto == 1234:
            
        while valor == False:
            senha = int(input("Digite a senha: "))
            if senha != 3571:
                print("Senha incorreta... Tente novamente.")
                continue
                
            print(" Votação encerrada pelo presidente")
            valor = True
            break
    
    if valor == True:
        break
    
    numeroeleitores = numeroeleitores -1
    total = total + 1
    
    if voto == 11:
        joao = joao + 1
    elif voto == 45:
        maria = maria + 1
    elif voto == 0:
        branco = branco + 1
    elif voto != 0 or voto != 45 or voto != 11:
        nullo = nullo + 1
    
        print ("Seu voto foi: {}\n".format(voto))

porcentagem = (total * 100.0) / totalEleitores
print("Total de votos esperados: {} {}%".format(totalEleitores, porcentagem))

print("=================\nTotalização de votos\n=================\n")
print("João: {}".format(joao))
print("Maria: {}".format(maria))
print("Branco: {}".format(branco))
print("Nullo: {}".format(nullo))