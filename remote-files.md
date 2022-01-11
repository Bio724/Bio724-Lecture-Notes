
## Moving files to/from your VM


### Using the command line

* `scp` -- secure copy.  Command line tool to copy files to or from a remote machine via SSH.
  * Move a local file (`foo.txt`) to your virtual machine: 
    - `scp foo.txt netid@hostname:~`
  * Move a remote file (`~/data/bar.txt`) to your local machine (`~/bio208/data`):
    - `scp netid@hostname:~/data/bar.txt ~/bio208/data` (saves `bar.txt` under the local directory `/bio208/data`)

* `wget` -- a command line program for downloading files from the web. You would typically use this to download files from a URL to a remote machine without.
    * e.g. Download the plain text version of the SARS-CoV-2 reference genome from the course website to your local machine:
       - `wget https://raw.githubusercontent.com/bio208fs-class/bio208fs-lecture/master/data/covid-ref-unwrapped.txt`  


### Using Cyberduck (or another SFTP client)

Cyberduck provides a graphical interface for moving files back and forth from a remote machine.  We'll demonstrate how to use Cyberduck in class.


### Editing remote files using VSCode

We'll be using the Visual Studio Code (VSCode) text editor for many of our programming tasks.  One of the powerful aspects of VSCode is it's powerful extension system. We will use the [Visual Studio Code Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) to facilitate working with files on our virtual machines. I will review in class how to set this up.