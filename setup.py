from setuptools import setup, find_packages


setup(
    name="advent_of_code_22023",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "black==22.10.0",
        "flake8==6.0.0",
        "ipython==8.7.0",
        "isort==5.10.1",
        "pyyaml",
        "pytest",
    ],
    author="Javier",
    author_email="javier.gonzalezbonilla@getrev.ai",
    description="Solution for the advent of code 2023",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="git@github.com:javiergonzalezbonilla/advent_of_code_2023.git",
)
