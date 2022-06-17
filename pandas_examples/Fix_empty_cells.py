import pandas as pd

dataframe = pd.read_csv('data.csv')
print(dataframe.to_string())

# Remove row that contain empty cell
new_dataframe = dataframe.dropna()
print(new_dataframe.to_string())
# If want to change a original data, inplace = True argument

# Replace empty cell with new value
new_dataframe = dataframe.fillna(130)
print(new_dataframe.to_string())
# Other, we can replace in the specific column with new value


# Using mean, median, mode to calculate and replace to empty cell
new_dataframe = dataframe.mean()

