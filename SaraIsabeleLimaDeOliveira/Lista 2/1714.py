#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714
precoproduto = float(input())

valor1 = 0.45
valor2 = 0.30 

if precoproduto < 20.00:
    lucro = precoproduto * valor1
    valordavenda = lucro + precoproduto 
else: 
    lucro = precoproduto * valor2
    valordavenda = lucro + precoproduto 
    
print("Valor de venda: R$%.2f" %(valordavenda)) 
