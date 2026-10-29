historico = []  

print("----- Ponto de Venda -----")
print("Digite 0 no valor da compra para encerrar.\n")

while True:
    valor = float(input("Valor da compra (R$): "))

    if valor == 0:
        break

    if valor < 0:
        print("Aviso: o valor não pode ser negativo. Tente novamente.\n")
        continue

    idade = int(input("Idade do cliente: "))

    if idade <= 1:
        print("Aviso: a idade não pode ser negativa. Tente novamente.\n")
        continue

    valor_final = valor

    if idade >= 65:
        valor_final = round(valor_final * 0.80, 2)

    if valor_final > 100:
        valor_final = round(valor_final * 0.90, 2)

    valor_final = round(valor_final, 2)

    print(f"Valor final: R$ {valor_final:.2f}\n")

    historico.append([valor, idade, valor_final])

quantidade = len(historico)
total_bruto = 0
total_final = 0

for compra in historico:
    total_bruto += compra[0]
    total_final += compra[2]

total_descontos = total_bruto - total_final

print("\n----- RESUMO DO DIA -----")
print(f"Quantidade de compras: {quantidade}")
print(f"Total bruto:           R$ {total_bruto:.2f}")
print(f"Total de descontos:    R$ {total_descontos:.2f}")
print(f"Total final:           R$ {total_final:.2f}")
