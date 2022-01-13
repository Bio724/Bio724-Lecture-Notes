
## Example pipeline

This illustrates a simple pipeline to compare and analyze genome features using simplified annotation files. Replicate these analyses on your own VM and think about ways you can extend them:

* [yeast_genome_features_R40-1-1.txt](https://github.com/Bio724/Bio724-Example-Data/raw/main/yeast_genome_features_R40-1-1.txt) -- Genome release R40.1.1 from July 2004

* [yeast_genome_features_R64-3-1.txt](https://github.com/Bio724/Bio724-Example-Data/raw/main/yeast_genome_features_R64-3-1.txt) -- Genome release 64.3.1 from April 2021

These two files were derived from standard GFF annotation files downloaded from the Saccharomyces Genome Database (SGD).  There are 6 columns in each file:

1. The ID of the "landmark" object on which each feature is found (equivalent to chromosome in this case)
2. The feature type
3. The start coordinate of the feature
4. The end coordinate of the feature
5. The coding strand , +, -, or . (no strand) of the feature
6. A free form field that includes information on systematic IDs, common gene names, short descriptions, etc




### Download the data 


```
pm21:~$ wget https://github.com/Bio724/Bio724-Example-Data/raw/main/yeast_genome_features_R40-1-1.txt
<output omitted>

pm21:~$ wget https://github.com/Bio724/Bio724-Example-Data/raw/main/yeast_genome_features_R64-3-1.txt
<output omitted>
```

### Do a little exploration before building the pipeline

Using the `less` pager:

```
pm21:~$ pm21:~$less yeast_genome_features_R40-1-1.txt
<output omitted>
```

Using the `head` command:

```
pm21:~$ head yeast_genome_features_R40-1-1.txt
<output omitted>
```

How many features are in each file? `wc` helps us answer this:

```
pm21:~$ wc -l yeast_genome_features_R40-1-1.txt
15385 yeast_genome_features_R40-1-1.txt

pm21:~$ wc -l yeast_genome_features_R64-3-1.txt
28386 yeast_genome_features_R64-3-1.txt 
```

### Feature types

The second column of the data files has all the information about the types of each feature. The question we want to ask is: "What are the feature types in each file?". We'll see how to solve this one step at a time, piping the intermediate steps to the `less` pager program so we can view the output we're generating along the way (remember to type `q` to quit `less` when you're done looking at the output)

Since we're focus only the the feature types, it's convenient to reduce our data to that single column. Cut let's us do that:

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | less
```

We then pass the output of cut to the `sort` command so that features of the same type appear next to each other:

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | sort | less
```

Finally we incorporate `uniq` into our pipeline to reduce the features to the unique values:

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | sort | uniq
ARS
CDS
centromere
chromosome
... <output truncated>
```

Now that our pipeline for reducing the annotation file to it's unique features is working let's redirect the output to a file:

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | sort | uniq > features_2004.txt
```

Now apply the same pipeline to the 2021 annotation:

```
pm21:~$ cut -f 2 yeast_genome_features_R64-3-1.txt | sort | uniq > features_2021.txt
```

### Comparing the features

What feature types were recognized in 2004 but not in 2021? What features are unique to 2021? What features are shared?  The `comm` (short for common) command helps us explore this. 

By default the `comm` command outputs lines with up to three columns (using tabs as the default delimiter) -- items in the first column are unique to FILE1, items in the second column are unique to FILE2, and the items in the third column are shared by both FILES.

```
pm21:~$ comm features_2004.txt features_2021.txt
<output omitted>
```

You'll see that this output is confusing/ugly because the whitespace delimiters make it hard to see the column boundaries. I  prefer to output the various items subsets like so:

Unique to FILE1:
```
pm21:~$ comm -23 features_2004.txt features_2021.txt 
```

Unique to FILE2:
```
pm21:~$ comm -13 features_2004.txt features_2021.txt 
```

Common to both:
```
pm21:~$ comm -12 features_2004.txt features_2021.txt 
```

### How many genes were annotated in the yeast genome in 2004 vs 2021?

Let's see another example -- how many "gene" features were annotated in 2004 vs 2021?

Here we combine `cut` with a tool called `grep` which does regular expression matching.  grep returns each line that has a match. Here we're searching for "whole words" (-w) that match the expression "gene":

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | grep -w "gene" | wc -l
6606
```

We can actually leave out the `wc` step, as grep has an option for counting:

```
pm21:~$ cut -f 2 yeast_genome_features_R40-1-1.txt | grep -c -w "gene"
6606
```

Here's the same calculation for the 2021 annotation data:

```
pm21:~$ cut -f 2 yeast_genome_features_R64-3-1.txt | grep -c -w "gene"
6607
```


**Try this**: What happens to the counts if you leave out the `-w` option from grep?  Can you figure out what the difference is? Hint: remove the `-c` option as well so you can see the lines returned by grep.

### How many genes are there on chromosome 1?

For the 2004 data:

```
pm21:~$ cut -f 1,2 yeast_genome_features_R40-1-1.txt | grep -w "gene" | grep -c -w "chrI"
119
```

For the 2021 data:

```
pm21:~$ cut -f 1,2 yeast_genome_features_R64-3-1.txt | grep -w "gene" | grep -c -w "chrI"
117
```

In a future lecture we'll see how to do some of these calculations more succinctly using a simple programming language called Awk.