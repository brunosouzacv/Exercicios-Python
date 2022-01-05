from random import randint

n = int(randint(0,10)) #faz o computador 'PENSAR'
acertou = False
palpites = 0
print('Adivinhe qual número estou pensando...')
while not acertou:
    num = int(input('Em qual número eu pensei? De 0 a 10?')) #jogador tenta adivinhar
    palpites += 1
    if num == n:
        acertou = True
    else:
        if n < num:
            print('Menos...Tente mais uma vez.')
        elif n > num:
            print('Mais...Tente mais uma vez.')
print('Você acertou! Precisou de {} tentativas.'.format(palpites))