n = int(input('Digite um número para ver seus divisores: '))

for c in range(1, n+1):
    if n % c == 0:
        print(f'{c} é um divisor {n}')
        
    