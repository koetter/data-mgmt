
from dotenv import load_dotenv

class Config:
    
    def __init__(self, env):
        self.env = env
        print("Environment:", self.env)