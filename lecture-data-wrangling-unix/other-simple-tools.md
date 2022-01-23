# Other useful simple tools


## bc -- a calculator program

The program `bc` (installable via `sudo apt install bc`) provides an arbitrary precision calculator. `bc` operates in two modes: 

1. an interactive mode invoked by typing `bc` (press `Ctrl-D` or type `quit` to exit)

2. by taking input from a file(s) or from stdin: 
       
    * `echo "3 * 12" | bc` 
    
    * Note that by default `bc` displays the results of its calculations rounded to integer values; to change this you need to set the `scale` variables as so: 
     
        `echo "scale=5; 3/12" | bc` 
    
        Compare this to the same computation w/out setting `scale`)

