import os

def limpar_console():
    if os.name == 'nt':  # Se for Windows
        os.system('cls')
    else:  # Se for Linux ou macOS
        os.system('clear')

def ficha_aluno(
        nome='',
        telefone='',
        data_pagamento='',
        nome_pacote='',
        valor_pacote=0,
        forma_de_pagamento='',
        observacoes = ''
):
    title('Adicionar Aluno/Pagamento', 'amarelo')
    print(f'''\n
    Nome do Aluno:       {nome}
    Número de Telefone:  {telefone}
    Data de Pagamento:   {data_pagamento}
    Pacote de Pagamento: {nome_pacote} -> R$ {valor_pacote}
    Forma de Pagamento:  {forma_de_pagamento}
    Observações:         {observacoes}''')

def lista_alunos(data):
    limpar_console()
    print("===> Lista de Alunos: <===\n\n")
    for aluno in sorted(data.keys()):
        print("    ",aluno)
    print("\n^^^^ Lista de Alunos ^^^^")

def title(txt, cor = 'verde'):
    if cor == 'verde':
        cor = str('\33[32m')
    elif cor == 'vermelho':
        cor = str('\33[31m')
    elif cor == 'amarelo':
        cor = str('\33[33m')
    elif cor == 'azul':
        cor = str('\33[34m')
    elif cor == 'cancelar':
        cor = str('\33[m')

    linha = len(txt) + 4

    print(f'{cor}='*linha)
    print(f'  {txt}')
    print('='*linha)
    print('\33[m')