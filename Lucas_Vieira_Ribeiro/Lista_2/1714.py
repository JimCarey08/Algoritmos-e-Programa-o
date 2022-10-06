# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

precoProduto = float(input())

if precoProduto<20:
    valorDeVenda = precoProduto * 1.45
else:
    valorDeVenda = precoProduto * 1.3;

print("Valor de venda: R$%.2f" %(valorDeVenda))
