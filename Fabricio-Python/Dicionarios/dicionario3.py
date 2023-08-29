# dicionário de carros.
carros = {
    "Fusca": 1990,
    "Brasilia": 1975,
    "Gol": 2000,
    "Impala": 1978,
    "Opala": 1997
}

# Verifica se existe uma chave no dicionário.
if("Impala" in carros):
    print("O carro Impala existe no dicionário...")
else:
    print("O carro Impala não existe no dicionário...")

# Verifica se existe uma chave no dicionário. 
if (2000 in carros.values()):
    print("Existem carros do ano 2000 no dicionário...")
else:
    print("Não existem carros do ano 2000 no dicionário...")    

# Remove do dicionário um par de chave-valor.
del carros ["Brasilia"]
eliminado = carros.pop("Impala")

# Exibe o carro que foi eliminado.
print(f"{eliminado} foi eliminado do dicionário !!!")


