#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759
anoInicial = 2005
salarioInicial = 1000
anoAtual = 2005
anoFinal = int(input())
taxaDeAumento = 1.015
salarioAtual = 1000
if anoFinal<=2005:
    print("O ano informado deverá ser > 2005!") 
else: 
    while anoAtual<anoFinal:
        anoAtual+=1
        salarioAtual*=taxaDeAumento
        taxaDeAumento+=0.01 
    print("Salário atual: R$%.2f" %(salarioAtual))