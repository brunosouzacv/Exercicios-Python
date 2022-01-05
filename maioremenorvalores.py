som = quant = media = maior = menor = 0
resp = 'S'
while resp in 'Ss':
        n = int(input('Digite um número:'))
        quant += 1
        som += n
        if quant == 1:
            maior = menor = n
        else:
            if n > maior:
                maior = n
            if n < menor:
                menor = n
        resp = str(input('Você deseja continuar digitando números (SIM ou NÃO)?')).upper().strip()
print('A média entre os valores digitados foi {}.'.format(som / quant))
print('O maior número é o {}.'.format(maior))
print('O menor número é o {}.'.format(menor))