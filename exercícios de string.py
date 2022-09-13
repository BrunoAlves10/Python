strin = "A areia marcada pelas ondas do mar, que transbordava  e seguia com espumas amarradas ao vento, em singela brancura, refletia a luz vibrante de uma tarde de outono, com um marcante aroma de paz"
print (strin)

print(len(strin)) #quantos caracteres tem

#range gera uma série numérica, muito usado com for loop.


list(range(5))
print (str.lower(strin))

#split separa palavras dentro de uma string


#str.split(strin)

resultado = len(strin.split())
print( "existem " + str(resultado) + " palavras\n\n\n")

bucket_list = strin
bucketresultado = len(bucket_list.split(' ', 3))

print(bucket_list.split(' ', 3))

print("\n\n\ntem " + str(resultado) + " palavras.")
