from os import system

dados_moedas = {}

def popular():
    system("cls")
    n = int(input("digite a quantidade de moedas a ser cadastrada(s): "))
    var = 0
    while var < n:
        codigo = str(input("digite o código: "))
        pais = str(input("digite o pais de origem: "))
        ano = int(input("digite o ano de fabrição: "))
        moeda = str(input("digite o nome da moeda: "))
        vf = float(input("digite o valor da face da moeda: "))
        vm = float(input("digite a valor do mercado: "))
        dados_moedas[codigo] = pais,ano,moeda,vf,vm
        var += 1

    menu()

def menu():
    system("cls")

    print(
        "1. Consultar DADOS de Uma Moeda\n"
        "2. Incluir Uma Nova Moeda\n"
        "3. Imprimir TODAS as moedas com um determinado Valor de Venda\n"
        "4. Imprimir TODAS as Moedas no formato de Tabela (*)\n"
        "0. Encerrar Programa\n"
    )
    escolha = int(input("Escolha <0 a 4>: "))

    if escolha == 0:
        print("Programa Finalizado.")
    elif escolha == 1:
        imprime_valor_unico()
    elif escolha == 2:
        popular()
    elif escolha == 3:
        popular()
    elif escolha == 4:
        imprime()

def imprime():
    print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format("Código","Pais","Ano","Moeda","VF","VM"))
    for key,value in dados_moedas.items():
        print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(key,value[0],value[1],value[2],value[3],value[4]))


def imprime_valor_unico():
    system("cls")
    codigo = str(input("digite o código: "))
    system("cls")

    print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format("Código", "Pais", "Ano", "Moeda", "VF", "VM"))
    print("{:>10} {:>10} {:>10} {:>10} {:>10} {:>10}".format(codigo, dados_moedas[codigo][0], dados_moedas[codigo][1], dados_moedas[codigo][2], dados_moedas[codigo][3], dados_moedas[codigo][4]))


popular()