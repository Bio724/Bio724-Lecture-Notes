
## Moving files to/from your VM


### Using the command line

* `scp` -- secure copy.  Command line tool to copy files to or from a remote machine via SSH.
  * Move a local file (`foo.txt`) to your virtual machine: 
    - `scp foo.txt netid@hostname:~`
  * Move a remote file (`~/data/bar.txt`) to your local machine (`~/bio724/data`):
    - `scp netid@hostname:~/data/bar.txt ~/bio724/data` (saves `bar.txt` under the local directory `~/bio724/data` assuming that directory already exists)

* `wget` -- a command line program for downloading files from the web. You would typically use this to download files from a URL to a remote machine without.
    * e.g. Download the GFF formatted genome annotation for the reference budding yeast (Saccharomyces cerevisiae) genome from NCBI:
      - `wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.gff.gz`



### Using Cyberduck (or another SFTP client)

Cyberduck provides a graphical interface for moving files back and forth from a remote machine.  We'll demonstrate how to use Cyberduck in class.


### Editing remote files using VSCode

We'll be using the Visual Studio Code (VSCode) text editor for many of our programming tasks.  One of the powerful aspects of VSCode is it's powerful extension system. We will use the [Visual Studio Code Remote Development Extension Pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) to facilitate working with files on our virtual machines. I will review in class how to set this up.