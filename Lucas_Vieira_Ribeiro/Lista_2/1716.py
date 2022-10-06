# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

plano = input()
salarioAtual = float(input())

aumentoA = 1.10
aumentoB = 1.15
aumentoC = 1.20

if plano=="A":
    print("Novo salário: R$%.2f"%(salarioAtual*aumentoA))
elif plano=="B":
    print("Novo salário: R$%.2f"%(salarioAtual*aumentoB))
elif plano=="C":
    print("Novo salário: R$%.2f"%(salarioAtual*aumentoC))
    