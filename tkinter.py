from tkinter import *

# PROGRAMA DE CALCULAR IMC E CONSUMO CALORICO

# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- VARIABLES
# --------------------------------------------------------------------------------------------------------------------------------------------------------
from os import system
from time import sleep


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- FUNÇÃO EXTRA
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def cleartime():
    system("cls")


def returnmenu():
    system("cls")
    print("Retornado ao menu ...")
    sleep(3)
    menu()


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- FUNÇÃO IMC
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def imc():
    cleartime()
    try:
        peso = int(input("Qual o seu PESO em quilogramas? "))
        altura = float(input("Qual a sua ALTURA em metros? "))

        resultado = peso / (altura ** 2)
        cleartime()
        if resultado <= 18.5:
            print(f"Seu IMC é {int(resultado)} e você está abaixo do peso")
        elif resultado <= 25.0:
            print(f"Seu IMC é {int(resultado)} e você está com o peso normal")
        elif resultado <= 30:
            print(f"Seu IMC é {int(resultado)} e você está com sobre peso")
        elif resultado <= 35:
            print(f"Seu IMC é {int(resultado)} e você está com Obesidade Grau 1")
        elif resultado <= 40:
            print(f"Seu IMC é {int(resultado)} e você está com Obesiade Grau 2")
        else:
            print(f"Seu IMC é {int(resultado)} e você está com Obesidade Grau 3 ou Mórbida")

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()
    except:
        cleartime()
        print("Digite apenas números!")
        sleep(2)
        imc()


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- FUNÇÃO DE CALORIAS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def caloria():
    cleartime()
    notes = ["Café da Manha", "Café", "Almoço", "Café da Tarde", "Jantar", "Ceia"]
    tabela = []
    print(
        "Escolha o sexo"
        "\nMasculino (M) ou Feminino (F)"
    )
    s = str(input("Digite aqui: ").upper())
    cleartime()

    try:
        idade = int(input("Qual a sua IDADE? "))
        peso = int(input("\nQual o seu PESO (kg)? "))
    except:
        cleartime()
        print("Apenas números inteiros!")
        sleep(2)
        caloria()

    if idade < 0 or idade < 0:
        cleartime()
        print("Apenas números postivos!")
        sleep(2)
        caloria()

    gastom1 = (59.512 * peso) - 30.4  # 0 a 3 anos
    gastom2 = (22.706 * peso) + 504.3  # 3 a 10 anos
    gastom3 = (17.686 * peso) + 658.2  # 10 a 18 anos
    gastom4 = (15.057 * peso) + 692.2  # 18 a 30 anos
    gastom5 = (11.472 * peso) + 873.1  # 30 a 60 anos
    gastom6 = (11.711 * peso) + 587.7  # maior do que 60 anos

    gastof1 = (58.317 * peso) - 31.1  # 0 a 3 anos
    gastof2 = (20.315 * peso) + 485.9  # 3 a 10 anos
    gastof3 = (13.384 * peso) + 692.6  # 10 a 18 anos
    gastof4 = (14.818 * peso) + 486.6  # 18 a 30 anos
    gastof5 = (8.126 * peso) + 845.6  # 30 a 60 anos
    gastof6 = (9.082 * peso) + 658.5  # maior do que 60 anos

    if 3 > idade >= 0:
        gastocal = gastom1
    elif 10 > idade >= 3:
        gastocal = gastom2
    elif 18 > idade >= 10:
        gastocal = gastom3
    elif 30 > idade >= 18:
        gastocal = gastom4
    elif 60 > idade >= 30:
        gastocal = gastom5
    else:
        gastocal = gastom6

    if 3 > idade >= 0:
        gastocal = gastof1
    elif 10 > idade >= 3:
        gastocal = gastof2
    elif 18 > idade >= 10:
        gastocal = gastof3
    elif 30 > idade >= 18:
        gastocal = gastof4
    elif 60 > idade >= 30:
        gastocal = gastof5
    else:
        gastocal = gastof6

    if s == "M":
        var = 0
        while var < 6:
            cleartime()
            number = int(input(f"Digite o consumo calorico de cada refeição ({notes[var]})\n: "))
            tabela.append(number)
            var += 1

            result = sum(tabela)

        cleartime()
        print(f"O seu consumo total foi de {int(result)} calorias no dia.")

        escolha = str(input(f"\nDeseja checar o seu consumo médio ({int(gastocal)})? (S) | (N)\n").lower())
        cleartime()

        if escolha == "s":
            if result == gastocal:
                print(f"Voce está na média, com {int(result)}")
            elif result > gastocal:
                print(f"Voce está acima da média, com {int(result - gastocal)} calorias a mais.")
            else:
                print(f"Voce está abaixo da média, com {int(gastocal - result)} calorias a menos.")
        else:
            returnmenu()

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()

    if s == "F":
        var = 0
        while var < 6:
            cleartime()
            number = int(input(f"Digite o consumo calorico de cada refeição ({notes[var]})\n: "))
            tabela.append(number)
            var += 1

            result = sum(tabela)

        cleartime()
        print(f"O seu consumo total foi de {int(result)} calorias no dia.")

        escolha = str(input(f"\nDeseja checar o seu consumo médio ({int(gastocal)})? (S) | (N)\n").lower())
        cleartime()

        if escolha == "s":
            if result == gastocal:
                print(f"Voce está na média, com {int(result)}")
            elif result > gastocal:
                print(f"Voce está acima da média, com {int(result - gastocal)} calorias a mais.")
            else:
                print(f"Voce está abaixo da média, com {int(gastocal - result)} calorias a menos.")
        else:
            returnmenu()

        input("\nPressione ENTER para retornar ao menu inicial.")
        returnmenu()

    if s != "M" or s != "F":
        cleartime()
        print("Escolha Masculino (M) ou Feminino (F)")
        sleep(2)
        caloria()


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- FUNÇÃO DE CREDITOS
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def creditos():
    print(
        "Pessoas envolvidas nesse projeto:"
        "\n\nJoão Paulo Toledo de Almeida Arrigo"
        "\nBruno Fontolan Alves"
        "\nEnrico Ribeiro Farina"
        "\nMathues Furlan Ferragut de Oliveira"
        "\nGustavo de Campos Soares"
    )

    input("\nPressione ENTER para retornar ao menu inicial.")
    returnmenu()


# --------------------------------------------------------------------------------------------------------------------------------------------------------
# -- MENU
# --------------------------------------------------------------------------------------------------------------------------------------------------------
def menu():
    cleartime()
    print(
        "=========================="
        "\n= 1- Calculo de IMC      ="
        "\n= 2- Calculo de Calorias ="
        "\n= 3- Creditos            ="
        "\n=========================="
    )

menu()








#row = linha
#janela2 = Tk()

janela = Tk()

janela.title("Programa De Calculo De IMC e Gestão De Calorias")

texto_orientação = Label(janela, text="Clique na função que você deseja executar")
texto_orientação.grid(column=0, row=0)

texto_orientação2 = Label(janela, text="Clique aqui")
texto_orientação2.grid(column=1, row=1)

botão = Button(janela, text="Iniciar programa de cálculo de 1+1",command=imc)
botão.grid(column=0, row=1)
texto_imc = Label(janela, text="")
texto_imc.grid(column=0, row=2)

janela.mainloop()