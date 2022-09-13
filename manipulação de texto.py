#fatiamento de texto.
#string se conta do 0 até n caractéres.
frase = input("curso em video python")
print(frase[3:10])
#ele inclui o 3 e ignora o 10

print(frase[3])

print(frase[9:21:2])
#ele vai pular de 2 em 2

print(frase[:5])
#o : fala q ele vai começar do 1° caracter até o 5.
#o inverso tbm pode ser feito.

print(frase[9::3])
# vai do 9 e vai até o final só que pulando de 3 em 3, mesmo esquema do terceiro exemplo só q sem um final de string específico definido.

# análise de string: len
#len vai ler o tamanho 
# frase.count("o") ele vai contar qunatos o tem no texto.
print(len(frase))
print(frase.count('o'))
print(frase.count('o',0,13)) # ele conta do caracter 0 até o 13.
print(frase.find('deo'))
print(frase.replace('python', 'android'))
#frase.upper() é pra deixar maiúsculo. frase.lower()  frase.capitalize() só o primeiro caractere da string fica maiuscula e deixa todo o resto fica minúsculo.

#frase.striP() remove espaços inuteis da string.
