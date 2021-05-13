num1 = float(input('Digite um número: '))
num2 = float(input('Digite um número: '))
num3 = float(input('Digite um número: '))
num4 = float(input('Digite um número: '))

tupla = (num1, num2, num3, num4)

a = 0
for num in tupla:
    if num == 9:
        a+=1
        

print(f'O número 9 aparece: {a} vezes. ')

print(f'O número três foi digitado pela primeira vez na posição: {tupla.index(3)}')


   

