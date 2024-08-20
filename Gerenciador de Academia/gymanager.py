from re import match
import os
import json
import datetime
from utils import limpar_console, ficha_aluno, lista_alunos, title

# Obtém o diretório onde o script está localizado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define o nome do arquivo JSON
json_filename = "academiadata.json"

# Caminho completo para o arquivo JSON
json_filepath = os.path.join(script_dir, json_filename)

# Carrega os dados existentes do arquivo JSON, se houver

if os.path.exists(json_filepath):
    with open(json_filepath, 'r') as json_file:
        data = json.load(json_file)
else:
    data = {}

def salvar_dados():
    with open(json_filepath, 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

def adicionar_aluno():
    while True:
        limpar_console()
        if data:
            lista_alunos(data=data)
            print('(Para adicionar um aluno ou registro,\ndigite o nome exato do aluno.Verifique o nome\nna lista acima.)\n')
        title("Adicionar Aluno/Pagamento", 'verde')

        nome = input("\n\n\n ==> Digite o nome do aluno (0 = abortar): ")
        if nome == '0':
            limpar_console()
            title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
            return
        # Verifica se o nome não está em branco e não começa com espaços em branco
        if nome:
            nome = nome.upper().strip()
            break
            
        else:
            limpar_console()
            title("===>E R R O !! --- NOME INVÁLIDO. O nome não pode estar em branco.", 'vermelho')
            opcao = input("\nEscolha uma opção:\n1. Tentar novamente\n2. Voltar ao menu principal\n==> Escolha sua opcão: ")
            if opcao == '2':
                limpar_console()
                title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
                return
            elif opcao != '1':
                limpar_console()
                title("E R R O !! --- Opção inválida. Voltando ao menu principal.", 'vermelho')
                return

    while True:
        limpar_console()
        ficha_aluno(nome=nome)
        telefone = input("\n==> Digite o número de TELEFONE do aluno (0 = abortar): ")
        if telefone == '0':
            limpar_console()
            title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
            return
        limpar_console()
        ficha_aluno(nome=nome, telefone=telefone)
        escolha_data = input("\n==> Deseja USAR a data de HOJE (0 = abortar)? S/N: ").lower()
        if escolha_data == 's':
            data_pagamento = datetime.date.today().strftime('%d-%m-%Y')
        elif escolha_data == '0':
            limpar_console()
            title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
            return
        else:
            limpar_console()
            while True:
                ficha_aluno(nome=nome, telefone=telefone)

                data_pagamento = input("\n==> Digite a DATA DE PAGAMENTO da mensalidade (0 = abortar) (formato DD-MM-AAAA): ")
                if data_pagamento == '0':
                    limpar_console()
                    title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
                    return
                try:
                    datetime.datetime.strptime(data_pagamento, '%d-%m-%Y')
                    break
                except ValueError:
                    limpar_console()
                    title("E R R O !! --- Formato de data inválido. Tente novamente (0 = abortar).", 'vermelho')
        break
    limpar_console()
    while True:
        
        ficha_aluno(nome=nome, telefone=telefone, data_pagamento=data_pagamento)

        print(f'''\n== Pacote de pagamento ==\n
1. Mensalidade (R$ 70,00)
2. Trimestral (R$ 180,00)
3. Casadinha (R$ 120,00)
4. Parcial 3xSemana (R$ 50,00)
5. Outro Valor (entrada do usuário)

0 = Abortar e voltar ao Menu Principal''')
        escolha_pacote = input("\n==> Escolha uma opção: ")

        if escolha_pacote == '1':
            nome_pacote = 'Mensalidade'
            valor_pacote = 70.00
            data_pagamento_dt = datetime.datetime.strptime(data_pagamento, '%d-%m-%Y').date()
            proximo_pagamento_dt = data_pagamento_dt + datetime.timedelta(days=30)
            proximo_pagamento = proximo_pagamento_dt.strftime('%d-%m-%Y')
            break
        elif escolha_pacote == '2':
            nome_pacote = 'Trimestral'
            valor_pacote = 180.00
            # Calcula a data do próximo pagamento (90 dias depois)
            data_pagamento_dt = datetime.datetime.strptime(data_pagamento, '%d-%m-%Y').date()
            proximo_pagamento_dt = data_pagamento_dt + datetime.timedelta(days=90)
            proximo_pagamento = proximo_pagamento_dt.strftime('%d-%m-%Y')
            break
        elif escolha_pacote == '3':
            nome_pacote = 'Casadinha'
            valor_pacote = 120.00
            data_pagamento_dt = datetime.datetime.strptime(data_pagamento, '%d-%m-%Y').date()
            proximo_pagamento_dt = data_pagamento_dt + datetime.timedelta(days=30)
            proximo_pagamento = proximo_pagamento_dt.strftime('%d-%m-%Y')
            break
        elif escolha_pacote == '4':
            nome_pacote = 'Parcial 3x Semana'
            valor_pacote = 50.00
            data_pagamento_dt = datetime.datetime.strptime(data_pagamento, '%d-%m-%Y').date()
            proximo_pagamento_dt = data_pagamento_dt + datetime.timedelta(days=30)
            proximo_pagamento = proximo_pagamento_dt.strftime('%d-%m-%Y')
            break
        elif escolha_pacote == '5':
            nome_pacote = 'Outro Valor'

            while True:

                try:
                    valor_pacote = float(input("\n  ==> Digite o valor da mensalidade: "))
                    if valor_pacote == 0:
                        limpar_console()
                        title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
                        return
                    data_pagamento_dt = datetime.datetime.strptime(data_pagamento, '%d-%m-%Y').date()
                    proximo_pagamento_dt = data_pagamento_dt + datetime.timedelta(days=30)
                    proximo_pagamento = proximo_pagamento_dt.strftime('%d-%m-%Y')
                    break
                except ValueError:
                    limpar_console()
                    title("E R R O !! --- Valor inválido. Tente novamente (0 = abortar).", 'vermelho')
            break
        elif escolha_pacote == '0':
            limpar_console()
            title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
            return
        else:
            limpar_console()
            title("E R R O !! --- Opção inválida. Tente novamente.", 'vermelho')
    

    limpar_console()

    while True:
        ficha_aluno(nome=nome, telefone=telefone, data_pagamento=data_pagamento,
                    nome_pacote=nome_pacote, valor_pacote=valor_pacote)
        forma_de_pagamento = str(input("""\n== FORMA DE PAGAMENTO ==\n
1. Dinheiro
2. Pix
3. Cartão
4. Outra Forma

0. Abortar e voltar ao Menu Principal

==> Escolha uma opção: """))
        if forma_de_pagamento == '4':
            forma_de_pagamento = str(input('''Exemplo: Uma parte em dinheiro, outra no pix...
                                           
    ==> Digite como foi a forma de pagamento: '''))
            while forma_de_pagamento == '':
                limpar_console()
                ficha_aluno(nome=nome, telefone=telefone, data_pagamento=data_pagamento,
                            nome_pacote=nome_pacote, valor_pacote=valor_pacote)
                
                title('E R R O !! --- Este campo não pode estar em branco.', 'vermelho')
                forma_de_pagamento = str(input('''\n==> Digite a forma de pagamento: '''))
            forma_de_pagamento = forma_de_pagamento[:100]
            break
        if forma_de_pagamento == '1':
            forma_de_pagamento = 'Dinheiro'
            break
        elif forma_de_pagamento == '2':
            forma_de_pagamento = 'Pix'
            break
        elif forma_de_pagamento == '3':
            forma_de_pagamento = 'Cartão'
            break
        elif forma_de_pagamento == '0':
            limpar_console()
            title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
            return
        else:
            limpar_console()
            title('E R R O !! --- Opção inválida. Tente novamente.', 'vermelho')
    
    limpar_console()
    ficha_aluno(nome=nome, telefone=telefone, data_pagamento=data_pagamento,
                nome_pacote=nome_pacote, valor_pacote=valor_pacote,
                forma_de_pagamento=forma_de_pagamento)
    # Adicionar observações
    observacoes = input("\n==> Digite observações (máximo 100 caracteres, 0 = abortar): ")
    observacoes = observacoes[:100]  # Limitar a 100 caracteres
    if observacoes == '0':
        limpar_console()
        title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
        return

    # Adiciona ou atualiza as informações do aluno no dicionário
    if nome not in data:
        data[nome] = {
            "Telefone": telefone,
            "Pagamentos": [],
            "Observacoes": observacoes
        }

    data[nome]["Pagamentos"].append({
        "Data Pagamento": data_pagamento,
        "Próximo Pagamento": proximo_pagamento,
        "Valor Pacote": valor_pacote,
        "Forma de Pagamento": forma_de_pagamento
    })
    limpar_console()
    # Salva o dicionário atualizado no arquivo JSON
    ficha_aluno(nome=nome, telefone=telefone, data_pagamento=data_pagamento,
                nome_pacote=nome_pacote, valor_pacote=valor_pacote,
                forma_de_pagamento=forma_de_pagamento, observacoes=observacoes)
    
    pergunta = input('\n==> CONFIRMAR REGISTRO? (Enter para confirmar, 0 = abortar): ').upper().strip()
    if pergunta == '0':
        limpar_console()
        title('Voltando ao Menu Principal. NENHUM registro foi salvo', 'azul')
        return
    salvar_dados()
    limpar_console()
    title(f"Informações do aluno {nome} adicionadas com SUCESSO!", 'verde')

def visualizar_alunos():
    limpar_console()
    title('Visualizar Alunos', 'azul')
    print('''
1. Consultar TODOS os alunos
2. Consultar aluno por NOME ou inicial do nome
3. Consultar aluno por MÊS e ANO de pagamento
4. Consultar alunos por DIA
5. Consultar NÃO PAGANTES''')

    opcao_visualizacao = input("\nEscolha uma opção: ")

    if opcao_visualizacao == '1':
        if not data:
            limpar_console()
            title("Nenhum aluno registrado.\n", 'azul')
            return

        limpar_console()
        print("===> Lista de Alunos: <===\n\n")
        for nome in sorted(data.keys()):
            info = data[nome]
            print(f"\nNome: {nome}")
            if 'Observacoes' in info:
                print(f"      Observações: {info['Observacoes']}")

            for pagamento in info['Pagamentos']:
                print(f"      Telefone: {info['Telefone']}")
                print(f"      Data de Pagamento: {pagamento['Data Pagamento']}")
                print(f"      Próximo Pagamento: {pagamento['Próximo Pagamento']}")
                print(f"      Valor da Mensalidade: R$ {pagamento['Valor Pacote']:.2f}")
                print(f"      Forma de Pagamento: {pagamento['Forma de Pagamento']}")
                print("-" * 30)

    elif opcao_visualizacao == '2':
        limpar_console()
        consulta = input("\n\n\n===>Digite o nome ou a inicial do nome do aluno: ").upper().strip()
        limpar_console()
        print("\n\n===>Resultado da Consulta:",consulta)
        
        encontrou_aluno = False
        
        for nome in sorted(data.keys()):
            if nome.startswith(consulta):
                encontrou_aluno = True
                info = data[nome]
                print(f"\nNome: {nome}")
                print(f"      Telefone: {info['Telefone']}")
                if 'Observacoes' in info:
                    print(f"      Observações: {info['Observacoes']}")
                for pagamento in info['Pagamentos']:
                    print(f"      Data de Pagamento: {pagamento['Data Pagamento']}")
                    print(f"      Próximo Pagamento: {pagamento['Próximo Pagamento']}")
                    print(f"      Valor da Mensalidade: R$ {pagamento['Valor Pacote']:.2f}")
                    print(f"      Forma de Pagamento: {pagamento['Forma de Pagamento']}")
                    print("-" * 30)
    
        if not encontrou_aluno:
            title("NENHUM aluno registrado com ESSE NOME", 'vermelho')

    elif opcao_visualizacao == '3':
        limpar_console()
        escolha_mes = input("Escolha uma opção:\n1. Esse mês\n2. Outro mês\nOpção: ")

        if escolha_mes == '1':
            mes_ano_consulta = datetime.datetime.now().strftime('%m-%Y')
        elif escolha_mes == '2':
            mes_ano_consulta = input("Digite o mês e ano que deseja consultar (formato MM-AAAA): ")
        else:
            title("Opção inválida. Tente novamente.", 'vermelho')
            return

        limpar_console()
        print("\nResultado da Consulta por Mês e Ano:",mes_ano_consulta)
        for nome in sorted(data.keys()):
            info = data[nome]
            for pagamento in info['Pagamentos']:
                mes_ano_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y').strftime('%m-%Y')
                if mes_ano_pagamento == mes_ano_consulta:
                    print(f"\nNome: {nome}")
                    print(f"      Telefone: {info['Telefone']}")
                    if 'Observacoes' in info:
                        print(f"      Observações: {info['Observacoes']}")
                    print(f"      Data de Pagamento: {pagamento['Data Pagamento']}")
                    print(f"      Próximo Pagamento: {pagamento['Próximo Pagamento']}")
                    print(f"      Valor da Mensalidade: R$ {pagamento['Valor Pacote']:.2f}")
                    print(f"      Forma de Pagamento: {pagamento['Forma de Pagamento']}")
                    print("-" * 30)

    elif opcao_visualizacao == '4':
        limpar_console()
        escolha_dia = input("Escolha uma opção:\n1. Hoje\n2. Outro dia\nOpção: ")

        if escolha_dia == '1':
            data_consulta = datetime.datetime.now().strftime('%d-%m-%Y')
        elif escolha_dia == '2':
            data_consulta = input("Digite a data que deseja consultar (formato DD-MM-AAAA): ")
        else:
            title("Opção inválida. Tente novamente.", 'vermelho')
            return

        limpar_console()
        print("\nResultado da Consulta por Dia:", data_consulta)
        for nome in sorted(data.keys()):
            info = data[nome]
            for pagamento in info['Pagamentos']:
                if pagamento['Data Pagamento'] == data_consulta:
                    print(f"\nNome: {nome}")
                    print(f"      Telefone: {info['Telefone']}")
                    if 'Observacoes' in info:
                        print(f"      Observações: {info['Observacoes']}")
                    print(f"      Data de Pagamento: {pagamento['Data Pagamento']}")
                    print(f"      Próximo Pagamento: {pagamento['Próximo Pagamento']}")
                    print(f"      Valor da Mensalidade: R$ {pagamento['Valor Pacote']:.2f}")
                    print(f"      Forma de Pagamento: {pagamento['Forma de Pagamento']}")
                    print("-" * 30)
    elif opcao_visualizacao == '5':
        limpar_console()
        if __name__ == "__main__":
            print('=== Verificar não Pagantes ===\n')
            data_input = input("Digite a data no formato MM-AAAA a partir da qual deseja verificar os não pagantes: ")

            try:
                mes_escolhido = datetime.datetime.strptime(data_input, "%m-%Y")
            except ValueError:
                limpar_console()
                title("E R R O !! ==> Formato de data inválido. Use o formato MM-AAAA.", 'vermelho')
            else:
                alunos_sem_pagamento_escolhida = alunos_sem_pagamento(mes_escolhido)

                if alunos_sem_pagamento_escolhida:
                    limpar_console()
                    print(f"vvvv Alunos SEM PAGAMENTO a partir de {data_input}: vvvv\n")
                    for nome in sorted(alunos_sem_pagamento_escolhida.keys()):
                        info = alunos_sem_pagamento_escolhida[nome]
                        print(f"\nNome: {nome}")
                        print(f"      Telefone: {info['Telefone']}")
                        if 'Observacoes' in info:
                            print(f"      Observações: {info['Observacoes']}")
                        for pagamento in info['Pagamentos']:
                            print(f"      Data de Pagamento: {pagamento['Data Pagamento']}")
                            print(f"      Próximo Pagamento: {pagamento['Próximo Pagamento']}")
                            print(f"      Valor da Mensalidade: R$ {pagamento['Valor Pacote']:.2f}")
                            print(f"      Forma de Pagamento: {pagamento['Forma de Pagamento']}")
                            print("-" * 30)
                    print(f'\n\n^^^^ Alunos SEM PAGAMENTO a partir de {data_input} ^^^^\n')
                else:
                    limpar_console()
                    print(f"Todos os alunos pagaram a partir de {data_input}.")
    else:
        limpar_console()
        title("E R R O !! ==> Opção inválida. Tente novamente.", 'vermelho')

def alunos_sem_pagamento(data_escolhida):
    academia_data = data

    if academia_data:
        alunos_sem_pagamento = {}
        for aluno, dados in academia_data.items():
            pagamentos = dados.get("Pagamentos", [])
            ultimo_pagamento = pagamentos[-1] if pagamentos else None

            if ultimo_pagamento:
                data_proximo_pagamento = datetime.datetime.strptime(ultimo_pagamento["Próximo Pagamento"], "%d-%m-%Y")
                if data_proximo_pagamento >= data_escolhida:
                    continue
            alunos_sem_pagamento[aluno] = dados  # Armazenar todas as informações do aluno

        return alunos_sem_pagamento

def apagar_aluno():
    limpar_console()
    if data:
        lista_alunos(data=data)
        print('(Para apagar um aluno ou registro,\ndigite o nome exato do aluno.Verifique o nome\nna lista acima.)\n')
    
    title("Apagar Registro de Aluno", 'amarelo')
    aluno_a_apagar = input("\n\n\nDigite o nome do aluno que deseja apagar: ").upper().strip()
    if aluno_a_apagar in data:
        limpar_console()
        print("\n=== Apagar Registro de Aluno ===\n")
        print("\nEscolha uma opção: ",aluno_a_apagar)
        print("1. Apagar aluno")
        print("2. Apagar um registro de pagamento")
        opcao = input()

        if opcao == '1':
            limpar_console()
            tem_certeza = input(f'!!!ATENÇÃO!!!\nVocê está prestes a EXCLUIR PERMANENTEMENTE o aluno {aluno_a_apagar}.\nTEM CERTEZA? S/N\n').upper()
            if tem_certeza == 'S':
                del data[aluno_a_apagar]
                salvar_dados()
                limpar_console()
                title(f"Aluno {aluno_a_apagar} removido com SUCESSO!", 'verde')
            else:
                limpar_console()
                title('NENHUM ALUNO FOI APAGADO','azul')
                return

        elif opcao == '2':
            limpar_console()
            print(f"\n===>Registros de pagamento para {aluno_a_apagar}:\n")
            for i, pagamento in enumerate(data[aluno_a_apagar]['Pagamentos']):
                print(f"{i + 1}. Data de Pagamento: {pagamento['Data Pagamento']} | Valor: R$ {pagamento['Valor Pacote']:.2f}")

            try:
                indice_pagamento = int(input("\nDigite o número do registro que deseja apagar: "))
                if 1 <= indice_pagamento <= len(data[aluno_a_apagar]['Pagamentos']):
                    del data[aluno_a_apagar]['Pagamentos'][indice_pagamento - 1]
                    salvar_dados()
                    limpar_console()
                    print(f"\n\n\n===>Registro de pagamento do aluno {aluno_a_apagar} removido com SUCESSO!\n\n\n")
                else:
                    limpar_console()
                    title("E R R O !! ==> Índice inválido. Nenhum registro removido.\n", 'vermelho')
            except ValueError:
                limpar_console()
                title("E R R O !! ==> Entrada inválida. Nenhum registro removido.\n", 'vermelho')

        else:
            limpar_console()
            title("E R R O !! ==> Opção inválida. Nenhum registro removido.\n", 'vermelho')

    else:
        limpar_console()
        title(f"\nAluno {aluno_a_apagar} não encontrado.\n", 'vermelho')

def consultar_entradas():
    limpar_console()
    title('ENTRADAS', 'verde')
    opcao = input('''1. DIA
2. MÊS

Escolha uma opção: ''')
    if opcao == '1':
        limpar_console()
        print("\n=== Entradas Diárias ===")
        if not data:
            limpar_console()
            title("Nenhum aluno registrado.\n", 'azul')
            return

        usar_dia_atual = input("Deseja usar o dia de hoje para a consulta? (S/N): ").strip().lower()
        
        if usar_dia_atual == 's':
            data_atual = datetime.datetime.now()
            dia_consulta = str(data_atual.day)
            mes_ano_consulta = data_atual.strftime('%m-%Y')
        else:
            dia_consulta = input("Digite o DIA (formato DD): ")
            mes_ano_consulta = input("Digite o MÊS (formato MM-AAAA): ")

        if not dia_consulta.isdigit() or not 1 <= int(dia_consulta) <= 31:
            limpar_console()
            title("Por favor, digite um dia válido.", 'vermelho')
            return

        total_entradas_diarias = 0.0
        total_alunos_pagantes = 0

        for nome in data.keys():
            info = data[nome]
            for pagamento in info['Pagamentos']:
                data_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y')
                if data_pagamento.day == int(dia_consulta) and data_pagamento.strftime('%m-%Y') == mes_ano_consulta:
                    total_entradas_diarias += pagamento['Valor Pacote']
                    total_alunos_pagantes += 1
    
        limpar_console()
        print(f"\n\nTotal de Entradas Diárias para {dia_consulta}-{mes_ano_consulta}: R$ {total_entradas_diarias:.2f}")
        print(f"Total de Alunos que Pagaram: {total_alunos_pagantes}\n")


################################ INICIO DO FILTRO DE ENTRADAS ###########################

        while True:
            total_entradas_diarias = 0
            total_alunos_pagantes = 0

            filtro = str(input('''Filtrar entradas por:
    1. Dinheiro
    2. Cartão/Pix
    3. Outras formas
                               
    0. Voltar ao Menu Principal
        
        -> Sua opção: '''))
            if filtro not in '0123' or filtro == '':
                limpar_console()
                title('E R R O !! ==> OPÇÃO INVÁLIDA', 'vermelho')
                continue
            if filtro == '0':
                limpar_console()
                title('Voltando ao Menu Principal.', 'azul')
                return
            elif filtro == '1':
                limpar_console()
                for nome in data.keys():
                    info = data[nome]
                    for pagamento in info['Pagamentos']:
                        if pagamento['Forma de Pagamento'] == 'Dinheiro':
                            data_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y')
                            if data_pagamento.day == int(dia_consulta) and data_pagamento.strftime('%m-%Y') == mes_ano_consulta:
                                print(f'''\nAluno: {nome}\nValor: {pagamento['Valor Pacote']}\nForma de Pagamento: {pagamento['Forma de Pagamento']}\n{'-'*30}''')
                                total_entradas_diarias += pagamento['Valor Pacote']
                                total_alunos_pagantes += 1
                print(f"\n\nTotal de Entradas Diárias (EM DINHEIRO) para {dia_consulta}-{mes_ano_consulta}: R$ {total_entradas_diarias:.2f}")
                print(f"Total de Alunos que Pagaram (EM DINHEIRO): {total_alunos_pagantes}\n")

            elif filtro == '2':
                limpar_console()
                for nome in data.keys():
                    info = data[nome]
                    for pagamento in info['Pagamentos']:
                        if pagamento['Forma de Pagamento'] in ['Cartão', 'Pix']:
                            data_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y')
                            if data_pagamento.day == int(dia_consulta) and data_pagamento.strftime('%m-%Y') == mes_ano_consulta:
                                print(f'''\nAluno: {nome}\nValor: {pagamento['Valor Pacote']}\nForma de Pagamento: {pagamento['Forma de Pagamento']}\n{'-'*30}''')
                                total_entradas_diarias += pagamento['Valor Pacote']
                                total_alunos_pagantes += 1
                print(f"\n\nTotal de Entradas Diárias (PIX/CARTÃO) para {dia_consulta}-{mes_ano_consulta}: R$ {total_entradas_diarias:.2f}")
                print(f"Total de Alunos que Pagaram (PIX/CARTÃO): {total_alunos_pagantes}\n")
            elif filtro == '3':
                limpar_console()
                for nome in data.keys():
                    info = data[nome]
                    for pagamento in info['Pagamentos']:
                        if pagamento['Forma de Pagamento'] not in ['Dinheiro','Pix','Cartão']:
                            data_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y')
                            if data_pagamento.day == int(dia_consulta) and data_pagamento.strftime('%m-%Y') == mes_ano_consulta:
                                print(f'''\nAluno: {nome}\nValor: {pagamento['Valor Pacote']}\nForma de Pagamento: {pagamento['Forma de Pagamento']}\n{'-'*30}''')
                                total_alunos_pagantes += 1
                print(f"\nTotal de Alunos que Pagaram (OUTRAS FORMAS): {total_alunos_pagantes}\n")
            title('Pressione ENTER para retornar aos filtros:', 'amarelo')
            input()
            



################################ FIM DO FILTRO DE ENTRADAS ###########################





    elif opcao == '2':
        limpar_console()
        print("\n=== Entradas Mensais ===")
        if not data:
            title("Nenhum aluno registrado.\n", 'azul')
            return

        escolha_mes_atual = input("\nDeseja usar o mês atual? (S/N): ").upper()

        if escolha_mes_atual == 'S':
            mes_ano_consulta = datetime.datetime.now().strftime('%m-%Y')
        else:
            formato_correto = False
            while not formato_correto:        
                mes_ano_consulta = input("\nDigite o mês e ano que deseja consultar (formato MM-AAAA): ")
                # Utilize expressão regular para verificar o formato
                if match(r'^\d{2}-\d{4}$', mes_ano_consulta):
                    formato_correto = True
                else:
                    limpar_console()
                    title("Formato INCORRETO. Por favor, insira no formato correto (MM-AAAA).\n", 'vermelho')
                    return

        total_entradas_mensais = 0.0
        total_alunos_pagantes = 0

        for nome in data.keys():
            info = data[nome]
            for pagamento in info['Pagamentos']:
                mes_ano_pagamento = datetime.datetime.strptime(pagamento['Data Pagamento'], '%d-%m-%Y').strftime('%m-%Y')
                if mes_ano_pagamento == mes_ano_consulta:
                    total_entradas_mensais += pagamento['Valor Pacote']
                    total_alunos_pagantes += 1

        limpar_console()
        print(f"\nTotal de Entradas Mensais para {mes_ano_consulta}: R$ {total_entradas_mensais:.2f}")
        print(f"Total de Alunos que Pagaram: {total_alunos_pagantes}\n")
    else:
        limpar_console()
        title('E R R O !! ==> OPÇÃO INVÁLIDA', 'vermelho')
        return

def editar_registro():
    limpar_console()
    
    # Exibir lista de alunos em ordem alfabética
    if data:
        lista_alunos(data=data)
        print('(Para editar informações de registro,\ndigite o nome exato do aluno.Verifique o nome\nna lista acima.)')

    # Solicitar ao usuário escolher o aluno
    title("Editar Registro", 'amarelo')
    aluno_escolhido = input("\n\n\nDigite o nome do aluno que deseja editar: ").upper().strip()

    # Verificar se o aluno existe no arquivo
    if aluno_escolhido not in data:
        limpar_console()
        title("Aluno não encontrado. Saindo.", 'azul')
        return

    # Exibir registros de pagamento do aluno escolhido
    registros = data[aluno_escolhido]['Pagamentos']
    limpar_console()
    print(f"\n===> Registros de Pagamento para {aluno_escolhido}:\n")
    for i, registro in enumerate(registros, start=1):
        print(f"{i}. Data: {registro['Data Pagamento']}, Valor: {registro['Valor Pacote']}")

    # Solicitar ao usuário escolher o registro de pagamento
    try:
        indice_registro = int(input("\n===> Escolha o número do registro de pagamento que deseja editar: ")) - 1
        registro_escolhido = registros[indice_registro]
    except (ValueError, IndexError):
        limpar_console()
        title("Opção inválida. Saindo.", 'vermelho')
        return

    # Solicitar ao usuário escolher o que deseja editar
    limpar_console()
    print("\n===> Escolha o que deseja editar: {} <===".format(aluno_escolhido))
    print("1. Nome do aluno")
    print("2. Telefone")
    print("3. Pacote de pagamento")
    print("4. Observações")

    try:
        opcao = int(input("\nEscolha uma opção: "))
    except ValueError:
        limpar_console()
        title("Opção inválida. Saindo.", 'vermelho')
        return

    if opcao == 1:
        novo_nome = input("Digite o novo nome: ").strip().upper()

        # Verificar se o novo nome já existe nos registros
        if novo_nome in data and novo_nome != aluno_escolhido:
            limpar_console()
            title("O nome já existe nos registros. Nenhuma edição foi feita.", 'azul')
            return

        # Verificar se o novo nome não está em branco ou contém apenas espaços
        if not novo_nome:
            limpar_console()
            title("Nome inválido. Saindo.", 'vermelho')
            return

        data[novo_nome] = data.pop(aluno_escolhido)
        
    elif opcao == 2:
        novo_telefone = input("Digite o novo número de telefone: ")
        data[aluno_escolhido]['Telefone'] = novo_telefone
    elif opcao == 3:
        novo_pacote = float(input("Digite o novo valor do pacote de pagamento: "))
        registro_escolhido['Valor Pacote'] = novo_pacote
    elif opcao == 4:
        novas_observacoes = input("Digite as novas observações: ")
        data[aluno_escolhido]['Observacoes'] = novas_observacoes
    else:
        limpar_console()
        title("Opção inválida. Saindo.", 'vermelho')
        return

    # Salvar alterações
    salvar_dados()
    limpar_console()
    title(f"Edição para o aluno {aluno_escolhido} concluída com SUCESSO!", 'verde')
    title(f'REINICIE O PROGRAMA para atualizar as informações.', 'azul')

while True:
    title("ACADEMIA ELITE FITNESS", 'amarelo')

    print(f'''1.  Adicionar Aluno/Pagamento
2.  Consultar Aluno/Pagamento
3.  Apagar Aluno/Registro
4.  Consultar Entradas
5.  Editar Registro
6.  Sair''')
    opcao = input("\nEscolha uma opção: ")

    if opcao == '1':
        adicionar_aluno()
    elif opcao == '2':
        visualizar_alunos()
    elif opcao == '3':
        apagar_aluno()
    elif opcao == '4':
        consultar_entradas()
    elif opcao == '5':
        editar_registro()
    elif opcao == '6':
        limpar_console()
        input('Pressione ENTER para sair do programa: ')
        break
    else:
        limpar_console()
        title("E R R O !! --- Opção inválida. Tente novamente.", 'vermelho')
