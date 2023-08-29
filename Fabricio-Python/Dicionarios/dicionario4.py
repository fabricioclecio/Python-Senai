# Função que exibe as informações de um dicionário.
def exibir (modelo, ano):
    print("Veículos a Venda: ")
    print(f"Modelo : {modelo}")
    print(f"Ano : {ano}")

# Dicionário de carro.
carro = {
    'modelo': "Fusca",
    'ano': "1973"
}

# Chama a função e desempacota o dicionário.
exibir(**carro)

print(type(carro))
print(carro)