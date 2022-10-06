# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

salarioMinimo = 1192.40
valorHoraExtra = 10
nome= input()
horasExtras = float(input())
salarioHoraExtra = valorHoraExtra*horasExtras
salarioBruto = 3*salarioMinimo + salarioHoraExtra

if salarioBruto>2000:
    descontoINSS = salarioBruto*0.12;
else:
    descontoINSS= salarioBruto*0.05;
    
if salarioBruto>2500:
    descontoImposto = salarioBruto*0.2
else:
    descontoImposto = 0;
    
salarioLiquido = salarioBruto - (descontoImposto+descontoINSS)

print("Nome: %s" %(nome));
print('Salário bruto: R$%.2f' %(salarioBruto))
print('Salário líquido: R$%.2f' %(salarioLiquido))
