i = int(input('Quantas matérias tem sua escola: '))
notas = list()
 
for c in range(i):
     notas.append(float(input('Qual a nota: ').replace(',','.')))
     soma = sum(notas)
     media = soma/i

print(f'a media geral é: {media:.2f}')
