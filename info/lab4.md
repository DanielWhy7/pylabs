# Laboratory Work No. 4
# Data Analysis and Visualization

- [Theory](#theory)
  - [Pandas](#pandas)
  - [Useful links](#useful-links)
- [Task](#task)

# Theory

## pandas

Pandas is a library for data analysis and processing. It provides tools for managing and analyzing structured data.

Installation:
```
pip install pandas
```

Example of reading data:
```py
import pandas as pd  # import

df = pd.read_csv("data.csv")  # load data from a csv file
print(df.head())  # display the first rows of the table

```

## Useful links

- [Pandas (doc)](https://pandas.pydata.org/docs/)

# Task

## General task
1. Using the data and annotation from the second laboratory work, form a DataFrame that will contain 2 columns - the absolute and relative path to the file.
2. Name the columns of the formed DataFrame. The column names must reflect the data content.
3. Add a new column according to the variant. 
4. Implement a sorting function by the added column.
5. Implement a filtering function by the added column.
6. Create and display a histogram based on the added column using matplotlib for **all sorted data** (the graphs and axes must have appropriate labels).
7. Save the dataframe and the graph to files.


## Variants

1. Add a column with the height of each image.
2. Add a column with the width of each image.
3. Add a column with the area of each image.
4. Add a column with the average brightness values *across all channels* of the image (not for each!).
5. Add columns with the average brightness values *for each channel* (r, g, b) of the image. Display 3 curves on the graph.
6. Add a column with the dominant color value (r, g, b) of the image (based on the average brightness value). Display a histogram of the dominant color distribution on the graph.
7. Add a column with the orientation value of the image (vertical, horizontal, or square). Display a histogram of the orientation distribution on the graph.
8. Add a column with the brightness range values (range=max-min) of the image *across all channels* (not for each!).
9. Add a column with the brightness range values (range=max-min) of the image *for each channel* (r, g, b). Display 3 curves on the graph.
10. Add a column with the aspect ratio values of the image (height to width or width to height).


11. Add a column with the number of samples of each audio file.
12. Add a column with the duration (array length / sampling rate) of each audio file.
13. Add a column with the minimum amplitude values (in absolute value) for each audio file.
14. Add a column with the maximum amplitude values (in absolute value) for each audio file.
15. Add a column with the average amplitude values (in absolute value) for each audio file.
16. Add a column with the amplitude range values (range=max-min) for each audio file.
17. Add a column with the ratio of the number of samples with an amplitude above a given threshold to the total number of samples for each audio file.
18. Add a column with the ratio of the number of samples with an amplitude below a given threshold to the total number of samples for each audio file.
19. Add a column with the ratio of the number of zero samples to the total number of samples for each audio file.
20. Add a column with the ratio of the number of non-zero samples to the total number of samples for each audio file.
