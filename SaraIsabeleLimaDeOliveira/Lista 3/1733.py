#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733
nomeFuncionario = input("")
horasExtrasTrabalhadas = float(input())

salarioMinimo = 1192.40 
valorHoraExtra = 10.00
valorInss1 = 0.12 
valorInss2 = 0.05
valorImposto = 0.20

salarioHoraExtra = horasExtrasTrabalhadas * 10.00
salarioBruto = 3 * 1192.40 + salarioHoraExtra 
if salarioBruto > 2000 and salarioBruto < 2500:
    salarioLiquido = salarioBruto - (valorInss1 * salarioBruto)
elif salarioBruto > 2500:
    salarioLiquido = salarioBruto - (valorInss1 * salarioBruto) - (valorImposto*salarioBruto)
elif salarioBruto < 2000:
    salarioLiquido = salarioBruto - (valorInss2 * salarioBruto) 
    
print("Nome: %s" %(nomeFuncionario)); 
print("Salário bruto: R$ %.2f" % (salarioBruto)) 
print("Salário líquido: R$ %.2f" % (salarioLiquido)) 