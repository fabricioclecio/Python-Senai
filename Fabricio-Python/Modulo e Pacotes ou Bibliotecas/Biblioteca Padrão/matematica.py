# importa o módulo.
import math

# Ângulo simulado.
x = math.pi / 4

# Exibe o seno, cosseno e a tangente.
print(f"O seno é: {math.sin(x)}")
print(f"O cosseno é: {math.cos(x)}")
print(f"A tangente é: {math.tan(x)}")

# Eleva um número por outro.
x = 10
y = 2

# Exibe os números elevados.
print(f"{x} elevado a {y} é: {math.pow(x, y)}")

# Exibe a raiz quadrada.
print(f"A raiz quadrada de {x} é: {math.sqrt(x)}")

# Números que será arredondado.
z = 99.87598475987

# Exibe o número arredondado e truncado.
print(f"O número escolhido é: {z}")
print(f"O número arredondado para cima é: {math.ceil(z)}")
print(f"O número arredondado para baixo é: {math.floor(z)}")
print(f"O número Truncado é: {math.trunc(z)}")