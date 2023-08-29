# Cria um dicionário vázio.
carros = {}

# Adiciona um par de chave-valor no dicionário.
carros ["Fusca"] = "Raridade"

# Adicion ou atualiza um par de chave-valor no diacionario.
carros.update({"Ferrari": "Esportivo"})

# Desempacota os valores do dicionário em variáveis.
carro1 = carros ["Fusca"]
categoria2 = carros["Ferrari"]

# Exibe dicionários.
print(carros)

# Exibe o dicionário de forma iterável.
for chave, valor in carros.items():
    print(f"O carro {chave} é da categoria {valor} ...")

