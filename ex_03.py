import json
from statistics import mean

with open("dados.json", "r") as f:
    raw_dados = json.load(f)

dados = {
    dado['dia']: dado['valor']
    for dado in raw_dados
    if dado['valor'] != 0}

media = mean(dados.values())
menor_dia = min(dados, key=dados.get)
maior_dia = max(dados, key=dados.get)
qtd_dias_maior_faturamento = sum(v > media for v in dados.values())

print(f"O menor faturamento foi de '{dados[menor_dia]}' no dia {menor_dia}.")
print(f"O maior faturamento foi de '{dados[maior_dia]}' no dia {maior_dia}.")
print(f"A quantidade de dias com faturamento maior que a média foram '{qtd_dias_maior_faturamento}'.")