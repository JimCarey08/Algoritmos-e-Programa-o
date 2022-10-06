#https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713
valorrecebidohora = float(input())
numerodehoras = float(input())

salariobruto = valorrecebidohora * numerodehoras
valorimposto = salariobruto * 0.11
valorinss = salariobruto * 0.08
valorsindicato = salariobruto * 0.05
salarioliquido = salariobruto * 0.76