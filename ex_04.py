dados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

total = sum(dados.values())
for k, v in dados.items():
    print(f"{k} = {((v/total)*100):.2f}% do total.")