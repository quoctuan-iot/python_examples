import pandas as pd

dataframe = pd.read_excel('sampledatainsurance.xlsx',sheet_name='PolicyData')
print(dataframe.head(15).to_string())

# Format datetime is wrong
# Convert into a correct format
dataframe['Expiry'] = pd.to_datetime(dataframe['Expiry'])

print(dataframe.head(15).to_string())

