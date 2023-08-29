# Entrada de dados do usuário.
idade = int(input("digite a sua idade: "))

if (idade <= 12):
    print("Você é criança !!")
elif (idade <= 17):
    print("Você é adolescente !!")
elif(idade <= 59):
    print("Você é adulto !!")
else:
    print("Você é legendário !!")    