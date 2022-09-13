#jogo da adivinhação.
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 10)
#print("Pensei no número {}".format(computador))
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print('-=-' * 10)
jogador = int(input("Em que número eu pensei? "))
print("processando...")
sleep(2)
if jogador == computador:
    print("Parabéns, você conseguiu pensar no mesmo número que eu.")
else:
    print("Ganhei, eu pensei no número {} e não no número {}".format(computador, jogador))