from setuptools import setup, find_packages


def parse_requirements(file):
    """Load requirements from a set of requirements files"""
    requirements = []
    with open(file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                if line.startswith("-r"):
                    nested_file = line.split(" ")[1]
                    requirements.extend(parse_requirements(nested_file))
                else:
                    requirements.append(line)
    return requirements


setup(
    name="notificationservice",
    version="0.1",
    packages=find_packages(where="src"),
    entry_points={
        "console_scripts": [
            "modaknotificationservice=modaknotificationservice.notifications:main"
        ],
    },
    install_requires=parse_requirements("py.requirements/basic.txt"),
)
