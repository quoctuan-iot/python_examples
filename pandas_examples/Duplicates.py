import pandas as pd

dataframe = pd.read_csv('clean_data.csv')

# Check duplicate
print(dataframe.duplicated())

# Check duplicate at column
print(dataframe['Duration'].duplicated())

# Remove duplicate
#new_df = dataframe['Duration'].drop_duplicates()
index = 0
list_drop =[]
for ret in dataframe['Duration'].duplicated():
    if ret:
        list_drop.append(index)
    index +=1
    
new_df = dataframe.drop(index=list_drop) 
print(new_df.to_string())