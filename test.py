import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    port=3307,
    user='root',
    password='2712',
    database='sistema'
)

cursor = conexao.cursor()


def listar_reclamacoes():
    cursor.execute("SELECT * FROM reclamacoes")
    resultados = cursor.fetchall()

    if len(resultados) == 0:
        print('Nenhuma reclamação encontrada')
    else:
        for reclam in resultados:
            print(f"\nid: {reclam[0]}")
            print(f"Título: {reclam[1]}")
            print(f"Comentário: {reclam[2]}")


def registrar_reclamacao():
    titulo = input('Sobre o que seria a reclamação? ')
    comentario = input('Deixe o seu comentário: ')

    comando = "INSERT INTO reclamacoes (titulo, comentario) VALUES (%s, %s)"
    valores = (titulo, comentario)

    cursor.execute(comando, valores)
    conexao.commit()

    print('Reclamação registrada!')


def pesquisar_reclamacao():
    busca = int(input('Digite a id do comentário: '))

    comando = "SELECT * FROM reclamacoes WHERE id = %s"
    cursor.execute(comando, (busca,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Título: {resultado[1]}")
        print(f"Comentário: {resultado[2]}")
    else:
        print('Reclamação não encontrada.')


def atualizar_reclamacao():
    busca = int(input('Digite a id do comentário a ser atualizado: '))

    novo_titulo = input('Novo titulo: ')
    novo_comentario = input('Novo comentario: ')

    comando = "UPDATE reclamacoes SET titulo = %s, comentario = %s WHERE id = %s"
    valores = (novo_titulo, novo_comentario, busca)

    cursor.execute(comando, valores)
    conexao.commit()

    if cursor.rowcount > 0:
        print('Reclamação atualizada.')
    else:
        print('Reclamação não encontrada')


def remover_reclamacao():
    busca = int(input('Digite a id do comentário a ser removido: '))

    comando = "DELETE FROM reclamacoes WHERE id = %s"
    cursor.execute(comando, (busca,))
    conexao.commit()

    if cursor.rowcount > 0:
        print('Reclamação removida')
    else:
        print('Reclamação não encontrada.')


def quantidade_de_reclamacoes():
    cursor.execute("SELECT COUNT(*) FROM reclamacoes")
    total = cursor.fetchone()[0]

    print(f"Total de reclamações: {total}")


def suporte():
    print('Algum problema?, podemos ajudar!')
    print(" ")

    print("1 - Meus comentários não estão sendo enviados")
    print("2 - Enviei um comentário errado, como apagar?")
    print("3 - O sistema está lento")
    print("4 - Erro ao abrir a plataforma")
    print("5 - Voltar")

    print(" ")

    opcao = int(input("O que está acontecendo? "))

    if opcao == 1:
        print("Verifique sua conexão com a internet.")
    elif opcao == 2:
        print("Use a opção de remover reclamação pelo ID.")
    elif opcao == 3:
        print("Feche apps em segundo plano.")
    elif opcao == 4:
        print("Reinicie o sistema.")
    elif opcao == 5:
        return
    else:
        print("Opção inválida.")


def menu():
    while True:
        print(" ")
        print("<=========== MENU ===========>")

        print('1 - Listar reclamações')
        print('2 - Registrar reclamação')
        print('3 - Pesquisar por ID')
        print('4 - Atualizar reclamação')
        print('5 - Remover reclamação')
        print('6 - Quantidade total')
        print('7 - Suporte')
        print('0 - Sair')

        opcao = int(input('Digite uma opção: '))

        if opcao == 1:
            listar_reclamacoes()

        elif opcao == 2:
            registrar_reclamacao()

        elif opcao == 3:
            pesquisar_reclamacao()

        elif opcao == 4:
            atualizar_reclamacao()

        elif opcao == 5:
            remover_reclamacao()

        elif opcao == 6:
            quantidade_de_reclamacoes()

        elif opcao == 7:
            suporte()

        elif opcao == 0:
            print('Saindo...')
            break

        else:
            print('Opção inválida')


menu()
