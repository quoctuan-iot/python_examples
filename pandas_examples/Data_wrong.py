import pandas as pd

dataframe = pd.read_csv('clean_data.csv')
print(dataframe.to_string())

# Check if value of cell > index
# Getting data at cell with condition
for index in dataframe.index:
    if dataframe.loc[index,'Duration'] > 60:
        print(dataframe['Duration'].values[index])

        # Remove row that contain value incorret
        new_df = dataframe.drop(index)

print(new_df.to_string())