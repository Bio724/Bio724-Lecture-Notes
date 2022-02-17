

# Introduction to ggplot and dplyr

## Slides

* [ggplot intro slides](./ggplot-intro-slides.pdf)
    - [ggplot cheat sheet](https://github.com/rstudio/cheatsheets/blob/main/data-visualization-2.1.pdf)

* [dplyr intro slides](./dplyr-intro-slides.pdf)
    - [dplyr cheat sheet](https://github.com/rstudio/cheatsheets/blob/main/data-transformation.pdf)


## Packages to install in R

* [palmerpenguins](https://allisonhorst.github.io/palmerpenguins/)
* [viridis](https://sjmgarnier.github.io/viridis/index.html)


## Questions that came up in lecture

* Syntax for using `select` to take only numeric columns -- use `select_if` (a variant of `select`) and `is.numeric` as so:

    ```r
    penguins %>% select_if(is.numeric)
    ```

* Examples of the magrittr tee operator (`%T>%`) with ggplot

    ```r
    my_table <-
        penguins %T>% 
        {ggplot(.,mapping=aes(x=body_mass_g, fill=species)) + 
            geom_histogram() + facet_wrap(~species, ncol=1) ->> my_plot} %>%
        group_by(species) %>% 
        summarize(count = n(),
                  mean_body_mass = mean(body_mass_g, na.rm=TRUE),
                  sd_body_mass = sd(body_mass_g, na.rm=TRUE))
    ```


    Explanation: this looks complicated but I wanted to make it sufficiently realistic.  Here we use the `%T>%` operator to simultaneously create a plot (`my_plot`) and a table of summary statistics (`my_table`).  Note how we wrap the `ggplot` related arguments in braces and use the `.` to specify where the data frame passed by the tee operator should be applied (see the section entitled "The dot operator with pipes" in the Bio 723 workbook).  We even find use for the rarely used (in my experience) global assignment operator `->>` in this example; we could have used the left-pointing version `<<-` before the call the `ggplot` but I thought the right pointing version helped to make this assignment stand out better. 

    After executing that block you can view the table or plot by printing them:

    ```r
    my_table
    ```

    or 

    ```r
    my_plot
    ```