import random
import argparse
import subprocess
import os
import sys

programming_jokes = [
    "Why don't programmers like to code in the jungle? Because there are too many bugs.",
    "Why do beginners in programming always feel lost? Because they are in a new world without a map.",
]

human_error_jokes = [
    "Why do users love their smartphones? Because they think it makes them smart too.",
    "Why did the user bring their computer to the dentist? Because it had Bluetooth issues.",
]


def get_project_root():
    """Returns the root directory of the project based on the location of the main script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    return project_root


# Set project paths
PROJECT_ROOT = get_project_root()
GO_SRC_PATH = os.path.join(PROJECT_ROOT, "src", "go")
PYTHON_SRC_PATH = os.path.join(PROJECT_ROOT, "src", "python")


def add_language_subparsers(subparsers, command, help_text):
    """Add subparsers for different commands and languages."""
    parser = subparsers.add_parser(command, help=help_text)
    parser.add_argument(
        "language",
        nargs="?",
        choices=["go", "python"],
        help="Language to run the command for (go, python)",
    )


def handle_language_command(command, language):
    """Handle commands related to specific languages."""
    increment_moo_count()

    if language is None:
        run_command_for_both_languages(command)
    elif language == "go":
        run_command_for_go(command)
    elif language == "python":
        run_command_for_python(command)


def run_command_for_both_languages(command):
    """Run the specified command for both Go and Python projects."""
    command_map = {
        "build": build_project,
        "run": run_project,
        "test": test_project,
        "benchmark": benchmark_project,
        "install": install_project,
        "clean": clean_project,
    }
    command_map.get(command, lambda: print(f"Unknown command {command}"))()


def run_command_for_go(command):
    """Run the specified command for the Go project."""
    command_map = {
        "build": go_build_project,
        "run": go_run_project,
        "test": go_test_project,
        "benchmark": go_benchmark_project,
        "install": go_install_project,
        "clean": go_clean_project,
    }
    command_map.get(command, lambda: print(f"Unknown command {command}"))()


def run_command_for_python(command):
    """Run the specified command for the Python project."""
    command_map = {
        "build": python_build_project,
        "run": python_run_project,
        "test": python_test_project,
        "benchmark": python_benchmark_project,
        "install": python_install_project,
        "clean": python_clean_project,
    }
    command_map.get(command, lambda: print(f"Unknown command {command}"))()


def increment_moo_count():
    """Increment the moo count and return the updated count."""
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
    """Reset the moo count to zero and return the reset count."""
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, ".moo")
    with open(file_path, "w") as file:
        file.write("0")
    return 0


def build_project():
    """Build both Go and Python projects."""
    go_build_project()
    python_build_project()


def run_project():
    """Run both Go and Python projects."""
    go_run_project()
    python_run_project()


def test_project():
    """Run tests for both Go and Python projects."""
    go_test_project()
    python_test_project()


def benchmark_project():
    """Run benchmarks for both Go and Python projects."""
    go_benchmark_project()
    python_benchmark_project()


def install_project():
    """Install both Go and Python projects."""
    go_install_project()
    python_install_project()


def clean_project():
    """Clean both Go and Python projects."""
    go_clean_project()
    python_clean_project()


def go_benchmark_project():
    """Run Go benchmarks."""
    print("Running Go benchmarks...")
    subprocess.run(["go", "test", "-v", "-bench=."])


def go_build_project():
    """Build the Go project."""
    print(f"Running go mod tidy in {GO_SRC_PATH}...")
    subprocess.run(["go", "mod", "tidy"], cwd=GO_SRC_PATH, check=True)


def go_clean_project():
    """Clean the Go project."""
    print("Cleaning the Go project...")
    subprocess.run(["go", "clean", "-v"], cwd=GO_SRC_PATH, check=True)


def go_install_project():
    """Install the Go project."""
    print("Installing the Go project...")
    subprocess.run(["go", "install", "-v"], cwd=GO_SRC_PATH, check=True)


def go_run_project():
    """Run the Go project."""
    print("Running the Go project...")
    subprocess.run(["go", "run", "-v", GO_SRC_PATH])


def go_test_project():
    """Run Go tests."""
    print("Running Go tests...")
    subprocess.run(["go", "test", "-v"])


def python_benchmark_project():
    """Run Python benchmarks."""
    print("Running Python benchmarks...")
    subprocess.run(["pytest", "-v", "--benchmark-only"])


def python_build_project():
    """Build the Python project."""
    print("Building the Python project...")
    subprocess.run(
        [sys.executable, "setup.py", "sdist", "bdist_wheel"],
        cwd=PYTHON_SRC_PATH,
        check=True,
    )


def python_clean_project():
    """Clean the Python project."""
    print("Cleaning the Python project...")
    subprocess.run(["rm", "-rf", "build", "dist", "*.egg-info"], cwd=PYTHON_SRC_PATH)


def python_install_project():
    """Install the Python project."""
    print("Installing the Python project...")
    subprocess.run([sys.executable, "-m", "pip", "install", "."], cwd=PYTHON_SRC_PATH)


def python_run_project():
    """Run the Python project."""
    print("Running the Python project...")
    subprocess.run(
        [sys.executable, os.path.join(PYTHON_SRC_PATH, "main.py")], cwd=PYTHON_SRC_PATH
    )


def python_test_project():
    """Run Python tests."""
    print("Running Python tests...")
    subprocess.run(["pytest", "-v"], cwd=PYTHON_SRC_PATH)


def make_commit(message):
    """Make a git commit with the given message."""
    print(f"Making a git commit with message: '{message}'")
    subprocess.run(["git", "commit", "-m", message])


def push_code(remote, branch):
    """Push code to the specified remote and branch."""
    print(f"Pushing code to {remote}/{branch}")
    subprocess.run(["git", "push", remote, branch])


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

    if moo_count < 10:
        print_basic_cow()
    elif moo_count < 20:
        print_medium_cow()
    elif moo_count < 30:
        print_super_cow()
    else:
        print_ultimate_cow()


def run_go_mod_tidy():
    """Run the 'go mod tidy' command in the './src/go/...' folder."""
    print(f"Running go mod tidy in {GO_SRC_PATH}...")
    subprocess.run(["go", "mod", "tidy"], cwd=GO_SRC_PATH, check=True)


def run_pre_commit(test_type):
    """Run pre-commit tests based on the specified type."""
    if test_type in ["go", "1"]:
        print("Running pre-commit over Go...")
        # Add the command to run Go pre-commit tests
    elif test_type in ["python", "2"]:
        print("Running pre-commit over Python...")
        # Add the command to run Python pre-commit tests
    else:
        # If no test_type is provided, prompt the user to choose
        choice = input(
            "Please choose the pre-commit to run (1 for Go, 2 for Python, q to quit): "
        )
        if choice == "q":
            print("Skipping pre-commit checks.")
        else:
            run_pre_commit(choice)


def explain_code(file):
    """Explain the code in the given file."""
    print(f"Explaining code in file: {file}")
    # TODO: Explain the code with GPT in the future


def handle_no_command_provided(parser):
    """Handle the case when no command is provided."""
    print(
        "Human error joke: Why don't users tell jokes? Because they can't find the 'any' key."
    )
    parser.print_help()
    sys.exit(1)


def parse_arguments(parser):
    """Parse command line arguments."""
    if len(sys.argv) == 1:
        print("No arguments provided. Use -h for help.")
        print("Remember, this program has supercow powers!")
        sys.exit(1)

    args = parser.parse_args()
    return args


class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        """Handle argument parsing errors."""
        if "'moo'" in message:
            message = message.replace(", 'moo'", "")
            message = message.replace("'moo', ", "")
            message = message.replace("'moo'", "")
            message = message.replace(", 'miau'", "")
            message = message.replace("'miau', ", "")
            message = message.replace("'miau'", "")
        print(f"error: {message}")
        print_human_error_joke()
        self.print_help(filtered=True)
        sys.exit(2)

    def print_help(self, filtered=False):
        """Print help message."""
        if filtered:
            import io
            import contextlib

            help_output = io.StringIO()
            with contextlib.redirect_stdout(help_output):
                super().print_help()
            help_text = help_output.getvalue()
            help_lines = help_text.splitlines()
            filtered_help_lines = [
                line for line in help_lines if "moo" not in line and "miau" not in line
            ]
            filtered_help_text = "\n".join(filtered_help_lines)
            print(filtered_help_text)
        else:
            super().print_help()


def setup_parser():
    """Set up the argument parser."""
    parser = CustomArgumentParser(
        description="A CLI tool for the modak project. This program has supercow powers!"
    )
    subparsers = parser.add_subparsers(dest="command")

    add_language_subparsers(subparsers, "build", "Build the project")
    add_language_subparsers(subparsers, "run", "Run the project")
    add_language_subparsers(subparsers, "test", "Run tests")
    add_language_subparsers(subparsers, "benchmark", "Run benchmarks")
    add_language_subparsers(subparsers, "install", "Install the project")
    add_language_subparsers(subparsers, "clean", "Clean the project")

    subparsers.add_parser("go-mod-tidy", help="Run go mod tidy")

    supercow_parser = subparsers.add_parser("moo", help=argparse.SUPPRESS)
    supercow_parser.set_defaults(func=print_supercow)

    return parser


def main():
    """Main entry point of the script."""
    parser = setup_parser()
    args = parse_arguments(parser)

    if args.command is None:
        handle_no_command_provided(parser)

    if args.command in ["build", "run", "test", "benchmark", "install", "clean"]:
        handle_language_command(args.command, args.language)
    elif args.command == "go-mod-tidy":
        run_go_mod_tidy()
    elif args.command == "moo":
        print_supercow()


if __name__ == "__main__":
    main()
