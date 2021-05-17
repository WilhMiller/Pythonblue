
a = 0
b = 0
c = 0

r1 = int(input('Qual sua idade? '))
r2 = input('Qual o seu sexo? M(masculino) ou F(feminino): ').upper()
r3 = input('Quer continuar? ').upper()
if r1 >18:
    a +=1
if r2 == 'M':
    b +=1 
if r1 <20 and r2 == 'F':
    c +=1

while r3 == 'SIM':
    if r1 >18:
      a +=1
    if r2 == 'M':
      b +=1 
    if r1 <20 and r2 == 'F':
      c +=1
    r1 = int(input('Qual sua idade? '))
    r2 = input('Qual o seu sexo? M(masculino) ou F(feminino): ').upper()
    r3 = input('Quer continuar? ').upper()
    
      


print(f'Pessoas maiores de 18 anos: {a} ')
print(f'Homens cadastrados: {b} ')
print(f'Mulheres que tem menos de 20 anos: {c} ')


    
    

    

