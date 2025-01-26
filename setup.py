# setup.py
from setuptools import setup, find_packages

setup(
    name="fast-hard",
    version="0.1.2",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "fast-hard=fast_hard.cli:cli",
        ],
    },
    author="Felipe Hardmann",
    author_email="fashardmann@gmail.com",
    description="Um pacote para gerar projetos FastAPI com estrutura básica.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/seu-usuario/fast_hard",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
