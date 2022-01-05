frase = str(input('Escreva uma frase qualquer:')).upper().replace(' ', '')
fraseinvertida = frase[::-1]
if frase == fraseinvertida:
    print('A frase citada é um palíndromo!')
else:
    print('A frase citada não é um palíndromo!')