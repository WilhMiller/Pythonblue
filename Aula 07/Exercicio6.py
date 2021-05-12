def notas(n1, n2, n3):  
    n1, n2, n3 = n1, n2, n3
    mediag = (n1 + n2 + n3) / 3
    media1 = (n1 + n2) / 2
    media2 = (n1 + n3) / 2
    media3 = (n2 + n1) / 2
    media4 = (n2 + n3) / 2
    media5 = (n3 + n1) / 2
    media6 = (n3 + n2) / 2
    print(f'Sua média geral seria: {mediag}')
    if n1 >= n2 and n2>= n3:
        print(f'Sua média com as duas notas mais altas: {media1}')
    elif n1 >= n3 and n3 >= n2:
        print(f'Sua média com as duas notas mais altas: {media2}')
    elif n2 >= n1 and n1 >= n3:
        print(f'Sua média com as duas notas mais altas: {media3}')
    elif n2 >= n1 and n3 >= n1:
        print(f'Sua média com as duas notas mais altas: {media4}')
    elif n3 >= n1 and n1 >= n2:
        print(f'Sua média com as duas notas mais altas: {media5}')
    elif n3 >= n1 and n2 >= n1:
        print(f'Sua média com as duas notas mais altas: {media6}')
        return n1, n2, n3 
    if n1>=n2>=n3:
        print(f'Sua nota mais alta: {n1}')
        print(f'Sua nota mais baixa: {n3}')
    elif n2>=n1>=n3:
        print(f'Sua nota mais alta: {n2}')
        print(f'Sua nota mais baixa: {n3}')
    elif n3>=n1>=n2:
        print(f'Sua nota mais alta: {n3}')
        print(f'Sua nota mais baixa: {n2}')
    elif n2>=n3>=n1:
        print(f'Sua nota mais alta: {n2}')
        print(f'Sua nota mais baixa: {n1}')
    elif n3>=n2>=n1:
        print(f'Sua nota mais alta: {n3}')
        print(f'Sua nota mais baixa: {n1}')
    elif n1>=n3>=n2:
        print(f'Sua nota mais alta: {n1}')
        print(f'Sua nota mais baixa: {n2}')
        return n1, n2, n3
    



n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))


notas(n1, n2, n3)
        
   


