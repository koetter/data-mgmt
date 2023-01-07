
import os
import logging
import json
from dotenv import dotenv_values


def read_secrets():
    if os.path.isfile(_secret_file_path):
        with open(_secret_file_path) as f:
            content = f.read()
            if len(content) > 0:
                secrets = json.loads(content)
            else:
                secrets = {"conn":{}, "keys":{}}
    else:
        secrets = {"conn":{}, "keys":{}}
        write_secrets(secrets)
    
    locals().update(secrets)
    return secrets
 
def write_secrets():
    with open(_secret_file_path, "w") as f:
        f.write(json.dumps(secrets))

def set_mail_config(smtp_host, port, sender, login="", pwd=""):
    smtp_config = {
        "host": smtp_host
        ,"port": port
        ,"login": login
        ,"pwd": pwd
        ,"sender": sender
        }
    configuration.secrets["CONN"]["smtp"] = smtp_config
    locals().update(configuration.secrets)
    configuration.write_secrets()


env = dict(dotenv_values())
locals().update(env)
_secret_file_path = os.path.join(os.path.expanduser('~'), ".config/projects", PROJID)
secrets = read_secrets()
logging.basicConfig(filename=os.path.join(PROJPATH,"logs/app.log"))