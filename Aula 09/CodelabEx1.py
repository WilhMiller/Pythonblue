n = int(input('Digite qual tabuada você quer ver?: '))

print('-------------Soma------------')

for i in range(1, 11):
    soma = n + i
    print(f'Soma: {n} + {i} = {soma} ' )


print('-------------Subtração------------')

for i in range(1, 11):
    subtracao = n - i
    print(f'Subtração: {n} - {i} = {subtracao} ' )


print('-------------Multiplicação------------')

for i in range(1, 11):
    multiplicacao = n * i
    print(f'Multiplicação: {n} * {i} = {multiplicacao} ' )


print('-------------Divisão------------')

for i in range(1, 11):
    divisão = n / i
    print(f'Divisão : {n} / {i} = {divisão:.2f} ' )

    
    
    
    
    

