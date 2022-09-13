from re import M


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

matriz = [[2,3,5,1],\
          [9,2,6,7],\
          [3,6,2,9]]
          
poeUmNaDiagonalPrincipalNaLinha(1,matriz)
print(matriz)
print (haZeroNaDiagonal(matriz))

diagonal_principal=[]
for lin in matriz:
    for i in range(0, len(lin)-1):
        if i == matriz.index(lin):
            diagonal_principal.append(lin[i])
        print(diagonal_principal)