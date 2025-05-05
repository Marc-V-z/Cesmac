# Passo 1: Definir o recurso e criar a listagem que será otimizada
# Tema escoolhido: Sistema de busca de produtos. Estrutura: AVL
# v2.1

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
    Classe para representar um nó em uma Árvore AVL.
    """
    def __init__(self, produto):
        self.produto = produto
        self.esquerda = None
        self.direita = None
        self.altura = 1

# Passo 2: Criar e aplicar a estrutura que permite realizar a busca otimizada.
class SistemaBusca:
    """
    Sistema para gerenciar produtos usando uma Árvore AVL.
    """
    def __init__(self):
        self.raiz = None

    def adicionar_produto(self, produto):
        """
        Adiciona um produto à Árvore AVL, garantindo o balanceamento.
        """
        self.raiz = self._adicionar(self.raiz, produto)

    def _adicionar(self, no, produto):
        if no is None:
            return No(produto)
        if produto.id < no.produto.id:
            no.esquerda = self._adicionar(no.esquerda, produto)
        elif produto.id > no.produto.id:
            no.direita = self._adicionar(no.direita, produto)
        else:
            # Atualiza o nome e o preço se o ID já existir
            no.produto.nome = produto.nome
            no.produto.preco = produto.preco
            return no

        # Atualiza a altura do nó
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

        # Balanceia o nó
        return self._balancear(no)

    def _altura(self, no):
        if no is None:
            return 0
        return no.altura

    def _fator_balanceamento(self, no):
        if no is None:
            return 0
        return self._altura(no.esquerda) - self._altura(no.direita)

    def _rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        # Rotação
        x.direita = y
        y.esquerda = T2

        # Atualiza as alturas
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))

        return x

    def _rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        # Rotação
        y.esquerda = x
        x.direita = T2

        # Atualiza as alturas
        x.altura = 1 + max(self._altura(x.esquerda), self._altura(x.direita))
        y.altura = 1 + max(self._altura(y.esquerda), self._altura(y.direita))

        return y

    def _balancear(self, no):
        # Verifica o fator de balanceamento
        fator = self._fator_balanceamento(no)

        # Rotação à direita
        if fator > 1 and self._fator_balanceamento(no.esquerda) >= 0:
            return self._rotacao_direita(no)

        # Rotação à esquerda
        if fator < -1 and self._fator_balanceamento(no.direita) <= 0:
            return self._rotacao_esquerda(no)

        # Rotação dupla (esquerda-direita)
        if fator > 1 and self._fator_balanceamento(no.esquerda) < 0:
            no.esquerda = self._rotacao_esquerda(no.esquerda)
            return self._rotacao_direita(no)

        # Rotação dupla (direita-esquerda)
        if fator < -1 and self._fator_balanceamento(no.direita) > 0:
            no.direita = self._rotacao_direita(no.direita)
            return self._rotacao_esquerda(no)

        return no

    def buscar_produto(self, id_produto):
        """
        Busca um produto pelo ID na Árvore AVL.
        """
        return self._buscar_recursivo(self.raiz, id_produto)

    def _buscar_recursivo(self, no, id_produto):
        if no is None:
            return "Produto não encontrado."
        if id_produto == no.produto.id:
            return no.produto
        elif id_produto < no.produto.id:
            return self._buscar_recursivo(no.esquerda, id_produto)
        else:
            return self._buscar_recursivo(no.direita, id_produto)

    def remover_produto(self, id_produto):
        """
        Remove um produto pelo ID e reorganiza a árvore, se necessário.
        """
        self.raiz = self._remover(self.raiz, id_produto)

    def _remover(self, no, id_produto):
        if no is None:
            return no

        if id_produto < no.produto.id:
            no.esquerda = self._remover(no.esquerda, id_produto)
        elif id_produto > no.produto.id:
            no.direita = self._remover(no.direita, id_produto)
        else:
            # Caso 1: Nó sem filhos
            if no.esquerda is None and no.direita is None:
                return None
            # Caso 2: Nó com um único filho
            if no.esquerda is None:
                return no.direita
            if no.direita is None:
                return no.esquerda
            # Caso 3: Nó com dois filhos
            menor_no = self._encontrar_menor(no.direita)
            no.produto = menor_no.produto
            no.direita = self._remover(no.direita, menor_no.produto.id)

        # Atualiza a altura do nó
        no.altura = 1 + max(self._altura(no.esquerda), self._altura(no.direita))

        # Balanceia o nó
        return self._balancear(no)

    def _encontrar_menor(self, no):
        while no.esquerda is not None:
            no = no.esquerda
        return no

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
