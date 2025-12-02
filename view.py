import sqlite3

# Conectar ao banco de dados 
def connect():
    conn = sqlite3.connect('dados.db')
    return conn 

# Função para inserir um novo livro
def insert_book(titulo, autor, editora, ano_publicacao, isbn):
    conn = connect()
    conn.execute("INSERT INTO livros(titulo, autor, editora, ano_publicacao, isbn) VALUES (?, ?, ?, ?, ?)",
                 (titulo, autor, editora, ano_publicacao, isbn))
    conn.commit()
    conn.close()

# Função para inserir usuários 
def insert_user(nome, sobrenome, endereco, email, telefone):
    conn = connect()
    conn.execute("INSERT INTO usuarios(nome, sobrenome, endereco, email, telefone) VALUES (?, ?, ?, ?, ?)",
                 (nome, sobrenome, endereco, email, telefone))
    conn.commit()
    conn.close()

# Função para exibir usuários
def get_users():
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT * FROM usuarios")
    users = c.fetchall()
    conn.close()
    return users

# Função para exibir os livros
def exibir_livros():
    conn = connect()
    livros = conn.execute("SELECT * FROM livros").fetchall()
    conn.close()
    return livros

# Função para realizar empréstimos
def insert_loan(id_livro, id_usuario, data_emprestimo, data_devolucao=None):
    conn = connect()
    conn.execute("INSERT INTO emprestimos(id_livro, id_usuario, data_emprestimo, data_devolucao) VALUES (?, ?, ?, ?)",
                 (id_livro, id_usuario, data_emprestimo, data_devolucao))
    conn.commit()
    conn.close()

# Função para recuperar todos os livros emprestados no momento
def get_books_on_loan():
    conn = connect()
    result = conn.execute("SELECT emprestimos.id, livros.titulo, usuarios.nome, usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                           FROM livros \
                           INNER JOIN emprestimos ON livros.id = emprestimos.id_livro \
                           INNER JOIN usuarios ON usuarios.id = emprestimos.id_usuario \
                           WHERE emprestimos.data_devolucao IS NULL").fetchall()
    conn.close()
    return result

# Função para atualizar a data de devolução de empréstimo
def update_loan_return_date(id_emprestimo, data_devolucao):
    conn = connect()
    conn.execute("UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (data_devolucao, id_emprestimo))
    conn.commit()
    conn.close()

# Exemplo de inserção de livro, usuário e empréstimo
# insert_book("Dom Quixote", "Miguel de Cervantes", "Editora 1", 1605, "123456789")
# insert_user("João", "Silva", "Rua A, 123", "joao@gmail.com", "123456789")
# insert_loan(1, 1, "2024-01-01")

# Recuperando e exibindo livros emprestados
# livros_emprestados = get_books_on_loan()
# print(livros_emprestados)
