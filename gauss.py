from pickle import TRUE


def divisao (a,b):
    if a==0 and b==0:
        return "indeterminado"
    elif b==0:
        return "infinito"
    else:
        return a/b
        
def divDumVetorPorOutro (x,y):
    ret=[]
    for i in range(len(x)-1): ret.append(divisao(x[i],y[i]))
    return ret
    
print(divDumVetorPorOutro([1,0,2,0],[0,0,4,2]))


# função auxiliar  recursivo que, de fato, gera as permutacoes
# NÃO USE DIRETAMENTE ESTA FUNÇÃO; USE A FUNÇÃO permutacoes
# recebe uma lista com os valores a serem permutados (linha),
# uma lista com os itens na permutação sendo gerada (perm) e
# uma lista com as permutações geradas (perms) 
def permuta (linha, perm, perms):
    if linha==[]:
        perms.append(perm)
    else:
        for lin in range(len(linha)):
            permuta(linha[0:lin]+linha[lin+1:len(linha)],perm+[linha[lin]],perms)

# função principal para gerar permutações;
# USA A FUNÇÃO permuta, QUE NÃO DEVE SER USADA DIRETAMENTE;
# recebe uma lista com os valores a serem permutados (linha)
# retorna as permutações geradas
def permutacoes (linha):
    perms=[]
    permuta(linha,[],perms)
    return perms
    
#print(permutacoes([0,1,2,3]))

def haZeroNaDiagonal (m):
    qtdDeZeros=0
    posicao=0
    while posicao<len(m):
        if m[posicao][posicao]==0: qtdDeZeros+=1
        posicao+=1
    return qtdDeZeros>0
    
def poeUmNaDiagonalPrincipalNaLinha (lin,m):
    divisor=m[lin][lin]
    col=0
    while col<=len(m):
        m[lin][col]/=divisor
        col+=1
    
#--------------------------------------------------------------------#    



matriz = [[2,3,5,1],\
          [9,2,6,7],\
          [3,6,2,9]]




