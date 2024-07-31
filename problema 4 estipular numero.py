#valor = 5
import random
valor_aleatorio = random.sample(range(1,11),1)
valor = valor_aleatorio [0]


valor_input = 0
while valor != valor_input:
    valor_input = int(input("estipule um numero que não seje diferente"))
    if valor_input > valor:
        print ("valor eh maior")
    elif valor_input < valor:
        print("valor eh menor")
