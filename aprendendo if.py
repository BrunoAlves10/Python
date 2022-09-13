print("hello world")

n1 = int(input("Digite o número 1: "))

n2 = int(input("Digite o número 2: "))

if n1 > n2:
    print (f"caso 1 \n O número 1 digitado é maior que o número 2::: {n1} > {n2}")
elif n1 < n2:
    print (f"caso 2 \n O número 2 digitado é maior que o número 1::: {n2} < {n1}")
elif n1 == n2:
    print (f"caso 3 \n Os dois números são iguais::: {n1} = {n2}")