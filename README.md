# Dependencies
The code depends on two non-system libraries:
```
NumPy
Matplotlib
```

### Math helper-functions
Functions `project_on_line` and `project_from_line` are used to approximate the cluster with a line segment. The line is determined with least-squares fit, and the ends by converting coordinates to a coordinate along the line, calculating 0.2 and 0.8 quantiles of those, and converting (projecting) back.

### Load the data from a file
NumPy function `np.loadtxt()` is provided arguments such as delimiter, data type, encoding, etc., in order to read the file and extract the data. These specific settings are required because the file is in CSV format and the data is stored as strings.

### Perform calculations
We perform calculations similar to those in Excel’s `LINEST()` function. To achieve this, we use `linalg.lstsq`, which is a built-in NumPy function. For approximating the cluster with a line segment, the ends of the segment are determined using the `quantile` function from NumPy, which calculates 0.2 and 0.8 quantiles.

### Draw the diagram
In this part of the code, we use variables defined earlier. We set the graph type to a scatter plot, assign the x and y axes, and use `plt.plot` to create the chart. The `plt.show()` function displays the plot. The `export()` function saves the graph as a separate file in the directory.

# Using instruction
This section provides brief instructions on using the code.


### Basic
To run the code, open the file `settings.py` and specify the directory of the file you want to execute (usually `main.py`). You can adjust visual settings in `settings.py` or leave them as default. After that, you can run the code.

### Having precalculated approximations
Once you have a calculated `out.csv` file in project root, running becomes as simple as launching `common.py` script. It produces a common diagram of all the clusters, that shows clear diference between the two types.

### Calculating approximations
`settings.py` file contains id (name), type (*oc* for Open Cluster or *gc* for Globular Cluster) of the object you want to work with, and filename of `.csv` file containing data for that object.

**Filenames should be entered as names, not paths. Python's os module should handle walking between directories.**
**The data is expected inside the `data` folder.**

After setting up the settings, run `main.py`. It will show a chart related to this particular object along with its approximated segment, and export approximation parameters to the end of `out.csv` file in the root directory. If there is no such file, it will create it.

In order to see the common diagram, we ran the `main.py` six times with different settings for each object. We believe, although this might not be the most effective approach, it allows for close control of the program's motions with the data, especially important in scientific context.

### Getting the data
The data we used was obtained from Gaia Data Release 3 using Gaia Data Archive's built-in query language ADQL. To fascilitate this job, a script `utils/query_gen.py` was developed, that generates needed queries from provided input. The result of the query was then exported as `.csv` file for each object.
