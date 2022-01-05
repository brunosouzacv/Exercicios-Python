n1 = int(input('Digite o primeiro termo da P.A.:'))
r = int(input('Digite a razão da P.A.:'))
qtd_termo = int(input('Digite a quantidade de termos desejados:'))
termo1 = n1
termo = qtd_termo
cont = 1
while cont <= termo:
    print('{} > '.format(termo1), end='')
    termo1 += r
    cont += 1
print('FIM')