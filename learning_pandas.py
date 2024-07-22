# print("Learning Pandas")

# # Load a CSV file into a Pandas DataFrame:

# import pandas as pd

# df = pd.read_csv('data.csv')

# print(df.to_string()) 

# import pandas

# mydataset = {
#   'cars': ["BMW", "Volvo", "Ford"],
#   'passings': [3, 7, 2]
# }

# myvar = pandas.DataFrame(mydataset)

# print(myvar)


# Create your own labels:

# import pandas as pd

# a = [1, 7, 2]

# myvar = pd.Series(a, index = ["x", "y", "z"])

# print(myvar)

# DataFrames
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.

# Series is like a column, a DataFrame is the whole table.

# Example
# Create a DataFrame from two Series:

# import pandas as pd

# data = {
#   "calories": [420, 380, 390],
#   "duration": [50, 40, 45]
# }

# myvar = pd.DataFrame(data)

# print(myvar)