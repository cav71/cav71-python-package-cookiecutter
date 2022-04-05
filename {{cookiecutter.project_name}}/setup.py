import os
import pathlib

from setuptools import setup, find_packages
from setuptools_github import tools

{% if cookiecutter.is_package %}
initfile = pathlib.Path(__file__).parent / "src" / "{{cookiecutter.package_name}}" / "__init__.py"
{% else %}
initfile = pathlib.Path(__file__).parent / "src" / "{{cookiecutter.package_name}}.py"
{% endif %}
version = tools.update_version(initfile, os.getenv("GITHUB_DUMP"))

setup(
    name="{{cookiecutter.project_name}}",
    version=version,
    description="{{cookiecutter.project_short_description}}",
    url="{{cookiecutter.url}}",
    
{% if cookiecutter.is_package %}
    packages=find_packages("src"),
{% else %}
    py_modules=[
        "{{cookiecutter.package_name}}",
    ],
    package_dir = {"": "src"},
{% endif %}

    # CHANGEME adds as many entry points as you need
    entry_points={
        "console_scripts": ["{{cookiecutter.package_name}}={{cookiecutter.package_name}}:main"],
    },

    # CHANGEME replace "text/markdown" with "text/x-rst" for rst READMEs
    long_description=pathlib.Path("README.md").read_text(),
    long_description_content_type="text/markdown",

    # CHANGEME adds as many classifiers
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: MIT License",
    ],
)
