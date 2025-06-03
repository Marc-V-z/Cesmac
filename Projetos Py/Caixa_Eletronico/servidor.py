import json
from socket import *

# Configuração do servidor
HOST = '127.0.0.1'
PORTA = 12345
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.bind((HOST, PORTA))
sockobj.listen(1)

# Banco de dados de usuários (arquivo JSON)
ARQUIVO_USUARIOS = "usuarios.json"

# Função para carregar usuários do arquivo
def carregar_usuarios():
    try:
        with open(ARQUIVO_USUARIOS, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {}  # Retorna dicionário vazio se o arquivo não existir

# Função para salvar usuários no arquivo
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, "w") as f:
        json.dump(usuarios, f)

usuarios = carregar_usuarios()

print(f"Servidor rodando em {HOST}:{PORTA}, aguardando conexões...")

while True:
    conexao, endereco = sockobj.accept()
    print("Conectado:", endereco)

    while True:
        data = conexao.recv(1024)
        if not data:
            break
        
        opcao = data.decode()

        if opcao == "1":  # Cadastro de novo usuário
            nome = conexao.recv(1024).decode()
            senha = conexao.recv(1024).decode()

            if nome in usuarios:
                conexao.send("Erro: Usuário já existe!".encode())
            else:
                usuarios[nome] = {"senha": senha, "saldo": 0}
                salvar_usuarios(usuarios)
                conexao.send("Cadastro realizado com sucesso!".encode())

        elif opcao == "2":  # Login
            nome = conexao.recv(1024).decode()
            senha = conexao.recv(1024).decode()

            if nome in usuarios and usuarios[nome]["senha"] == senha:
                conexao.send("Login realizado com sucesso!".encode())
            else:
                conexao.send("Erro: Nome ou senha incorretos!".encode())

        elif opcao == "3":  # Consulta de saldo
            nome = conexao.recv(1024).decode()
            if nome in usuarios:
                conexao.send(str(usuarios[nome]["saldo"]).encode())
            else:
                conexao.send("Erro: Usuário não encontrado!".encode())

        elif opcao == "4":  # Depósito
            nome = conexao.recv(1024).decode()
            valor = float(conexao.recv(1024).decode())

            if nome in usuarios:
                usuarios[nome]["saldo"] += valor
                salvar_usuarios(usuarios)
                conexao.send("Depósito realizado com sucesso!".encode())
            else:
                conexao.send("Erro: Usuário não encontrado!".encode())

        elif opcao == "5":  # Saque
            nome = conexao.recv(1024).decode()
            valor = float(conexao.recv(1024).decode())

            if nome in usuarios and usuarios[nome]["saldo"] >= valor:
                usuarios[nome]["saldo"] -= valor
                salvar_usuarios(usuarios)
                conexao.send("Saque realizado com sucesso!".encode())
            else:
                conexao.send("Erro: Saldo insuficiente ou usuário não encontrado!".encode())

        elif opcao == "6":  # Encerrar conexão
            print("Cliente desconectado")
            break

        else:
            conexao.send("Opção inválida!".encode())

    conexao.close()