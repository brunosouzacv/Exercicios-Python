from time import sleep

#MENU

#Apresentação do jogo e suas regras

def menu():

    print('-=' *20)
    print('HOTEL DOS ANIMAIS')
    regras = [
        ['Regra nº 1: O rato não pode ficar ao lado do gato.'], ['Regra nº 2: O cão não pode ficar ao lado do osso.'],
        ['Regra nº 3: O gato não pode ficar ao lado do cão.'], ['Regra nº 4: O queijo não pode ficar ao lado do rato.'], ['Para escolher suas opções, considere:'], ['1', '2', '3', '4'], ['5', '6', '7', '8'], ['Observação: os inquilinos não podem ficar no mesmo quarto!']
    ]
    print('-=' *20)

    nome = input('Antes de iniciar, qual o seu nome?')
    print(f'Belo nome, {nome}! Bora lá!')
    print('-=' *30)
    print('CARREGANDO AS REGRAS...')
    print('-=' *30)
    sleep(3)

    for linha in regras: #estabelecendo as regras
        print(linha)
    print('-=' *45)
    sleep(3)

    print('Agora que você já sabe as regras, é hora de colocar a mão na massa e quebrar a cabeça!')
    print('-=' *45)
    sleep(3)

    print('CARREGANDO O JOGO...')
    print('-=' *20)
    sleep(3)

#Programa principal com o jogo

while True:

    menu() #Retomada da função com o Menu

    #FASE1

    hotel = [
        ['*', '*', '_', 'G'], ['R', '_', '*', '*']  #Lista com as posições estabelecidas pelo jogo
    ]

    solucao1 = [
        3, 6        #Lista com a solução da fase
    ]

    print('FASE 1')
    print('-=' * 45)
    sleep(2)

    print('Na fase 1, você deve alocar o RATO e o GATO na matriz que representa os quartos:')

    for linha in hotel:     #Mostrando ao jogador suas opções
        print(linha)
    print('-=' * 20)

    posicaoGATO = int(input('Posição do GATO:'))        #Jogador escolhe a posição do gato
    posicaoRATO = int(input('Posição do RATO:'))        #Jogador escolhe a posição do rato

    opcao = [
        posicaoGATO, posicaoRATO        #Lista com as opções do jogador
    ]

    if opcao != solucao1:       #Se a lista com as opções do jogador não for igual a solução, ele perde e o loop é encerrado
        print('-=' * 20)
        print('Você perdeu!')
        print('-=' * 20)
        break

    else:                       #Se for igual, ele passa de fase
        print('-=' * 20)
        print('Você ganhou!')
        print('-=' * 20)
        print('CARREGANDO A FASE 2...')
        sleep(3)

        #FASE2

        hotel1 = [
            ['_', '*', '*', '*'], ['*', 'C', '_', '_']  #Criando nova lista atualizada com as posições
        ]

        print('-=' * 20)
        print('FASE 2')
        print('-=' * 45)
        sleep(2)

        print('Na fase 2, você deve deve alocar : CÃO, CÃO E OSSO.')

        for linha in hotel1:    #Mostrando ao jogador suas opções
            print(linha)
        print('-=' * 20)

        posicaoCAO1 = int(input('Posição do CÃO:'))     #Jogador escolhe a posição do cão 1
        posicaoCAO2 = int(input('Posição do CÃO:'))     #Jogador escolhe a posição do cão 2
        posicaoOSSO = int(input('Posição do OSSO:'))    #Jogador escolhe a posição do osso

        if posicaoCAO1 == 1:        #Nessa etapa, o osso obrigatoriamente deve ser alocado no quarto 1.
            print('-=' * 20)
            print('Você perdeu!')   #Por isso, caso um dos cães seja alocado nele, os jogadores perderão e o loop será encerrado
            print('-=' * 20)
            break

        if posicaoCAO2 == 1:
            print('-=' * 20)
            print('Você perdeu!')
            print('-=' * 20)
            break

        if posicaoOSSO == 1:
            print('-=' * 20)
            print('Você ganhou!')
            print('-=' * 20)
            print('CARREGANDO A FASE 3...')
            sleep(3)

            #FASE3

            hotel2 = [
                ['_', '*', '*', '*'], ['_', 'G', '_', '*']  # criando nova lista atualizada com as posições
            ]

            print('-=' * 20)
            print('FASE 3')
            print('-=' * 45)
            sleep(2)

            print('Na fase 3, você deve deve alocar : GATO, RATO E OSSO.')

            for linha in hotel2:    #Mostrando ao jogador suas opções
                print(linha)
            print('-=' * 20)

            posicaoGATO1 = int(input('Posição do GATO:'))     #Jogador escolhe a posição do gato
            posicaoRATO1 = int(input('Posição do RATO:'))     #Jogador escolhe a posição do rato
            posicaoOSSO1 = int(input('Posição do OSSO:'))     #Jogador escolhe a posição do osso

            if posicaoGATO1 == 1:
                print('-=' * 20)
                print('Você perdeu!')       #Nessa fase, o gato não pode ser alocado no quarto 1.
                print('-=' * 20)            #Por isso, se o jogador escolher a opção 1, perderá o jogo e o loop será encerrado
                break

            if posicaoRATO1 == 5 or posicaoRATO1 == 7:      #O rato não pode ficar no quarto 5 ou 7.
                print('-=' * 20)                            #Por isso, se o jogador escolher a opção, perderá o jogo e o loop será encerrado
                print('Você perdeu!')
                print('-=' * 20)
                break

            if posicaoOSSO1 == 5 or posicaoOSSO1 == 7:      #O osso deve ficar na posição 5 ou 7.
                print('-=' * 20)                            #Por isso, se o jogador acertar ele avançará no jogo
                print('Você ganhou!')
                print('-=' * 20)
                print('CARREGANDO A FASE 4...')
                sleep(3)

                #FASE4

                hotel3 = [
                    ['_', '_', '_', '*'], ['*', 'R', '*', '*']     #Criando nova lista atualizada com as posições
                ]

                print('-=' * 20)
                print('FASE 4')
                print('-=' * 45)
                sleep(2)

                print('Na fase 4, você deve deve alocar : QUEIJO, QUEIJO E OSSO.')

                for linha in hotel3:        #Mostrando ao jogador suas opções
                    print(linha)
                print('-=' * 20)

                posicaoQUEIJO1 = int(input('Posição do QUEIJO:'))   #Jogador escolhe a posição do queijo 1
                posicaoQUEIJO2 = int(input('Posição do QUEIJO:'))   #Jogador escolhe a posição do queijo 2
                posicaoOSSO2 = int(input('Posição do OSSO:'))       #Jogador escolhe a posição do osso

                if posicaoQUEIJO1 == 2:     #O queijo não pode ficar na posição 2.
                    print('-=' * 20)        #Por isso, se o jogador optar por essa opção perderá o jogo e o loop será encerrado
                    print('Você perdeu!')
                    print('-=' * 20)
                    break

                if posicaoQUEIJO2 == 2:     #O queijo não pode ficar na posição 2.
                    print('-=' * 20)        #Por isso, se o jogador optar por essa opção perderá o jogo e o loop será encerrado
                    print('Você perdeu!')
                    print('-=' * 20)
                    break

                if posicaoOSSO2 == 2:       #O osso, por sua vez, deve ficar na posição 2.
                    print('-=' * 20)        #Por isso, se o jogador optar por essa opção vencerá.
                    print('Você ganhou!')
                    print('-=' * 20)
                    print('Você se provou ser um especialista em hóteis!')
                    print('-=' * 20)

    fimdejogo = int(input('Deseja jogar novamente?'     #Pergunta ao jogador se ele deseja jogar novamente
                          '\n1 - SIM'
                          '\n2 - NÃO'
                          '\nOpção: '))
    if fimdejogo == 1:      #Se responder que sim, o loop reiniciará
        continue
    else:
        print('-=' * 20)
        print('Obrigado pela partida e até breve!')     #Senão, será encerrado.
        print('-=' * 20)
        break