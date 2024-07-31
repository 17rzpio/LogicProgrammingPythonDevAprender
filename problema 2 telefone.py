





def pegar_telefone ():
    sensor_acessar_celular = input ("valor do sensor")
    if sensor_acessar_celular:
        acesso_celular = True
    else:
        acesso_celular = False
    return (acesso_celular)

def trava_telefone (senha):
    senha_programada = 2222
    if senha != 0:
        if senha == senha_programada:
            destravado = True
        else:
            print ("senha incorreta")
            destravado = False
    else:
        destravado = True
    return (destravado)

def sinal_operadora ():
    sensor_sinal_operadora = bool (input ("valor do sensor"))
    if sensor_sinal_operadora:
        sinal = True
    else:
        sinal = False
    return (sinal)

def navegar_telefone ():
    flag_acesso_teclado = input ("valor do sensor")
    if flag_acesso_teclado:
        acesso_teclado = True
    else:
        acesso_teclado = False
    return (acesso_teclado)

def telefonar ():
    botao_ligacao = input ("valor do sensor")
    if botao_ligacao:
        chamada_celular = True
    else:
        chamada_celular = False
    return (chamada_celular)

def ligacao (tempo):
    timer_ligacao_celular = input ("valor do sensor")
    if timer_ligacao_celular == tempo:
        efetivar_ligacao = True
    else:
        efetivar_ligacao = False
    return (efetivar_ligacao)


def main():

    ligar_passo_um = False
    ligar_passo_dois = False
    ligar_passo_tres = False
    ligar_passo_quatro = False
    ligar_passo_seis= False

    while not ligar_passo_um:
        ligar_passo_um = pegar_telefone ()

    while not ligar_passo_dois:
        senha = int(input("digite a senha para destravar, se nao tem senha digite zero"))
        ligar_passo_dois = trava_telefone (senha)

    while not ligar_passo_tres:
        ligar_passo_tres = sinal_operadora ()
        print ("o sinal da operadora eh", ligar_passo_tres)

    while not ligar_passo_quatro:        
        ligar_passo_quatro = navegar_telefone ()     

    #ligar_passo_cinco:        
    numero_discar = input ("digite o telefone a discar")

    while not ligar_passo_seis:
        ligar_passo_seis = telefonar ()


    #ligar_passo_sete:
    timer = int (input("configure quanto tempo aguarde para fazer a chamada"))
    ligar_passo_sete = ligacao (timer)
    if ligar_passo_sete:
        print ("conversar pelo telefone com o amigo")
    else:
        mensagem = input ("digite a mensagem pois o amigo não atendeu a ligacao")
main()
