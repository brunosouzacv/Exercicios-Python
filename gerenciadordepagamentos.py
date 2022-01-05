from time import sleep

print('{:=^40}'.format(' LOJA DO BRUNO '))
valor = float(input('\033[1;35mQual o valor do produto? R$\033[m'))
print('=' *40)
opção = int(input('\033[1;33mSelecione uma condição de pagamento:\033[m'
      '\n\033[1;31m[Opção 1]\033[m à vista dinheiro/cheque: 10% de desconto'
      '\n\033[1;31m[Opção 2]\033[m à vista no cartão: 5% de desconto'
      '\n\033[1;31m[Opção 3]\033[m em até 2x no cartão: preço normal'
      '\n\033[1;31m[Opção 4]\033[m 3x ou mais no cartão: 20% de juros'
      '\n\033[1;31mOpção desejada:\033[m'))
print('=' *40)
print('\033[0;32mPROCESSANDO...\033[m')
print('=' *40)
sleep(2)
if opção == 1:
      print('\033[0;32mO produto sairá por R${:.2f}.\033[m'.format(valor - valor * 0.10))
      print('{:=^40}'.format(' FIM '))
elif opção == 2:
      print('\033[0;32mO produto sairá por R${:.2f}.\033[m'.format(valor - valor * 0.05))
      print('{:=^40}'.format(' FIM '))
elif opção == 3:
      print('\033[0;32mO produto sairá por R${:.2f}.\033[m'.format(valor))
      print('=' * 40)
      parc = int(input('Serão quantas parcelas? Até duas.'))
      print('=' * 40)
      print('\033[1;32mPROCESSANDO...\033[m')
      sleep(2)
      valparc = valor / parc
      print('=' * 40)
      print('\033[1;33mSendo assim, serão {} vezes de R${:.2f}.\033[m'.format(parc, valparc))
      print('{:=^40}'.format(' FIM '))
elif opção == 4:
      print('\033[0;32mO produto sairá por R${:.2f}.\033[m'.format(valor + valor * 0.20))
      print('=' * 40)
      parc = int(input('Serão quantas parcelas?'))
      print('=' * 40)
      print('\033[1;32mPROCESSANDO...\033[m')
      sleep(2)
      valparc = (valor + valor * 0.20) / parc
      print('=' * 40)
      print('\033[1;33mSendo assim, serão {} vezes de R${:.2f}.\033[m'.format(parc, valparc))
      print('{:=^40}'.format(' FIM '))
else:
      print('\033[4;31mErro! Tente Novamente!\033[m')
      print('{:=^40}'.format(' FIM '))