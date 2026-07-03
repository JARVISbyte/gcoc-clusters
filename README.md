# GC-OC clusters
`gcoc-clusters` is a set of scripts used to assist in bulk-downloading data from Gaia Data Release 3 for globular and open clusters (gc/oc).

Our main goal was to build cluster-specific Hertzsprung–Russell diagrams for several globular and open clusters to experimentally show the difference in their respective star compositions. To achieve easier comparison of HR diagrams, we implemented a custom-built simplification algorithm that represents cluster as a line segment. The algorithm can be found in `gcoc-clusters/code/main.py`.

The `gcoc-clusters/code/common.py` file serves a sole purpose of plotting all the clusters on one graph.

The `gcoc-clusters/code/settings.py` file is used to allow `main.py` to name calculated simplification according to the specific cluster when saving it.

The `gcoc-clusters/utils/query_gen.py` semi-interactively generates ADQL (Astronomical Data Query Language) query to use with Gaia. The `gcoc-clusters/utils/adqlq.txt`, as the obsure name could have suggested would it be any less obscure, contains base query used by `query_gen.py`.

This repository also contains data for a few globular (M14, M56, M79) and a few open (M6, M29, M103) clusters under `gcoc-clusters/data/`, as well as calculated simplifications in `gcoc-clusters/out.csv`, an example single-cluster HR diagram `M79.png` built from downloaded data, and the final multi-cluster HR diagram `OC_GC.png`.

*Sidenote: what follows is the original README.md file written hastily for a hackaton. Some information may be repeated or incomplete, and the style may be childish. Please kindly note that the project (including the old README.md) was made in 8 hours by 4 sleep-deprived students from different countries.*

## Brief description
This section gives a brief description of code and its underlying logic.

### Dependencies
The code depends on two non-system libraries:
```
NumPy
Matplotlib
```

### Math helper-functions
Functions `project_on_line` and `project_from_line` are used to help with approximating the cluster with a line segment. The line is determined by least-squares fit, and the ends by converting x,y-coordinates to along-the-line coordinate, calculating 0.2 and 0.8 quantiles of it, and converting (projecting) back.

### Load the data from a file
NumPy function `np.loadtxt()` is provided arguments such as delimiter, data type, encoding, etc., in order to read the file and extract the data. These specific settings are required because the file is in CSV format and the data is stored as strings.

### Perform calculations
We perform calculations similar to those in Excel’s `LINEST()` function. To achieve this, we use `linalg.lstsq`, which is a built-in NumPy function. For approximating the cluster with a line segment, the ends of the segment are determined using the `quantile` function from NumPy, which calculates 0.2 and 0.8 quantiles.

### Draw the diagram
In this part of the code, we use variables defined earlier. We set the graph type to a scatter plot, assign the x and y axes, and use `plt.plot` to create the chart. The `plt.show()` function displays the plot. The `export()` function saves the graph as a separate file in the directory.

## Using instruction
This section provides brief instructions on using the code.

### Basic
To run the code, open the file `settings.py` and specify the directory of the file you want to execute (usually `main.py`). You can adjust visual settings in `settings.py` or leave them as default. After that, you can run the code.

### Having precalculated approximations
Once you have a calculated `out.csv` file in project root, running becomes as simple as launching `common.py` script. It produces a common diagram of all the clusters, that shows clear diference between the two types.

### Calculating approximations
`settings.py` file contains id (name), type (*oc* for Open Cluster or *gc* for Globular Cluster) of the object you want to work with, and filename of `.csv` file containing data for that object.

**Filenames should be entered as names, not paths. Python's os module should handle walking between directories.**
**The data is expected inside the `data/` folder.**

After setting up the settings, run `main.py`. It will show a chart related to this particular object along with its approximated segment, and export approximation parameters to the end of `out.csv` file in the root directory. If there is no such file, it will create it.

In order to see the common diagram, we ran the `main.py` six times with different settings for each object. We believe, although this might not be the most effective approach, it allows for close control of the program's motions with the data, especially important in scientific context.

### Getting the data
The data we used was obtained from Gaia Data Release 3 using Gaia Data Archive's built-in query language ADQL. To fascilitate this job, a script `utils/query_gen.py` was developed, that generates needed queries from provided input. The result of the query was then exported as `.csv` file for each object.
