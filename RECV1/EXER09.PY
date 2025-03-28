 #Faça um programa que solicite uma mensagem qualquer para o usuário e exiba esta mensagem com todas as letras em maiúsculo.

mensagem = input("Digite uma mensagem: ")

print(mensagem.upper())

idade = input("Digite a sua idade: ")

if idade.isdigit():
    print(f"Você tem {idade} anos.")
else:
    print("Você digitou uma idade inválida.")