#https://www.beecrowd.com.br/judge/pt/problems/view/1009
NomeDoVendedor = input("")
SalarioFixo = float(input())
TotalVendas = float(input())

Total= SalarioFixo + (TotalVendas * 0.15) 

print("TOTAL = R$ %.2f" %(Total))