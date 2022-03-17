from pathlib import Path
from setuptools import find_namespace_packages, setup

BASE_DIR = Path(__file__).parent

# Load packages from requirements.txt
with open(Path(BASE_DIR, "requirements.txt")) as file:
    required_packages = [ln.strip() for ln in file.readlines()]

test_packages = [
    "coverage[toml]==6.0.2",
    "pytest==6.0.2",
    "pytest-cov==2.10.1",
]

dev_packages = [
    "black==20.8b1",
    "flake8==3.8.3",
    "isort==5.5.3",
    "pre-commit==2.11.1",
]

docs_packages = [
    "mkdocs==1.1.2",
    "mkdocs-material==7.2.3",
    "mkdocstrings==0.15.2",
]

setup(
    name="",
    version="",
    license="",
    description="",
    author="Luís Vilaça",
    author_email="luismiguelvilaca@hotmail.com",
    url="",
    keywords=[
        "machine-learning",
        "artificial-intelligence",
        "deep-leaning"
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Academics",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
    ],
    python_requires=">=3.8",
    packages=find_namespace_packages(),
    install_requires=[required_packages],
    extras_require={
        "test": test_packages,
        "dev": test_packages + dev_packages + docs_packages,
        "docs": docs_packages,
    },
)
