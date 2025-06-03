from socket import *
import os

# Configuração do cliente
HOST = '127.0.0.1'
PORTA = 12345
sockobj = socket(AF_INET, SOCK_STREAM)
sockobj.connect((HOST, PORTA))

#print("ON")
#mensagem_boas_vindas = sockobj.recv(1024).decode()
#print(mensagem_boas_vindas)
Login = None

while True:
    if Login:
        print(Login.Name, "               -", Login.Saldo)
    print("\n=== Caixa Eletrônico ===")
    print("1. Criar conta")
    print("2. Fazer login")
    print("3. Consultar saldo")
    print("4. Depositar")
    print("5. Sacar")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")
    sockobj.send(opcao.encode())

    if opcao == "1":  # Criar conta
        nome = input("Digite um nome de usuário: ")
        senha = input("Digite uma senha: ")
        sockobj.send(nome.encode())
        sockobj.send(senha.encode())
        resposta = sockobj.recv(1024).decode()
        print(resposta)

    elif opcao == "2":  # Login
        nome = input("Digite seu nome de usuário: ")
        senha = input("Digite sua senha: ")
        sockobj.send(nome.encode())
        sockobj.send(senha.encode())
        resposta = sockobj.recv(1024).decode()
        print(resposta)

    elif opcao == "3":  # Consultar saldo
        nome = input("Digite seu nome de usuário: ")
        sockobj.send(nome.encode())
        saldo = sockobj.recv(1024).decode()
        print("Seu saldo é:", saldo)

    elif opcao == "4":  # Depositar
        nome = input("Digite seu nome de usuário: ")
        valor = input("Digite o valor a depositar: ")
        sockobj.send(nome.encode())
        sockobj.send(valor.encode())
        resposta = sockobj.recv(1024).decode()
        print(resposta)

    elif opcao == "5":  # Sacar
        nome = input("Digite seu nome de usuário: ")
        valor = input("Digite o valor a sacar: ")
        sockobj.send(nome.encode())
        sockobj.send(valor.encode())
        resposta = sockobj.recv(1024).decode()
        print(resposta)

    elif opcao == "6":  # Sair
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Testando a função
limpar_terminal()

sockobj.close()