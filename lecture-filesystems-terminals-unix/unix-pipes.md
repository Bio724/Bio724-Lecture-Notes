## Unix standard streams

Programs that follow Unix conventions and that execute in a shell have associated with them a set of what are called "standard streams", which you can think of as channels for communicating with the outside world. The three standard streams are referred to as:

* standard input (stdin)
* standard output (stdout)
* standard error (stderr)

By default, stdin is usually associated with keyboard input and stdout and stderr are the terminal display, but these can be changed as show below.



## Redirection and pipes



* `>` -- redirect the output operator. Sends the output of the command on the left to the file, device, or stream on the right. If the file already exists, it will be overwritten. If the file doesn't exist it will be created.
  - `echo "Hello, World!"` -- by default, stdout is associated with the terminal so executing this command command prints the result of the echo command to terminal display.
  - `echo "Hello, World!" > hello.txt` -- We're now redirecting stdout to a file called `hello.txt` (open this file to confirm that the contents are what is expected)

* `>>` -- append output operator. Like redirect operator but appends output to the specified file rather than creating/overwriting.
  
  ```
  echo "first line" >> lines.txt
  echo "second line" >> lines.txt
  ```


* `<` -- redirect input operator
  - The `tr` (translate) doesn't have a built in mechanism for reading from a file, only from stdio. However we can redirect a file to stdio use the `<` operator. For example, here we read text from the file `hello.txt` (created above) and translate all upper case letters to their lower case equivalents:

  ```
  tr '[:upper:]' '[:lower:]' < hello.txt
  ```

  We can even chain together redirect operators like so:

  ```
  tr '[:upper:]' '[:lower:]' < hello.txt > lower_hello.txt
  ```

  
* `|` -- pipe operator. The output of the command on the left is used as the input for the command on the right.
  - `ls *.jpg | wc -l` -- list all files ending in `.jpg` and count how many they are using the `wc` utility



### More about redirection and pipes

Additional reading: [Five ways to use redirect operators in Bash](https://www.redhat.com/sysadmin/redirect-operators-bash)

Video: [Brian Kernighan on Unix pipelines](https://www.youtube.com/watch?v=bKzonnwoR2I)

