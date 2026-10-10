#work in HR AND salary > ₹55,000

import pandas as pd

# --------------------------------
# DATASET
# --------------------------------

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106],
    "Employee": ["Amit", "Priya", "Rahul", "Sneha", "Vikas", "Neha"],
    "Department": ["IT", "HR", "Finance", "IT", "Sales", "HR"],
    "City": ["Mumbai", "Delhi", "Pune", "Mumbai", "Bangalore", "Delhi"],
    "Salary": [60000, 55000, 70000, 65000, 75000, 58000],
    "Experience": [3, 2, 5, 4, 6, 3]
})

print(df)
print("--"*10)
#Update Based on Condition
df['level']='Junior'
df.loc[df['Experience']>3,['level']]='Senior'
print(df)



