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

The prior example demonstrated how "variables" are created in Awk. Variables store values. In Awk that are only two variable types, strings and numbers.  

### Numerical variables

In the example above `gene_ct` and `mRNA_ct` are numerical variables. In Awk, when a numerical value is first created (initialized) it's automatically assigned the value zero.   In this example we used these variables in lines that look like `gene_ct += 1`; the `+=` operator is a short-hand way of saying "add the value on the right to the value of the variable on the left" so this statement is equivalent to the slightly wordier `gene_ct = gene_ct + 1`.

### String variables


## Some useful Awk constructs

- `BEGIN {action}` -- do the specified action before reading any input

- `END {action}` -- do the specified action after reading all input

- Record and field counts:

  - `FNR` and `NR` -- `FNR` gives the current record number in the current file (awk can process multiple files simultaneously); `NR` gives the total number of records seen so far. When processing a single file, `FNR` == `NR`

  - `NF` -- gives the number of fields in the current record(line)

    ```bash
    awk -F "\t" `{print "There are", NF, "fields in line", FNR}` yeast_features.txt 
    ```

- Arrays -- read the Gawk manual on the [Basics of Arrays](https://www.gnu.org/software/gawk/manual/html_node/Array-Basics.html)

  - e.g. `$3 == "ncRNA_gene" { cts[$1] += 1}` -- here `cts` is an array, indexed by the values in field 1. We might use this as follows:

    ``` awk
    $3 == "ncRNA_gene" {
        cts[$1] += 1
    }

    END {
        for (seqid in cts) 
            print seqid, cts[seqid]
    }
    ```

    To use this code put it in a source file `ncRNAs.awk` and call the program as:

    ```bash
    awk -f ncRNAs.awk yeast_features.txt 
    ```

- `match(field, regex)` -- this is a function that finds the specified regex (regular expression) in the given field. Per the Gawk manual: 

    > "Returns the character position (index) at which that substring begins (one, if it starts at the beginning of string). If no match is found, return zero."

    The following example returns all features for which the attribute field indicates the product is uncharacterized:

    ```bash
    awk 'match($9, "product=uncharacterized") {print $0}' yeast.gff
    ```

- `gawk` provides a more powerful version of `match` where the matches can take an optional array as the third argument. As described in the Gawk manual:

    > If array is present, it is cleared, and then the zeroth element of array is set to the entire portion of string matched by regexp. If regexp contains parentheses, the integer-indexed elements of array are set to contain the portion of string matching the corresponding parenthesized subexpression.

    Here's an example of using the gawk `match` function:

    ```awk
    $3 == "protein_coding_gene" {
        id = ""
        if (match($9, "ID=([^;]+);", matchvar))
            id = matchvar[1]
        print id, $1, $4, $5
    }
    ```
