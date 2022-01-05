from time import sleep
from random import choice

print('\033[1;30;45mVamos jogar Jokenpô? Boa sorte!\033[m') #INÍCIO

print('-=-' *20)

usuário = int(input('\033[1;43mEscolha uma das opções abaixo:\033[m' #USUÁRIO ESCOLHE
          '\n\033[7;37;40m[1] Pedra\033[m' 
           '\n\033[7;40m[2] Papel\033[m' 
           '\n\033[7;34m[3] Tesoura\033[m'
           '\n\033[7;31;40mQual a sua escolha?\033[m'))

lista = [1, 2, 3]
máquina = choice(lista) #MÁQUINA ESCOLHE

print('-=-' *20)
print('\033[1;30;43mJO\033[m')
sleep(1)
print('\033[1;30;43mKEN\033[m')
sleep(1)
print('\033[1;30;43mPÔ\033[m')
print('-=-' *20)

if usuário == máquina: #EMPATE
    print('\033[4;33mDEU EMPATE! VAMOS DESEMPATAR?\033[m')

elif usuário != máquina: #OUTRAS POSSIBILIDADES
    if usuário == 1 and máquina == 2:
        print('\033[1;32mEU VENCI!\033[m Você escolheu Pedra e eu escolhi Papel! \033[4mQUER MAIS UMA CHANCE?\033[m')
    elif usuário == 1 and máquina == 3:
        print('\033[1;32mVOCÊ VENCEU!\033[m Você escolheu Pedra e eu escolhi Tesoura! \033[4mPODE ME DAR MAIS UMA CHANCE?\033[m')
    elif usuário == 2 and máquina == 1:
        print('\033[1;32mVOCÊ VENCEU!\033[m Você escolheu Papel e eu escolhi Pedra! \033[4mPODE ME DAR MAIS UMA CHANCE?\033[m')
    elif usuário == 2 and máquina == 3:
        print('\033[1;32mEU VENCI!\033[m Você escolheu Papel e eu escolhi Tesoura! \033[4mQUER MAIS UMA CHANCE?\033[m')
    elif usuário == 3 and máquina == 1:
        print('\033[1;32mEU VENCI!\033[m Você escolheu Tesoura e eu escolhi Pedra! \033[4mQUER MAIS UMA CHANCE?\033[m')
    elif usuário == 3 and máquina == 2:
        print('\033[1;32mVOCÊ VENCEU!\033[m Você escolheu Tesoura e eu escolhi Papel! \033[4mPode me dar mais uma chance?\033[m')
    else: #ESCOLHE ERRADO
        print('\033[4;31mVocê não sabe jogar Jokenpô? Tente novamente!\033[m')

print('-=-' *20)
print(' \033[1;30;45mJOGO FINALIZADO\033[m ') #FIM DO JOGO