## Unix core utilities

Most of the commmands below are described in detail in the [HTML manual for the GNU coreutils](https://www.gnu.org/software/coreutils/manual/html_node/index.html)

### Command-line options

Many Unix programs accept command-line optoins (switches) to control or modify their behavior.  Generally there are two styles: short switches designated with a single letter preceded by a hyphen (e.g. `ls -a`) or  keyword options designated by two hyphens followed by a keyword (e.g. `ls --all`). There are no hard and fast rules about how command-line options are used, but there are some conventions that most programs follow:

* When using multiple single letter options, multiple options can be written together after a single hyphen, e.g. `ls -la` == `ls -l -a`.

* Options can be be configured to accept arguments. 
  - Sometimes arguments are optional, but sometimes they are required 
  - In the case of single letter options the argument comes immediately after the switch or can be separated by a space, e.g. `cut -f 3 file.txt` == `cut -f3 file.txt` (cut the third column from each line; see below for info about `cut`)
  - When using keyword options, arguments can be separated by a space of an equal sign, e.g. `ls --hide="*.txt"` (lists files, hiding everything that matches the given pattern)
  - Some switches accept multiple arguments, e.g. `cut -f 1,3 file.txt`

* Many programs have a `--help` switch that prints out a brief summary of the standard usage pattern along with a list of the available options. A program's `man` pages are usually the best place to get more detailed explanations of how the options work. 

Futher discussion of command line switches can be found here: http://catb.org/esr/writings/taoup/html/ch10s05.html


### Navigating the file system and file manipulation

All of the [commands for navigating and manipulating files and diretories](./navigating-filesystems.md) that we previously discussed apply. Here are a few additional useful tools:

* `ln` -- make links between files.  Typically you'll want to create "symbolic links" (symlinks), which act like "shortcuts" on Windows systems. Links are useful to create references to files located nested deep in directory hierarchies or with long and tedious names. 
    - Example: recall that the SARS-CoV-2 GFF file we downloaded had a very long name of the form `GCF_009...`.  That would be tedious to type everytime we wanted to refer to the file, so let's create a symlink to it in our home directory (note this is all one line:)

        ```
        ln -s genome_annotations/GCF_009858895.2_ASM985889v3_genomic.gff ~/covid.gff
        ```

* `touch` -- change the modification time stamp of a file, or if file doesn't exist create an empty file
    - `touch newfile.txt`

* `df` -- report the amount of space used/available on the file sytem
    - `df -h`: the `-h` option reports space in "human readable" units (K = kilobyte, M = megabyte, G = gigabyte) instead of raw bytes


### Other commonly used commands

* `less` -- a "pager" program for reading text one page at a time ("less is a better more"!). Useful when output spans multiple pages.  To advance/go back a page use `<space>/b` and to quit type `q`.
    - `less covid.txt`
    - `ls -l /bin/ | less`  -- notice that that the `ls` command here generates a long list of files. `less` helps us read the output one page at a time.
   
* `head` and `tail` -- output the first/last part of a file.  Both default to output 10 lines.
    - `head covid.gff`
    - `tail covid.gff`
    - `head -n 5 covid.gff`: show the first 5 lines of the file

* `cat` -- copies file(s) to stdout 
  - `cat file.txt`: write file to stdout
  - `cat file1.txt file2.txt > file1and2.txt`: concatenate two files

* `wc` -- counts bytes, characters, words, or lines
  - `wc -l file.txt`: count the number of lines in `file.txt`
  - `wc -m file.txt`: count the number of characters in `file.txt`

* `echo` -- send input text to standard output (stdout)
  - `echo Hello World!`
  - `echo -e 'Hello\nWorld!'`
    - Here we wrap the input in quotes so we can use the "backslash escape" representation of a newline (`\n`). The `-e` argument tells `echo` to interpret backsplash escapes appropriately. Another common backslash escape is `\t` to represent a tab character.
  - `echo Hello World > hello.txt`: send text to a new file `hello.txt` using the redirection operator.
  - `echo Hello World | wc -m`: send text to another command using the pipe operator (see `wc` below)


* `fold` -- wrap lines to the specified with, printing to stdout
  - `fold -w 5 file.txt`:
  - `echo 12345 | fold -w 1`

* `tr` -- translate (substitute) or delete characters in input. Note that unlike most commands `tr` will not take a file as an argument, so typically you would use `cat` to send the contents of a file through `tr`
  - `echo ATGCAA | tr A a`: substitute lower case "a" for uppercase "A"
  - `echo ATGCAA | tr -d A`: delete all "A" characters
  - `echo ATGCAA | tr ATGC TACG`: substitute each character in the first set ("ATGC") with the matching character in the second set ("TAGC"). 

* `rev` -- reverse input
  - `echo ATGCAAA | rev`
  - `echo ATGCAAA | rev | tr ATGC TACG` -- why might this be useful when working with representations of nucleotides?

* `sort` -- sorts lines of input
  - `sort file.txt` --  sort line in `file.txt`
  - `echo -e 'foo\nbar\nbaz\qux' | sort` 
  - `sort -k 3 -n columns.txt` -- sort numerically on the 3rd field (column) of the data
  - `sort -k 3 -n --debug columns.txt` -- the `--debug` option is useful when you're getting unexpected results. This highlights the field that `sort` is using in each line to do the sorting.
    - See [this page](./unexpected-sorting.md) and the [GNU FAQ](https://www.gnu.org/software/coreutils/faq/coreutils-faq.html#Sort-does-not-sort-in-normal-order_0021) if you've doubled and triple checked your commands and yet getting unexpected sorting results

* `uniq` -- report/omit adjacent repeated lines.  The adjacency requirement means you usually need to sort the input first.
  - `echo 1235231443551 | fold -w 1 | sort | uniq`: get unique digits from input. Also try this without sorting first to see the difference.

* `comm` -- compares two sorted files, line by line. By default produces three-column output 

* `cut` -- removes sections (bytes, characters, or fields) from input
  - For this example create a file (`columns.txt`) with the following command (`\t` = TAB character, `\n` = newline character): 
    `echo -e 'one\ttwo\tthree\nfour\tfive\tsix' > columns.txt`
  If you open the file you will see it is formatted like this:
    ```
    one     two     three
    four    five    six
    ```
  - `cut -f 2 columns.txt`: get the second column (`cut` assumes columns are separated by tabs by default)
  - `cut -f1,3 columns.txt` get first and third column

* `paste` -- merge corresponding lines from inputs
  - `paste columns.txt columns.txt`
  - `tac columns.txt | paste columns.txt -`: the dash (`-`) here specifies that input should come from stdin. Can you guess what the command `tac` does?
  - `paste -s columns.txt`: The `-s` command merges lines within the file. This gives us behavior that is like the inverse of the `fold` command we saw previously.

* `grep` -- find regions of the input that match the specified pattern. Pattern matching uses what is known as "Regular Expressions" (regex). See a [short introduction to grep](https://informatics.fas.harvard.edu/short-introduction-to-grep.html) and the [Grep Manual](https://www.gnu.org/software/grep/manual/grep.html) for more details.
  - `grep "A" genome.txt`: find all lines in `genome.txt` that include the letter "A". 
    * By default `grep` returns lines, rather than the matches themselves.
  - `grep -o "A" genome.txt`: the `-o` option tells grep to return only the matching parts of the input.
  - `grep -c "A" genome.txt`: count the number of matches in the input.

* `sed` -- sed is a "stream editor", a tool that offers powerful text manipulation capabilities.  For the purposes of this introduction we're going to focus on just one use case -- text substitution.
  - `echo "Hello world, Hello universe" | sed 's/Hello/Goodbye/`: substitute the first occurence of "Hello" with "Goodbye"
  - `echo "Hello world, Hello universe" | sed 's/Hello/Goodbye/'`: substitute the all occurences of "Hello" with "Goodbye" (the `g` at the end of the sed command means "globally")
  - `echo "Hello world, Hello universe" | sed 's/Hello//g'`: delete all occurences of "Hello"
