num = int(input('Digite um número:'))
escolha = int(input('Escolha a conversão desejada: 1 - binário, 2 - octal e 3 - Hexadecimal.'))
if escolha == 1:
    print('O número {} em sua base binária fica {}.'.format(num, bin(num)[2:]))
elif escolha == 2:
    print('O número {} em sua base octal fica {}.'.format(num, oct(num)[2:]))
elif escolha == 3:
    print('O número {} em sua base hexadecimal fica {}.'.format(num, hex(num)[2:]))
else:
    print('Opção inválida! Tente novamente!')