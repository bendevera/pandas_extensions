from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="pandas_extensions",
    version="0.1",
    author="Ben de Vera",
    author_email="ben10devera@gmail.com",
    description="Extensions to the pandas package.",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    license="MIT",
    url="https://github.com/bendevera/pandas_extensions.git",
    keywords="data tools pandas",
    packages=find_packages(),
    install_requires=[
        "pandas"
    ]
)