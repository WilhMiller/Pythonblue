lista = list()

r1 = input('Telefonou para a vítima?: ').lower()
r2 = input('Esteve no local do crime?: ').lower()
r3 = input('Mora perto da vítima?: ').lower()
r4 = input('Devia para a vítima?: ').lower()
r5 = input('Já trabalhou com a vaítima?: ').lower()

lista = (r1, r2, r3, r4, r5)
if lista.count('SIM') == 2:
    print('Suspeita')
elif lista.count('SIM') >2 and lista.count('sim') <=4:
    print('Cúmplice')
elif lista.count('SIM') == 5:
    print('Assassino')
else:
    print('Inocente')




