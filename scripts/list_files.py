import os
import fnmatch

def load_gitignore_patterns(gitignore_path):
    patterns = []
    with open(gitignore_path, "r") as file:
        for line in file:
            line = line.strip()
            if line and not line.startswith("#"):
                patterns.append(line)
    return patterns

def matches_patterns(path, patterns):
    for pattern in patterns:
        path_norm = path.replace(os.sep, '/')
        pattern_norm = pattern.replace(os.sep, '/')

        # Exact match
        if fnmatch.fnmatch(path_norm, pattern_norm):
            return True
        # Directory match with trailing slash
        if path_norm.endswith('/') and fnmatch.fnmatch(path_norm.rstrip('/'), pattern_norm):
            return True
        # Any level directory match (e.g., **/__pycache__)
        if '**/' in pattern_norm:
            if fnmatch.fnmatch(path_norm, pattern_norm.replace('**/', '**/')):
                return True
        # Specific pattern for directories
        if pattern_norm.endswith('/') and fnmatch.fnmatch(path_norm + '/', pattern_norm):
            return True
        # Match without trailing slash
        if fnmatch.fnmatch(path_norm, pattern_norm.rstrip('/')):
            return True
    return False

def list_files(startpath, gitignore_path, output_file=None):
    patterns = load_gitignore_patterns(gitignore_path)
    file_content = []
    for root, dirs, files in os.walk(startpath):
        # Filter directories
        dirs[:] = [
            d
            for d in dirs
            if not matches_patterns(
                os.path.relpath(os.path.join(root, d), startpath) + os.sep, patterns
            )
        ]
        level = root.replace(startpath, "").count(os.sep)
        indent = " " * 4 * (level)
        line = "{}{}/".format(indent, os.path.basename(root) or ".")
        if not matches_patterns(os.path.relpath(root, startpath) + os.sep, patterns):
            print(line)
            file_content.append(line)
        subindent = " " * 4 * (level + 1)
        for f in files:
            file_path = os.path.relpath(os.path.join(root, f), startpath)
            if not matches_patterns(file_path, patterns):
                line = "{}{}".format(subindent, f)
                print(line)
                file_content.append(line)

    if output_file:
        with open(output_file, "w") as f:
            for line in file_content:
                f.write(line + "\n")

if __name__ == "__main__":
    directory = "."  # Use the current directory
    gitignore_path = "./.gitignore"  # Adjust this path if the script is run from a different directory
    output_choice = (
        input("Do you want to save the output to a file? (yes/no): ").strip().lower()
    )
    if output_choice == "yes":
        output_file = input("Enter the output file path: ")
        list_files(directory, gitignore_path, output_file)
    else:
        list_files(directory, gitignore_path)
