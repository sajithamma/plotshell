import argparse
import sys
from .config import get_config, set_key, set_model, ask_ai

def main():
    parser = argparse.ArgumentParser(description='Plot: AI helper for DevOps.',
                                     epilog=
                'Examples:\n'
                '  plot setup nginx webserver\n'
                '  plot how to initialize git repository\n'
                '  plot create python virtual environment',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument('prompt', nargs='*', help='What task/command you want to know', default=None)
    parser.add_argument('--setkey', help='Set the OpenAI API key.', action='store_true')
    parser.add_argument("--set-model", metavar='MODEL', help="Set the GPT model. Default is gpt-4.")
    args = parser.parse_args()

    if args.setkey:
        api_key = input("Enter your OpenAI API key: ")
        set_key(api_key)
        print("API key set successfully.")
    elif args.set_model:
        set_model(args.set_model)
        print(f"Model set to {args.set_model} successfully.")
    elif args.prompt:
        prompt_query = " ".join(args.prompt)  # Join all parts of the command into a single string
        api_key, model = get_config()
        if not api_key:
            print("API key not found. Please set it using --setkey.")
            sys.exit(1)
        response = ask_ai(prompt_query, api_key, model)
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
