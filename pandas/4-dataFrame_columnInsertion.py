import pandas as pd

data = {
    "Name": ['Arjun', 'Arun', 'Tarun', 'Ankur', 'Tanu', 'Manu'],
    "Age" : [20,32,21,35,37,31],
    "Salary": [70000, 40000, 41000, 50000, 60000, 88000],
    "Performance": [89,90,91,87,86,93],
    "City": ['Mumbai', 'Agra', 'Chennai', 'Goa', 'Meerut', 'Paris']
}

df = pd.DataFrame(data)
print(f'Original Data:\n{df}')

#adding a new column at the end of all columns
df["Bonus"] = df['Salary'] * 0.10
print(f'\n\nAfter adding Bonus column:\n{df}')

#adding column at desired place
df.insert(0, "Employee ID", [10,20,30,40,54,62]) 
print(f'\n\nAfter adding Employee ID column at index 0:\n{df}')

