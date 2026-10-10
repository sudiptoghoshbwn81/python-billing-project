import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Employee": ["Amit", "Priya", "Rahul", "Sneha", "Neha",
                 "Amit", "Priya", "Rahul", "Sneha", "Neha"],

    "Department": ["IT", "HR", "IT", "Finance", "HR",
                   "IT", "HR", "IT", "Finance", "HR"],

    "Salary": [50000, 45000, 60000, 55000, 48000,
               70000, 52000, 65000, 58000, 50000],

    "Experience": [2, 3, 5, 4, 2, 7, 4, 6, 5, 3],

    "Performance": [70, 75, 90, 80, 72, 95, 85, 92, 88, 78]
}

df = pd.DataFrame(data)

print("\nDataframe:\n",df)
sns.barplot(df,x='Department',y='Salary')
plt.show()
sns.histplot(data=df,x="Salary",bins=5,hue="Department")
plt.title="Histogram"
plt.show()
corelation=df.corr(numeric_only=True)
sns.heatmap(corelation,annot=True)
plt.title='Histogram'
plt.show()