#Entrada de dados do usuário.
idade = int(input("Informe a sua idade: "))

#Execução do operador ternário.
# variável     # Condição Verdadeiro        #Condicional.      # Condiçao Falsa.          
resultado = 'Você é maior de idade !!' if idade >= 18 else 'Você é menor de idade !!'

# Exibe o resultado para o usuário.
print(resultado)