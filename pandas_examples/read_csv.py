import pandas as pd

# Read csv
dataframe = pd.read_csv(filepath_or_buffer='data.csv')
print(dataframe.to_string())

# Write csv
dataframe.index.name = "ID"
dataframe.to_csv('data_output.csv')

# Conver dataframes to dictionary
for col,row in dataframe.to_dict().items():
    print(col)
    print(row)

# Create data data -> convert to dataframe
data = {
    "calories":[42,34,34],
    "duration":[45,24,23]
} 

dataframe = pd.DataFrame(data)
