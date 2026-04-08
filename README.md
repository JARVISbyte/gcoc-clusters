# Code explanation
We need to import two libraries using `import` at the beginning of the code.  
Libraries used:
```
NumPy
Matplotlib
```

### Math helper-functions
Functions `get_component` and `get_x` are used to calculate the components of the least squares fit line.

### Load the data from a file
We assign properties such as delimiter, data type, encoding, etc., in order to read the file and extract the data. These specific settings are required because the file is in CSV format and the data is stored as strings.

### Perform calculations
We perform calculations similar to those in Excel’s `LINEST()` function. To achieve this, we use `linalg.lstsq`, which is a built-in NumPy function. For the “median” of the line, we use the `quantile` function from NumPy, which calculates components within the range of 20–80% of the x-values.

### Draw the diagram
In this part of the code, we use variables defined earlier. We set the graph type to a scatter plot, assign the x and y axes, and use `plt.plot` to create the chart. The `plt.show()` function displays the plot. The `export()` function saves the graph as a separate file in the directory.

# Code instruction
To run the code, open the file `settings.py` and specify the directory of the file you want to execute (usually `main.py`). You can adjust visual settings in `settings.py` or leave them as default. After that, you can run the code.
