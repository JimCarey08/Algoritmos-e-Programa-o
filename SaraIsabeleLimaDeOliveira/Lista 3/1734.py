#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734
valorN = int(input("")) 
contador = 1
res= 1
while contador<=valorN:
    res*=contador
    contador+=1
print("%i! = %i"%(valorN,res))