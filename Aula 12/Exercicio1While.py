#01 - Crie um programa que leia dois valores e mostre um menu na tela:
   # [ 1 ] somar
   # [ 2 ] multiplicar
   # [ 3 ] maior
   # [ 4 ] novos números
   # [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso. (utilizar while sem break)

numeros = list()

while True:
    valor1 = int(input('Digite um valor: '))
    valor2 = int(input('Digite outro valor: '))
    print('________MENU__________-')
    print('[ 1 ] somar')
    print('[ 2 ] multiplicar')
    print('[ 3 ] maior')
    print('[ 4 ] novos números')
    print('[ 5 ] sair do programa')
    print('________________________')
    numeros = (valor1, valor2)
    esc = int(input('Digite o número da sua opção: '))
   
    if esc == 1:
       soma = valor1 + valor2 
       print(f'A soma é: {soma}')
    if esc == 2:
        mult = valor1 * valor2
        print(f'A multiplicação é: {mult} ')
    if esc ==3:
        print(f'O maior número é: {max(numeros)}')
    if esc ==4:
        print('')
    if esc ==5:
        print('Até logo!!')
        break

