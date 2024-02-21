import random

nomes = ['João da Silva', 'Maria Oliveira', 'Pedro Santos', 'Ana Souza', 'Lucas Pereira']
emails = ['joao.silva@example.com', 'maria.oliveira@example.com', 'pedro.santos@example.com', 'ana.souza@example.com', 'lucas.pereira@example.com']
telefones = ['(11) 91234-5678', '(21) 98765-4321', '(31) 99876-5432', '(41) 98765-1234', '(51) 91234-5678']
cidades = ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba', 'Porto Alegre']
estados = ['São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Paraná', 'Rio Grande do Sul']

def pegar_opcoes():
    print('=' * 82)
    print('Bem-vindo ao Gerador de Dados de Teste - Para finalizar o programa, digite "Parar"')
    print('-' * 82)

    print('Escolher uma ou mais opções a baixo a serem geradas aleatóriamente: \n'
          '[1] - Nome \n'
          '[2] - E-mail \n'
          '[3] - Telefone \n'
          '[4] - Cidade \n'
          '[5] - Estado')
    return input('Digite uma(as) opções: ')

def gerar_dados(opcao):
    if opcao == 1:
        dado = random.choice(nomes)
    elif opcao == 2:
        dado = random.choice(emails)
    elif opcao == 3:
        dado = random.choice(telefones)
    elif opcao == 4:
        dado = random.choice(cidades)
    elif opcao == 5:
        dado = random.choice(estados)
    return f'{dado}'

def mostrar_dados_na_tela(dados_a_mostrar):
    print('Dados Gerados:')
    for dado in dados_a_mostrar:
        print(dado)

def salvar_dados(dados_a_mostrar):
    salvar = input('Gostaria de salvar os dados em um arquivo de texto?(s/n): ')
    if salvar.lower() == 's':
        with open('dados.txt', 'a', newline='') as arquivo:
            for dado in dados_a_mostrar:
                arquivo.write(dado + '\n')
        print('Dados salvos com sucesso!')

def main():
    while True:
        opcoes = pegar_opcoes()
        if opcoes.lower() == 'parar':
            break

        opcoes_lista = [int(op) for op in opcoes.split(',') if op.strip().isdigit()]
        dados_a_mostrar = [gerar_dados(opcao) for opcao in opcoes_lista]
        mostrar_dados_na_tela(dados_a_mostrar)
        salvar_dados(dados_a_mostrar)
    print('Programa encerrado!')

if __name__ == "__main__":
    main()
