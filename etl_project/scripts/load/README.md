# 🚀 PySpark to Snowflake ETL Pipeline

## 📌 Overview
This script (`load.py`) is designed to **load cleaned data** from a CSV file into **Snowflake** using **PySpark and Pandas**. It includes **error handling, logging, and automatic table creation**.

---

## 🏗️ Steps Performed in `load.py`
### 1️⃣ **Initialize Spark Session**
- Creates a **PySpark session** for data processing.

### 2️⃣ **Set Up Logging** 📝
- Logs events in an `etl_log.log` file inside the `logs` directory.

### 3️⃣ **Load Cleaned Data into PySpark** 📂
- Reads a **cleaned CSV file** into a **Spark DataFrame**.

### 4️⃣ **Convert PySpark DataFrame to Pandas** 🔄
- Converts the Spark DataFrame to a **Pandas DataFrame** for Snowflake compatibility.

### 5️⃣ **Connect to Snowflake** ❄️
- Uses `snowflake.connector` to establish a secure connection.

### 6️⃣ **Load Data into Snowflake** 🚛
- Uploads data into the **PEOPLE** table.
- **Automatically creates the table** if it doesn’t exist (`auto_create_table=True`).

---

## ⚙️ **Configuration**
### 🔑 **Snowflake Credentials**

Ensure you update your **Snowflake credentials** in the script:
```python
conn = snowflake.connector.connect(
   user="YOUR_USERNAME",
   password="YOUR_PASSWORD",
   account="YOUR_ACCOUNT",
   warehouse="YOUR_WAREHOUSE",
   database="YOUR_DATABASE",
   schema="YOUR_SCHEMA"
)
.
