print ("programa que calcula o consumo de gasolina de um veículo.\n\n")

distancia=float(input("Qual a distancia que você percorreu?"))
combustivel=float(input("Quanto combustivel foi gasto?"))

consumo= distancia/combustivel
print (f"A média de consumo do carro é de {consumo}/km. Ou seja, com 1 litro, o seu carro percorre {consumo} quilometros.")