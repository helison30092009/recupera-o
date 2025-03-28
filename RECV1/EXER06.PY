Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

idade = int(input("Digite sua idade: "))

if idade < 11:
    print("Você é uma Criança.")
elif idade < 17:
    print("Você é um Adolescente.")
elif idade < 60:
    print("Você é um Adulto.")
else:
    print("Você é um Idoso.")