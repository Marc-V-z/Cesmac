import tkinter as tk
from tkinter import scrolledtext, simpledialog
from BashManager import BashManager
from directory_manager import DirectoryManager

class BashInterface:
    def __init__(self, start_dir=None):
        self.bash = BashManager(start_dir)
        self.directory_manager = DirectoryManager()
        self.setup_gui()

    def setup_gui(self):
        self.root = tk.Tk()
        self.root.title("GitFace - Interface Git")

        self.warpText = "char"  # "none" "word" "char"
        self.espacamento = 0    # 0  5

        # Frame principal que contém toda a interface 
        main_frame = tk.Frame(self.root) 
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        Home_dir_button = tk.Button(main_frame, text="Home", command=self.home_directory)
        Home_dir_button.pack(side= tk.TOP, anchor=tk.NW)

        command_frame = tk.Frame(main_frame, bg="WhiteSmoke", bd=2, relief=tk.RIDGE)  # alternativa: self.root
        command_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        """left_spacer = tk.Frame(self.root, width=15) # 10 pixels de largura 
        left_spacer.pack(side=tk.LEFT, fill=tk.Y) # Espaço vazio na parte inferior 
        bottom_spacer = tk.Frame(self.root, height=10) # 10 pixels de altura 
        bottom_spacer.pack(side=tk.BOTTOM, fill=tk.X)
        #Right_spacer = tk.Frame(self.root, width=10) # 10 pixels de largura 
        #Right_spacer.pack(side=tk.RIGHT, fill=tk.Y) # Espaço vazio na parte inferior """

        Back_dir_button = tk.Button(command_frame, text="Voltar", command=self.back_directory)
        Back_dir_button.pack(side= tk.TOP, anchor=tk.NW)

        command_label = tk.Label(command_frame, text="Comando:")
        command_label.pack()

        self.command_entry = tk.Entry(command_frame, width=50)
        self.command_entry.pack()

        execute_button = tk.Button(command_frame, text="Executar", command=self.execute_command)
        execute_button.pack()

        self.output_text = scrolledtext.ScrolledText(command_frame, width=70, height=5) # w 60   h 20
        self.output_text.pack(side= tk.TOP, fill=tk.X, expand=True)

        self.directory_frame = tk.Frame(command_frame)
        self.directory_frame.pack(side= tk.TOP, fill=tk.BOTH, expand=True, anchor=tk.CENTER)

        self.update_directory_list()

        create_dir_button = tk.Button(command_frame, text="Criar Diretório", command=self.create_directory_prompt)
        create_dir_button.pack(side= tk.RIGHT)

        ini_git_button = tk.Button(command_frame, text="Iniciar Repositorio", command=self.Ini_Git_prompt)
        ini_git_button.pack(side= tk.LEFT)

    def execute_command(self):
        cmd = self.command_entry.get()
        result = self.bash.Send_Command(cmd)
        self.output_text.insert(tk.END, result)

    def update_directory_list(self):
        for widget in self.directory_frame.winfo_children():
            widget.destroy()

        contents = self.directory_manager.list_directory_contents()

        directory_scroll = tk.Canvas(self.directory_frame, bg= "Gainsboro")
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
                button = tk.Button(scrollable_frame, text=item, command=lambda i=item: self.change_directory(i), bg="LightGrey", fg="Black") 
                button.pack(side=tk.TOP, fill=tk.X) 
            else: 
                text_widget = tk.Text(scrollable_frame, height=1, bg="white", fg="black", wrap=self.warpText, relief=tk.FLAT) 
                text_widget.tag_configure("center", justify='center')
                text_widget.tag_add("center", "1.0", "end")
                text_widget.insert(tk.END, item) 
                text_widget.config(state=tk.DISABLED) # Tornar o widget não editável 
                text_widget.pack(side=tk.TOP, fill=tk.X, padx=self.espacamento, pady=self.espacamento)

        directory_scroll.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scroll_bar.pack(side=tk.RIGHT, fill=tk.Y)

    def change_directory(self, directory_name):
        self.directory_manager.change_directory(directory_name)
        self.update_directory_list()

    def back_directory(self):
        self.directory_manager.change_directory("..")
        self.update_directory_list()
        #self.update_buttons()

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
        #self.update_buttons()


    def Ini_Git_prompt(self):
            self.directory_manager.INIT_GIT()
            self.update_directory_list()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    start_directory = None  # None para iniciar no diretório padrão do usuário
    BashInterface(start_directory).run()
