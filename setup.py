from setuptools import setup, find_packages
import os


def find_subdir(start_dir):
    # Get the list of all subdirectories starting at the given path
    subdirectories = [x[0] for x in os.walk(start_dir)]
    subdirectories = [x.split('/',1)[-1]+'/*' for x in subdirectories]
    return subdirectories

# Lendo o conteúdo do README.md para usar como descrição longa
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

MODULE_SLUG = "aps_4_alglin"

setup(
    name=MODULE_SLUG,
    version="0.1.0",
    author="prady001",
    author_email="gabrielpac@al.insper.edu.br",
    description="aps_4_alglin",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/prady001/aps_4_alglin",  # URL do repositório do seu projeto (se houver)
    packages=find_packages(),  # Encontra automaticamente todos os pacotes no diretório
    package_data={
    '': find_subdir(f'{MODULE_SLUG}/assets'),
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
    entry_points={
        'console_scripts': [
            f'aps_4_alglin-cli={MODULE_SLUG}.main:app',
        ],
    },
    install_requires=[  # Instala as dependências especificadas no requirements.txt
        line.strip() for line in open("requirements.txt").readlines()
    ],
)
