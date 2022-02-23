

# Data wrangling with tidyr and dplyr

## Cheat sheets

* [tidyr cheat sheet](https://github.com/rstudio/cheatsheets/blob/main/tidyr.pdf)
* [dplyr cheat sheet](https://github.com/rstudio/cheatsheets/blob/main/data-transformation.pdf)

## Slides

* [Data wrangling in R](https://bio724.github.io/Bio724-web-pages/slides-data-wrangling-R.html)



## Example Data

* [small-messy-data.csv](./small-messy-data.csv)

## In-class questions

### Creating plots and saving them in a for loop



```r
# gene a vector of the unique gene names from the Gene column
# of the data frame of intereset
genes <- unique(tidy_summary$Gene)

# iterate over the set of gene names
for (gene in genes) {
  # create a sub-dataframe for the information associated
  # with the current gene
  filtered_data <- tidy_summary %>% filter(Gene == gene)

  # create the plot, saving the output to a variable
  p <- ggplot(filtered_data, aes(x = Dosage, y = Mean_Expression, color=Drug)) +
        geom_point(size=3, alpha=0.75) + 
        ylim(-1.5,1.5) + 
        labs(title = gene)
    
  # save the plot to a file name constructed from the gene name
  ggsave(str_c(gene, ".pdf"), plot=p, device="pdf")
}
```
