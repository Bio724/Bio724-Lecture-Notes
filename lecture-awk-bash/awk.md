# Awk

Awk (`awk`) is a programming language designed for processing structured text files. You can use it to write short one liners or to write full blown programs. We'll use Awk to illustrate how you might transitions from simple command line usage into slightly more complicated scripts.

## Simple examples

One simple thing we can do with Awk is to use it to re-order fields in a structured data file:

```bash
awk '{print $2, $1, $3}' columns.txt
```

The text in quotes represents the Awk program which we're apply to the file `columns.txt`. The dollar signs followed by numbers refer to the fields of the file. With it's default setting `awk` operates line by line, so you can interpret the above statement as saying:

> "for each line, print the fields 2, 1, and 3".

## Awk delimiters

By default, Awk recognizes any non printing character including spaces to delineate fields/columns. If we want to be specific about the character used as a delimiter, we can set the `-F` or `--field-separator` option. For example to use tabs as the delimiter we could do:

```bash
awk -F'\t' '{print $2, $1, $3}' columns.txt
```

## `pattern {action}` syntax

The basic syntax of `awk` is often depicted in the form `pattern {action}`. The above command only specified an action, so it was applied to every line. By contrast, in the example below we specify both a pattern and an action. The pattern can be read as -- "if the 2nd field is 'chromosome'". For all lines that match that pattern the corresponding action is applied; in this case the action is "print fields 1 and 4" (the chromosome name and its length):

```bash
awk '$2=="chromosome" {print $1, $4}' yeast_features.txt
```

Here's another `pattern {action}` pair that shows how we could find all gene features with length less than 300 and count them:

```bash
awk '$2 == "gene" && ($4 - $3 + 1) < 300 {print $0 }' yeast_features.txt | wc -l
```

`&&` is the AND operator. Read this as "if the 2nd field is 'gene' AND the length of the feature is less than 300." (Note: we add one to the calculation of length because the feature coordinates are inclusive of both the start and end coordinate).

In this last example we add one more condition -- we use a regular expression against the 6th field (`$6 ~ /../`) to look for the string "orf_classification=Dubious". The results indicate that about a third of these small gene features have been classified as "dubious" (i.e. may not actually code for proteins).

```bash
awk '$2 == "gene" && ($4 - $3 + 1) < 300 && $6 ~ /orf_classification=Dubious/ {print $0 }' yeast_features.txt | wc -l
```


## Multiple rules and Awk scripts

So far our `pattern {action}` rules have matched focused on single patterns.  However, you can specify multiple matching rules and do different computations depending on which one matches. For example, if we wanted to count genes and mRNAs simultaneously in an annotation file and then print out the counts at the end, we can construct a awk call with three rules:

```bash
awk '$2 == "gene" {gene_ct += 1} $2 == "mRNA" {mRNA_ct += 1} END {print gene_ct, mRNA_ct}' yeast_features.txt
```

At this point the command line is getting a little out of control so it would be better to put the rules into a file we can call. In your editor create a file called `count_genes_mRNAs.awk` with the following contents:

```awk
$2 == "gene" {
    gene_ct += 1
} 

$2 == "mRNA" {
    mRNA_ct += 1
} 

## called once all lines have been processed
END {
    print gene_ct, mRNA_ct
}
```

This file works exactly like our command line version, but it has the advantages that it's easier to read and thus easier to debug or modify.  To call this Awk program from the command line we use the `-f` option to specify the script:

```bash
awk -f count-genes-mRNAs.awk yeast_features.txt
```

## Variables in Awk

The prior example introduced the use of "variables" in Awk. Variables store values; in Awk that are only two variable types, strings and numbers.  

### Numerical variables

In the example above `gene_ct` and `mRNA_ct` are numerical variables. In Awk, when a numerical value is first created (initialized) it's automatically assigned the value zero.   In this example we used these variables in lines that look like `gene_ct += 1`; the `+=` operator is a short-hand way of saying "add the value on the right to the value of the variable on the left" so this statement is equivalent to the slightly wordier `gene_ct = gene_ct + 1`.

### String variables

String variables are created by wrapping characters in double quotes.

```awk
awk 'BEGIN {a = "Hello"; b = "World"; print a b}'
```

You can get the length of a string using the `length()` function:

```awk
awk 'BEGIN {a = "Hello"; print "The length of " a " is " length(a)}'
```

The GNU Awk implementation (`gawk`) provides a wide variety of [string functions](https://www.gnu.org/software/gawk/manual/gawk.html#String-Functions). Some of the most useful include: `substr()`, `split()`, and `gsub()`/`sub()` . Here's an example using `substr()`:

```awk
awk '
BEGIN {
  s = "Jabberwocky"
  print substr(s, 4, 7) # arguments are string, start, length
}'
```

## Arrays in Awk

Most programming languages have a core set of "data structures" which specify different ways of storing and accessing values. In Awk the core data structure is called an array. It has some superficial similarities to arrays (sometimes called lists) in other languages, but also has some features that are fairly unique to Awk.  

An array can be thought of being made up of a contiguous set of slots or positions where we can store values.  Each slot has an associated label that we call its index (plural indices). In most languages array indices are integers, with the first position indexed by successive integer values (some languages start indexing the 0, others with 1). In Awk, array indices can be either numbers or strings.  This makes arrays in Awk a little like a combination between what other languages might call an array (or list) and a dictionary (hash map). 

Here are some illustrations of using arrays in Awk:

* The `split()` function splits a string based on a delimiter and returns the substrings in an array that is indexed by integer position

  ```bash
  awk '
  BEGIN {
    name = "kebab-case-name"
    split(name, parts, "-")  # parts array is created
    print "part 1: " parts[1]
    print "part 2: " parts[2]
    print "part 3: " parts[3]
  }'
  ```

  Typically you'd use a for-loop to iterate over the indices of `parts`

  ```bash
  awk '
  BEGIN {
    name = "kebab-case-name"
    # split() return the number of substrings it creates
    n = split(name, parts, "-") 

    # for-loop iterating over integer indices
    for (i = 1; i <= n; ++i )
      print "part " i ": " parts[i]
  }'
  ```

* `uniqct.awk` -- a program that outputs a table listing the unique set of lines in the input, and the number of times that each line  appears

  ```awk
  # this rule applies to every line, $0 returns the whole line
  { counts[$0] += 1 }

  END{
    # for loop with implicit indices
    for (idx in counts)   
      print idx, counts[idx]
  }
  ```

  This code might be used like so:

  ```bash
  cut -f 2 yeast_features.txt | awk -f uniqct.awk
  ``` 

For a full exposition on Awk's arrays, read the Gawk manual on the [Basics of Arrays](https://www.gnu.org/software/gawk/manual/html_node/Array-Basics.html). Here I illustrate some basic uses of arrays.


## Some useful Awk constructs

- `BEGIN {action}` -- do the specified action before reading any input

- `END {action}` -- do the specified action after reading all input

- Record and field counts:

  - `FNR` and `NR` -- `FNR` gives the current record number in the current file (awk can process multiple files simultaneously); `NR` gives the total number of records seen so far. When processing a single file, `FNR` == `NR`

  - `NF` -- gives the number of fields in the current record(line)

    ```bash
    awk -F "\t" `{print "There are", NF, "fields in line", FNR}` yeast_features.txt 
    ```

- Field separators -- both the input field seperator (`FS`) and the output field separator (`OFS`) can be specified in an Awk program. This is usually done in a `BEGIN` rule:

  - `firstlast_csv.awk` -- outputs first and last fields of input file in CSV separated fileds

    ```awk
    BEGIN {
      OFS = ","
    }

    {print $1, $NF} # applies to every line
    ```
