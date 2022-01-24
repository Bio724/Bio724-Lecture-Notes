# Bash



## Lists of commands and grouping commands


## Parameter expansion and Command substitution

### Arithmetic expansion

## Process substitution

## Writing shell scripts

You'll recall that a shell is the command line interface by which you interact with the operating system.  Shell scripts are small programs written in the language of the shell you're using; they're convenient for tying together a series of commands that you might otherwise type by hand into a repeatable and documented set of operations.

For these exercises we will assume that you use the bash shell, which is the default shell on most Linux based systems (this also used to be the case on OSX, but macOS has now moved to zsh as the default). You can examine which shell you're using by typing:

```bash
echo $SHELL
```

## Bash scripts are picky

One annoying feature of bash scripting is that it's particularly picky about white space around commands and arguments, because essentially it tries to execute each line as if it was written at the command line itself ([see](https://uvesway.wordpress.com/2013/03/11/some-whitespace-pitfalls-in-bash-programming/)). When writing the scripts below I recommend you be careful to follow the spacing I've used to avoid hard to diagnose syntax errors.  For this reason, bash is *not* my preferred scripting environment. However it's so ubiquitous in bioinformatics that it's worth learning the basics of bash.

## Simple shell script 01

Let's start with the simplest possible shell script -- one that simply writes a message to stdout.

Using your editor of choice put the following code into a file named `tut01.sh`:

```bash
echo "Hello, shell world!"
```

Now you can call your shell script as so from the command line (assuming it's in your current working directory)

```bash
bash tut01.sh
```

This one line script simply called the `echo` command line tool to write text to stdout.

## Simple shell script 02

That's a pretty boring shell script.  Let's create a new version that takes as input an argument telling it what to print after the initial greeting. `$1` is how we designate the first argument from the command line.  

```bash
# tut02.sh
echo "Hello, $1"
```

This expects an argument from the command line, so run this script as follows, substituting `Paul` as appropriate:

```bash
bash tut02.sh Paul
```

## Simple shell script 03

Shell scripts can create variables to hold the output of commands. This is illustrated below in which we create a variable `input_reversed` to hold the value of a computation done on the first argument to the script:

```bash
# tut03.sh
# note that rev command reverses lines of input
input_reversed=$(echo $1 | rev) 
echo "$1 reversed is $input_reversed"
```

And we again run it as:

```bash
bash tut03.sh "Twas brillig and the slithey toves..."
```

Notice that I wrapped the text in quotes.  What happens if you don't include the quotes?

## Simple shell script 04

We can get multiple arguments from the command line:

```bash
# tut04.sh
echo "The first argument was: $1"
echo "The second argument was: $2"
```

Or we can check the number of arguments:

```bash
# tut04a.sh
nargs=$#

if [[ $nargs -ne 2 ]]
then
    echo "I need two arguments!"
    exit
fi

echo "The first argument was: $1"
echo "The second argument was: $2"
```

## A bash script for mapping reads

Recall that [mapping reads and calling variants](./mapping-reads-and-calling-variants.md) required multiple steps to go from raw fastq files to VCF output. This task is therefore a good candidate to wrap up in a shell script:

```bash
#!/bin/bash

# map_and_call.sh -- a script for aligning reads and calling variants
#  using minimap2 and bcftools
#
# NOTES:
# Assumes you've already indexed the reference fasta file: bwa index ref.fasta
#

scriptargs="ref.fasta reads1.fastq reads2.fastq outdir"
nexpargs=4
nargs=$#

if [[ $nargs -ne $nexpargs ]]
then
    echo
    echo "Usage: `basename $0` $scriptargs"
    echo
    exit
fi

ref=$1
reads1=$2
reads2=$3
outdir=$4

# make output directory if it doesn't exist
if [ ! -d $outdir ]; then
    mkdir $outdir
fi

# align reads
minimap2 -ax sr $ref $reads1 $reads > $outdir/aln.sam

# sort aligned reads and convert to bam
samtools sort $outdir/aln.sam -o $outdir/aln.bam 

# create pileup
bcftools mpileup -f $ref $outdir/aln.bam > $outdir/pileup.vcf

# call variants
bcftools call $outdir/pileup.vcf -m -v --ploidy 1 -o $outdir/called_variants.vcf

# filter variants
bcftools view -i 'QUAL>20 && DP >= 5' $outdir/called_variants.vcf > $outdir/filtered_variants.vcf
```

To make this script executable without having to type `bash` each time we call it you can do the following:

```bash
chmod +x map_and_call.sh
```

To run the script you need to specify four arguments -- 1) the reference genome fasta file, 2) and 3) the fastq files for your paired reads; and 4) the output directory.  

If the `map_and_call.sh` file is in my home directory and I'm working in the directory `~/home/saudi_sample` (created in previous weeks) I'd call this script like so to align the reads from sample `SRR14332322` and put the output files in the subdirectory `output_SRR14332322`:

```bash
~/map_and_call.sh FungiDB-53_CneoformansH99_Genome.fasta SRR14332322_1.fastq SRR14332322_2.fastq output_SRR14332322
```


## Other resources

The above is just a quick intro to bash scripting. Some other useful resources include:

* https://linuxconfig.org/bash-scripting-tutorial-for-beginners -- an in-depth bash tutorial
* https://devhints.io/bash -- a nice bash cheatsheet
* https://www.gnu.org/software/bash/manual/ -- the official  bash manual