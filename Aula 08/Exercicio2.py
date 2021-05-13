frase = input('Digite uma frase: ').lower()

a=0
e=0
i=0
o=0
u=0


for digite in frase:
    if digite == 'a':
        a+=1
    if digite == "e":
        e+=1
    if digite == "i":
        i+=1
    if digite == 'o':
        o+=1
    if digite == 'u':
        u+=1
    
print(f'a:{a}')
print(f'e:{e}')
print(f'i:{i}')
print(f'o:{o}')
print(f'u:{u}')

print('FIM!')




   
     
    