import pandas as pd

dataframe = pd.read_json('data.json')

print(dataframe.to_string())

# Dictionary as json file. 
# We can load dictionary to json
data = {
    "Duration":{
        '0':54,
        '1':34,
        '2':17
    },
    "Pulse":{
        '0':13,
        '1':30,
        '2':40
    }   
}

# Row [0..2]
# Col [Duration,Pulse]

dataframe = pd.DataFrame(data)
print(dataframe.to_string())


