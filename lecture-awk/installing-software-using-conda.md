# Conda

[Conda](https://docs.conda.io/en/latest/) is a "package manager" tool that was originally designed for the Python ecosystem but has been widely adopted as a tool for distributing scientific computing software.

Package managers are tools for installing/uninstalling software tools, code libraries, and creating computing environments that provide specific functionality.  One of the powerful aspects of Conda is that it allows users to install and use specific version of software packages in isolated or "sandboxed" environments.  This allows users to highly customize their computing environments without impacting other users of the same system.

## Steps to install conda

1. Download the "miniconda" binary

    ```bash
    wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
    ```

1. Run the installer and follow the prompts, accepting all the defaults:

    ```bash
    bash Miniconda3-latest-Linux-x86_64.sh
    ```

1. Make the conda tools available from the command line by sourcing your shell profile (execute `source .bashrc` at the terminal) or logging off and logging back on

1. Setup software "channels" for common bioinformatics tools

    ```bash
    conda config --add channels defaults
    conda config --add channels bioconda
    conda config --add channels conda-forge
    ```

## Update your Conda distribution

The first time you install Conda it's a good idea to make sure you're using the latest version of the various tools that are included. Update all the packages at once with this command

```bash
conda update --all
```

## Searching and Installing packages

Searching for and installing packages with Conda is  straightforward.

To search packages that match a given string, call `conda search` with a search string (wild-card matching works). For example, if you wanted to search for the [Clustal family of sequence alignment tools](http://www.clustal.org/) you could search as follows:

```bash
conda search clustal*
```

You'll get a list of packages that match, including different versions of the same package.

To install a package, such as `clustalo` (Clustal Omega), you use the subcommand `conda install`:

```bash
conda install clustalo
```


## Creating a conda environment

By default, when you login to your terminal after installing Conda, you will be working in the "base" conda environment.  For the purposes of this class we'll install most of our tools in this base environment, but if you're testing out software or setting up complex analysis pipelines it's often useful to create separate environments to work in. Here's the basic steps on how to do that:

1. Create a new environment (here named "genomics")
  
    ```bash
    conda create -n genomics  
    ```

1. Activate a specific environment

    ```bash
    conda activate genomics
    ```

1. When working in an environment you can search for and install other tools using `conda search` and `conda install`. Any software you install is only available **in that environment**:

    ```
    conda search bwa
    conda install bwa
    ```

1. To leave your current conda environment

    ```bashs
    conda deactivate
    ```

1. To activate the base environment:

    ```bash
    conda activate
    ```

See  the conda docs for more info on managing environments:

<https://docs.conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html>
