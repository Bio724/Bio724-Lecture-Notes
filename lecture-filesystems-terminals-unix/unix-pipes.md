## Redirection and pipes

* `>` -- redirect output operator. Sounds the output of the command on the left to the file on the right. 
  - `ls > files.txt` -- `files.txt` now contains a list of all the files in the working directory
  - `ls *.fastq > fastq_list.txt` -- list all fastq files and send this lsiting to `fastq_list.txt`
* `|` -- pipe operator. The output of the command on the left is used as the input for the command on the right.
  - `ls *.jpg | wc -l` -- list all files ending in `.jpg` and count how many they are using the `wc` utility
* `>>` -- append output operator. Like redirect operator but appends output to the specified file rather than creating/overwritng.
* `<` -- redirect input operator