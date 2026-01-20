import pandas as pd

data = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,32,21,35,37,31],
    "Salary": [70000, 40000, 41000, 50000, 60000, 88000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df = pd.DataFrame(data)

#selecting single columns
name = df['Name']
print(f'Name Column: \n{name}')

#selecting multiple columns
subset = df[["Name", "Salary"]]
print(f'\n\nSubset of data with names and salary: \n{subset}')


#filtering rows with salary > 50000
high_salary = df[df["Salary"]>50000]
print(f'\n\nEmployees whose Salary is greater than 50000: \n{high_salary}')

#filtering rows with 2 conditions
filter_row = df[(df["Salary"]>50000) & (df["Age"]>30)]
print(f'\n\nRows with Salary greater than 50k and age greater than 30: \n{filter_row}')



data1 = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,22,21,25,30,31],
    "Salary": [30000, 40000, 41000, 50000, 60000, 44000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df1 = pd.DataFrame(data1)


#read first 3 rows of df1 data
print("First 3 rows:")
print(df1.head(3)) #if no value passed by default it will show first 5 rows


#read last 3 rows of df1 data
print("\n\nLast 3 rows")
print(df1.tail(3)) #if no value passed by default it will show last 5 rows


#get information about the whole data
print("\n\nInfo method:")
print(df1.info())


#print Descriptive Statistics of Data
print("\n\nDescriptive statistics of data:")
print(df1.describe())


#print the shape of data
print(f'\nShape: {df1.shape}')

#print all the column's name
print(f'\ncolumns: {df1.columns}')