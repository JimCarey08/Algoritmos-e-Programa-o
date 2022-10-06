# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

numerosInformados = int(input())
contador = 1 
acumlador = 0
if numerosInformados<=0:
    print("Informe uma quantidade > 0!");
else:
    while contador<=numerosInformados:
        numero = float(input())
        acumlador+=numero
        contador+=1 
    print("Soma dos números informados: %.2f" %(acumlador))