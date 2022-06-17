import pandas as pd

# Read a sheet excel 
dataframe = pd.read_excel('sampledatainsurance.xlsx',sheet_name='PolicyData')
print(dataframe.to_string())
print('===================================================================')

# Loop all sheets 
dataframe = pd.read_excel('sampledatainsurance.xlsx',sheet_name=None)
#print(dataframe['Instructions'])

# Getting data at sheet PolicyData
PolicyData = dataframe['PolicyData']
print(PolicyData)

print('===================================================================')
print(' Analyzing data  ')

# Analyzing data 
print(PolicyData.head()) # Return specified number of row

print('===================================================================')
# Getting data from start row to index, example: 30
print(PolicyData.head(30))

# Getting data from end row to index,
print(PolicyData.tail(10))

# Getting information of data frame
print(PolicyData.info())
