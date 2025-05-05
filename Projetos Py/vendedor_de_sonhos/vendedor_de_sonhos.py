# Início
import os        # Instalação de bibliotecas

# Função de apagar terminal
def Limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

# Inicialização das variáveis e lista
total_sonhos_vendidos = 0
total_valor_vendido = 0.0
historico = []

# Função de cálculo
def Calculo():
    global total_sonhos_vendidos
    global total_valor_vendido
    
    # Entrada da quantidade de sonhos vendidos
    quantidade_sonhos = int(input("Informe a quantidade de sonhos vendidos: "))

    # Verificação do desconto por quantidade
    if quantidade_sonhos >= 100:
        preco_unitario = 5.50
    else:
        preco_unitario = 8.00

    # Cálculo do valor total
    valor_total = quantidade_sonhos * preco_unitario

    # Atualização dos totais
    total_sonhos_vendidos += quantidade_sonhos
    total_valor_vendido += valor_total

    # Adicionar ao histórico
    historico.append((quantidade_sonhos, valor_total, preco_unitario))

    # Exibir informações da venda atual
    print(f"__Venda atual:")
    print(f"Quantidade de sonhos vendidos: {quantidade_sonhos}")
    print(f"Preço unitário: R$ {preco_unitario:.2f}")
    print(f"Valor total da venda: R$ {valor_total:.2f}")

    # Chamar função dos resultados totais (histórico)
    Resultados()

# Função de exibir resultados
def Resultados():
    global total_sonhos_vendidos
    global total_valor_vendido

    # Exibição dos resultados
    print(f"\n__Total acumulado:")
    print(f"Total de sonhos vendidos: {total_sonhos_vendidos}")
    if total_sonhos_vendidos != 0:
        preco_medio = total_valor_vendido / total_sonhos_vendidos
    else:
        preco_medio = 0
    print(f"Preço médio da unidade: R$ {preco_medio:.2f}")
    print(f"Valor total vendido: R$ {total_valor_vendido:.2f}")

    # Perguntar se o usuário quer voltar ao menu
    print()  # pular linha
    input("Aperte enter para voltar ao menu")
    # Chamar função de voltar ao menu
    VoltarMenu()

# Função de exibir histórico
def ExibirHistorico():
    # Exibição do histórico
    contador = 1

    for registro in historico:
        print(f"-- Registro {contador} --")
        print(f"Quantidade de sonhos vendidos: {registro[0]}")
        print(f"Valor total da venda: R$ {registro[1]:.2f}")
        print(f"Preço unitário: R$ {registro[2]:.2f}")
        contador += 1
    
    Resultados()

    # Perguntar se o usuário quer voltar ao menu
    print()  # pular linha
    input("Aperte enter para voltar ao menu")
    # Chamar função de voltar ao menu
    VoltarMenu()

# Função de apagar histórico
def ApagarHistorico():
    global historico
    historico = []

    global total_sonhos_vendidos
    global total_valor_vendido

    total_valor_vendido = 0.0
    total_sonhos_vendidos = 0

    print("Histórico apagado com sucesso.")

    # Perguntar se o usuário quer voltar ao menu
    print()  # pular linha
    input("Aperte enter para voltar ao menu")
    # Chamar função de voltar ao menu
    VoltarMenu()

# Função de escolhas
def Escolhas():
    # Exibir escolhas
    print("Calcular vendas  - 1")
    print("Ver histórico    - 2")
    print("Apagar histórico - 3")
    print("Sair             - 4")
    print()  # pular linha
    print("(Digite o número correspondente à opção que deseja acessar e pressione Enter.)")
    escolha = int(input())

    # Apagar/limpar terminal
    Limpar()

    # Verificar escolha
    if escolha == 1:
        Calculo()  # Chamar função de cálculo
    elif escolha == 2:
        ExibirHistorico()  # Chamar função de exibir histórico
    elif escolha == 3:
        ApagarHistorico()  # Chamar função de apagar histórico
    elif escolha == 4:
        exit()
    else:
        print("         (Escolha inválida. Tente novamente.)")
        Escolhas()

# Função de voltar ao menu
def VoltarMenu():
    # Apagar/limpar terminal
    Limpar()

    # Voltar ao menu
    Escolhas()

# Iniciar programa chamando a primeira função
VoltarMenu()
# Fim

#Autor do codigo: Marcelo Victor Monteiro Tomaz