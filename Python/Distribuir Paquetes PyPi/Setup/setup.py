# Author: Daniel Benjamin Perez Morales
# GitHub: https://github.com/D4nitrix13
# GitLab: https://gitlab.com/D4nitrix13
# Email: danielperezdev@proton.me

from typing import Optional
from setuptools import setup, find_packages
from io import TextIOWrapper

f: Optional[TextIOWrapper] = None

with open(file = r"README.md", mode = "r", encoding = "utf-8") as f:
    README: str = f.read()

setup(
    name = "pycrypy",
    version = "1.0.5",
    author = "Daniel Benjamin Perez Morales",
    author_email = "danielperezdev@proton.me",
    description = "Esta utilidad, desarrollada en Python3, simplifica significativamente el proceso de configuracion de Alacritty, permitiendo ajustar de manera simple la fuente, el tema, el padding, los cursores y los estilos de la fuente.",
    long_description = README,
    long_description_content_type = "text/markdown",
    url = "https://github.com/D4nitrix13/pycrypy.git",
    packages = find_packages(where = "src"),
    package_dir = {"": "src"},  # Indica que los paquetes están en "src"
    license="MIT",
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Topic :: Terminals :: Terminal Emulators/X Terminals"
    ],
    keywords = "alacritty",
    python_requires = ">=3.6",
    install_requires = [
        "pytoml >= 0.1.21",
        "colored >= 2.2.4",
        "mypy >= 1.10.0",
        "pyinstaller >= 6.6.0",
        "prettytable >= 3.10.2",
    ],
    include_package_data = True,
    entry_points = {
        "console_scripts": ["pycrypy = cli.main:main"]
    }
)
