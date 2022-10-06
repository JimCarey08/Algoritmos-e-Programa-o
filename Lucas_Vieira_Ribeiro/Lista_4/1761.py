# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

valorTotal =0;
item=-1;
while item!=0:
    item = float(input(''))
    valorTotal+=item
valorRecebido = float(input(''))
troco= valorRecebido-valorTotal;

print('Total da compra: R$%.2f'%(valorTotal))
print('Valor pago: R$%.2f'%(valorRecebido))
print('Troco: R$%.2f' %(troco))
