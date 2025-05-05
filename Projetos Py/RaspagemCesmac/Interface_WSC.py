import tkinter as tk
from tkinter import ttk
from WebScraping_CESMAC import conectar_banco

def carregar_dados_do_banco():
    """Carrega os dados do banco de dados para exibição na interface."""
    conn = conectar_banco()
    if not conn:
        return []
    cur = conn.cursor()
    cur.execute("SELECT titulo, descricao, categoria, link FROM conteudos")
    resultados = cur.fetchall()
    conn.close()
    return [
        {"titulo": row[0], "descricao": row[1], "categoria": row[2], "link": row[3]}
        for row in resultados
    ]

def filtrar_dados(dados, filtro, termo_pesquisa):
    """Filtra os dados com base no filtro e no termo de pesquisa."""
    resultado = []
    for conteudo in dados:
        if filtro and filtro != conteudo['categoria']:
            continue
        if termo_pesquisa and termo_pesquisa.lower() not in conteudo['titulo'].lower():
            continue
        resultado.append(conteudo)
    return resultado

def criar_janela_detalhes(root, conteudo, voltar_callback):
    """Exibe os detalhes de uma matéria."""
    for widget in root.winfo_children():
        widget.destroy()

    titulo_label = tk.Label(root, text=conteudo['titulo'], font=("Helvetica", 16, "bold"))
    titulo_label.pack(pady=10)

    categoria_label = tk.Label(root, text=f"Categoria: {conteudo['categoria']}", font=("Helvetica", 12, "italic"))
    categoria_label.pack(pady=5)

    descricao_label = tk.Label(root, text=f"Descrição: {conteudo['descricao']}", wraplength=500, justify="left")
    descricao_label.pack(pady=10)

    link_label = tk.Label(root, text=f"Link: {conteudo['link']}", fg="blue", cursor="hand2")
    link_label.pack(pady=10)
    link_label.bind("<Button-1>", lambda e: print(f"Abrindo link: {conteudo['link']}"))  # Substitua por webbrowser.open()

    voltar_button = tk.Button(root, text="Voltar", command=voltar_callback)
    voltar_button.pack(pady=20)

def criar_janela_principal(root, dados):
    """Cria a janela principal com barra de ferramentas e área scrollável."""
    for widget in root.winfo_children():
        widget.destroy()

    # Frame da barra de ferramentas
    toolbar = tk.Frame(root, bg="lightgray", height=50)
    toolbar.pack(side="top", fill="x")

    # Filtros
    filtro_var = tk.StringVar(value="Todos")
    pesquisa_var = tk.StringVar()

    def atualizar_lista():
        filtro = filtro_var.get() if filtro_var.get() != "Todos" else None
        termo_pesquisa = pesquisa_var.get()
        dados_filtrados = filtrar_dados(dados, filtro, termo_pesquisa)
        criar_lista_scrollavel(root, dados_filtrados)

    filmes_button = tk.Radiobutton(toolbar, text="LISTA DE FILMES", variable=filtro_var, value="LISTA DE FILMES", command=atualizar_lista, bg="lightgray")
    filmes_button.pack(side="left", padx=10, pady=10)

    series_button = tk.Radiobutton(toolbar, text="MARATONAS DE SÉRIES", variable=filtro_var, value="MARATONAS DE SÉRIES", command=atualizar_lista, bg="lightgray")
    series_button.pack(side="left", padx=10, pady=10)

    todos_button = tk.Radiobutton(toolbar, text="Todos", variable=filtro_var, value="Todos", command=atualizar_lista, bg="lightgray")
    todos_button.pack(side="left", padx=10, pady=10)

    # Barra de pesquisa
    search_label = tk.Label(toolbar, text="Pesquisar:", bg="lightgray")
    search_label.pack(side="left", padx=10)

    search_entry = tk.Entry(toolbar, textvariable=pesquisa_var)
    search_entry.pack(side="left", padx=5)
    search_entry.bind("<Return>", lambda e: atualizar_lista())  # Atualiza ao pressionar "Enter"

    search_button = tk.Button(toolbar, text="Buscar", command=atualizar_lista)
    search_button.pack(side="left", padx=10)

    # Criação da área scrollável com os dados
    criar_lista_scrollavel(root, dados)

def criar_lista_scrollavel(root, dados):
    """Cria a área scrollável com os botões das matérias."""
    for widget in root.winfo_children():
        if isinstance(widget, tk.Canvas) or isinstance(widget, ttk.Scrollbar):
            widget.destroy()

    # Canvas com scroll
    canvas = tk.Canvas(root)
    frame_scroll = ttk.Frame(canvas)
    scroll = ttk.Scrollbar(root, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll.set)
    canvas.pack(side="left", fill="both", expand=True)
    scroll.pack(side="right", fill="y")
    canvas_frame = canvas.create_window((0, 0), window=frame_scroll, anchor="nw")

    def ajustar_scroll(event):
        canvas.configure(scrollregion=canvas.bbox("all"))
    frame_scroll.bind("<Configure>", ajustar_scroll)

    # Botões com as matérias
    for conteudo in dados:
        button_frame = tk.Frame(frame_scroll, relief="groove", bd=2, padx=5, pady=5)
        button_frame.pack(fill="x", padx=10, pady=5)

        titulo_label = tk.Label(button_frame, text=conteudo['titulo'], font=("Helvetica", 14, "bold"))
        titulo_label.pack(anchor="w")

        categoria_label = tk.Label(button_frame, text=f"Categoria: {conteudo['categoria']}", font=("Helvetica", 12, "italic"))
        categoria_label.pack(anchor="w")

        button_button = tk.Button(
            button_frame, text="Ver detalhes", command=lambda c=conteudo: criar_janela_detalhes(root, c, lambda: criar_janela_principal(root, dados))
        )
        button_button.pack(anchor="w", pady=5)

    canvas.bind(
        "<Configure>",
        lambda e: canvas.itemconfig(canvas_frame, width=e.width)
    )

def main():
    """Executa a interface gráfica."""
    root = tk.Tk()
    root.title("Raspagem de Matérias - CESMAC")
    root.geometry("800x600")

    dados = carregar_dados_do_banco()  # Carrega os dados do banco
    criar_janela_principal(root, dados)

    root.mainloop()

if __name__ == "__main__":
    main()