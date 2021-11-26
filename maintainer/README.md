## Introduction
This directory contains all it is needed to support one-stop package development.

We use conda as tool to manage packages during the development, but the final 
product is going to be a wheel file that can be installed using pip: so if you
really don't want to be tight to conda (and its ecosystem) you don't need to be.

## First time setup
Conda supports "*environemnts*" similar to the venv python environemnt except
it has a concept of "root" environemnt: this is special as it hold the base python
distribution. The advantage over venv is the derived "environments" can use any 
version of python and it is not bound to the "root" python version (eg. a "root"
environment can use python 3.10 and a created environemnt can be 2.7).

### root environment
This step is usually taken once only, and it can be installed system wide (from an admin)
or can be user installed without special permissions.

The original [anaconda]("https://conda.io") contains the conda implementation, but there are many (compatible) altrnative
you can use [here](https://github.com/conda-forge/miniforge/#download).

1. ["miniforge"](https://github.com/conda-forge/miniforge/#miniforge3) is a conda using the non-commercial conda-forge package repository
2. ["mambaforge"](https://github.com/conda-forge/miniforge/#mambaforge) improves the SAT solver for speedups

We're using here the "mambaforge" version targeting apple M1, but there are supported versions for linux, windows and intel macs.

```shell
curl -LO https://github.com/conda-forge/miniforge/releases/latest/download/Mambaforge-MacOSX-arm64.sh
sh Mambaforge-MacOSX-arm64.sh -b -p ~/envs/mambaforge
```

> **NOTE** we'll be using the conda command, but you can replace conda -> mamba to use the improvements

```shell
~/envs/mambaforge/bin/conda init

# you need to exit the current shell
exit
```


### working environemnt

```shell
mamba create -p $(pwd)/env wheel flake8 mypy pre-commit mock pytest pytest-html pytest-cov pygit2 click
```
