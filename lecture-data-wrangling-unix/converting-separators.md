
# Converting field separators

The tables provided by Ames et al. are CSV separated -- that is, commas are used to indicate the boundaries between different columns in the tables. This is not uncommon, however many of our Unix command line tools work with tab-delimited fields by default so it is  convenient to convert the field separators (note that some programs allow you to specify field separators as a command line argument).

A simple tool for doing this is the `tr` (translate command).  For example, let's convert `LeafTraits.csv` to `LeafTraits.tsv` (tab-separated values).

```
 cat LeafTraits.csv | tr ',' '\t' > LeafTraits.tsv
```


## Applying this conversion to multiple files

Above we used a small three step pipeline to convert a CSV file to a TSV file. However, we have multiple `.csv` files to convert. Unlike the `dos2unix` command used previously, our little pipeline wont take a wildcard (e.g. `*.csv`) as input without some effort on our part.  We could, of course, run the pipeline by hand for each different CSV file, but if the number of input files is large this is tedious and error-prone. Instead, let's see how we can use a tool called `parallel` to apply the same pipeline to multiple inputs.


### A quick primer on `parallel`

The `parallel` tool takes as input a command to run, and a set of input to run the command on. In the following example `echo` is the command and `foo`, `bar`, and `qux` are the inputs that echo is applied to.

```
parallel echo ::: foo bar qux
```

The output is:

```
foo
bar
qux
```

The above command is equivalent to running `echo` individually on each input, one after the other, collecting the outputs, and displaying them.

#### Complex commands with `parallel`

When you want to use `parallel` with a pipeline you need typically will need to wrap the set of commands in quotes, and use parallels templating system to indicate where the inputs are applied. In this example, the `{}` tells parallel to "insert each input at this location".

```
parallel "echo {} | tr [:lower:] [:upper:]" ::: foo bar qux
```

#### `parallel` can be used in a pipeline

A call to `parallel` can itself be part of a pipeline. For example, here we use `ls` to list all the `*.csv` files (use `man` to see what the `-1` argument does) and then pipe the output of `ls` as the input to `parallel`:

```
ls -1 *.csv | parallel "echo {} | tr [:lower:] [:upper:]" :::
```

Because it is often used with file names as input, parallel has a special templating syntax (`{.}) for stripping the extension off an input:

```
ls -1 *.csv | parallel "echo {.} | tr [:lower:] [:upper:]" :::
```

#### Implementing our conversion pipeline

Now we have the necessary tools in hand to apply our simple conversion pipeline to a bunch of CSV files translating each to a corresponding TSV file:


```
ls -1 *.csv | parallel "cat {} | tr ',' '\t' > {.}.tsv" :::
```