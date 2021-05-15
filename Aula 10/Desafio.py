# Candidatos
Harry = 1
Rony = 2
Hermione = 3
Sirius = 4
Branco = 5
Nulo = 6
lista = list()

v1 = int(input('Digite o número do seu candidato: '))
v2 = int(input('Digite o número do seu candidato: '))
v3 = int(input('Digite o número do seu candidato: '))
v4 = int(input('Digite o número do seu candidato: '))
v5 = int(input('Digite o número do seu candidato: '))
v6 = int(input('Digite o número do seu candidato: '))

lista = (v1, v2, v3, v4, v5, v6)
print(lista)

r1 = lista.count(1)
r2 = lista.count(2)
r3 = lista.count(3)
r4 = lista.count(4)
r5 = lista.count(5)
r6 = lista.count(6)

print(f'O candidato Harry levou: {r1} votos.\nO candidato Rony levou : {r2} votos.\nA candidata Hermione levou: {r3} votos.\nO cadidato Sirius levou: {r4} votos.')
print(f'Votos em branco: {r5}')
print(f'Votos nulos: {r6}')