lista = list()

r1 = input('Telefonou para a vítima?: ')
r2 = input('Esteve no local do crime?: ')
r3 = input('Mora perto da vítima?: ')
r4 = input('Devia para a vítima?: ')
r5 = input('Já trabalhou com a vaítima?: ')

lista = (r1, r2, r3, r4, r5)
if lista.count('sim') == 2:
    print('Suspeita')
elif lista.count('sim') >2 and lista.count('sim') <=4:
    print('Cúmplice')
elif lista.count('sim') == 5:
    print('Assassino')
else:
    print('Inocente')




