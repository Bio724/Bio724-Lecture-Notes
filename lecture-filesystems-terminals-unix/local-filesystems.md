## Mac OS

* Root = `/`
* Other disks (USB, etc) mounted under `/Volumes`
* User directories under `/Users`; your home directory at `/Users/yourusername`
* System wide applications under `/Applications`; users can also install applications under `/Users/username/Applicatons`
* User specific config files under `/Users/username/Library` (hidden by default)
* Unix related executables under `/bin`, `/sbin`, etc
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