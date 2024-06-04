import random
import argparse
import subprocess
import sys
import os

def increment_moo_count():
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, ".moo")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            count = int(file.read().strip())
    else:
        count = 0

    count += 1

    with open(file_path, "w") as file:
        file.write(str(count))

    return count

def reset_moo_count():
    print("A little cat has miau'd, the cow is afraid of the cat's super cuteness...")
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, ".moo")
    with open(file_path, "w") as file:
        file.write("0")
    return 0

programming_jokes = [
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "A SQL query walks into a bar, walks up to two tables and asks: 'Can I join you?'",
    "Why do Java developers wear glasses? Because they don't C#.",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
    "Why was the JavaScript developer sad? Because he didn't know how to 'null' his feelings.",
    "What's a programmer's favorite place to hang out? Foo Bar.",
    "How do you comfort a JavaScript bug? You console it.",
    "Why do Python programmers prefer snake_case? Because it's easy to slither through the code.",
    "Why did the developer go broke? Because he used up all his cache.",
    "What's the object-oriented way to become wealthy? Inheritance.",
    "Why did the tester refuse to enter the bar? Because there was a bug in the door.",
    "Why was the math book sad? It had too many problems.",
    "Why did the programmer quit his job? Because he didn't get arrays.",
    "How do you tell an introverted computer scientist from an extroverted one? The extroverted one looks at your shoes when talking to you.",
    "How many software testers does it take to change a light bulb? None. They just report that it’s dark.",
    "Why do programmers hate nature? It has too many bugs.",
    "Why don't programmers like to code in the jungle? Because there are too many bugs.",
    "Why do beginners in programming always feel lost? Because they are in a new world without a map."
]

human_error_jokes = [
    "What is Layer 8? The user. The problem usually exists between keyboard and chair.",
    "Why don't users tell jokes? Because they can't find the 'any' key.",
    "Why do users always get lost? Because they don't read the manual.",
    "How many users does it take to change a light bulb? None. They just wait for IT to do it.",
    "Why was the computer cold? Because it left its Windows open.",
    "Why did the user stare at the screen for hours? Because the message said 'Press any key to continue'.",
    "Why did the user call tech support? Because the computer told them to 'Enter their password' and they couldn't find the 'Enter' key.",
    "Why do users always call IT? Because their coffee holder is broken (CD drive).",
    "Why do users love their smartphones? Because they think it makes them smart too.",
    "Why did the user bring their computer to the dentist? Because it had Bluetooth issues.",
]

def main():
    parser = CustomArgumentParser(description="A CLI tool for the modak project. This program has supercow powers!")
    subparsers = parser.add_subparsers(dest='command')

    # Subcommand for joke
    subparsers.add_parser('joke', help='Print a programming joke')

    # Subcommand for test
    test_parser = subparsers.add_parser('test', help='Run tests')
    test_parser.add_argument('test_type', nargs='?', choices=['go', 'python', '1', '2'], help='Type of tests to run (go, python, 1, or 2)')

    # Subcommand for pre-commit
    pre_commit_parser = subparsers.add_parser('pre-commit', help='Run pre-commit checks')
    pre_commit_parser.add_argument('test_type', nargs='?', choices=['go', 'python', '1', '2'], help='Type of pre-commit checks to run (go, python, 1, or 2)')

    # Subcommand for commit
    commit_parser = subparsers.add_parser('commit', help='Make a git commit')
    commit_parser.add_argument('message', help='Commit message')

    # Subcommand for push
    push_parser = subparsers.add_parser('push', help='Push code to remote repository')
    push_parser.add_argument('remote', help='Remote repository name')
    push_parser.add_argument('branch', help='Branch name')

    # Subcommand for explain
    explain_parser = subparsers.add_parser('explain', help='Explain code in a file')
    explain_parser.add_argument('file', help='File to explain')

    # Subcommand for build-docs
    subparsers.add_parser('build-docs', help='Build the documentation')

    # Hidden subcommand for supercow
    supercow_parser = subparsers.add_parser('moo', help=argparse.SUPPRESS)
    supercow_parser.set_defaults(func=print_supercow)

    minimiau_parser = subparsers.add_parser('miau', help=argparse.SUPPRESS)
    minimiau_parser.set_defaults(func=reset_moo_count)

    help_parser = subparsers.add_parser('-h', help='Show the help message and exit')
    help_parser.set_defaults(func=CustomArgumentParser.print_help)

     # Subcommand for go mod tidy
    subparsers.add_parser('go-mod-tidy', help='Run go mod tidy')

    if len(sys.argv) == 1:
        print("No arguments provided. Use -h for help.")
        print("Remember, this program has supercow powers!")
        sys.exit(1)

    args = parser.parse_args()
    if args.command is None:
        print_human_error_joke()
        parser.print_help(filtered=True)
        sys.exit(1)

    joke_flag = handle_command(args)

    if joke_flag:
        print_programming_joke()

def handle_command(args):
    if args.command == 'joke':
        print_programming_joke()
        return False
    elif args.command == 'pre-commit':
        run_pre_commit(args.test_type)
    elif args.command == 'commit':
        make_commit(args.message)
    elif args.command == 'push':
        push_code(args.remote, args.branch)
    elif args.command == 'explain':
        explain_code(args.file)
    elif args.command == 'build-docs':
        build_docs()
    elif args.command == 'moo':
        print_supercow()
        return False
    elif args.command == 'miau':
        reset_moo_count()
        print_supercow()
        return False
    elif args.command == 'go-mod-tidy':
        run_go_mod_tidy()
        return False
    return True

def run_go_mod_tidy():
    # Navigate to the Go source directory and run go mod tidy
    go_src_dir = os.path.join(os.getcwd(), 'src', 'go')
    if os.path.isdir(go_src_dir):
        print(f"Navigating to {go_src_dir} and running 'go mod tidy'...")
        result = subprocess.run(['go', 'mod', 'tidy'], cwd=go_src_dir, capture_output=True, text=True)
        if result.returncode == 0:
            print("Successfully ran 'go mod tidy'.")
        else:
            print(f"Error running 'go mod tidy': {result.stderr}")
    else:
        print(f"Directory {go_src_dir} does not exist. Please check the path.")


def print_programming_joke():
    joke = random.choice(programming_jokes)
    print(joke)

def print_human_error_joke():
    joke = random.choice(human_error_jokes)
    print(joke)

def run_pre_commit(test_type):
    if test_type in ['go', '1']:
        print("Running pre-commit over Go...")
        # Aquí podrías añadir el comando para ejecutar las pruebas de Go
    elif test_type in ['python', '2']:
        print("Running pre-commit over Python...")
        # Aquí podrías añadir el comando para ejecutar las pruebas de Python
    else:
        # Si no se proporciona test_type, solicitamos al usuario que elija
        choice = input("Please choose the pre-commit to run (1 for Go, 2 for Python, q to quit): ")
        if choice == 'q':
            print("Skipping pre-commit checks.")
        else:
            run_pre_commit(choice)

def make_commit(message):
    print(f"Making a git commit with message: '{message}'")
    subprocess.run(['git', 'commit', '-m', message])

def push_code(remote, branch):
    print(f"Pushing code to {remote}/{branch}")
    subprocess.run(['git', 'push', remote, branch])

def explain_code(file):
    print(f"Explaining code in file: {file}")
    # Aquí podrías añadir el comando para explicar el código del archivo

def build_docs():
    print("Building the documentation...")
    # Aquí podrías añadir el comando para construir la documentación

def print_supercow():
    moo_count = increment_moo_count()
    print("You have mooed " + str(moo_count) + " times")

    if moo_count < 10:
        print_basic_cow()
    elif moo_count < 20:
        print_medium_cow()
    elif moo_count < 30:
        print_super_cow()
    else:
        print_ultimate_cow()

def print_basic_cow():
    print("        (__)")
    print("        (oo)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Have you mooed today?...")

def print_medium_cow():
    print("        (__)")
    print("        (oo)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Keep mooing!...")

def print_super_cow():
    print("        (__)")
    print("        (@@)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Super Moo!...")

def print_ultimate_cow():
    print("        (__)")
    print("        (@@)")
    print("  /------\\/")
    print(" / |   |S|")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Ultimate Super Moo!!!...")

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Eliminar "moo" del mensaje
        if "'moo'" in message:
            message = message.replace(", 'moo'", "")
            message = message.replace("'moo', ", "")
            message = message.replace("'moo'", "")
            message = message.replace(", 'miau'", "")
            message = message.replace("'miau', ", "")
            message = message.replace("'miau'", "")
        print(f'error: {message}')
        print_human_error_joke()
        self.print_help(filtered=True)
        sys.exit(2)

    def print_help(self, filtered=False):
        if filtered:
            import io
            import contextlib
            help_output = io.StringIO()
            with contextlib.redirect_stdout(help_output):
                super().print_help()
            help_text = help_output.getvalue()
            help_lines = help_text.splitlines()
            filtered_help_lines = [line for line in help_lines if 'moo' not in line and 'miau' not in line]
            filtered_help_text = '\n'.join(filtered_help_lines)
            print(filtered_help_text)
        else:
            super().print_help()

if __name__ == "__main__":
    main()
