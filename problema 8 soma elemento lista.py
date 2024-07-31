'''def coleta_numero (quantidade_entrada_valores):
    lista_completa=[0]*quantidade
    for atribuir in range(quantidade_entrada_valores):
        numero = int(input("digite o valor"))
        lista_completa[atribuir]=numero
    return(lista_completa)'''
'''
def soma_lista (lista_a_somar,quantidade_lista):
    resultado_soma=0
    for n in range(quantidade_lista):
        resultado_soma += lista_a_somar [n]
    return(resultado_soma)
'''
def soma_lista (lista_a_somar):
    resultado_soma=0
    for elemento_lista in lista_a_somar:
        resultado_soma += elemento_lista
    return(resultado_soma)



def coleta_numero():
    lista =[]
    enlace = True
    while enlace == True:
        lista.append(int (input("digite o valor da lista")))
        enlace = input("gostaria de digitar")
    return(lista)


'''
quantidade_str = input("digite quantos valores quer somar")
quantidade = int(quantidade_str)
#colecao=[0]*quantidade
'''
#for atribuir in range(quantidade):
#    numero = int(input("digite o valor"))
 #   colecao[atribuir]=numero
#colecao = coleta_numero(quantidade)
colecao = coleta_numero()
soma=0
#soma=soma_lista (colecao, quantidade)
soma=soma_lista (colecao)
#for constante in range(quantidade):
 #   variavel = int (colecao[constante])
  #  soma += variavel
    
print("a soma dos valores eh",soma)
    
#main()
