<<<<<<< Updated upstream

from dotenv import load_dotenv

class Config:
    
    def __init__(self, env):
        self.env = env
        print("Environment:", self.env)
=======
import os
import json
from dotenv import dotenv_values

class Config:
    
    def __init__(self):
        values = dict(dotenv_values())
        for key in values:
            setattr(self, key, os.getenv(key))
        self._secret_file_path = os.path.join(os.path.expanduser('~'), ".config/projects", self.PROJID)
        self.read_secrets()
    
    def get_attributes(self):
        for attr in dir(self):
            if (attr[0] != "_"):
                print(attr)

    def read_secrets(self):
        if os.path.isfile(self._secret_file_path):
            with open(self._secret_file_path) as f:
                content = f.read()
                if len(content) > 0:
                    self.secrets = json.loads(content)
                else:
                    self.secrets = {"conn":{}, "keys":{}}
        else:
            self.secrets = {"conn":{}, "keys":{}}
            self.write_secrets()
 
    def write_secrets(self):
        with open(self._secret_file_path, "w") as f:
            content = f.write(json.dumps(self.secrets))
>>>>>>> Stashed changes
