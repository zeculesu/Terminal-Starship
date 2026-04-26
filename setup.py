
from setuptools import setup, find_packages

setup(
    name="terminal-starship",
    version="0.1.0",
    description="Real-time ANSI orbital control system",
    author="Artemiya",
    python_requires=">=3.8",
    py_modules=["main", "engine", "scene", "screen", "sprites"],
    package_dir={"": "src"},
    entry_points={
        "console_scripts": [
            "terminal-starship = main:main",
        ]
    },
)
