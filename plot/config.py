import os
import configparser
import openai
import platform
import distro

from rich.console import Console
from rich.markdown import Markdown


console = Console()


def clear_terminal():
    # Clears the terminal window
    os.system('cls' if os.name == 'nt' else 'clear')

def get_key():
    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.plotshrc'))
    return config.get('DEFAULT', 'api_key', fallback=None)

def set_key(api_key):
    config = configparser.ConfigParser()
    config['DEFAULT'] = {'api_key': api_key}
    with open(os.path.expanduser('~/.plotshrc'), 'w') as configfile:
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
        
        clear_terminal()

        # Once all content is received, render it as Markdown
        if full_response:
            console.print("Formatted response:")
            md = Markdown(full_response)
            console.print(md)


    except Exception as e:
        return f"An error occurred: {str(e)}"
