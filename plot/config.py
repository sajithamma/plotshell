import os
import configparser
import openai
import platform
import distro

from rich.console import Console
from rich.markdown import Markdown

CONFIG_PATH = os.path.expanduser('~/.plotshrc')


console = Console()


def clear_terminal():
    # Clears the terminal window
    os.system('cls' if os.name == 'nt' else 'clear')

def get_config():
    """Retrieve the API key and model from the config file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    api_key = config.get('DEFAULT', 'api_key', fallback=None)
    model = config.get('DEFAULT', 'model', fallback='gpt-4')  # Default to gpt-4 if not set
    return api_key, model

def set_key(api_key):
    """Set the API key in the config file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    config['DEFAULT']['api_key'] = api_key
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)

def set_model(model):
    """Set the GPT model in the config file."""
    config = configparser.ConfigParser()
    config.read(CONFIG_PATH)
    config['DEFAULT']['model'] = model
    with open(CONFIG_PATH, 'w') as configfile:
        config.write(configfile)


def ask_ai(prompt, api_key, model="gpt-4"):
    # Dummy implementation for now
    client = openai.OpenAI(api_key=api_key)
    full_response = ""  # Initialize an empty string to accumulate the response


    os_name = platform.system().lower()  # will return 'windows', 'darwin' (for macOS), or 'linux'
    if os_name == 'darwin':
        os_name = 'macos'
    elif os_name == 'linux':
        # Get more detailed distribution information on Linux
        os_name = distro.id() 
    
    instructions = f"Provide precise terminal commands for {os_name} without introductory explanations. Assume the user is already in the terminal and understands basic command execution. Provide only essential options."

    try:
        stream = client.chat.completions.create(
            model=model,
            
            messages=[{"role": "system", "content": instructions},
                      {"role": "user", "content": prompt}],
            stream=True
        )
        
        for chunk in stream:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="")
                full_response += chunk.choices[0].delta.content
        
        # Ensure the terminal prompt starts on a new line
        print() # This will print a newline character

        
        #clear_terminal()
        # Once all content is received, render it as Markdown
        # if full_response:
        #     console.print("Formatted response:")
        #     md = Markdown(full_response)
        #     console.print(md)


    except Exception as e:
        return f"An error occurred: {str(e)}"
