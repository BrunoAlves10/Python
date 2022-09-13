#daria para multiplicar por 7 só, não precisa criar uma variavel pra fazer essa conta.
velocidade = int(input("Qual a velocidade que o carro estava? "))
km = 7
print("Se ele passar de 80km/h você está multado e a cada km acima do limite a multa aumenta 7 reais.\n\n\n")
if velocidade >=80:
    print("Você estava acima de 80 km/h e será multado em:")
    multa = (velocidade - 80) * km
    print("{} reais".format(multa))
else:
    print("Você está dentro do limite de velocidade, andando a {}km/h.".format(velocidade))