import os
import configparser

def get_key():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.plotshrc'))
    return config.get('DEFAULT', 'api_key', fallback=None)

def set_key(api_key):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'api_key': api_key}
    with open(os.path.expanduser('~/.plotshrc'), 'w') as configfile:
        config.write(configfile)

def ask_ai(command, api_key):
    # Dummy implementation for now
    return "Dummy response for: " + command
