n = int(input('Digite qual tabuada você quer ver?: '))

print('-------------Soma------------')

for i in range(1, 11):
    soma = n + i
    print(f'Soma: {i} + {n} = {soma} ' )


print('-------------Subtração------------')

for i in range(1, 11):
    subtracao = n - i
    print(f'Subtração: {i} - {n} = {subtracao} ' )


print('-------------Multiplicação------------')

for i in range(1, 11):
    multiplicacao = n * i
    print(f'Multiplicação: {i} * {n} = {multiplicacao} ' )


print('-------------Divisão------------')

for i in range(1, 11):
    divisão = n / i
    print(f'Divisão : {i} / {n} = {divisão:.2f} ' )

    
    
    
    
    

