# Cria uma tupla numérica.
numeros = (1, 2, 3, 4, 5)

# Cria uma tupla de texto (string).
carros = ("Opalão", "Fusca","Brasilia")

# Cria uma tupla sem parenteses.
frutas = "Banana", "Abacaxi", "Morango"

# Converte uma lista em uma tupla.
comidas = ["Lasanha", "Macarrão", "Churrasco"]
tupla = tuple(comidas)

# Verifica se as estruturas realmente são tuplas.
print(type(numeros))
print(type(carros))
print(type(frutas))
print(type(tupla))

# Exibe o elemento da tupla (da esquerda para a direita).
print(carros[1])

# Exibe o elemento da tupla (da direita para esquerda).
print(carros[-1])

# Exibe os elementos contidos no intervalo.
print(numeros[2:4])
