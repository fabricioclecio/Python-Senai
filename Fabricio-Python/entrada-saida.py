# Recebe o nome do usuário.
nome = input("Informe seu nome: ") # Tudo que recebo pelo input é uma String.

# Recebe a idade do usuário.
idade = int(input("Informe sua idade: "))

# Exibe para o usuário sua idade + 10 anos.
print (idade + 10)

#Formatação de strings( F-STRINGS)
#Exemplo de saída sem formatação.
print("Seja bem-vindo", nome, "de", idade, "anos...")

#Exemplo de saída com formatação
print(f"Seja bem-vindo {nome} de {idade} anos...")

#Exemplo de saída com formatação
print()

# Função PRINT com o parâmetro END.
print("Hello", "Wolrd", end="\n !\n")

# Função PRINT com o parâmetro SEP.
print("O", "Python", "é", "legal", sep="-")


