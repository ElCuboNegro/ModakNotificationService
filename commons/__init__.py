import os

def get_project_root():
    """Returns the root directory of the project based on the location of the main script."""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir)
    return project_root

def read_moo_count():
    """Read the moo count and return the count."""
    home_dir = os.path.expanduser("~")
    file_path = os.path.join(home_dir, ".moo")

    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            count = int(file.read().strip())
    else:
        count = 0

    return count
