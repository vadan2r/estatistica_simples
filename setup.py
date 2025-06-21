# setup.py

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='estatistica_simples',
    version='0.1.0',
    author='Seu Nome',
    author_email='seu.email@example.com',
    description='Um pacote Python simples para cálculos estatísticos básicos.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/seu_usuario/estatistica_simples',  # Substitua pelo seu repositório
    packages=find_packages(),  # Encontra automaticamente os pacotes
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)