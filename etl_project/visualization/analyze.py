import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

project_root = Path(__file__).resolve().parents[2]  # Move up two levels to reach the project root
cleaned_data = project_root / "etl_project" / "data" / "cleaned_data" / "cleaned_data.csv"
cleaned_data_path_str = str(cleaned_data)
df = pd.read_csv(cleaned_data_path_str)

df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Salary'] = df['Salary'].round(2)


result = df.groupby('Department').agg(
    total_count=('Department', 'count'),
    total_salary=('Salary', 'sum')
).reset_index()

# Filter departments where total_count > 1000
filtered_result = result.query("total_count > 1000").reset_index()

plt.figure(figsize=(10, 6))
sns.barplot(data=filtered_result, x='Department', y='total_salary', palette='viridis')

plt.xlabel("Department", fontsize=12)
plt.ylabel("Total Salary", fontsize=12)
plt.title("Total Salary by Department (Only Departments with Count > 1000)", fontsize=14)

plt.xticks(rotation=45)  # Rotate x labels for better readability
plt.show()