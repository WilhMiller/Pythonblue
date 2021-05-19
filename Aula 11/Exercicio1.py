
pessoa = list()
peso = list()
peso1=list()

while True:
    pessoa.append((input('Nome: ')))
    peso.append(int(input('Peso: ')))
    peso.append(pessoa[:])
    peso.clear()
    pesq = input('Quer continuar: ').upper()
    break

peso1=pessoa
a = max(peso1)
b = min(peso1)

print(pessoa) 
print(f'Foram cadastradas {len(pessoa)} pessoas. ')
print(f'O maior peso é {a} e o menor peso é {b}')







