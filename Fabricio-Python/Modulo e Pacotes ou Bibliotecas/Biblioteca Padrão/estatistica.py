# Importação do Módulo.
import statistics

# Simula dados de temperatura do ar.
dados = [15.54, 20.89, 17.50, 13.34, 26.56, 31.04]

# Exibe a média, desvio padrão e a variância dos dados.
print(f"Informações Estatísticas da Temperatura do Ar:")
print(f"Média: {statistics.mean(dados)}")
print(f"Desvio Padrão é: {statistics.stdev(dados)}")
print(f"Variância é: {statistics.variance(dados)}")

# Exibe a média, desvio padrão e a variância dos dados com 2 casas decimais.
print(f"Média: {statistics.mean(dados):.2f}")
print(f"Desvio Padrão é: {statistics.stdev(dados):.2f}")
print(f"Variância é: {statistics.variance(dados):.2f}")