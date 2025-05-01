import mysql.connector
import time

# Aguarda o MySQL estar pronto
time.sleep(2)

def conectar():
    return mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",
        database="db"
    )

def inserir_filme():
    titulo = input("Título: ")
    diretor_id = input("ID do Diretor: ")
    genero_id = input("ID do Gênero: ")
    ano = input("Ano de lançamento: ")
    classificacao = input("Classificação indicativa: ")

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO filmes (titulo, diretor_id, genero_id, ano_lancamento, classificacao_indicativa) VALUES (%s, %s, %s, %s, %s)",
        (titulo, diretor_id, genero_id, ano, classificacao)
    )
    conn.commit()
    print("Filme inserido com sucesso!\n")
    conn.close()

def listar_filmes():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT f.id, f.titulo, d.nome, g.nome, f.ano_lancamento, f.classificacao_indicativa
        FROM filmes f
        JOIN diretores d ON f.diretor_id = d.id
        JOIN generos g ON f.genero_id = g.id
    """)
    filmes = cursor.fetchall()
    print("\n--- Lista de Filmes ---")
    for f in filmes:
        print(f"ID: {f[0]}, Título: {f[1]}, Diretor: {f[2]}, Gênero: {f[3]}, Ano: {f[4]}, Classificação: {f[5]}")
    print()
    conn.close()

def atualizar_filme():
    id_filme = input("ID do filme a atualizar: ")

    conn = conectar()
    cursor = conn.cursor()

    # Busca o filme atual
    cursor.execute("SELECT titulo, diretor_id, genero_id, ano_lancamento, classificacao_indicativa FROM filmes WHERE id = %s", (id_filme,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Filme não encontrado.\n")
        conn.close()
        return

    titulo_atual, diretor_atual, genero_atual, ano_atual, classificacao_atual = resultado

    print("\nDeixe em branco para manter o valor atual.\n")
    novo_titulo = input(f"Título ({titulo_atual}): ") or titulo_atual
    novo_diretor = input(f"ID do Diretor ({diretor_atual}): ") or diretor_atual
    novo_genero = input(f"ID do Gênero ({genero_atual}): ") or genero_atual
    novo_ano = input(f"Ano de Lançamento ({ano_atual}): ") or ano_atual
    nova_classificacao = input(f"Classificação ({classificacao_atual}): ") or classificacao_atual

    cursor.execute("""
        UPDATE filmes 
        SET titulo = %s, diretor_id = %s, genero_id = %s, ano_lancamento = %s, classificacao_indicativa = %s 
        WHERE id = %s
    """, (novo_titulo, novo_diretor, novo_genero, novo_ano, nova_classificacao, id_filme))

    conn.commit()
    print("Filme atualizado com sucesso!\n")
    conn.close()


def deletar_filme():
    id_filme = input("ID do filme a deletar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM filmes WHERE id = %s", (id_filme,))
    conn.commit()
    print("Filme deletado com sucesso!\n")
    conn.close()

def menu():
    while True:
        print("==== MENU CRUD ====")
        print("1. Inserir novo filme")
        print("2. Listar todos os filmes")
        print("3. Atualizar filme por ID")
        print("4. Deletar filme por ID")
        print("5. Sair")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            inserir_filme()
        elif escolha == '2':
            listar_filmes()
        elif escolha == '3':
            atualizar_filme()
        elif escolha == '4':
            deletar_filme()
        elif escolha == '5':
            print("Encerrando...")
            break
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
