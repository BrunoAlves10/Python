print("Programa de trocos\n===============================\n")

valor=int(input("Qual o valor da sua compra?"))
pagamento=int(input("Qual o valor que você pagou?"))

resto= pagamento-valor

print("\n Você pagou {} em uma compra que custou {} reais, restando {} reais para receber de troco\n\n".format(pagamento, valor, resto))

vinte= resto / 20
restovinte= resto % 20

dez= restovinte / 10
restodez= resto % 10

cinco = restodez / 5
restocinco = resto % 5

um = restocinco / 1

print ("\nO troco será de:\n====================\n {} notas de 20 reais.\n {} notas de 10 reais.\n {} notas de 5 reais.\n {} moedas de 1 real".format(int(vinte), int(dez), int(cinco), int(um)))