from setuptools import setup

setup(
    name='modak',
    version='0.1',
    packages=['scripts'],
    package_dir={'scripts': 'scripts'},
    entry_points={
        'console_scripts': [
            'modak=scripts.cli:main',
        ],
    },
)
