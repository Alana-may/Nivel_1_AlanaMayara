# Desafio Nível 1 — PDV com Descontos (Python)

## O que o código faz

Este programa simula um PDV (Ponto de Venda) que calcula o valor final de compras aplicando descontos progressivos: um desconto por idade do cliente e um desconto extra por valor da compra. Ele permite registrar várias compras seguidas, guarda cada uma em um histórico e, ao encerrar, mostra um resumo do dia com a quantidade de compras, o total bruto, o total de descontos concedidos e o total final.

## Como ele faz

1. O código pede o **valor da compra** (decimal). Se for `0`, o loop termina.
2. Se o valor for negativo, mostra um aviso e pede novamente (`if` + `continue`).
3. Pede a **idade do cliente** (inteiro). Se for negativa, mostra um aviso e pede novamente.
4. **Regra 1:** se a idade for maior ou igual a 65, aplica 20% de desconto.
5. **Regra 2:** se o valor *já com o desconto de idade* for maior que 100, aplica mais 10% sobre esse valor.
6. Exibe o valor final formatado em reais com duas casas decimais (ex.: `R$ 144.00`).
7. Guarda a compra (valor original, idade e valor final) numa lista com `.append()`.
8. Ao digitar `0`, percorre a lista com um `for`, soma os valores e mostra o resumo do dia.

## Como rodar

```
python pdv.py
```
ou 
```
py pdv.py
```

## Tabela de exemplos (casos de teste)

| #  | Valor (R$) | Idade | Desconto idade | Desconto valor | Valor final esperado |
|----|-----------:|------:|---------------:|---------------:|---------------------:|
| 1  | 50.00      | 30    | 0%             | 0%             | R$ 50.00             |
| 2  | 100.00     | 30    | 0%             | 0%             | R$ 100.00            |
| 3  | 80.00      | 65    | 20%            | 0%             | R$ 64.00             |
| 4  | 100.00     | 70    | 20%            | 0%             | R$ 80.00             |
| 5  | 125.00     | 70    | 20%            | 0%             | R$ 100.00            |
| 6  | 200.00     | 30    | 0%             | 10%            | R$ 180.00            |
| 7  | 101.00     | 30    | 0%             | 10%            | R$ 90.90             |
| 8  | 200.00     | 65    | 20%            | 10%            | R$ 144.00            |
| 9  | 1000.00    | 80    | 20%            | 10%            | R$ 720.00            |
| 10 | 200.00     | 64    | 0%             | 10%            | R$ 180.00            |

### Casos-limite

- **Caso 5** (125.00, idade 70): 125 × 0,8 = 100. Como não é maior que 100, os 10% não se aplicam → R$ 100.00.
- **Caso 10** (200.00, idade 64): sem desconto de idade, só o de valor (10%) → R$ 180.00.
- **Caso 7** (101.00, idade 30): 101 × 0,9 = 90,90 → duas casas decimais.
