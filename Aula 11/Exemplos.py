pessoa = list()
pessoa.append('Thiago')
pessoa.append('27 anos')
print(pessoa)

povoado = list()
povoado.append(pessoa[:])

pessoa[0]= 'Maria'
pessoa[1] = 34
print(pessoa)