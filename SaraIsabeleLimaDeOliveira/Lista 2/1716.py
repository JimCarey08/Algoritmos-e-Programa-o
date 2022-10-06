#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716
funcionarioA = 0.10
funcionarioB = 0.15
funcionarioC = 0.20

tipoDeFuncionario = input()
salarioInicial = float(input())
if tipoDeFuncionario =="A":
    salarioFinal = salarioInicial * 1.10
elif tipoDeFuncionario =="B":
    salarioFinal = salarioInicial * 1.15
elif tipoDeFuncionario =="C": 
    salarioFinal = salarioInicial * 1.20 

print("Novo salário: R$%.2f" %(salarioFinal))