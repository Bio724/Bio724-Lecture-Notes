# Conda


Package managers are tools for installing/uninstalling software tools, code libraries, and creating computing environments that provide specific functionality.
[Conda](https://docs.conda.io/en/latest/) is a"package manager that was originally designed for the Python ecosystem but has be generally adopted by the scientific computing community as a convenient tool for installing software.

One of the powerful aspects of Conda is that it allows users to install and use specific version of software packages in isolated or "sandboxed" environments.  This allows users to highly customize their computing environments without impacting other users of the same system.


## Steps to install conda on your VM

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

## Adding Python packages to the base environment

By default, conda created a "base" environment for you to work in.  These base environment is where I recommend installing standard tools and packages that you commonly work with.  Let's customize our base environment:

```
conda install jupyterlab matplotlib numpy scipy
```

You can search for packages use the `search` subcommand:

```
conda search biopython
```


## Creating a new conda environment


1. Create a new environment (here named "genomics") 
```
conda create -n genomics
```

2.  Activate the new environment
```
conda activate genomics
```

3. When working in an environment you can search for and install  tools using `conda search` and `conda install`.  These tools will be available only in this specific environment.

```
conda search fastp
conda install fastp
```

4. To leave your current conda environemnt
```
conda deactivate
```


See also the conda docs for more info:

https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html