import pandas as pd

data = {
    "Name" : ['Arjun', 'Sumit', 'Ram'],
    "Age" : [20,21,30],
    "City" : ['Mumbai', 'Delhi', 'Agra']
}

#creating dataFrame from the above data
df = pd.DataFrame(data)
print(df)

#converting dataFrame into a csv file into a particular folder
df.to_csv("Python-core/pandas/datasets/1-sampleFile.csv",index=False)

#converting dataFrame into a excel file into a particular folder
df.to_excel("Python-core/pandas/datasets/2-sampleFile.xlsx",index=False)

#converting dataFrame into a json file into a particular folder
df.to_json("Python-core/pandas/datasets/3-sampleFile.json",index=False)
