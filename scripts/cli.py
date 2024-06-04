import random
import argparse
import subprocess
import sys
import os

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

def add_language_subparsers(subparsers, command, help_text):
    """Add subparsers for different commands and languages.

    Args:
        subparsers (argparse._SubParsersAction): The subparsers action object.
        command (str): The command to add a subparser for.
        help_text (str): The help text for the command.
    """
    parser = subparsers.add_parser(command, help=help_text)
    parser.add_argument('language', nargs='?', choices=['go', 'python'], help='Language to run the command for (go, python)')

def benchmark_project():
    """Run benchmarks for both Go and Python projects."""
    go_benchmark_project()
    python_benchmark_project()

def build_docs():
    """Build the project documentation."""
    print("Building the documentation...")
    # Aquí podrías añadir el comando para construir la documentación

def build_project():
    """Build both Go and Python projects."""
    go_build_project()
    python_build_project()

def clean_project():
    """Clean both Go and Python projects."""
    go_clean_project()
    python_clean_project()

def explain_code(file):
    """Explain the code in the given file.

    Args:
        file (str): The file to explain.
    """
    print(f"Explaining code in file: {file}")
    # TODO: explicar el código del archivo con GPT, lo hare en algun momento de la vida

def go_benchmark_project():
    """Run Go benchmarks."""
    print("Running Go benchmarks...")
    subprocess.run(['go', 'test', '-v', '-bench=.'])

def go_build_project():
    """Build the Go project."""
    print("Building the Go project...")
    subprocess.run(['go', 'build', '-v'])

def go_clean_project():
    """Clean the Go project."""
    print("Cleaning the Go project...")
    subprocess.run(['go', 'clean', '-v'])

def go_install_project():
    """Install the Go project."""
    print("Installing the Go project...")
    subprocess.run(['go', 'install', '-v'])

def go_run_project():
    """Run the Go project."""
    current_file = sys.argv[0]
    print(f"Running the Go project using {current_file}...")
    subprocess.run(['go', 'run', '-v', current_file])

def go_test_project():
    """Run Go tests."""
    print("Running Go tests...")
    subprocess.run(['go', 'test', '-v'])

def handle_language_command(command, language):
    """Handle commands related to specific languages.

    Args:
        command (str): The command to run.
        language (str): The language to run the command for.
    """
    increment_moo_count()

    if language is None:
        run_command_for_both_languages(command)
    elif language == 'go':
        run_command_for_go(command)
    elif language == 'python':
        run_command_for_python(command)

def handle_no_command_provided(parser):
    """Handle the case when no command is provided.

    Args:
        parser (argparse.ArgumentParser): The argument parser object.
    """
    print("Human error joke: Why don't users tell jokes? Because they can't find the 'any' key.")
    parser.print_help()
    sys.exit(1)

def increment_moo_count():
    """Increment the moo count.

    Returns:
        int: The updated moo count.
    """
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

def install_project():
    """Install both Go and Python projects."""
    go_install_project()
    python_install_project()

def make_commit(message):
    """Make a git commit with the given message.

    Args:
        message (str): The commit message.
    """
    print(f"Making a git commit with message: '{message}'")
    subprocess.run(['git', 'commit', '-m', message])

def parse_arguments(parser):
    """Parse command line arguments.

    Args:
        parser (argparse.ArgumentParser): The argument parser object.

    Returns:
        argparse.Namespace: The parsed arguments.
    """
    if len(sys.argv) == 1:
        print("No arguments provided. Use -h for help.")
        print("Remember, this program has supercow powers!")
        sys.exit(1)

    args = parser.parse_args()
    return args

def print_basic_cow():
    """Print the basic cow ASCII art."""
    print("        (__)")
    print("        (--)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Have you mooed today?...")

def print_medium_cow():
    """Print the medium cow ASCII art."""
    print("        (__)")
    print("        (oo)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Keep mooing!...")

def print_super_cow():
    """Print the super cow ASCII art."""
    print("        (__)")
    print("        (@@)")
    print("  /------\\/")
    print(" / |    ||")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Super Moo!...")

def print_ultimate_cow():
    """Print the ultimate cow ASCII art."""
    print("        (__)")
    print("        (@@)")
    print("  /------\\/")
    print(" / |   |S|")
    print("*  /\\---/\\")
    print("   ~~   ~~")
    print("...Ultimate Super Moo!!!...")

def print_human_error_joke():
    """Print a random human error joke."""
    joke = random.choice(human_error_jokes)
    print(joke)


def print_programming_joke():
    """Print a random programming joke."""
    joke = random.choice(programming_jokes)
    print(joke)

def print_supercow():
    """Print the supercow ASCII art based on the moo count."""
    moo_count = increment_moo_count()
    print("You have mooed " + str(moo_count) + " times")

    if (moo_count < 10):
        print_basic_cow()
    elif (moo_count < 20):
        print_medium_cow()
    elif (moo_count < 30):
        print_super_cow()
    else:
        print_ultimate_cow()

def push_code(remote, branch):
    """Push code to the specified remote and branch.

    Args:
        remote (str): The remote repository name.
        branch (str): The branch name.
    """
    print(f"Pushing code to {remote}/{branch}")
    subprocess.run(['git', 'push', remote, branch])

def python_benchmark_project():
    """Run Python benchmarks."""
    print("Running Python benchmarks...")
    subprocess.run(['pytest', '-v', '--benchmark-only'])

def python_build_project():
    """Build the Python project."""
    print("Building the Python project...")
    subprocess.run(['python', 'setup.py', 'sdist', 'bdist_wheel'])

def python_clean_project():
    """Clean the Python project."""
    print("Cleaning the Python project...")
    subprocess.run(['rm', '-rf', 'build', 'dist', '*.egg-info'])

def python_install_project():
    """Install the Python project."""
    print("Installing the Python project...")
    subprocess.run(['pip', 'install', '.'])

def python_run_project():
    """Run the Python project."""
    current_file = sys.argv[0]
    print(f"Running the Python project using {current_file}...")
    subprocess.run(['python', current_file])

def python_test_project():
    """Run Python tests."""
    print("Running Python tests...")
    subprocess.run(['pytest', '-v'])

def reset_moo_count():
    """Reset the moo count to zero.

    Returns:
        int: The reset moo count.
    """
    print("A little cat has miau'd, the cow is afraid of the cat's super cuteness...")
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, ".moo")
    with open(file_path, "w") as file:
        file.write("0")
    return 0

def run_command_for_both_languages(command):
    """Run the specified command for both Go and Python projects.

    Args:
        command (str): The command to run.
    """
    if command == 'build':
        build_project()
    elif command == 'run':
        run_project()
    elif command == 'test':
        test_project()
    elif command == 'benchmark':
        benchmark_project()
    elif command == 'install':
        install_project()
    elif command == 'clean':
        clean_project()

def run_command_for_go(command):
    """Run the specified command for the Go project.

    Args:
        command (str): The command to run.
    """
    if command == 'build':
        go_build_project()
    elif command == 'run':
        go_run_project()
    elif command == 'test':
        go_test_project()
    elif command == 'benchmark':
        go_benchmark_project()
    elif command == 'install':
        go_install_project()
    elif command == 'clean':
        go_clean_project()

def run_command_for_python(command):
    """Run the specified command for the Python project.

    Args:
        command (str): The command to run.
    """
    if command == 'build':
        python_build_project()
    elif command == 'run':
        python_run_project()
    elif command == 'test':
        python_test_project()
    elif command == 'benchmark':
        python_benchmark_project()
    elif command == 'install':
        python_install_project()
    elif command == 'clean':
        python_clean_project()

def run_go_mod_tidy():
    """Run the 'go mod tidy' command."""
    print("Running go mod tidy...")
    subprocess.run(['go', 'mod', 'tidy'])

def run_pre_commit(test_type):
    """Run pre-commit tests based on the specified type.

    Args:
        test_type (str): The type of test to run ('go', 'python', '1', '2').
    """
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

def run_project():
    """Run both Go and Python projects."""
    go_run_project()
    python_run_project()

def setup_parser():
    """Set up the argument parser.

    Returns:
        argparse.ArgumentParser: The configured argument parser.
    """
    parser = CustomArgumentParser(description="A CLI tool for the modak project. This program has supercow powers!")
    subparsers = parser.add_subparsers(dest='command')

    add_language_subparsers(subparsers, 'build', 'Build the project')
    add_language_subparsers(subparsers, 'run', 'Run the project')
    add_language_subparsers(subparsers, 'test', 'Run tests')
    add_language_subparsers(subparsers, 'benchmark', 'Run benchmarks')
    add_language_subparsers(subparsers, 'install', 'Install the project')
    add_language_subparsers(subparsers, 'clean', 'Clean the project')

    subparsers.add_parser('go-mod-tidy', help='Run go mod tidy')

    supercow_parser = subparsers.add_parser('moo', help=argparse.SUPPRESS)
    supercow_parser.set_defaults(func=print_supercow)

    return parser

def test_project():
    """Run tests for both Go and Python projects."""
    go_test_project()
    python_test_project()

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """Handle argument parsing errors.

        Args:
            message (str): The error message.
        """
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
        """Print help message.

        Args:
            filtered (bool): Whether to filter the help message.
        """
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


def main():
    """Main entry point of the script."""
    parser = setup_parser()
    args = parse_arguments(parser)

    if args.command is None:
        handle_no_command_provided(parser)

    if args.command in ['build', 'run', 'test', 'benchmark', 'install', 'clean']:
        handle_language_command(args.command, args.language)
    elif args.command == 'go-mod-tidy':
        run_go_mod_tidy()
    elif args.command == 'moo':
        print_supercow()

if __name__ == "__main__":
    main()
