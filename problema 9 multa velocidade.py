velocidade = int(input("Qual a velocidade: "))
if velocidade < 80:
    print("Nao levou multa")
elif velocidade < 90:
    print("levou multa leve")
elif velocidade < 100:
    print("levou multa grave")
else:
    print("levou multa gravissima")
