# Conda

[Conda](https://docs.conda.io/en/latest/) is a "package manager" tool that was originally designed for the Python ecosystem but has be generally adopted as

Package managers are tools for installing/uninstalling software tools, code libraries, and creating computing environments that provide specific functionality.  One of the powerful aspects of Conda is that it allows users to install and use specific version of software packages in isolated or "sandboxed" environments.  This allows users to highly customize their computing environments without impacting other users of the same system.


## Steps to install conda

1. Download the "miniconda" binary 
```
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
```

2. Run the installer and follow the prompts
```
bash Miniconda3-latest-Linux-x86_64.sh
```

3. Make the conda tools available from the command line by sourcing your shell profile file or logging off and logging back on


4. Setup software "channels" for common bioinformatics tools

```
conda config --add channels defaults
conda config --add channels bioconda
conda config --add channels conda-forge
```

## Installing a package

1. Activate the default (base) conda environment
```
conda activate
```

2. When working in a conda environment you can search for and install Python libraries using `conda search` and `conda install`

The following command install three libraries (jupyterlab, matplotlib, pandas) and all their dependencies.

```
conda install jupyterlab matplotlib pandas
```

