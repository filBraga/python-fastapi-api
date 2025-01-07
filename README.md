# What is PIP and Conda?

Conda = Environment Management

PIP = Package Management

# Conda

### How to install Conda:

https://docs.anaconda.com/miniconda/

### Check version

```
conda --version
```

### Create a env

```
conda create --name <name> python=3.x
```

### List all envs

```
conda env list
```

### List all packages and versions installed in active env

```
conda list
```

### Delete an environment and everything in it

```
conda env remove --name <name>
```

# PIP

### Install pip

```
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```
```
python3 get-pip.py
```


### Create requirements.txt

```
pip freeze > requirements.txt
```

### Create requirements.txt

```
pip install "fastapi[standard]"
```

# Project

### Run project

```
fastapi dev main.py
```

### Run test

```
pytest -s
```
