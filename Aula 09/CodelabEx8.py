import random as rd

def combinacoes():
    d1 = rd.randrange(1, 56)
    d2 = rd.randrange(d1 + 1, 57)
    d3 = rd.randrange(d2 + 1, 58)
    d4 = rd.randrange(d3 + 1, 59)
    d5 = rd.randrange(d4 + 1, 60)
    d6 = rd.randrange(d5 + 1, 61)
    return d1, d2, d3, d4, d5, d6


while(True):
    print(f'\nGerando uma combinação para a Mega Sena:\n')
    print(f'Combinação gerada: ', combinacoes() )
    if(input('\nDigite 0 para continuar: ') !="0"):
        break

