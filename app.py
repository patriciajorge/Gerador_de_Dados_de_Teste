import random

nomes = ['João da Silva', 'Maria Oliveira', 'Pedro Santos', 'Ana Souza', 'Lucas Pereira']
emails = ['joao.silva@example.com', 'maria.oliveira@example.com', 'pedro.santos@example.com', 'ana.souza@example.com', 'lucas.pereira@example.com']
telefones = ['(11) 91234-5678', '(21) 98765-4321', '(31) 99876-5432', '(41) 98765-1234', '(51) 91234-5678']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
estados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Paraná', 'Rio Grande do Sul']

while True:
    print('Bem-vindo ao Gerador de Dados de Teste - Para finalizar o programa, digite "Parar"')
    print('-'*60)

    print('Escolher uma ou mais opções a baixo a serem geradas aleatóriamente: \n'
          '[1] - Nome \n'
          '[2] - E-mail \n'
          '[3] - Telefone \n'
          '[4] - Cidade \n'
          '[5] - Estado')
    opcoes = input('Digite uma(as) opções: ')

    if opcoes.lower() == 'parar':
        break

    opcoes_lista = [int(op) for op in opcoes.split(',') if op.strip().isdigit()]

    dados_a_mostrar = []

    for opcao in opcoes_lista:
        if opcao == 1:
            dado = random.choice(nomes)
            dados_a_mostrar.append(f'Nome: {dado}')
        elif opcao == 2:
            dado = random.choice(emails)
            dados_a_mostrar.append(f'E-mail: {dado}')
        elif opcao == 3:
            dado = random.choice(telefones)
            dados_a_mostrar.append(f'Telefone: {dado}')
        elif opcao == 4:
            dado = random.choice(cidades)
            dados_a_mostrar.append(f'Cidade: {dado}')
        elif opcao == 5:
            dado = random.choice(estados)
            dados_a_mostrar.append(f'Estado: {dado}')

    print('Dados Gerados:')
    for dado in dados_a_mostrar:
        print(dado)

    salvar = input('Gostaria de salvar os dados em um arquivo de texto?(s/n): ')
    if salvar.lower() == 's':
        with open('dados.txt', 'a', newline='') as arquivo:
            for dado in dados_a_mostrar:
                arquivo.write(dado + '\n')
        print('Dados salvos com sucesso!')
