

    #Faça um algoritmo que solicite o ano que o usuário nasceu, depois disso, faça o programa descrever se o usuário fará ou já fez 18 anos neste ano.

    ano_nascimento = int(input("Em que ano você nasceu? "))


ano_nascimento = int(input("Digite o ano em que você nasceu: "))

from datetime import datetime
ano_atual = datetime.now().year


idade = ano_atual - ano_nascimento
if idade == 18:
    print("Você faz 18 anos neste ano!")
elif idade > 18:
    print("Você já fez 18 anos.")
else:
    print("Você ainda não tem 18 anos.")