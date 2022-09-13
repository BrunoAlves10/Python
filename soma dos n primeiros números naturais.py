#soma dos n primeiros números naturais
from re import S


n = int(input("Valor de n é: "))

k = 1
s = 0

while k <=n:
    s= s + k
    k = k + 1
print("o resultado da soma é:{}".format(s))