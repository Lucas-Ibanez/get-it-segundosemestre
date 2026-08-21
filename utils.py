import sqlite3

def iniciar_db():
    # Abrir conexão
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    # O IF NOT EXISTS impede que o programa quebre se a tabela já existir
    cursor.execute("CREATE TABLE IF NOT EXISTS note (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, content TEXT)")

    # Commitar a conexão
    conexao.commit()

    # Fechar conexão
    conexao.close()

def obter_notas():
    # Abrir conexão
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()

    # Executar comando SLQ e transformar conteúdo em uma lista de tuplas
    cursor.execute("SELECT * FROM note")
    notas = cursor.fetchall()

    # Fechar conexão
    conexao.close()

    # Retornar conteúdo de notas
    return notas

def adicionar_nota(titulo, detalhes):
    # Abrir conexão
    conexao = sqlite3.connect("banco.db")
    cursor = conexao.cursor()
    
    # Executar comando SLQ e salvar novas notas
    cursor.execute("INSERT INTO note (title, content) VALUES (?, ?)", (titulo, detalhes))

    # Commitar mudanças
    conexao.commit()

    # Fechar conexão
    conexao.close()

def load_template(nome_template):
    with open(f"static/templates/{nome_template}", "r") as arquivo_template:
        conteudo_arquivo = arquivo_template.read()

    return conteudo_arquivo
