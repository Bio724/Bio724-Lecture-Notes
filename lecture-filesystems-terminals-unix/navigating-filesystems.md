
## Commands for navigating the file system on Unix based systems 

NOTE: The following commands also work in Windows Powershell

* `pwd` -- prints name of your "working" directory (i.e. the directory you're currently in)
* `ls` -- lists the contents of the working directory
* `cd` -- change directory
  * `cd Downloads`
  * `cd ~` (move to your home directory)
* `mkdir` -- make a new directory
  * `mkdir foo_dir`
  * `mkdir bar_dir`
* `rmdir` -- remove a directory (must be empty)
  * `rmdir bar_dir`  
* `rm` -- remove a file
  * `rm bar.txt`
* `cp` -- copy a file
  * `cp foo.txt foo_copy.txt`
* `mv` -- move a file or directory
  * `mv foo.txt baz.txt`
  * `mv foo_dir foo.dir`
* `cat` -- write the contents of a file to the terminal:
  * `cat foo.txt`
* `more` -- a pager program. View the contents of a file, one page at a time. Type `<space>` to advance pages, `q` to quit.

Side note: Why is it common to use names like `foo`, `bar`, and `baz` in examples? See https://en.wikipedia.org/wiki/Foobar


## Shortcuts for working with the file system

* `~` -- refers to the users home directory.  
  * `cd ~` = change to my home directory
  * `ls ~/*.txt` = list all files ending with the prefix `.txt` in your home directory
* `.` -- the current directory
  * `cd ./tmp` = move to the directory called `tmp` that is located in the directory the `cd` command is executed from.  
* `..` -- the directory above the current directory (if it exists)
  * `cd ..` = move up one level in the directory hierarchy.  For example if `pwd` is `/home/jsmith` then `cd ..` moves you to `/home`
*  `/` -- the root directory of the file system
  * `cd /data` = move to the `data` directory that is the subdirectory of the root
  * `ls /` = list all files and directories in the root directory
