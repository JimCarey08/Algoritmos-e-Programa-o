#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761
valorTeste = 3
valorTotal = 0 
while valorTeste!=0:
    valorTeste = float(input(""))
    valorTotal += valorTeste
valorPago = float(input(""))
troco = valorPago - valorTotal

print("Total da compra: R$ %.2f" %(valorTotal))
print("Valor pago: R$ %.2f" %(valorPago))
print("Troco: R$ %.2f" %(troco)) 