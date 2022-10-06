#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715
cliente = 1
funcionario = 2
clientespremium = 3

tipoDeCliente = int(input()) 
valordacompra = float(input()) 

if tipoDeCliente == funcionario:
    valorFinal = valordacompra * 0.87
    print("Valor total a ser pago: R$%.2f"%(valorFinal))
elif tipoDeCliente == clientespremium:
    valorFinal = valordacompra * 0.93
    print("Valor total a ser pago: R$%.2f"%(valorFinal))
elif tipoDeCliente == cliente:
    valorFinal = valordacompra 
    print("Valor total a ser pago: R$%.2f"%(valorFinal))
else:
    print("OPÇÃO INVÁLIDA!")