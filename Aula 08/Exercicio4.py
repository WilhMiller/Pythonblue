frase = input('Digite uma frase: ')
vogais = "aeiou"
for i in vogais:
    frase = frase.replace(i, " ")

print(frase)

