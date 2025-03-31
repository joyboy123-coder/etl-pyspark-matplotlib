## 📂 Project Data Overview

### 🗂 raw_data
The `raw_data` directory contains 100,000 rows of messy data, which includes missing values, inconsistencies, and incorrect formatting. This data needs to undergo cleaning and transformation to be usable for analysis.

### 🧹 cleaned_data
The `cleaned_data` directory contains the transformed data stored in the `cleaned_data.csv` file. The data is cleaned using the transformations in the `transform.py` file, which handles missing values, data type conversion, and other necessary transformations.

## 🛠 Data Transformation

The transformation process includes:
- Handling missing values by filling with appropriate replacements (e.g., using the mean for numerical columns).
- Rounding off numerical columns to a standard format.
- Performing other necessary data cleaning steps to prepare the data for analysis.

### Example: Before vs After Transformation

#### **Before (Raw Data)**

| Name        | Department   | Salary   | Joining Date |
|-------------|--------------|----------|--------------|
| john doe    | ENGINEER     | NaN      | 2020-01-15   |
| JANE SMITH  | psychologist | 70000    | NaN          |
| emily lee   | engineer     | 55000    | 2021-03-22   |
| MICHAEL P   | scientist    | 45000    | 2019-07-30   |
| sarah wong  | engineer     | NaN      | 2020-10-12   |

#### **After (Cleaned Data)**

| Name        | Department   | Salary  | Joining Date |
|-------------|--------------|---------|--------------|
| John Doe    | Engineer     | 57000   | 2020-01-15   |
| Jane Smith  | Psychologist | 70000   | 2020-03-25   |
| Emily Lee   | Engineer     | 55000   | 2021-03-22   |
| Michael P   | Scientist    | 45000   | 2019-07-30   |
| Sarah Wong  | Engineer     | 57000   | 2020-10-12   |

In the cleaned data:
- Missing `Salary` values have been replaced with the mean salary for that department.
- Missing `Joining Date` values have been filled with a default date or handled in another way.
- Data formatting has been standardized, and the data is now ready for analysis.

## 🔧 How the Code Works

1. The `transform.py` file performs the data cleaning and transformation.
2. The cleaned data is saved as `cleaned_data.csv` in the `cleaned_data` directory.

## 📁 Files in this Project

- **raw_data**: Contains the raw, messy data (100k rows).
- **cleaned_data**: Contains the cleaned data (`cleaned_data.csv`).
- **transform.py**: The Python script that performs the data cleaning and transformation.
.
