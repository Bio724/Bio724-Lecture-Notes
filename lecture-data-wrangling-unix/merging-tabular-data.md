
# Filtering, sorting, and merging tabular data

Now we turn to the task of filtering and merging our data


### Filtering using grep

The `grep` command is particularly useful for filtering (we'll see another tool called Awk next lecture which can complement or replace `grep` in many cases). For the sake of illustration, let's filter the `LeafTraits.tsv`  focusing on data collected in years 2011 and 2012.  

```
grep -E "^(2011|2012)" LeafTraits.tsv 
```

The argument `"^(2011|2012)"` is a regular expression.  A regular 
