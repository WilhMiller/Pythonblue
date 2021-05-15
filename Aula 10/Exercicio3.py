import random as rd

sorte = rd.randint(1, 10)
num = 0
numero = int(input('Digite um número: '))

while numero != sorte:
    numero = int(input('Digite um número: '))
    if numero != sorte:
      num +=1
    if numero == sorte:
      print(f'Foram necessário {num} tentativas.')
      print('Game Over')
    

