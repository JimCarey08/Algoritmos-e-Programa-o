#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760 
idade1 = int(input(""))
peso1 = float(input(""))
idade2 = int(input(""))
peso2 = float(input(""))
idade3 = int(input(""))
peso3 = float(input(""))
idade4 = int(input(""))
peso4 = float(input(""))
contador = 0 
if peso1 > 90:
    contador = contador + 1 
if peso2 > 90:
    contador = contador + 1 
if peso3 > 90:
    contador = contador + 1 
if peso4 > 90:
    contador = contador + 1 
 
mediaDasIdades = (idade1 + idade2 + idade3 + idade4) /4 
print("Qtd pessoas > 90 Kg: %.i" %(contador)) 
print("Idade média: %.2f" %(mediaDasIdades))