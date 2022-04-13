# Writing Command Line Programs in Python

We will explore how to construct command line programs in Python that follow the [Unix philosophy](../lecture-filesystems-terminals-unix/unix-philosophy.md).

## Modules and Libraries 

* [PyVCF](https://pyvcf.readthedocs.io/en/latest/) -- a Python library for working with [Variant Call Format](https://en.wikipedia.org/wiki/Variant_Call_Format) (VCF) files . Install PyVCF via Conda (`conda install pyvcf`).

    * [The VCF Specification](https://samtools.github.io/hts-specs/VCFv4.1.pdf) -- VCF is a commonly used text file format for representing genotype information, typically produced by high throughput sequence analysis.  Many common genomics tools will produce VCF files to represent genetic differences between a sample and a reference genome, or to represent differences among individuals in a sample.

* [argparse](https://docs.python.org/3/library/argparse.html) -- A Python module for parsing for command-line options, arguments and sub-commands. Part of the Python standard library.

* [click](https://click.palletsprojects.com/en/8.1.x/) -- another library for writing command-line interfaces. Very popular and makes it easy to turn functions into subcommands.


## Example data

* [Cryptococcus_Bt22_mapped_to_Ftc555-1.vcf.gz](https://github.com/Bio724/Bio724-Example-Data/raw/main/Cryptococcus_Bt22_mapped_to_Ftc555-1.vcf.gz)
