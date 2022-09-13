#Faça um programa que dadas as medidas de uma sala em metro (comprimento e largura), bem como o preço do metro quadrado do carpete, informe o custo total para forrar o piso da sala

comprimento=float(input("Qual o comprimento do chão?\n"))

largura=float(input("Qual a largura do chão?\n"))

total= comprimento*largura

print(f"A área do chão é de: {total}\n\n")

print("===========================================")

preco=float(input("Qual o preço do metro quadrado de carpete?\n"))

forrar=total*preco

print(f"O preço para forrar o chão é de: {forrar}.")