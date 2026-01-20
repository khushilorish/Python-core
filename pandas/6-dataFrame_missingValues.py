import pandas as pd

data = {
    "S.No.": [1,2,None,4,None],
    "Name": ["Kunal", "Tanu", "Sejal", "Arjun", None],
    "Salary": [50000, 65000, 55000, None, None]
}
df = pd.DataFrame(data)
print(f'Original Data:\n{df}')


#finding null values
print("\nisnull() method:\n",df.isnull()) #print True where null values are present
print("\n",df.isnull().sum()) #print total number of null values in each column


#to remove rows containing none values
df1 = df.dropna(axis=0, inplace=False)
print(f'\n\nData after removing rows with None values:\n{df1}')


#to fill data in place of missing values
df2 = df.fillna(0, inplace=False)
print(f'\n\nAll values with none will be replaced by 0:\n{df2}')


#to fill the missing data with mean of that particular column
df["Salary"].fillna(df['Salary'].mean(), inplace=True)
print(f'\n\nData after filling missing values of Salary column with mean of all Salaries:\n{df}')


#interpolate method
df['S.No.'] = df['S.No.'].interpolate(method="linear")
print("\n\nInterpolate method:\n",df)