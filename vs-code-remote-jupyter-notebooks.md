
## Setting up VS Code to work with remote Jupyter notebooks

After installing Conda on your VM, you can use the Remote SSH features of VS Code to interact with Jupyter notebooks that are running on the VM.  


#### Connect to the remote host

1. `View > Command Palette...`: Connect to VM via "Remote-SSH: Connect to Host..."

### In the Remote-SSH session

1. `View > Command Palette...`: "Python: Select Interpreter"
    Choose the interpreter corresponding to your "base" Conda environment

2. `View > Command Palette...`: "Jupyter: Create New Blank Notebook"

3. You should now be working 

See [Jupyter Notebooks in VS Code](https://code.visualstudio.com/docs/datascience/jupyter-notebooks) for more info.


