import tkinter as tk
from tkinter import scrolledtext, simpledialog
from BashManager import BashManager
from directory_manager import DirectoryManager
from Config import Config

class BashInterface:
    def __init__(self, start_dir=None):
        self.bash = BashManager(start_dir)
        self.directory_manager = DirectoryManager()
        self.config = Config()
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("GitFace - Interface Git")

        self.warpText = "char"  # "none" "word" "char"
        self.espacamento = 0    # 0  5

        # Frame principal que contém toda a interface 
        self.main_frame = tk.Frame(self.root) 
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.Home_dir_button = tk.Button(self.main_frame, text="Home", command=self.home_directory)
        self.Home_dir_button.pack(side= tk.TOP, anchor=tk.NW)

        self.Change_Tema_button = tk.Button(self.main_frame, text="Conf.", command=self.Change_Tema)
        self.Change_Tema_button.pack(side= tk.TOP, anchor=tk.NE)
        #self.Change_Tema_button.grid(row=0, column=1, sticky="e")

        self.command_frame = tk.Frame(self.main_frame, bg="WhiteSmoke", bd=2, relief=tk.RIDGE)  # alternativa: self.root
        self.command_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)


        self.Back_dir_button = tk.Button(self.command_frame, text="Voltar", command=self.back_directory)
        self.Back_dir_button.pack(side= tk.TOP, anchor=tk.NW)

        self.command_label = tk.Label(self.command_frame, text="Comando:")
        self.command_label.pack()

        self.command_entry = tk.Entry(self.command_frame, width=50)
        self.command_entry.pack()

        self.execute_button = tk.Button(self.command_frame, text="Executar", command=self.execute_command)
        self.execute_button.pack()

        self.output_text = scrolledtext.ScrolledText(self.command_frame, width=70, height=5) # w 60   h 20
        self.output_text.pack(side= tk.TOP, fill=tk.X, expand=True)

        self.directory_frame = tk.Frame(self.command_frame)
        self.directory_frame.pack(side= tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

        self.update_directory_list()

        self.create_dir_button = tk.Button(self.command_frame, text="Criar Diretório", command=self.create_directory_prompt)
        self.create_dir_button.pack(side= tk.RIGHT)

        if not self.directory_manager.is_git_initialized():
            self.ini_git_button = tk.Button(self.command_frame, text="Iniciar Repositorio", command=self.Ini_Git_prompt)
            self.ini_git_button.pack(side= tk.LEFT)
        else:
            self.commit_button = tk.Button(self.command_frame, text=" Commit ", command=self.Commit_All)
            self.commit_button.pack(side= tk.LEFT)
        if self.bash.is_in_git_repo(self.directory_manager.current_directory):
            result = self.bash.is_in_git_repo(self.directory_manager.current_directory)
            self.output_text.insert(tk.END, result) 
            self.add_stage_button = tk.Button(self.command_frame, text="Add Stage", command=self.Add_on_Stage)
            self.add_stage_button.pack(side= tk.LEFT) 

    def execute_command(self):
        cmd = self.command_entry.get()
        result = self.bash.Send_Command(cmd)
        self.output_text.insert(tk.END, result)

    def update_MainWindow(self):
        self.root.config(bg=self.config.cor1[0])
        self.main_frame.config(bg=self.config.cor3) 
        self.command_frame.config(bg=self.config.cor6) 
        # Atualizar botões 
        #self.Home_dir_button.config(bg=self.config.cor3, fg=self.config.cor5[0]) 
        #self.Change_Tema_button.config(bg=self.config.cor3, fg=self.config.cor5[0]) 
        #self.Back_dir_button.config(bg=self.config.cor3, fg=self.config.cor5[0]) 
        #self.execute_button.config(bg=self.config.cor3, fg=self.config.cor5[0]) 
        #self.create_dir_button.config(bg=self.config.cor3, fg=self.config.cor5[0]) 

        self.old_Init_Git()
        #self.new_dinamic_Buttons()

        # Atualizar outros widgets 
        self.command_label.config(bg=self.config.cor6, fg=self.config.cor5[0])
        self.command_entry.config(bg=self.config.cor1[0], fg=self.config.cor5[0]) 
        self.output_text.config(bg=self.config.cor1[1], fg=self.config.cor5[2]) 
        # Atualizar a lista de diretórios self
        self.update_directory_list()

    def update_directory_list(self):
        for widget in self.directory_frame.winfo_children():
            widget.destroy()

        contents = self.directory_manager.list_directory_contents()

        directory_scroll = tk.Canvas(self.directory_frame, bg= self.config.cor4)  #"Gainsboro"
        scroll_bar = tk.Scrollbar(self.directory_frame, orient="vertical", command=directory_scroll.yview) 
        scrollable_frame = tk.Frame(directory_scroll)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: directory_scroll.configure(
                scrollregion=directory_scroll.bbox("all")
            )
        )

        directory_scroll.create_window((0, 0), window=scrollable_frame, anchor="nw")
        directory_scroll.configure(yscrollcommand=scroll_bar.set)

        for item, item_type in contents: 
            if item_type == 'dir': 
                button = tk.Button(scrollable_frame, text=item, command=lambda i=item: self.change_directory(i), bg=self.config.cor2, fg=self.config.cor5[1]) 
                button.pack(side=tk.TOP, fill=tk.X) 
            else: 
                text_widget = tk.Text(scrollable_frame, height=1, bg=self.config.cor3, fg=self.config.cor5[0], wrap=self.warpText, relief=tk.FLAT) 
                text_widget.tag_configure("center", justify='center')
                text_widget.tag_add("center", "1.0", "end")
                text_widget.insert(tk.END, item) 
                text_widget.config(state=tk.DISABLED) # Tornar o widget não editável 
                text_widget.pack(side=tk.TOP, fill=tk.X, padx=self.espacamento, pady=self.espacamento)

        directory_scroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

    def output_Update(self, texto):
        self.output_text.insert(tk.END, texto + '\n')  # Adiciona o texto ao final do widget
        self.output_text.yview(tk.END)  # Rola para o final do texto

        # self.output_Update("texto")


    def change_directory(self, directory_name):
        self.directory_manager.change_directory(directory_name)
        #result = self.bash.is_in_git_repo(self.directory_manager.current_directory)
        #self.output_text.insert(tk.END, result) #lembrar de remover.... e talvez fazer um metodo pra facilitar
        #self.update_directory_list()
        self.update_MainWindow()

    def back_directory(self):
        self.directory_manager.change_directory("..")
        #self.update_directory_list()
        self.update_MainWindow()

    def home_directory(self):
        self.directory_manager.change_directory("/")
        self.update_directory_list()

    def create_directory_prompt(self):
        dir_name = simpledialog.askstring("Criar Diretório", "Nome do novo diretório:")
        if dir_name:
            self.directory_manager.create_directory(dir_name)
            self.update_directory_list()

    def INIT_GIT(self):
        result = self.bash.Send_Command("git init")
        self.output_text.insert(tk.END, result) 
        self.update_MainWindow()


    def Ini_Git_prompt(self):
            self.directory_manager.INIT_GIT()
            self.update_directory_list()

    def new_dinamic_Buttons(self):
        if not self.directory_manager.is_git_initialized(): 
            if not hasattr(self, 'ini_git_button') or not self.ini_git_button.winfo_exists():
                self.ini_git_button = tk.Button(self.command_frame, text="Iniciar Repositorio", command=self.Ini_Git_prompt)
                self.ini_git_button.pack(side= tk.LEFT)
        else:
            if hasattr(self, 'ini_git_button') and self.ini_git_button.winfo_exists():
                self.ini_git_button.destroy()
                del self.ini_git_button
        if self.bash.is_in_git_repo(self.directory_manager.current_directory):
            result = self.bash.is_in_git_repo(self.directory_manager.current_directory)
            self.output_text.insert(tk.END, result) 
            self.add_stage_button = tk.Button(self.command_frame, text="Add Stage", command=self.Add_on_Stage)
            self.add_stage_button.pack(side= tk.LEFT) 
        else: self.output_text.insert(tk.END, "Fora de um repositório Git\n")

    def old_Init_Git(self):
        if not self.directory_manager.is_git_initialized(): 
            if not hasattr(self, 'ini_git_button') or not self.ini_git_button.winfo_exists():
                self.ini_git_button = tk.Button(self.command_frame, text="Iniciar Repositorio", command=self.Ini_Git_prompt)
                self.ini_git_button.pack(side= tk.LEFT)
        else:
            if hasattr(self, 'ini_git_button') and self.ini_git_button.winfo_exists():
                self.ini_git_button.destroy()
                del self.ini_git_button

    def Add_on_Stage(self):
        result = self.bash.Send_Command(f"git add {self.directory_manager.current_directory}")
        self.output_text.insert(tk.END, result) 
        self.update_MainWindow()

    def Commit_All(self):
        mensagem = simpledialog.askstring("Fazer commit", "Alterações da versão:")
        if not mensagem:
            mensagem = ""
        result = self.bash.Send_Command(f'git commit -m "{mensagem}"')
        self.output_text.insert(tk.END, result) 
        self.update_MainWindow() 

    
    def Change_Tema(self):
        janelatema = tk.Tk() 
        janelatema.title(f"Escolha o Tema") 

        for tema in self.config.temas: 
            botao = tk.Button(janelatema, text=tema, command=lambda t=tema: self.selecionar_tema(janelatema, t)) 
            botao.pack(padx=20, pady=5, fill= tk.X)   
            #self.criar_janela_tema(tema)
        self.confirmtema = tk.Button(janelatema, text="Concluir", command=lambda t=tema: janelatema.destroy())
        self.confirmtema.pack(padx=20, pady=15)
        janelatema.mainloop()

    def selecionar_tema(self, janela, tema): 
        self.config.Tema = tema  #self.atualizar_tema(tema) 
        self.config.Cores_Update()
        self.update_MainWindow()
        #janela.destroy()


    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    start_directory = None  # None para iniciar no diretório padrão do usuário
    BashInterface(start_directory).run()
