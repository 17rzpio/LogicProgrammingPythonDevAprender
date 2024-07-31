'''
def salario(valor_mensal, valor_horas, qntd_horas):
    return(valor_mensal+valor_horas*qntd_horas)

def main ():
    input_valor_mensal = int(input ("qual o valor mensal fixo do salario"))
    input_valor_horas = int(input("quanto vale a hora"))
    input_qntd_horas = int(input("quantas horas trabalhadas no mes"))
    print(salario(input_valor_mensal,input_valor_horas,input_qntd_horas))
main()
'''
def salario(valor_mensal, qntd_horas):
    return(valor_mensal/qntd_horas)

input_valor_mensal = int(input ("qual o valor mensal do salario"))
input_qntd_horas = int(input("quantas horas trabalhadas no mes"))
print(salario(input_valor_mensal,input_qntd_horas))
