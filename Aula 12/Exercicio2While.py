#02 - Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
   #  A) quantas pessoas tem mais de 18 anos.
   #  B) quantos homens foram cadastrados.
   #  C) quantas mulheres tem menos de 20 anos.


idade = list()
sexo = list()

while True:
    idade.append(int(input('Digite sua idade: ')))
    sexo.append(input('Digite seu sexo M ou F: ').upper())
    sexo.append(idade[:])
    sexo.clear
    pergunta = input('Quer continuar: S/N: ').upper()
    if pergunta == 'N':
       break


tota1 = sexo.count('F')
h = sexo.count('M')
total2 = ()


print(f'Foram cadastradas {total2} pessoas.')
print(f'Foram cadastrados {h} homens. ')
#print(f'{m1} mulheres tem menos de 20 anos. ')

    



    
    
    
    