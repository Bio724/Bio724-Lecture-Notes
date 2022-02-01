
# Example pipeline

## Goal

Analyze promoter regions of genes that are hypothesized to be targets of a transcription factor for the occurence of a binding site motif.

Starting data:

* Table of genes that are hypothesized to be targets of STE12
* FASTA file with the entire yeast genome
* GFF file with feature annotation for yeast genome
* Sequence logo of binding site motif of interest

## Data

* [RefSeq GFF file](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.gff.gz) -- A GFF file for Saccharomyces cerevisiae Genome release 64.3.1.

* [RefSeq FASTA file](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.fna.gz) -- gzipd FASTA file with DNA sequence of the S. cerevisiae genome.

* [STE12 Targets](https://raw.githubusercontent.com/Bio724/Bio724-Example-Data/main/STE12_targets.tsv) -- I downloaded this from SGD for this example, but would typically come from something like a clustering analysis.

* STE12 Sequence Motif -- via [The Yeast Transcription Factor Specificity Compendium](http://yetfasco.ccbr.utoronto.ca/) ![STE12 binding site motif](./figures/STE12-motif.png)



## Overview of Approach

* Filter GFF file for genes features corresponding to our targets of interest 

* Use filtered GFF in combination with [SeqKit](https://bioinf.shenwei.me/seqkit/) to extract promoter regions 

* Count occurences of motif in each promoter 

* Create a table with Systematic Name and Motif Count 

* Wrap our pipeline into a re-usable Bash script so it can be easily applied to other sets of genes and TF motifs

* How could we do this analysis efficiently for many sets of genes? For example, clusters of co-regulated genes identified in a transcriptome analysis 

## Detailed steps

### Create a working directory and download and decompress the data 

```bash
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.gff.gz
wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/146/045/GCF_000146045.2_R64/GCF_000146045.2_R64_genomic.fna.gz
wget https://raw.githubusercontent.com/Bio724/Bio724-Example-Data/main/STE12_targets.tsv
```

```bash
gunzip GCF_000146045.2_R64_genomic.gff.gz
gunzip GCF_000146045.2_R64_genomic.fna.gz
```

Setup symbolic links (symlinks) to have shorter, more convenient names to type while preserving full file names of source files:

```bash
ln -s GCF_000146045.2_R64_genomic.gff yeast.gff
ln -s GCF_000146045.2_R64_genomic.fna yeast.fna
```

### Filter on gene features in the GFF file

```bash
awk -F'\t' '$3 == "gene" {print}' yeast.gff > genes.gff
```

### A note on sorts and joins

As [mentioned previously](../lecture-filesystems-terminals-unix/unexpected-sorting.md), locale settings in your OS can effect sorting (e.g. the sorting rules for simple ASCII encoding are different than for UTF-8). This is especially true when combining `sort` and `join`.  For this reason, the [GNU documentation for join](https://www.gnu.org/software/coreutils/manual/html_node/Sorting-files-for-join.html) recommends: "The sort and join commands should use consistent locales and options if the output of sort is fed to join". 

Below I've added the invocation `LC_ALL=C` to the beginning every line involving sorting or joining to ensure this.  Another option would be to invoke `export LC=ALL` in your bash session or, to make this the default by adding `export LC=ALL` to your `.bashrc` file.



### Create an "augmented" GFF file that includes Systematic Names as a column

We'll create an Awk script that uses the [`match(field, regex, array)`](https://www.gnu.org/software/gawk/manual/html_node/String-Functions.html#index-match_0028_0029-function) function to identify `ID` attributes in the 9th field of the GFF file, and extract the corresponding systematic names for each gene.

`idmatcher.awk`:
```awk
BEGIN { 
  FS = "\t"
  OFS = "\t"
}

$3 == "gene" {
    id = ""
    if (match($9, "ID=gene-([^;]+);", matchvar))
        id = matchvar[1]
    print id, $0
}
```

We then apply this to our genes file and sort the output on the first column (systematic names):

```bash
LC_ALL=C; awk -f idmatcher.awk genes.gff | sort -k 1 -t$'\t' > augmented-genes.gff
```

### Reduce the STE12 targets file to systematic names

If you look at the `STE12-targets.tsv` file you'll see that is a tab-separated file that also include some metadata rows (prefixed by `!`) as well as a blank row and a header row.  We'll need to remove this extraneous information before extracting the systematic names of the targets from the fourth field of each row.  In lecture I did this in a quick-and-dirty way by using awk to ignore any rows that didn't have at least four fields, but here I'll demonstrate a more thorough approach in awk to explicitly remove these extraneous rows:

```bash
LC_ALL=C; awk -F '\t' '$1 !~ /^!|^$/ {print $4}' STE12_targets.tsv | tail -n +2 | sort > target-systnames.txt
```

Explanation:

* `'$1 !~ ` -- the `!~` operator evaluates to true  if the regular expression the follows **does not match**.
* `/^!|^$/` -- this is the regular expression; it has two parts separated by the or `|` operator. `^!` = starts with an exclamation mark; `^$` = empty line (`^` = starts, `$` ends; so with nothing separating them it just means a line with nothing in it)
* `tail -n +2` -- here we're trimming off the header line with the `tail` command. When the argument to `n` (`--lines=`) is prefixed with `+` it means output starting with the given line number 
* Finally we `sort`. Since we only have a single column we don't have to worry about specifying the column to sort on or field delimiters.

### Join the GFF and target gene files to reduce GFF to genes of interest

Now we want to filter the GFF records to only include our target genes of interest.  The prior data cleaning and filtering steps were all in the service of this step:

```bash
LC_ALL=C; join -j 1 -t $'\t' augmented-genes.gff target-systnames.txt > augmented-targets.gff
```
Since the field number we're joining on is the same for both files (field 1) could use the `-j` option here to specify this simultaneously for both files.

Take a moment to open the `augmented-targets.gff` file in your editor to confirm we've reduced the GFF file to just the 16 target genes of interest.

**Sidebar**: You might be wondering about the use of `$'\t'` above.  This is the "quoted" version of writing a TAB-character in the bash shell (see the explanation of [ANSI-C Quoting](https://www.gnu.org/software/bash/manual/html_node/ANSI_002dC-Quoting.html#ANSI_002dC-Quoting) in the GNU Bash Manual). Alternately, you could explicitly enter a TAB character in the terminal by typing `Ctrl-V TAB` (i.e. type the Control key and the "V" key simultaneously, and then hit the TAB key) but this would be hard for me to explicitly indicate in these examples. You might further wonder why some program allow  to just write '\t' (like `awk` above), while others require the extra step of adding the dollar sign (like `sort` and `join`). I don't know for sure, but I'm guessing this is primarily a function of historical legacy for commands like `sort` and `join` and the maintainers avoiding potentially code-breaking changes in how these programs parse characters.


### Remove the extra column from the augmented GFF file

We're almost ready to use our filter GFF file but there's one last step we need to take care. Because we augmented the GFF table with an extra column containing the systematic names (useful for our join operation), it's no longer in valid GFF format. Let's convert it back to a valid GFF file by simply dropping the augmented first column using cut:

```bash
cut -f 1 --complement augmented-targets.gff > targets.gff
```

### Extracting promoters using our target GFF file and SeqKit

[SeqKit](https://bioinf.shenwei.me/seqkit/) is a very useful command-line tool for working with sequence data in FASTA or FASTQ formats. It's fast, cross-platform, and well documented and has become one of my "go to" tools for computing on FASTA files. The `seqkit` program is built around a series of subcommands which are nicely summarized [here](https://bioinf.shenwei.me/seqkit/#subcommands).


Our first step use of `seqkit` is to extract the sequences from our whole genome FASTA file that correspond to the promoters of our target genes of interest. We'll use the `subseq` command to do this (type `seqkit subseq -h` to get a quick summary of available flags ).  `seqkit subseq` will accept a file of GFF info as a way of specifying what we want to extract, and it also has built in flags for extract flanking sequence around a specified feature.  Here we'll demonstrate how to extract the 500bp upstream (5') of each of our target genes:

```bash
seqkit subseq -f -u 500 --gtf targets.gff yeast.fna > target-promoters.fna
```

Explanation:

* `-f` = only flanking sequence; if not specified would include gene body plus any specified flanking sequence
* `-u 500` = upstream 500bp
* `--gtf targets.gff` = the GFF (GTF) file that specifies the feature regions we want

The output of this step looks like this:

```text
>NC_001135.5_71803-73341:+_usf:500 
AatccttcaatttttctggCAACTTTTCTCAACAGAACAATAACGGCAACCAGAACCGCT
ACTGAACGATGATTCAGTTCGCCTTCTATCCTTTGTTTACGtatttgtttatatatataa
ctttatttttttttattaattgGGCTGCAAGACAATTTTGTTGTCAGTGATGCCTCAATC
CTTCTTTTGCTTCCATATTTACCATGTGGACCCTTTCAAAACAGAGTTGTATCTCTGCAG
GATGCCCTTTTTGACGTATTGAATGGCATAATTGCACTGTCACTTTTCGCGCTGTCTCAT
TTTGGTGCGATGATGAAACAAACATGAAACGTCTGTaatttgaaacaaataaCGTAATTC
TCGGGATTGGTTTTATTTAAATGACAATGTAAGAGTGGCTTTGTAAGGTATGTGTTGCTC
ttaaaatatttggatACGACAtcctttatcttttttcctttaagAGCAGGATATAAGCCA
TCAAGTTTctgaaaatcaaa
>NC_001136.10_1206997-1212265:+_usf:500 
gatgagatgagatgaaattttttctgtaactgaaaaatttcgGAACGTCAATAATGATCG
...<output truncated>...
```

**Sidenote**: Wondering about GFF vs GTF files? See [this explanation](http://genome.ucsc.edu/FAQ/FAQformat.html#format4) at the UCSC genome browswer website. Essentially GTF is an extension of an older "GFF" format called GFF2; our "GFF" files are "GFF3" files which are largely backwards compatible with the older GFF2/GTF format.

### Turning FASTA data into a table

For the purposes of our simple `grep` based motif search (below) it will be convenient to reformat the sequence data into a table format. We're going to create a table with three columns: 1) the systematic names for each target gene; 2) the header information that `seqkit subseq` generated; and 3) the raw sequences.

We can accomplish this in one command line with clever application of `paste` and [process substitution](https://github.com/Bio724/Bio724-Lecture-Notes/blob/main/lecture-awk-bash/bash.md#process-substitution).

```bash
paste target-systnames.txt <(seqkit seq -n target-promoters.fna) <(seqkit seq -s -w 0 target-promoters.fna) > promoter-table.tsv
```


Explanation:

* `<(...)` = treat the outputs of the commands in the parenthes as if they were files via [process substitution](https://github.com/Bio724/Bio724-Lecture-Notes/blob/main/lecture-awk-bash/bash.md#process-substitution)
* `seqkit seq -n` = only return  the names of each sequence
* `seqkit seq -s -w 0` = only return the sequences themselves and unwrap the lines (`-w 0`)

### Counting occurences of binding site motifs in one sequence

Now we're ready to search for binding site motifs in our promoter sequences. We'll use regular expressions, as expressed in `grep` to do that.  We'll  start by demonstrating this with just a single sequence. 

Below I show searching the first promoter sequence in the table with a regular expression that allows some flexibility of the nucleotides in the first, second, and last position of the motif:

```bash
head -n 1 promoter-table.tsv | grep -i '[TA][GA]AAAC[AGT]'
```

Explanation:

* `head -n 1` = extract the first line from the file
* `grep -i` = ignore case
* `[TA]` etc = match one of these characters

If your terminal is setup to highlight matches returned by `grep` you'll see the matches highlighted in the output. If not you'll just see the line itself indicating that there was at least one match. To get a list of the specific matches we can modify the command line as follows (addition of `-o` flag to grep):

```bash
head -n 1 promoter-table.tsv | grep -i -o '[TA][GA]AAAC[AGT]'
```

Finally to count the hits we could do:

```bash
head -n 1 promoter-table.tsv | grep -i -o '[TA][GA]AAAC[AGT]' | wc -l
```

### Counting the motif hits in all the target sequences

Having solved the problem of counting motif hits in the promoter of one target gene, let's see how to do so for multiple targets. We will iterate over the lines of `promoter-table.csv`, doing a regex and count for each sequence line. For each line we'll output the systematic name for the target gene as well as the count of the regex hits. This seems like a job for `parallel`. We'll combine `parallel` with a few bash tricks to do this succinctly.


```bash
parallel --colsep='\t' 'echo -e {1} "\t" $(grep -i -o "[TA][GA]AAAC[AGT]" <<< {3} | wc -l)' :::: promoter-table.tsv
```

Explanation:

* `parallel --colsep='\t' '...' ::: promoter_table.tsv` = use parallel to execute the commands represented by the ellipsis where each execution of the commands will be populated by inputs found in the lines of the input file (`promoter_table.tsv`). `--colsep='\t'` specifies how fields within each line are parsed.

* `grep -i -o "[TA][GA]AAAC[AGT]" <<< {3}` = take the third field (the sequence itself) of each input line and send it to the `stdin` stream to be processed by `grep`. The `<<<` operator is called a ["here string"](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Here-Strings) (see also the related concept of ["here docs"](https://www.gnu.org/software/bash/manual/html_node/Redirections.html#Here-Documents)) and is a convenient way to inject strings into the `stdin` stream. 

  An equivalent way to construct this would have been to write it as: `echo {3} | grep -i -o "[TA][GA]AAAC[AGT]"` but I thought the "here string" is a little more compact. 

* `$(grep ... | wc -l)` = an example of [command subsitution](https://github.com/Bio724/Bio724-Lecture-Notes/blob/main/lecture-awk-bash/bash.md#command-substitution). The pipeline within `$(...)` is evaluated and then turned into a string.

* `echo -e {1} "\t" $(grep ...)` = use `echo` to output the first field (systematic names) from the parallel input along with a TAB character and the command substitution discussed above.

### Add a header

Since this table is meant to be the final output of our analysis, let's add an appropriate header and save it to a file:

```bash
(echo -e "systematic_name\tmotif_count"; 
parallel --colsep='\t' 'echo -e {1} "\t" $(grep -i -o "[TA][GA]AAAC[AGT]" <<< {3} | wc -l)' :::: promoter-table.tsv
) > motif_hits.tsv
```

Note: I'm taking advantage of the line breaking rules associated with [command grouping in bash](https://github.com/Bio724/Bio724-Lecture-Notes/blob/main/lecture-awk-bash/bash.md#grouping-commands) to make this visually a little easier to digest. You could type this all on a single line with equivalent results.


Here's what the first few lines of `motif_hits.tsv` look like:

```text
systematic_name motif_count
YAR009C          2
YBR067C          0
YCL027W          2
YDR365W-B        0
...<output truncated>...
```

Booyah!

### An alternate approach to counting motifs using Awk

Rather than using a combination of `grep` and `parallel` to build our table of counts, we could do an equivalent computation in Awk.

`countmotif.awk`:
```awk
BEGIN {
  IGNORECASE=1      # ignore case in regexp
  FS = "\t"         # tab-delimited input
  OFS = "\t"        # tab-delimited output
  print "systematic_name", "motif_count"  
}

# For every line do this
{
  count = patsplit($3, matches, /[TA][GA]AAAC[AGT]/)
  print $1, count
}
```

We run this program as:

```bash
awk -f countmotif.awk promoter-table.tsv
```

Explanation

* Awk has no dedicated function for counting regexp matches, but the `patsplit(string, array, pattern)` function will split a string based on a specified regexp pattern, and returns the number of times the pattern matched. The matches themselves end up in the specified array, which we gave the name `matches`.

## Room for improvement

There are a number of the things we didn't consider but might be good to add to make our pipeline more useful:

* Searching the reverse complement of each promoter sequence (or the motif itself)
* Returning both the number of hits and what the hits were (and possibly their location as well)


## Other tools for motif search

A more in-depth  analysis aiming to discover novel motifs, or incorporate more sensitive motif detection, could incorporate the motif search and identification tools provided by [MEME Suite](https://meme-suite.org/meme/index.html). Meme can be installed via Conda (`conda search meme` for more info).
