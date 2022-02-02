
# Package Managers on Linux Systems

Most popular Linux-based operating systems provide a package manager for installing software.  You can think of a package manager as akin to an "App Store", and most Linux desktop environments (e.g. Gnome, KDE) provide a simple point and click software installation interface that is very much like the app stores you are familiar with on Mac OS or Windows.  Since we're working with a remote VM, we'll see how to install software packages from the command line.

On derivates of Debian Linux (which includes Ubuntu, the system we're using on our VMs) the package manager is a tool called `apt`.  We can use the `apt` command to search for software as well as install software.

For example, over the next few lectures we're going to need a couple of software tools that are not installed by default on our VMs. These include a tool called `gawk` ([GNU awk](https://www.gnu.org/software/gawk/manual/gawk.html)), and a number of utilities (`zip`, `dos2unix` and `parallel` [[GNU parallel](https://www.gnu.org/software/parallel/)]).

### Searching for a package using `apt`

To search for a package using `apt` we can use the `search` subcommand:

```
pm21:~$ apt search gawk
Sorting... Done
Full Text Search... Done
dpkg-awk/focal,focal 1.2+nmu2 all
  Gawk script to parse /var/lib/dpkg/{status,available} and Packages

gawk/focal 1:5.0.1+dfsg-1 amd64
  GNU awk, a pattern scanning and processing language

gawk-doc/focal,focal 5.0.1-1 all
  Documentation for GNU awk

mawk/focal,now 1.3.4.20200120-2 amd64 [installed]
  Pattern scanning and text processing language

skktools/focal 1.3.4-1 amd64
  SKK dictionary maintenance tools

```
We see that there are multiple matches to our search (by default `awk` searches both titles and text descriptions of the packages).  The specific package we want is `gawk` itself.

### Installing a package using `apt`

To install a package using `apt` we can use the `install` subcommand:

```
sudo apt install gawk
```

This time we invoked `apt` by prefixing it with the `sudo` command ("super user do"). `sudo` is the command line equivalent of saying "invoke the following command with Administrator privileges". Like on a Mac or Windows machine, for security reasons, installing software "globally" on a Unix-based system requires you have administrative rights on a system.  You'll be prompted to enter your password (your NetID password in the case of your VM) before the `apt install` subcommand will work.

### Your turn

Use `apt` to search for and install the programs `zip`, `dos2unix`, and `parallel`.  Note that sometimes the output of `apt search` can be quite long, so you may want to pipe the output to `less` to facilitate reading.