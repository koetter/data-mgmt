
import os
import logging
import json
from dotenv import dotenv_values

def init():
    if os.path.exists('.env'):
        env = dict(dotenv_values())
        globals().update(env)
    else:
        print('No .env file was found in the project directory')
        exit

    secrets = read_secrets()
    globals()["secrets"] = secrets
    logging.basicConfig(filename="logs/app.log")

def read_secrets():
    projid = globals()["PROJID"]
    _secret_file_path = os.path.join(os.path.expanduser('~'), ".config/projects", projid)
    if os.path.isfile(_secret_file_path):
        with open(_secret_file_path) as f:
            content = f.read()
        
        if len(content) > 0:
            secrets = json.loads(content)
        else:
            secrets = {"conn":{}, "keys":{}, "comm":{}}
            write_secrets(secrets)
    else:
        secrets = {"conn":{}, "keys":{}, "comm":{}}
        write_secrets(secrets)

    return secrets
 
def write_secrets(secrets):
    projid = globals()["PROJID"]
    _secret_file_path = os.path.join(os.path.expanduser('~'), ".config/projects", projid)
    with open(_secret_file_path, "w") as f:
        f.write(json.dumps(secrets))

def set_secret(group, key, value):
    secrets = globals()['secrets']
    if group in secrets:
        secrets[group][key] = value
        globals()['secrets'] = secrets
        write_secrets(secrets)
    else:
        print(f"{group} doesn't exist in secrets")

def configure_smtp_server(smtp_host, port, sender, login="", pwd=""):
    smtp_config = {
        "host": smtp_host
        ,"port": port
        ,"login": login
        ,"pwd": pwd
        ,"sender": sender
        }
    secrets = globals()['secrets']
    secrets["comm"]["smtp"] = smtp_config
    globals()['secrets'] = secrets
    write_secrets(secrets)

def configure_teams_channel(channel, webhook):
    secrets = globals()['secrets']
    secrets['comm'][channel] = webhook
    globals()['secrets'] = secrets
    write_secrets(secrets)