import pandas as pd 

#creating the dataFrame
data = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,22,21,25,30,31],
    "Salary": [30000, 40000, 41000, 50000, 60000, 44000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df1 = pd.DataFrame(data)
print(f'Original Data:\n{df1}')


#access and update value of particular cell in a data
df1.loc[0, "Salary"] = 65000 #updated salary of Arjun from 30000 to 65000
print(f'\n\nAfter Arjun Salary increment:\n{df1}')

#access and update whole column
df1['Age'] = df1['Age'] + 1
print(f'\n\nIncreased age of every employee by 1 year:\n{df1}')


#deleting a column
df2 = df1.drop(columns = ["Performance"], inplace=False)
print(f'\n\nData after deleting Performance column:\n{df2}') #"inplace=False" means modification will not take place in original data 

#delete a row in original data
df1.drop(index = 2, inplace=True)
print(f'\n\nDeleted row of Tarun:\n{df1}')