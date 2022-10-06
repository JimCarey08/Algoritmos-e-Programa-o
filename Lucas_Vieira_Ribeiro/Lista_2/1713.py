#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

valorHora = float(input())
horasTrabalhadas = float(input())

salarioBruto = valorHora* horasTrabalhadas
impostoRenda = salarioBruto * 0.11
INSS = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto * 0.76

print("Salário bruto: R$%.2f\nImposto: R$%.2f\nINSS: R$%.2f\nSindicato: R$%.2f\nLíquido: R$%.2f" %(salarioBruto,impostoRenda,INSS,sindicato,salarioLiquido))
