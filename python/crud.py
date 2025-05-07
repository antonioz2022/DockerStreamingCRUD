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

# Funções para filmes
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

# Funções para diretores
def inserir_diretor():
    nome = input("Nome do Diretor: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO diretores (nome) VALUES (%s)", (nome,))
    conn.commit()
    print("Diretor inserido com sucesso!\n")
    conn.close()

def listar_diretores():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM diretores")
    diretores = cursor.fetchall()
    print("\n--- Lista de Diretores ---")
    for d in diretores:
        print(f"ID: {d[0]}, Nome: {d[1]}")
    print()
    conn.close()

def atualizar_diretor():
    id_diretor = input("ID do Diretor a atualizar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM diretores WHERE id = %s", (id_diretor,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Diretor não encontrado.\n")
        conn.close()
        return

    nome_atual = resultado[0]
    novo_nome = input(f"Novo nome ({nome_atual}): ") or nome_atual

    cursor.execute("UPDATE diretores SET nome = %s WHERE id = %s", (novo_nome, id_diretor))
    conn.commit()
    print("Diretor atualizado com sucesso!\n")
    conn.close()

def deletar_diretor():
    id_diretor = input("ID do Diretor a deletar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM diretores WHERE id = %s", (id_diretor,))
    conn.commit()
    print("Diretor deletado com sucesso!\n")
    conn.close()

# Funções para gêneros
def inserir_genero():
    nome = input("Nome do Gênero: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO generos (nome) VALUES (%s)", (nome,))
    conn.commit()
    print("Gênero inserido com sucesso!\n")
    conn.close()

def listar_generos():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM generos")
    generos = cursor.fetchall()
    print("\n--- Lista de Gêneros ---")
    for g in generos:
        print(f"ID: {g[0]}, Nome: {g[1]}")
    print()
    conn.close()

def atualizar_genero():
    id_genero = input("ID do Gênero a atualizar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM generos WHERE id = %s", (id_genero,))
    resultado = cursor.fetchone()

    if not resultado:
        print("Gênero não encontrado.\n")
        conn.close()
        return

    nome_atual = resultado[0]
    novo_nome = input(f"Novo nome ({nome_atual}): ") or nome_atual

    cursor.execute("UPDATE generos SET nome = %s WHERE id = %s", (novo_nome, id_genero))
    conn.commit()
    print("Gênero atualizado com sucesso!\n")
    conn.close()

def deletar_genero():
    id_genero = input("ID do Gênero a deletar: ")
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM generos WHERE id = %s", (id_genero,))
    conn.commit()
    print("Gênero deletado com sucesso!\n")
    conn.close()

def listar_qtd_filmes_por_diretor():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT d.nome AS diretor, COUNT(f.id) AS total_filmes
        FROM diretores d
        LEFT JOIN filmes f ON d.id = f.diretor_id
        GROUP BY d.nome
    """)

    resultados = cursor.fetchall()
    print("\n--- Quantidade de Filmes por Diretor ---")
    for diretor, total in resultados:
        print(f"Diretor: {diretor} | Total de Filmes: {total}")
    print()
    conn.close()

# Menu principal
def menu():
    while True:
        print("==== MENU ====")
        print("1. Inserir")
        print("2. Listar")
        print("3. Atualizar")
        print("4. Deletar")
        print("5. Ver total de filmes por diretor")
        print("6. Sair")

        acao = input("Escolha uma ação: ")

        if acao == '6':
            print("Encerrando...")
            break
        elif acao == '5':
            listar_qtd_filmes_por_diretor()
            continue

        print("\n== Em qual tabela? ==")
        print("1. Filme")
        print("2. Diretor")
        print("3. Gênero")

        tabela = input("Escolha a tabela: ")

        if acao == '1': 
            if tabela == '1':
                inserir_filme()
            elif tabela == '2':
                inserir_diretor()
            elif tabela == '3':
                inserir_genero()
        elif acao == '2':  
            if tabela == '1':
                listar_filmes()
            elif tabela == '2':
                listar_diretores()
            elif tabela == '3':
                listar_generos()
        elif acao == '3':  
            if tabela == '1':
                atualizar_filme()
            elif tabela == '2':
                atualizar_diretor()
            elif tabela == '3':
                atualizar_genero()
        elif acao == '4':  
            if tabela == '1':
                deletar_filme()
            elif tabela == '2':
                deletar_diretor()
            elif tabela == '3':
                deletar_genero()
        else:
            print("Opção inválida.\n")

if __name__ == "__main__":
    menu()
