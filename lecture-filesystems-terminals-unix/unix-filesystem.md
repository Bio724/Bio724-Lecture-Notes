
## Linux file system, typical structure

* Root = `/`
* Other disks (USB, etc) mounted under `/Vomntlumes`
* User directories under `/home`; your home directory at `/home/yourusername`
* System wide applications under `/usr/bin` (often linked to '/bin'); users can also install applications under `/usr/local/bin`
* User specific config files usually in home directory (hidden by default, use `ls -a` to see hidden files)
* `PATH` is an environment variable, settable from command line or `~/.profile`