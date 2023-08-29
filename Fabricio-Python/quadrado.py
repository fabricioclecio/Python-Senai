# Declaração da função.
def quadrado_numero(numero = 0):

    #Tenta capturar a operação.
    try:
        #Eleva o número ao quadrado e retorna o resultado
        resultado = numero ** 2
        return resultado
    
    # captura a Exceção
    except ValueError:
        return print("O número informado é inválido !!")

    except Exception:
        return print("Ocorreu uma falha inesperada !!")

# Entrada de dados do usuário.
numero = int(input("Digite um número: "))

# Exibe o resultado.

