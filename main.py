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
continuacao = "S"
while continuacao == "S":
    opcao = input("O que deseja fazer? Criar[C]/Ler[L]/Atualizar[A]/Excluir[E]: ")
    if len(opcao) == 1:

        # CREATE
        if opcao == "C":
            produto = input("Digite o nome do produto: ")
            preco = float(input("Digite o valor do produto: "))
            sql = f'INSERT INTO produtos (nome, preco) VALUES ("{produto}", {preco})'
            cursor.execute(sql)
            conexao.commit()
            print("Produto adicionado com sucesso!")

        # READ
        if opcao == "L":
            print("PRODUTOS\n")
            sql = 'SELECT * FROM produtos'
            cursor.execute(sql)
            produtos = cursor.fetchall()
            print(produtos)

        # UPDATE
        if opcao == "A":
            print("PRODUTOS\n")
            sql = 'SELECT * FROM produtos'
            cursor.execute(sql)
            produtos = cursor.fetchall()
            print(produtos)
            id = int(input("Selecione o produto que deseja atualizar pelo seu ID: "))
            if id <= 0:
                print("Digite um ID válido")
                exit()
            else:
                produto_novo = input("Digite o novo nome do produto: ")
                preco_novo = float(input("Digite o novo preço do produto: "))
                sql_att = f'UPDATE produtos SET nome="{produto_novo}", preco={preco_novo} WHERE id={id}'
                cursor.execute(sql_att)
                conexao.commit()

        # DELETE
        if opcao == "E":
            print("PRODUTOS\n")
            sql = 'SELECT * FROM produtos'
            cursor.execute(sql)
            produtos = cursor.fetchall()
            print(produtos)
            id = int(input("Selecione o produto que deseja excluir pelo seu ID: "))
            if id <= 0:
                print("Digite um ID válido")
                exit()
            else:
                sql_dele = f'DELETE FROM produtos WHERE id={id}'
                cursor.execute(sql_dele)
                conexao.commit()
    else:
        print("Digite somente a letra em [].")
        exit()
    continuacao = input("Deseja continuar? [S]/[N]: ")
print("Você optou sair.")
exit()
cursor.close()
conexao.close()
