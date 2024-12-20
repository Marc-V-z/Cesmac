import subprocess
import os

class BashManager:
    def __init__(self, start_dir=None):
        self.mingw64_path = "C:/Program Files/Git/bin/bash.exe"  # Caminho para o bash do Git
        if start_dir:
            os.chdir(start_dir)  # Muda para o diretório inicial, se fornecido
        else:
            os.chdir(os.path.expanduser("~"))  # Muda para o diretório do usuário
        self.current_directory = os.getcwd()

    def Send_Command(self, cmd):
        result = subprocess.run([self.mingw64_path, '-c', cmd], text=True, capture_output=True)
        return result.stdout + result.stderr

    def Read_Command(self):
        return "Função para ler comandos ainda não implementada"
    
