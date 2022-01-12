
## Moving files to/from your VM


### Using Cyberduck (or another SFTP client)

Cyberduck provides a graphical interface for moving files back and forth to/from a remote machine.  We'll demonstrate how to use Cyberduck in class.

### Using the command line

* `scp` -- secure copy.  Command line tool to copy files to or from a remote machine via SSH.
  * Move a local file (`foo.txt`) to your virtual machine: 
    - `scp foo.txt netid@hostname:~`
  * Move a remote file (`~/data/bar.txt`) to your local machine (`~/bio724/data`):
    - `scp netid@hostname:~/data/bar.txt ~/bio724/data` (saves `bar.txt` under the local directory `~/bio724/data` assuming that directory already exists)

* `wget` -- a command line program for downloading files from the web. You would typically use this to download files from a URL to a remote machine.

  To illustrate the use of `wget`, we'll download a file of interest from the NIH National Center for Biotechnology Information (NCBI), which hosts databases like Genbank, SRA, Pubmed, etc.


  * In your web browser, navigate to the [NCBI SARS-CoV-2 Resources website](https://www.ncbi.nlm.nih.gov/sars-cov-2/).  About half-way down the page are a set of blue buttons linking to information about the SARS-CoV-2 Genome Reference Sequence (NC_045512).

  * Right click the "Download Annotation" button and copy the URL link and then use `wget` to download the genome annotation file to your VM. 

    * `wget https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/009/858/895/GCF_009858895.2_ASM985889v3/GCF_009858895.2_ASM985889v3_genomic.gff.gz`

  * The `.gz` prefix indicates that this is a compressed file; compressed using a tool called `gzip`.  To uncompress this file we can use the `gunzip` command as folows:

    ```
    gunzip GCF_009858895.2_ASM985889v3_genomic.gff.gz
    ```

    This will create the uncompressed file named `GCF_009858895.2_ASM985889v3_genomic.gff`.

  * Let's create a directory for genome annotation files and move our file there:

    ```
    mkdir ~/genome_annotations
    ```
    
    ```
    mv GCF_009858895.2_ASM985889v3_genomic.gff ~/genome_annotations/
    ```

  * GFF files are a commonly used format for genome annotations.  This is a simple tab-delimited file format with nine columns. A full specification of the GFF format is provided here: https://github.com/The-Sequence-Ontology/Specifications/blob/master/gff3.md
