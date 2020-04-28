# Conda Packaging Hands-on Demo

We created this project for you to show you the minimal requirements for building and installing a python package with 
<a href="https://setuptools.readthedocs.io/en/latest/" target="_blank">setuptools</a>, <a href="https://packaging.python.org/tutorials/installing-packages/" target="_blank">pip</a> and <a href="https://docs.conda.io/en/latest/" target="_blank">conda</a>.


## Usage

### Create a conda environment

```
conda create -y -n 'conda-hands-on' python=3.7 conda-build conda-verify conda-smithy setuptools pip -c conda-forge
conda activate conda-hands-on
```


### Build and Install Package

#### setuptools

```
python setup.py install
```

#### pip
```
pip install .
```

#### conda
```
conda smithy conda.recipe # lint

# This block is optional and the build might work
# without explicitly building a local channel

mkdir ~/conda-bld         # Create folder which will act as a local channel
conda index ~/conda-bld   # Set up local channel

# Build and Install Package

CONDA_BLD_PATH=~/conda-bld conda-build conda.recipe
conda install my-package
