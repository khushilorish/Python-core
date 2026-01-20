import pandas as pd

#read data from csv file into a data
df1 = pd.read_csv(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\1-sampleFile.csv", encoding="latin1")

print(df1)

#read data from json file into a data
df2 = pd.read_json(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\3-sampleFile.json")

print(df2)

#read data from excel file into a data
df3 = pd.read_excel(r"C:\Users\hp\Desktop\PYTHON-CORE\Python-core\pandas\datasets\2-sampleFile.xlsx", engine="openpyxl")

print(df3)



