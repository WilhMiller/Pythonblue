valorpao = 0.18

print('Preço do Pão R$: 0.18')
print('Panificadora Pão de Ontem - Tabela de Preços')

for i in range(1,51):
    preço = valorpao * i
    print(f'{i} - R$: {preço:.2f} ')



