def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        print(f'Com {idade} anos o voto é NEGADO. ')
    elif idade >=16 and idade <18 or idade >65:
        print(f'Com {idade} anos o voto é OPICIOANAL. ')
    else:
        print(f'Com {idade} anos o voto é OBRIGATÓRIO. ')

    
ano = int(input('Digite o ano do seu nascimento: '))
voto(ano)

