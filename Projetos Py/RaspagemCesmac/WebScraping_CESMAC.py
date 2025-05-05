import json
import sqlite3
import requests
import pandas as pd
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

""" Créditos:
Matheus Bezerra.
Marcelo Victor.
"""

# Configurações globais
DB_FILE = "banco_de_dados_CESMAC.db"  # Nome do arquivo SQLite
BASE_URL = "https://nahoradoocio.lowlevel.com.br/"
STATUS_OK = 200
HEADERS = {'User-Agent': UserAgent().random}

# Banco de dados
def conectar_banco():
    """Estabelece a conexão com o banco SQLite."""
    try:
        conn = sqlite3.connect(DB_FILE)
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        return None

def criar_tabela():
    """Cria a tabela caso ela não exista."""
    conn = conectar_banco()
    if conn:
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS conteudos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descricao TEXT,
                categoria TEXT,
                link TEXT UNIQUE
            );
        """)
        conn.commit()
        cur.close()
        conn.close()
        print("Tabela criada/verificada com sucesso!")

def inserir_dados_no_banco(conteudos):
    """Insere os dados raspados no banco de dados."""
    if not conteudos:
        print("Nenhum dado para inserir.")
        return

    conn = conectar_banco()
    if conn:
        cur = conn.cursor()
        for conteudo in conteudos:
            try:
                cur.execute("""
                    INSERT INTO conteudos (titulo, descricao, categoria, link)
                    VALUES (?, ?, ?, ?)
                    ON CONFLICT(link) DO UPDATE SET
                        titulo = excluded.titulo,
                        descricao = excluded.descricao,
                        categoria = excluded.categoria
                """, conteudo)
            except Exception as e:
                print(f"Erro ao inserir dados: {e}")

        conn.commit()
        cur.close()
        conn.close()
        print(f"{len(conteudos)} registros inseridos/atualizados no banco de dados.")

def raspar_dados():
    """Realiza a raspagem de dados do site até encontrar páginas inválidas ou vazias."""
    conteudos_extraidos = []
    current_page = 1

    while True:
        url = f"{BASE_URL}/page/{current_page}"
        print(f"Acessando: {url}")
        try:
            response = requests.get(url, headers=HEADERS, timeout=10)
            if response.status_code != STATUS_OK:
                print(f"Erro ao acessar a página {current_page}: Status {response.status_code}")
                break

            soup = BeautifulSoup(response.text, 'html.parser')
            posts = soup.find_all("header", {"class": "post-header"})

            if not posts:
                print(f"Não há mais posts na página {current_page}. Encerrando...")
                break

            for post in posts:
                headPost = post.find("h2", {"class": "post-title"})
                link = headPost.find("a")
                titulo = link.get_text().strip()
                link_titulo = link.get("href")

                content = post.find_next_sibling('div', class_='post-content')
                descricao = content.find("p").text.strip() if content and content.find("p") else "Sem descrição"
                tag_link = post.find("div", class_="post-categories")
                categoria = tag_link.find("a").text.strip() if tag_link else "Sem categoria"

                conteudos_extraidos.append((titulo, descricao, categoria, link_titulo))

                # Os prints que estavam no código original
                print(f"Título: {titulo}")
                print(f"Link: {link_titulo}")
                print(f"Descrição: {descricao}")
                print(f"Categoria: {categoria}")

            current_page += 1

        except requests.exceptions.RequestException as e:
            print(f"Erro ao acessar a página {current_page}: {e}")
            break

    print(f"Raspagem concluída. Total de registros extraídos: {len(conteudos_extraidos)}")
    return conteudos_extraidos

# Exportação de dados
def salvar_como_csv(conteudos, arquivo="dados.csv"):
    """Salva os dados coletados em um arquivo CSV."""
    if not conteudos:
        print("Nenhum dado para salvar em CSV.")
        return
    df = pd.DataFrame(conteudos, columns=['Título', 'Descrição', 'Categoria', 'Link'])
    df.to_csv(arquivo, index=False, encoding='utf-8')
    print(f"Dados salvos em {arquivo} com sucesso!")

def salvar_como_json(conteudos, arquivo="dados.json"):
    """Salva os dados coletados em um arquivo JSON."""
    if not conteudos:
        print("Nenhum dado para salvar em JSON.")
        return
    dados_json = [
        {"titulo": titulo, "descricao": descricao, "categoria": categoria, "link": link}
        for titulo, descricao, categoria, link in conteudos
    ]
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados_json, f, ensure_ascii=False, indent=4)
    print(f"Dados salvos em {arquivo} com sucesso!")

if __name__ == "__main__":
    print("Iniciando o processo...")
    criar_tabela()
    dados = raspar_dados()
    inserir_dados_no_banco(dados)
    salvar_como_csv(dados)
    salvar_como_json(dados)
    print(f"Processo concluído. Total de registros processados: {len(dados)}")