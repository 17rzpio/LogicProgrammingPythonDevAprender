quantidade_agua = int(input ("quantos litros quer"))
tanque_um = int (input("digite quanto cabe no tanque 1"))
tanque_dois = int (input("digite quanto cabe no tanque 2"))
if tanque_um > tanque_dois:
    print("primeiro encha de agua no tanque 1 depois passe para tanque 2 e o que restar no tanque 2 eh a quantidade de agua")
else:
    print("primeiro encha de agua no tanque 2 depois passe para tanque 1 e o que restar no tanque 1 eh a quantidade de agua")



quantidade_agua = int (input("digite quantos litros ate 5 quer: "))
if quantidade_agua == 5:
    print ("para conseguir", quantidade_agua, " basta encher um tanque de cinco litro")
if quantidade_agua == 4:
    print ("para conseguir", quantidade_agua, "voce precisa encher um tanque de 5 litro, depois no de 1 litro depositar a agua e o que sobrar estara no de 5 litro e sera",quantidade_agua )
if quantidade_agua == 3:
    print ("para conseguir", quantidade_agua, "voce precisa encher um tanque de 5 litro, depois no de 2 litro depositar a agua e o que sobrar estara no de 5 litro e sera",quantidade_agua )
if quantidade_agua == 2:
    print ("para conseguir", quantidade_agua, "voce precisa encher um tanque de 5 litro, depois no de 3 litro depositar a agua e o que sobrar estara no de 5 litro e sera",quantidade_agua )
if quantidade_agua == 1:
    print ("para conseguir", quantidade_agua, "voce precisa encher um tanque de 5 litro, depois no de 4 litro depositar a agua e o que sobrar estara no de 5 litro e sera",quantidade_agua )


tanque_um = int (input("digite quanto cabe no tanque 1"))
tanque_dois = int (input("digite quanto cabe no tanque 2"))
if tanque_um > tanque_dois:
    print("a quantidade de agua que se tem eh",tanque_um - tanque_dois)
else:
    print("a quantidade de agua que se tem eh",tanque_dois - tanque_um)
