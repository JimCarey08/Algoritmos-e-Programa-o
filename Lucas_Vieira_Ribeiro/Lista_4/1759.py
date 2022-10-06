# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

salarioInicial = 1000
anoAtual = 2005
taxaAumento = 1.015
salarioAtual = 1000;
anoFinal = int(input(""))

if anoFinal<2006:
    print("O ano informado deverá ser > 2005!")
else:
    while anoAtual<anoFinal:
        anoAtual+=1
        salarioAtual= salarioAtual*taxaAumento
        taxaAumento+=0.01
        
    print("Salário atual: R$%.2f"%(salarioAtual))

    