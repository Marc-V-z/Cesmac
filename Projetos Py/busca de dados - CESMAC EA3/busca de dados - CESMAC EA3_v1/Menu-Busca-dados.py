import os
from Busca_dados import Produto, SistemaBusca
# v1.0

# Função para limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Instância do sistema
sistema = SistemaBusca()

def exibir_menu():
    """
    Exibe o menu principal.
    """
    limpar_tela()
    print("=== Menu do Sistema ===")
    print("1. Filtrar Produto")
    print("2. Adicionar Produto")
    print("3. Remover Produto")
    print("4. Listar Todos os Produtos")
    print("0. Sair")
    return input("Escolha uma opção: ")

def filtrar_produto():
    """
    Tela de filtro de produtos.
    """
    limpar_tela()
    print("=== Filtrar Produto ===")
    id_produto = input("Digite o ID do produto que deseja buscar: ")
    if id_produto.isdigit():
        resultado = sistema.buscar_produto(int(id_produto))
        if isinstance(resultado, Produto):
            print(f"Produto encontrado: ID={resultado.id}, Nome={resultado.nome}, Preço=R${resultado.preco:.2f}")
        else:
            print(resultado)
    else:
        print("ID inválido. Retornando ao menu principal.")
    input("\nPressione Enter para voltar ao menu.")

def adicionar_produto():
    """
    Tela de adição de produtos.
    """
    limpar_tela()
    print("=== Adicionar Produto ===")
    try:
        id_produto = int(input("Digite o ID do produto: "))
        nome_produto = input("Digite o nome do produto: ")
        preco_produto = float(input("Digite o preço do produto: "))
        sistema.adicionar_produto(Produto(id_produto, nome_produto, preco_produto))
        print("Produto adicionado com sucesso!")
    except ValueError:
        print("Dados inválidos. Retornando ao menu principal.")
    input("\nPressione Enter para voltar ao menu.")

def remover_produto():
    """
    Tela de remoção de produtos, com opção de remover todos os produtos.
    """
    limpar_tela()
    print("=== Remover Produto ===")
    produtos = sistema.listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
        input("\nPressione Enter para voltar ao menu.")
        return
    
    print("Produtos cadastrados:")
    for index, produto in enumerate(produtos, start=1):
        print(f"{index}. ID={produto.id}, Nome={produto.nome}, Preço=R${produto.preco:.2f}")
    print("\nDigite 'todos' para remover todos os produtos.")
    print("Ou digite 0 para voltar ao menu principal.")
    
    opcao = input("\nDigite a sua escolha: ").lower()
    if opcao == "0" or opcao == "":
        return
    elif opcao == "todos":
        sistema.raiz = None  # Limpa a árvore inteira
        print("Todos os produtos foram removidos com sucesso!")
    elif opcao.isdigit():
        opcao = int(opcao)
        if 1 <= opcao <= len(produtos):
            produto_para_remover = produtos[opcao - 1]
            sistema.remover_produto(produto_para_remover.id)
            print(f"Produto removido com sucesso: {produto_para_remover}")
        else:
            print("Opção inválida.")
    else:
        print("Entrada inválida.")
    input("\nPressione Enter para voltar ao menu.")

def listar_produtos():
    """
    Tela de listagem de todos os produtos.
    """
    limpar_tela()
    print("=== Lista de Produtos ===")
    produtos = sistema.listar_produtos()
    if not produtos:
        print("Nenhum produto cadastrado.")
    else:
        for produto in produtos:
            print(produto)
    input("\nPressione Enter para voltar ao menu.")

# Loop principal do sistema
while True:
    opcao = exibir_menu()
    if opcao == "1":
        filtrar_produto()
    elif opcao == "2":
        adicionar_produto()
    elif opcao == "3":
        remover_produto()
    elif opcao == "4":
        listar_produtos()
    elif opcao == "0":
        limpar_tela()
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Tente novamente.")
        input("\nPressione Enter para continuar.")
