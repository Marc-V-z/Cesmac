# Passo 1: Definir o recurso e criar a listagem que será otimizada
# Tema escoolhido: Sistema de busca de produtos. Estrutura: BST
# v1.0

class Produto:
    """
    Classe para representar um produto no sistema.
    """
    def __init__(self, id, nome, preco):
        self.id = id
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"ID={self.id}, Nome={self.nome}, Preço=R${self.preco:.2f}"


class No:
    """
    Classe para representar um nó na Árvore Binária de Busca.
    """
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None

# Passo 2: Criar e aplicar a estrutura que permite realizar a busca otimizada.
class SistemaBusca:
    """
    Sistema para gerenciar produtos usando Árvore Binária de Busca (BST).
    """
    def __init__(self):
        self.raiz = None

    def adicionar_produto(self, produto):
        """
        Adiciona um produto à Árvore Binária de Busca.
        Se o ID do produto já existir, atualiza o nome e o preço.
        """
        if self.raiz is None:
            self.raiz = No(produto)
        else:
            self._adicionar_ou_atualizar(self.raiz, produto)

    def _adicionar_ou_atualizar(self, atual, produto):
        if produto.id < atual.produto.id:
            if atual.esquerda is None:
                atual.esquerda = No(produto)
            else:
                self._adicionar_ou_atualizar(atual.esquerda, produto)
        elif produto.id > atual.produto.id:
            if atual.direita is None:
                atual.direita = No(produto)
            else:
                self._adicionar_ou_atualizar(atual.direita, produto)
        else:
            # Se o ID já existir, atualiza o nome e o preço
            atual.produto.nome = produto.nome
            atual.produto.preco = produto.preco

    def buscar_produto(self, id_produto):
        """
        Busca um produto pelo ID na Árvore Binária de Busca.
        """
        return self._buscar_recursivo(self.raiz, id_produto)

    def _buscar_recursivo(self, atual, id_produto):
        if atual is None:
            return "Produto não encontrado."
        if id_produto == atual.produto.id:
            return atual.produto
        elif id_produto < atual.produto.id:
            return self._buscar_recursivo(atual.esquerda, id_produto)
        else:
            return self._buscar_recursivo(atual.direita, id_produto)

    def remover_produto(self, id_produto):
        """
        Remove um produto pelo ID e reorganiza a árvore, se necessário.
        """
        self.raiz = self._remover_recursivo(self.raiz, id_produto)

    def _remover_recursivo(self, atual, id_produto):
        if atual is None:
            return None

        if id_produto < atual.produto.id:
            atual.esquerda = self._remover_recursivo(atual.esquerda, id_produto)
        elif id_produto > atual.produto.id:
            atual.direita = self._remover_recursivo(atual.direita, id_produto)
        else:
            # Caso 1: Nó sem filhos
            if atual.esquerda is None and atual.direita is None:
                return None
            # Caso 2: Nó com um único filho
            if atual.esquerda is None:
                return atual.direita
            if atual.direita is None:
                return atual.esquerda
            # Caso 3: Nó com dois filhos
            menor_no = self._encontrar_menor(atual.direita)
            atual.produto = menor_no.produto
            atual.direita = self._remover_recursivo(atual.direita, menor_no.produto.id)

        return atual

    def _encontrar_menor(self, atual):
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def listar_produtos(self):
        """
        Lista todos os produtos em ordem crescente pelo ID.
        """
        produtos = []
        self._em_ordem(self.raiz, produtos)
        return produtos

    def _em_ordem(self, atual, produtos):
        if atual is not None:
            self._em_ordem(atual.esquerda, produtos)
            produtos.append(atual.produto)
            self._em_ordem(atual.direita, produtos)