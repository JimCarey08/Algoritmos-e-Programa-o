# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

tipoCliente = int(input())
valorCompra = float(input())

if tipoCliente==1:
    print("Valor total a ser pago: R$%.2f"%(valorCompra))
elif tipoCliente==2:
    print("Valor total a ser pago: R$%.2f"%(valorCompra*0.87))
elif tipoCliente==3:
    print("Valor total a ser pago: R$%.2f"%(valorCompra*0.93))
else:
    print("OPÇÃO INVÁLIDA!")
    