from random import randint

#MENU

#Função para visualização do Menu

def menu():
    print('MENU')
    print('0 - Encerrar'
          '\n1 - Nova inscrição'
          '\n2 - Visualizar inscrição')

#VALIDAÇÃO DA OPÇÃO ESCOLHIDA

#Função para validar a opção do usuário. Pergunta e armazena sua opção

def valida_opcao(texto: str, min: int, max: int):
    while True:
        try:
            opcao = int(input(texto))
        except ValueError:
            print('Opção inválida! Tente novamente!')
            continue
        else:
            if min <= opcao <= max:
                return opcao
            print('Opção inválida! Tente novamente!')
            continue

#VALIDAÇÃO DO NOME

#Função para validar o nome do usuário.
#1º: Divide-se o nome com a função split()
#2º: Usa-se a função isalpha() para verificar a existência de números, caso tenha, será feita uma nova solitação ao usuário

def valida_nome(texto: str):
    nome = ''
    while not nome:
        nome = input(texto)
        for palavra in nome.split(' '):
            if not palavra.isalpha():
                print('Nome inválido! Tente novamente!')
                nome = ''
                break
    return nome

#VALIDAÇÃO DO EMAIL

#Função para validar o email. Usa-se a função find() para verificar a existência de @, . e '' . Senão houver, será feita uma nova solitação ao usuário

def valida_email(texto: str):
    while True:
        email = input(texto)
        if email.find('@') != -1 and email.find('.') != -1 and email.find(' ') == -1:
            return email
        print('Email inválido! Tente novamente!')

#VALIDAÇÃO DO CELULAR

#Função para validar o celular. Caso o valor de entrada não for um número, a exceção acusará e será feita nova solitação ao usuário.

def valida_celular(texto: str):
    while True:
        try:
            celular = int(input(texto))
        except ValueError:
            print('Número de celular inválido! Tente novamente!')
            continue
        else:
            return celular

#VALIDAÇÃO DO CURSO

#Função para validar o curso.
#1º: Divide-se o nome com a função split()
#2º: Usa-se a função isalnum() para verificar a existência de letras e números, caso não tenha, será feita uma nova solitação ao usuário

def valida_curso(texto: str):
    curso = ''
    while not curso:
        curso = input(texto)
        for palavra in curso.split(' '):
            if not palavra.isalnum():
                print('Curso inválido! Tente novamente!')
                curso = ''
                break
    return curso.upper()

#GERADOR DO VOUCHER

#Função para gerar o voucher.
#1º: Criação do dicionário para armazenar os dados do inscrito
#2º: Usa-se a função randint() para criar o número do voucher de forma aleatória
#3º: Verifica-se a existência do voucher, se já existir retornará ao início. Caso exista, será armazenado ao dicionário 'inscricao'

def gerador_voucher(cadastros: list):
    inscricao = {}
    if not cadastros:
        voucher = randint(1, 999)
        inscricao['Voucher'] = voucher
        return inscricao
    voucher = 0
    while not voucher:
        voucher = randint(1, 999)
        for cadastro in cadastros:
            if cadastro['Voucher'] == voucher:
                voucher = 0
                break
    inscricao['Voucher'] = voucher
    return inscricao

#PROGRAMA PRINCIPAL

'''Programa final
1º: Lista de dicionário para armazenar os dados dos inscritos
2º: Imprime na tela o MENU
3º: Opção selecionada pelo usuário
Opção = 1
-Gera e armazena o voucher
-Valida e armazena o nome
-Valida e armazena o email
-Valida e armazena o celular
-Valida e armazena o curso
-Armazena todos os dados
Opção = 2
-Imprime na tela os usuários cadastrados
Opção = 3
-Encerra o programa'''

cadastros = []
while True:
    menu()
    opcao = valida_opcao('Opção: ', 0, 2)
    if opcao == 1:
        inscricao = gerador_voucher(cadastros)
        nome = valida_nome('Digite seu nome: ')
        inscricao['Nome'] = nome
        email = valida_email('Digite seu email: ')
        inscricao['Email'] = email
        celular = valida_celular('Digite seu número de celular: ')
        inscricao['Celular'] = celular
        curso = valida_curso('Digite seu curso: ')
        inscricao['Curso'] = curso
        cadastros.append(inscricao)
    elif opcao == 2:
        print('LISTA DE INSCRITOS')
        for cadastro in cadastros:
            for i, j in cadastro.items():
                print(f'{i} = {j}')
    elif opcao == 0:
        print('PROGRAMA ENCERRADO!')
        break
