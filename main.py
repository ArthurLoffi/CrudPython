# Conectando com o banco de dados
import pymysql

conexao = pymysql.connect(
    host='localhost',
    user='root',
    password='root',
    database='crud_python',
)

cursor = conexao.cursor()

# CRUD
opcao = input("O que deseja fazer? Criar[C]/Ler[L]/Atualizar[A]/Excluir[E]: ")
continuacao = "S"
if len(opcao) == 1:
    while continuacao == "S":
        if opcao == "C":
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o valor do produto: "))
            sql = f'INSERT INTO produtos (nome, preco) VALUES ("{produto}", {preco})'
            cursor.execute(sql)
            conexao.commit()
            print("Produto adicionado com sucesso!")
        if opcao == "L":
            print("PRODUTOS\n")
            sql_read = 'SELECT * FROM produtos'
            cursor.execute(sql_read)
            produtos = cursor.fetchall()
            print(produtos)
        continuacao = input("Deseja continuar? [S]/[N]: ")
    print("Você optou sair.")
    exit()
else:
    print("Digite somente a letra em [].")
    exit()

# CREATE

# READ

# UPDATE
# DELETE
cursor.close()
conexao.close()
