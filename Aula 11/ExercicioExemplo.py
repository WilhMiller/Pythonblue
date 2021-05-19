galera = list()
dados = list()
totalmaior = totalmenor =0

for c in range(0,3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for g in galera:
    if g[1] >=18:
        print(f'{g[0]} é maior de idade. ')
        totalmaior +=1
    else:
        print(f'{g[0]} é menor de idade. ')
        totalmenor +=1

print(f'Temos {totalmaior} maiores e {totalmenor} menores de idade.')



