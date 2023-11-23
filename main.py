import random
pontos_seus = 0
pontos_deles = 0
while(True):
  numero_atual = random.randint(1,100)
  print(f"O número atual é {numero_atual}.")
  proximo_numero = random.randint(1,100)
  escolha = input("O próximo número será maior ou menor? ")
  print(f"O próximo número é {proximo_numero}.")
  if escolha == "maior" and proximo_numero > numero_atual:
    print('Você acertou! :3')
    pontos_seus = pontos_seus + 1
  elif escolha == "menor" and proximo_numero < numero_atual:
    print('Você acertou! ^^')
    pontos_seus = pontos_seus + 1
  else:
    print('Você errou...')
    pontos_deles = pontos_deles + 1
  print(f'Você {pontos_seus} VS Compiuter {pontos_deles}')