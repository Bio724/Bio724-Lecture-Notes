## Mac OS

* Root = `/`
* Other disks (USB, etc.) mounted under `/Volumes`
* User directories under `/Users`; your home directory at `/Users/yourusername`
* System wide applications under `/Applications`; users can also install applications under `/Users/username/Applicatons`
* User specific config files under `/Users/username/Library` (hidden by default)
* Unix related executables under `/bin`, `/sbin`, etc.
* `PATH` is an environment variable, settable from command line or `~/.profile`


## Windows 10/11

* Root = `C:\`
* Other disks mounted as `D:\`, `E:`, etc.
* User directories under `C:\Users`; your home directory at `C:\Users\yourusername`
* System wide applications under `c:\Program Files` (64 bit) and `C:\Program Files (x86)` (32 bit)
* `Path` variable settable from "System Properties" dialog


## Both

* Standard shortcuts like "Desktop", "Documents", and "Downloads" are usually subdirectories of your home directory
    
* Hidden files and directories can be viewed by setting appropriate options in Finder / Explorer

## Recommendations for file naming schemes

* Avoid spaces (or other non-printing characters) and punctuation other than dashes, underscores, and periods in file names

* File names that include dates should preferably follow the [ISO-8601 formatting standard](https://en.wikipedia.org/wiki/ISO_8601), which has the form "YYYY-MM-DD". For example, an experiment done of Jan 12, 2022 should be named something like "2022-01-12-Expt01.csv". 
    - The advantage of this is it makes it easy to sort and search by date

* Try and be consistent in your naming schemes. I promise this will make your life (and/or that of your collaborators) easier at some point in your research career!