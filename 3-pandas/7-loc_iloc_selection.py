import numpy as np
import pandas as pd

student_data ={
    "Name" : ["Alice", "Bob","Chrlie","David"],
    "Age" : [21, 22, 25, 31],
    "Score": [85, 93, 56, 72]
}
student_ids = ['S001', 'S002', 'S003', 'S004']
df = pd.DataFrame(student_data, index= student_ids)

print("Student Dataframe: ")
print(df)
print(" "+"="*30+" ")

# Select the row with index 'S002'
bob_data = df.loc['S002']
print("Data of index 'S002': ")
print(bob_data)
print(" "+"="*30+" ")

# Slect rows for alice and david
alice_david_data = df.loc[['S001', 'S004']]
print("Data of Alice and David: ")
print(alice_david_data)
print(" "+"="*30+" ")

# select the 'Name' COolumn
name_col = df.loc[:, 'Name']
print("Names of all students: ")
print(name_col)
print(" "+"="*30+" ")

# Select 'Name' ans 'Score' columns
cols = df.loc[:, ['Name', 'Score']]
print("Data of Names and Score of the students: ")
print(cols)
print(" "+"="*30+" ")

# Select 'Age' and 'Score' for Bob and Charlie
age_score_bob_charlie = df.loc[['S002','S003'], ['Age', 'Score']]
print("Age and Score for Bob and Charlie: ")
print(age_score_bob_charlie)
print(" "+"="*30+" ")

# Slicing with loc
# Select all columns for students from S002 to S004
students_S002_to_S004 = df.loc['S002':'S004']
print("Students from S002 to S004:")
print(students_S002_to_S004)
print("" + "="*30 + "")

# Select 'Name' column for students from S001 to S003
names_s001_to_s003 = df.loc['S001':'S003', 'Name']
print("Names from S001 to S003:")
print(names_s001_to_s003)
print("" + "="*30 + "")

# Selecting the first row (position 0)
first_row = df.iloc[0]
print("First row (position 0): ")
print(first_row)
print("" + "="*30 + "")

# Select the second and fourth rows (positions 1 and 3)
rows_1_and_3 = df.iloc[[1, 3]]
print("Rows at positions 1 and 3:")
print(rows_1_and_3)
print("" + "="*30 + "")

# Select the second column (position 1, which is 'Age')
ages = df.iloc[:, 1] # The ':' selects all rows
print("All student ages:")
print(ages)
print("" + "="*30 + "")

# Select the first and third columns (positions 0 and 2, 'Name' and 'Score')
name_score_cols = df.iloc[:, [0, 2]]
print("Names and Scores (using iloc):")
print(name_score_cols)
print("" + "="*30 + "")

# Selecting 'Age' and 'Score' for for first and third student
age_score_0_and_2 = df.iloc[[1,2], [1,2]]
print("'Age' and 'Score' for students at position 0 and 2: ")
print(age_score_0_and_2)
print(" "+"="*30+" ")

# Selecting all columns for students from position 0 up to position 4
students_1_to_3 = df.iloc[1:4]
print("Data of students from position 1 to 4: ")
print(students_1_to_3)
print(" "+"="*30+" ")

# selecting 'Name' column from position 0 to 3
name_0_to_3 = df.iloc[0:3, 0]
print("Names for students at positions 0 to 2:")
print(name_0_to_3)
print(" "+"="*30+" ")

