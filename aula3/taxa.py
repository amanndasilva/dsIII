valor = float(input("Informe o valor da prestação: "))
taxa = float(input("Informe a taxa mensal: "))
tempo = float(input("Informe a quantidades de meses atrasados: "))
prestacao = valor + (valor * (taxa / 100) * tempo)

print("O valor a ser pago e de: ", prestacao)