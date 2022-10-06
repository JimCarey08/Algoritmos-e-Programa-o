# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

idadeN=0;
pesoN=0;
somaIdades=0;
sobrepeso=0;

while (idadeN<4) and (pesoN<4):
    somaIdades+=float(input(""))
    idadeN+=1
    if (float(input(''))>90):
        sobrepeso+=1
    pesoN+=1
print("Qtd pessoas > 90 Kg: %i" %(sobrepeso))
print("Idade média: %.2f" %(somaIdades/idadeN))
