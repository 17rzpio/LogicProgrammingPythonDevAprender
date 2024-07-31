def fatorial (numero):
    resultado_fatorial = 1
    auxiliar_calculo = numero
    for quantidade in range(numero):
        resultado_fatorial *= auxiliar_calculo
        auxiliar_calculo -= 1
 
    return(resultado_fatorial)

def main():
    input_numero = int( input("qual o numero que deseja o fatorial"))
    resposta_fatorial = fatorial (input_numero)
    print ("o fatorial eh", resposta_fatorial)

main ()
