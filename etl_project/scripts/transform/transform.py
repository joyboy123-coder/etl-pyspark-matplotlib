import pandas as pd
import os

df = pd.read_csv(r"C:\Users\yamin\Downloads\realistic_messy_dataset_100k.csv")


# Get the absolute path of the project root
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

# Define correct paths
data_folder = os.path.join(PROJECT_ROOT, "data")
cleaned_data_folder = os.path.join(data_folder, "cleaned_data")

# Ensure the cleaned_data directory exists in the project root
os.makedirs(cleaned_data_folder, exist_ok=True)
df['Name'] = df['Name'].str.title().str.strip()
df['Email'] = df['Email'].str.replace(' ','')
df['Email'] = df['Email'].apply(lambda x: x + '.com' if x.endswith('o') or x.endswith('l') else x)
df['Department'] = df['Department'].str.title().str.strip()
df['City'] = df['City'].str.title().str.strip()
df['Salary'] = pd.to_numeric(df['Salary'],errors='coerce')
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Salary'] = df['Salary'].round(2)

# Save the cleaned CSV in the correct directory
cleaned_data_path = os.path.join(cleaned_data_folder, "cleaned_data.csv")
df.to_csv(cleaned_data_path, index=False)
