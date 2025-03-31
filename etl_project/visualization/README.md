## 📊 Project Overview

This project is focused on analyzing salary distribution across different departments using a dataset containing employee information. We are specifically visualizing the total salary by department, but only considering departments where the total count of employees is greater than 1000.

## 🛠 Steps Taken

1. **Data Loading** 📥:
   - The data is loaded from a CSV file (`cleaned_data.csv`) using Pandas.
   - The file path is dynamically built based on the project structure.

2. **Data Cleaning** 🧹:
   - The `Salary` column is cleaned by filling missing values (`NaN`) with the mean salary of the department.
   - The `Salary` column is rounded to 2 decimal places for better clarity.

3. **Data Aggregation** ➗:
   - We grouped the data by the `Department` column and calculated two aggregates:
     - `total_count`: Total number of employees in each department.
     - `total_salary`: Sum of the salary in each department.

4. **Data Filtering** 🔍:
   - We filtered the departments where the total employee count (`total_count`) is greater than 1000.

5. **Visualization** 📈:
   - A bar chart was created using Seaborn and Matplotlib to display the total salary by department for those departments with a total count greater than 1000.
   - The chart was saved as a PNG image (`salary_distribution.png`) with a resolution of 300 dpi.

6. **File Saving** 💾:
   - The final chart is saved as `salary_distribution.png` in the `visualization` folder of the project.

## 🏃 How to Run the Code

1. Clone the repository or download the project files.
2. Install the required dependencies by running:
   ```bash
   python analyze.py

