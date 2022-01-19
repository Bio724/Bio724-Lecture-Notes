
# Filtering, sorting, and merging tabular data

Now we turn to the task of filtering and merging our data


### Filtering using grep

The `grep` command is particularly useful for filtering (we'll see another tool called Awk next lecture which can complement or replace `grep` in many cases). For the sake of illustration, let's filter the `LeafTraits.tsv`  focusing on data collected in years 2011 and 2012.  

```
grep -E "^(2011|2012)" LeafTraits.tsv  > LeafTraits-2011-2012.tsv
```

The argument `"^(2011|2012)"` is a regular expression (the `-E` flag tells `grep` to use it's "extended" regular expression syntax).  Regular expressions are a way of describing patterns in strings.  This particular regular expression means "match at the beginning of a line the strings '2011' or '2012'".  



### Sorting using `sort`

We're going to combine data files using the 

