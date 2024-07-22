print("Learning Pandas")

# Load a CSV file into a Pandas DataFrame:

import pandas as pd

df = pd.read_csv('data.csv')

print(df.to_string()) 

import pandas

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

myvar = pandas.DataFrame(mydataset)

print(myvar)