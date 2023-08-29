# Função de soma de dois números.
def soma(x=0, y=0):
    return(x + y)

# Função de subtração de dois números.
def subtrai(x=0, y=0):
    return (x - y)

# Função de multiplicação de dois números.
def multiplica(x=0, y=0):
    return (x * y)

# Função de divisão de dois números.
def divide(x=1, y=1):

    # Verifica se o divisor é zero.
    if (y != 0):
        return (x/y)
    else:
        print("O divisor não pode ser zero !!!")
