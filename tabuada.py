while True:
    n = int(input('Digite um número para saber sua tabuada (número negativo para encerrar):'))
    if n < 0:
        print('Programa encerrado!')
        break
    else:
        print('=' * 50)
        for c in range(0, 11):
            print('{} x {} = {}'.format(n, c, c * n))
        print('=' * 50)