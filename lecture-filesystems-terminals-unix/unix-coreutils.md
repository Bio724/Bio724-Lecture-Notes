## Unixcore utilities

Most of the commmands below are described in detail in the [HTML manual for the GNU coreutils](https://www.gnu.org/software/coreutils/manual/html_node/index.html)


### Navigating the file system

All of the [commands for navigating and manipulating files and diretories](./navigating-filesystems.md) that we previously discussed apply on Unix based systems.

### Create an example file

Using VS Code, create a file named "names.txt" in your home directory, with the following contents:

```
# stage names of various musical artists
Peter
Paul
Mary
George
Ringo
John
Paul
Jose
Placido
Luciano
Beyonce
Kelly
Michelle
Run
DMC
Jay
Posdnuos
Trugoy
Maseo
Jin
Suga
J-Hope
RM
Jimin
V
Jungkook
```

### Other commonly used commands

* `less` -- a "pager" program for reading text, either from a file or stdout, one page at a time. Useful when output spans multiple pages.  To advance/go back a page use `<space>/b` and to quit type 'q'
    - `less file.txt`
    - `ls -l /bin/ | less`  -- notice that that the `ls` command here generates a long list of files. `less` helps us read the output one page at a time.

* `cat` -- print lines of a file to stdout 
  - `cat file.txt`    

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

* `uniq` -- report/omit adjacent repeated lines.  The adjacency requirement means you usually need to sort the input first.
  - `echo 1235231443551 | fold -w 1 | sort | uniq`: get unique digits from input. Also try this without sorting first to see the difference.

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
