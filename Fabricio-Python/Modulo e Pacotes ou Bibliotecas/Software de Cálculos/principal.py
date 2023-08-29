# Importação do módulo.
from recursos import calculadora

# Recupera os dados foenecidos pelo usuário.
x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))

# Menu de opções a serem selecionadas.
print("Operações Disponíveis: ")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

# Recupera a escolha do usuário.
escolha = input("Digite a opção desejada: ")

# Define a operação a ser realizada.
match escolha:
    case '1':
        resultado = calculadora.soma(x,y)
    case '2':
        resultado = calculadora.subtrai(x,y)
    case '3':
        resultado = calculadora.multiplica(x,y)
    case '4':
        resultado = calculadora.divide(x,y)
    case _:
        print("Opção inválida !!!")
        exit ()

# Exibe o resultado da operação escolhida.
print(f"O resultado da operação é: {resultado}")
        