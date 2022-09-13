from tkinter import *
from tkinker import Tk
#0.15 o custo do km
def imc():
    dia = int(input("Quantos dias o seu carro foi alugado?"))
    KM = float(input("Quantos KM vc rodou com o carro?"))

    pago= (dia * 60) + (KM * 0.15)
    print ("o total a pagar é RS:{:.2f}".format(pago))
    exit()


janela = Tk()

janela.title("Programa De Calculo De IMC e Gestão De Calorias")



texto_orientação2 = Label(janela, text="Clique aqui")
texto_orientação2.grid(column=0, row=1)

botão = Button(janela, text="Iniciar programa de cálculo de 1+1",command=imc)
botão.grid(column=0, row=1)
texto_imc = Label(janela, text="")
texto_imc.grid(column=0, row=2)

janela.mainloop()
