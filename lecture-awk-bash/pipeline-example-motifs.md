
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

* STE12 Sequence Motif -- via [The Yeast Transcription Factor Specificity Compendium](http://yetfasco.ccbr.utoronto.ca/) ![STE12 binding site motif](./figures/STE12-motif.png)

* [STE12 Targets](https://raw.githubusercontent.com/Bio724/Bio724-Example-Data/main/STE12_targets.tsv)

## Overview of Approach

* Filter GFF file for genes features corresponding to our targets of interest 

* Use filtered GFF in combination with [SeqKit](https://bioinf.shenwei.me/seqkit/) to extract promoter regions 

* Count occurences of motif in each promoter 

* Create a table with Systematic Name and Motif Count 

* Wrap our pipeline into a re-usable Bash script so it can be easily applied to other sets of genes and TF motifs

* How could we do this analysis efficiently for many sets of genes? For example, clusters of co-regulated genes identified in a transcriptome analysis 



## Other tools for motif search

A more in-depth  analysis aiming to discover novel motifs, or incorporate more sensitive motif detection, could incorporate the motif search and identification tools provided by [MEME Suite](https://meme-suite.org/meme/index.html). Meme can be installed via Conda (`meme search conda` for more info).
