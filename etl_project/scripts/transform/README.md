# transform.py - Data Transformation with PySpark ⚡

## 📝 Overview
This script performs **data transformation** using **PySpark** to clean and preprocess raw CSV data.  
The cleaned data is then saved as a CSV file using **Pandas**.

---

## 🔄 Transformation Steps

### 📌 1. Initialize Spark Session  
- A **Spark session** is created using `SparkSession.builder.appName()` to enable distributed data processing.  

### 📌 2. Set Up Logging  
- A **log directory** is created to store logs.  
- Logging is configured to record errors and progress in `etl_log.log`.  

### 📌 3. Read Input Data  
- The script **prompts the user** to enter the file path of the raw data.  
- The CSV file is read using **PySpark** with `header=True` and `inferSchema=True`.  
- A log entry is recorded for successful data extraction.  

### 📌 4. Data Cleaning and Transformation  

#### 🔹 Convert `ID` Column  
- The `ID` column is converted to an integer using `col("ID").cast("int")`.  

#### 🔹 Clean `Name` Column  
- Trims extra spaces and capitalizes names using `initcap(trim(col("Name")))`.  

#### 🔹 Clean `Department` Column  
- Trims extra spaces and capitalizes department names.  
- Removes unwanted characters (`/` and `,`) and keeps the relevant part.  

#### 🔹 Clean `City` Column  
- Trims extra spaces and capitalizes city names.  

#### 🔹 Process `Salary` Column  
- Calculates the **average salary** from existing values.  
- Replaces missing salary values with the calculated average.  
- Converts the column to **double** data type.  

#### 🔹 Clean `Email` Column  
- Converts emails to lowercase and removes spaces.  
- Replaces the email domain with a **random domain** (`@gmail.com`, `@yahoo.com`, or `@hotmail.com`).  

### 📌 5. Convert to Pandas and Save  
- The cleaned **PySpark DataFrame** is converted into a **Pandas DataFrame**.  
- The transformed data is saved as a CSV file in the output directory.  

### 📌 6. Error Handling  
- If an error occurs, it is logged in `etl_log.log`, and an error message is displayed.  

---

