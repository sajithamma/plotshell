import argparse
import sys
from .config import get_key, set_key, ask_ai

def main():
    parser = argparse.ArgumentParser(description='Plot: AI helper for DevOps.')
    parser.add_argument('command', nargs='+', help='Command to be explained by AI.', default=None)
    parser.add_argument('--setkey', help='Set the OpenAI API key.', action='store_true')
    args = parser.parse_args()

    if args.setkey:
        api_key = input("Enter your OpenAI API key: ")
        set_key(api_key)
        print("API key set successfully.")
    elif args.command:
        command_query = " ".join(args.command)  # Join all parts of the command into a single string
        api_key = get_key()
        if not api_key:
            print("API key not found. Please set it using --setkey.")
            sys.exit(1)
        response = ask_ai(command_query, api_key)
        print(response)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
