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
    
    def is_in_git_repo(self,file_path): 
        try: 
            repo_root = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'],stderr=subprocess.DEVNULL, cwd=os.path.dirname(file_path)).strip().decode('utf-8') 
            return file_path.startswith(repo_root) 
        except subprocess.CalledProcessError: 
            return False
        
    def find_git_repo(self, path): 
        #path = self.current_directory 
        while path != os.path.dirname(path): # Enquanto não atingir a raiz do sistema de arquivos 
            if self.is_in_git_repo(path): 
                return True 
            path = os.path.dirname(path) 
        return False