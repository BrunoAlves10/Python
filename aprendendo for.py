'''
#vai printar oi 6 vezes
for i in range(0, 6,):
    print ("oi")
print("fim")

for i in range(6, 0, -1): #ele vai tirar 1 de 6 até 0
    print("oi")
print("Fim")

n= int(input("digite um número"))
for i in range(0, n):
    print(i)
print("fim")
'''
'''
s=0
for i in range(0,4):
    n = int(input("digite um valor: "))
    s = s + n  # ou s += n
print("O somátório de todos os valores foi {}".format(s))
'''

# atividade 1
'''
for i in range(10, 0, -1):
    print(i)
print("a contagem acabou")
'''

####################      WHILE #################

#se vc sabe o limite do numero vc usa o for ou o while, se vc não sabe o limite vc usa o while
#isso ocorre pq pra usar for vc tem q ter bem determinado o ponto inicial e o ponto final do range.
'''
for c in range (1,10):
    print(c)
print("fim")
'''
'''
c = 1 
while c < 10:
    print(c)
    c = c + 1 #quando ele volta ele soma + 1 no c
print("Fim")
'''
'''
r = "s"
while r =="s":
    n = int(input("digite um valor: "))
    r = str(input("Quer Continuar? [s/n]"))
print("fim")
'''
'''
n = 1
par = impar = 0
while n != 0:
    n = int(input("digite um valor: "))
    if n % 2 == 0:           # % resto da divisão por 2.
        par += 1
    else:
        impar +=1
print("voce digitou {} números pares e {} números ímpares".format(par, impar))
'''


n = int(input("digite um número: "))
lista = []
