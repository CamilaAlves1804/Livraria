# titulo
print('Bem vindo a Livraria [NOME]!')
print('-' * 32)
print('-' * 8, 'MENU PRINCIPAL', '-' * 8)


# lista para os livros
lista_livro = []

# criar id para cada livro
id_global = 1

# criar função para o cadastro dos livros
def cadastrar_livro(id):
    print('-' * 5, 'MENU CADASTRAR LIVRO', '-' * 5)
    global id_global
    id_global += 1
    print(f'ID do livro a ser cadastrado: {id}')
    nome = input('Por favor entre com o nome do livro: ')
    autor = input('Por favor entre com o nome do autor do livro: ')
    editora = input('Por favor entre com o nome da editora do livro: ')
    livro = {'id': id, 'nome': nome, 'autor': autor, 'editora': editora}
    # adicionar livro a lista
    lista_livro.append(livro)
    print('Livro cadastrado!')
    print('-' * 32)

# criar função para a consulta dos livros
def consultar_livro():
    print('-' * 5, 'MENU CONSULTAR LIVRO', '-' * 5)
    while True:
        consulta = input('Escolha a opção desejada:\n'
                         '1 - Consultar todos os livros\n'
                         '2 - Consultar livros pelo ID\n'
                         '3 - Consultar livro(s) pelo autor\n'
                         '4 - Retornar ao menu principal\n'
                         '>> ')
        print('-' * 32)
        if consulta == '1':
            if lista_livro == []:
                print('Sem livros cadastrados no momento!')
                break
            else:
                for livro in lista_livro:
                    print('-' * 32)
                    print(f'ID: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')
                    print('-' * 32)
                print()
        elif consulta == '2':
            consulta_id = int(input('Digite o ID do livro: '))
            print('-' * 32)
            livro_encontrado = False
            for livro in lista_livro:
                if livro['id'] == consulta_id:
                    print('-' * 32)
                    print(f'ID: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')
                    print('-' * 32)
                    livro_encontrado = True
                    break
            if not livro_encontrado:
                print('ID inválido. Tente novamente!')
            print()
        elif consulta == '3':
            consulta_autor = input('Digite o autor do(s) livro(s): ')
            print('-' * 32)
            livro_encontrado = False
            for livro in lista_livro:
                if livro['autor'] == consulta_autor:
                    print('-' * 32)
                    print(f'ID: {livro["id"]}')
                    print(f'Nome: {livro["nome"]}')
                    print(f'Autor: {livro["autor"]}')
                    print(f'Editora: {livro["editora"]}')
                    print('-' * 32)
                    livro_encontrado = True
            if not livro_encontrado:
                print('Autor não encontrado. Tente novamente!')
            print()
        elif consulta == '4':
            print('Retornando ao menu principal')
            print('-' * 32)
            break
        else:
            print('Opção inválida!')

# criar função para remover livros
def remover_livro():
    print('-' * 32)
    print('-' * 6, 'MENU REMOVER LIVRO', '-' * 6)
    remover_id = int(input('Digite o ID do livro a ser removido: '))
    livro_encontrado = False
    for livro in lista_livro:
        if livro['id'] == remover_id:
            lista_livro.remove(livro)
            print('Livro removido com sucesso!')
            livro_encontrado = True
            break
    if not livro_encontrado:
        print('ID de livro não encontrado. Tente novamente!')

# menu principal
while True:
    esc_opc = input('Escolha a opção desejada\n'
                        '1 - Cadastrar livro\n'
                        '2 - Consultar livro(s)\n'
                        '3 - Remover livro\n'
                        '4 - Sair\n'
                        '>> ')

    # aplicando as funções
    if esc_opc == '1':
        cadastrar_livro(id_global)
    elif esc_opc == '2':
        consultar_livro()
    elif esc_opc == '3':
        remover_livro()
    elif esc_opc == '4':
        print('Encerrando o programa.')
        break
    else:
        print('Opção inválida. Tente novamente!')
