
## The Unix philosophy

Doug McIlroy who invented the concept of the Unix `pipe' (discussed below) summarized the Unix philosphy as follows:

> This is the Unix philosophy: Write programs that do one thing and do it well. Write programs to work together. Write programs to handle text streams, because that is a universal interface.

This is not some rigid set of specifications, but rather an approach to writing simple programs that can be tied together in useful ways to accomplish larger, more complex tasks. Most of the standard Unix commands are written with this philosophy in mind and we will endeavor to follow the same philosophy in this class.

The following video, filmed at Bell Labs in 1982, discusses some of the key concepts behind the Unix environment.  I'm highlighting the segment running from roughly 5:00-11:00 minutes that features a discussion of this  philosophy by [Brian Kernighan](https://www.cs.princeton.edu/people/profile/bwk), one of the key contributors to the creation of Unix:

* [Video: AT&T Archives -- The UNIX Operating System](https://youtu.be/tc4ROCJYbm0?t=296)

NOTE: In addition to contributing to the creation of Unix, Kernighan was involved in the invention of the AWK and Go programming languages, and along with Dennis Ritchie (the inventor of the C programming language) wrote the highly influential book "The C Programming Lanuguage" (often refered to as the "K&R C" book.

### Everything's a file

Another defining feature of Unix systems is often summarized as "everything is a file" (see for example [this article](https://dev.to/awwsmm/everything-is-a-file-3oa)).  What that means is that  files, directories, devices (e.g. terminals, printers, drives, etc), network sockets, and processes can all be treated or manipulated with similar semantics and syntax.

For example, we can use the same command to write something to a terminal device as we do to a file (we'll explain what the command `echo` and the `>` operator do below). To illustrate this try the following:

* Make sure you're logged into your VM via SSH
* Execute the command `tty`, which tells you what terminal device your ssh session is connected to. For example, on my virtual machine I see the following:

    ```
    pm21@vcm-24327:~$ tty
    /dev/pts/1
    ```

* Use the `echo` command to write to a message to a file (to confirm ):

    ```
    echo "Hello, file!" > ~/hello.txt
    ```

    To confirm this worked as expected, print the contents of the file using the `cat` command:

    ```
    cat ~/hello.txt
    ```

* Now, use the `echo` command to write a message to the terminal:

    ```
    echo "Hello, terminal" > /dev/pts/1
    ```

* We can even write messages between terminals. Without closing your first terminal window, open another terminal window and create a second SSH connection to your VM.  As before, use the `tty` command to figure out which terminal device that second session is associated with:

    ```
    pm21@vcm-24327:~$ tty
    /dev/pts/2
    ```

* From your first terminal window (associated with `/dev/pts/1` in my case), use the `echo` command to send a message to your second terminal window:

    ```
    echo "Hello, other terminal!" > /dev/pts/2
    ```

    If you executed the commands correctly, your message should show up in the second terminal window. Cool!
