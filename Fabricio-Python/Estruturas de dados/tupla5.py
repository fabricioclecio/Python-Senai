# Alternativa ou gambiarra para altera as tuplas (Não é uma boa prática).
# Cria um tupla vazia.
numeros = ()

# Laço de repetição de criação da tupla.
for item in range(5):

    # Permite a entradda de dados do usuário.
    item = int(input("Digite um número: "))

    # Faz o incremento do valor na tupla.
    numeros += (item,)

# Exibe a tupla completa.
print(numeros)

# Exibe a tupla completa.
print(type(numeros))
