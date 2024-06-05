import random
import argparse
import subprocess
import os
import sys
import shutil
import fnmatch
from scripts import list_files

import io
import contextlib

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

def get_version():
    version_file_path = os.path.join(PROJECT_ROOT, 'VERSION')
    with open(version_file_path, 'r') as version_file:
        return version_file.read().strip()

# Set project paths
PROJECT_ROOT = get_project_root()
PYTHON_SRC_PATH = PROJECT_ROOT
TREE_OUTPUTFILE_LOCATION = "project_structure.txt"
PROJECT_VERSION = get_version()

def handle_python_command(command):
    """Handle commands related to the Python project."""
    increment_moo_count()
    run_command_for_python(command)

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

def python_build_project():
    """Build the Python project."""
    print("Building the Python project...")
    subprocess.run(
        [sys.executable, "setup.py", "sdist", "bdist_wheel"],
        cwd=PYTHON_SRC_PATH,
        check=True,
    )

def python_run_project():
    """Run the Python project."""
    print("Running the Python project...")
    subprocess.run(
        [sys.executable, os.path.join(PYTHON_SRC_PATH, "main.py")], cwd=PYTHON_SRC_PATH
    )

def python_test_project():
    """Run Python tests."""
    print("Running Python tests...")
    subprocess.run(["pytest", "-v"])

def python_benchmark_project():
    """Run Python benchmarks."""
    print("Running Python benchmarks...")
    subprocess.run(["pytest", "-v", "--benchmark-only"])

def python_install_project():
    """Install the Python project."""
    print("Installing the Python project...")
    subprocess.run([sys.executable, "-m", "pip", "install", "."], cwd=PYTHON_SRC_PATH)

def python_clean_project():
    """Clean the Python project."""
    print("Cleaning the Python project...")
    patterns_to_remove = ["build", "dist", "*.egg-info", "__pycache__", ".pytest_cache"]

    for root, dirs, files in os.walk(PYTHON_SRC_PATH, topdown=False):
        for name in dirs:
            for pattern in patterns_to_remove:
                if name == pattern or fnmatch.fnmatch(name, pattern):
                    dir_path = os.path.join(root, name)
                    print(f"Removing directory: {dir_path}")
                    shutil.rmtree(dir_path, ignore_errors=True)

        for name in files:
            for pattern in patterns_to_remove:
                if fnmatch.fnmatch(name, pattern):
                    file_path = os.path.join(root, name)
                    print(f"Removing file: {file_path}")
                    os.remove(file_path)

def bump_version(part):
    """Bump the version in the VERSION file."""
    result = subprocess.run(['./bump_version.sh', part], capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error bumping version: {result.stderr}")
        sys.exit(1)
    new_version = result.stdout.strip()
    return new_version

def make_commit(message):
    """Make a git commit with the given message."""
    print(f"Making a git commit with message: '{message}'")
    subprocess.run(["git", "commit", "-am", message])

def push_code(remote, branch, part='patch'):
    """Push code to the specified remote and branch, with a version bump."""
    print(f"Bumping version ({part})...")
    new_version = bump_version(part)
    make_commit(f"Bump version to {new_version}")

    print(f"Tagging version {new_version}...")
    subprocess.run(["git", "tag", "-a", f"v{new_version}", "-m", f"Release {new_version}"])

    print(f"Pushing code to {remote}/{branch}...")
    subprocess.run(["git", "push", remote, branch, "--tags"])

def print_cow(moo_count):
    """Print the cow ASCII art based on the moo count."""
    cow_art = [
        "        (__) \n        (--) \n  /------\\/ \n / |    || \n*  /\\---/\\ \n   ~~   ~~ \n...Have you mooed today?...",
        "        (__) \n        (oo) \n  /------\\/ \n / |    || \n*  /\\---/\\ \n   ~~   ~~ \n...Keep mooing!...",
        "        (__) \n        (@@) \n  /------\\/ \n / |    || \n*  /\\---/\\ \n   ~~   ~~ \n...Super Moo!...",
        "        (__) \n        (@@) \n  /------\\/ \n / |   |S| \n*  /\\---/\\ \n   ~~   ~~ \n...Ultimate Super Moo!!!...",
    ]

    if moo_count < 10:
        print(cow_art[0])
    elif moo_count < 20:
        print(cow_art[1])
    elif moo_count < 30:
        print(cow_art[2])
    else:
        print(cow_art[3])

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
    print(f"You have mooed {moo_count} times")
    print_cow(moo_count)

def show_project_structure():
    """Show the project structure."""
    return list_files.list_files(
        PROJECT_ROOT,
        os.path.join(PROJECT_ROOT, '.gitignore'),
        os.path.join(PROJECT_ROOT, TREE_OUTPUTFILE_LOCATION))

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

    python_commands = ["build", "run", "test", "benchmark", "install", "clean"]
    for cmd in python_commands:
        subparsers.add_parser(cmd, help=f"{cmd.capitalize()} the project")

    tree = subparsers.add_parser("tree", help="Shows the project structure")
    tree.set_defaults(func=show_project_structure)

    supercow_parser = subparsers.add_parser("moo", help=argparse.SUPPRESS)
    supercow_parser.set_defaults(func=print_supercow)

    # Add the --version command
    parser.add_argument(
        '--version',
        action='version',
        version=f'%(prog)s {PROJECT_VERSION}',
        help="Show the project version"
    )

    return parser

def main():
    """Main entry point of the script."""
    parser = setup_parser()
    args = parse_arguments(parser)

    if args.command is None:
        handle_no_command_provided(parser)

    if args.command in ["build", "run", "test", "benchmark", "install", "clean"]:
        handle_python_command(args.command)
    elif args.command == "tree":
        show_project_structure()
    elif args.command == "moo":
        print_supercow()

if __name__ == "__main__":
    main()
