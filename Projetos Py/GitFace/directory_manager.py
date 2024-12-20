import os

class DirectoryManager:
    def __init__(self):
        self.current_directory = os.getcwd()

    def list_directory_contents(self):
        try:
            items = os.listdir(self.current_directory)
            return [(item, 'dir' if os.path.isdir(os.path.join(self.current_directory, item)) else 'file') for item in items]
        except OSError as e:
            return str(e)

    def change_directory(self, directory_name):
        try:
            os.chdir(os.path.join(self.current_directory, directory_name))
            self.current_directory = os.getcwd()
            return self.list_directory_contents()
        except OSError as e:
            return str(e)

    def create_directory(self, directory_name):
        try:
            os.mkdir(os.path.join(self.current_directory, directory_name))
            return self.list_directory_contents()
        except OSError as e:
            return str(e)
        
    def is_git_initialized(self):
        return os.path.isdir(os.path.join(self.directory_manager.current_directory, ".git"))
    
