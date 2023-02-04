import os

class AutoLoaderPackage:
    
    def __init__(self, dir):
        self.dir = dir

    def load_files(self):
        files = os.listdir(f'./{self.dir}')
        for file in files:
            if file != "__init__.py" and file != "__pycache__":
                file = file.replace(".py", "")
                exec(f"from {self.dir} import {file}")