n1 = float(input('Digite um valor:'))
n2 = float(input('Digite outro valor:'))
opção = int(input('Agora, selecione a opção desejada:'
                  '\n[ 1 ] somar'
                  '\n[ 2 ] multiplicar'
                  '\n[ 3 ] maior'
                  '\n[ 4 ] novos números'
                  '\n[ 5 ] sair do programa'
                  '\nSua opção:'))
if opção == 1:
    print('A soma de {} e {} é {}.'.format(n1, n2, (n1 + n2)))
elif opção == 2:
    print('A multiplicação de {} e {} é {}.'.format(n1, n2, (n1 * n2)))
elif opção == 3:
    if n1 > n2:
        maior = n1
    else:
        maior = n2
    print('Entre {} e {}, {} é o maior.'.format(n1, n2, maior))
elif opção == 5:
    print('Atendimento finalizado com sucesso!')
else:
    print('Opção inválida! Tente novamente!')
while opção == 4:
    n1 = float(input('Digite um valor:'))
    n2 = float(input('Digite outro valor:'))
    opção = int(input('Agora, selecione a opção desejada:'
                      '\n[ 1 ] somar'
                      '\n[ 2 ] multiplicar'
                      '\n[ 3 ] maior'
                      '\n[ 4 ] novos números'
                      '\n[ 5 ] sair do programa'
                      '\nSua opção:'))
    if opção == 1:
        print('A soma de {} e {} é {}.'.format(n1, n2, (n1 + n2)))
    elif opção == 2:
        print('A multiplicação de {} e {} é {}.'.format(n1, n2, (n1 * n2)))
    elif opção == 3:
        print('Entre {} e {}, {} é o maior.'.format(n1, n2, max(n1, n2)))
    elif opção == 5:
        print('Atendimento finalizado com sucesso!')
    else:
        print('Opção inválida! Tente novamente!')