# 🚀 PySpark ETL - Extract Data  

## 📌 Overview  
The `extract.py` script reads a **CSV file** from a user-specified location using **PySpark**, loads it into a **Spark DataFrame**, and logs the process.  

---

## 📜 How It Works  

1. **Takes user input** for the file path of the raw data.  
2. **Reads the CSV file** using `spark.read.csv()`.  
3. **Handles errors** if the file is missing or unreadable.  
4. **Logs the status** (success or failure) in the `logs/etl_log.log` file.  
5. **Returns the loaded DataFrame** for further processing.  

---

## 📥 How to Get Raw Data  

1. **Go to the `data` folder** in your project directory.  
2. **Navigate to the `raw_data` subfolder** (`data/raw_data/`).  
3. **Download the 50K row dataset** and place it in the `raw_data` folder.  
4. **Copy the full file path** of the dataset (e.g., `C:\Users\YourName\etl_project\data\raw_data\messy_data_50k.csv`).  
5. **Run the extraction script and provide this path as input**.  

---

## 🔧 Usage  

### Run the Script  
```bash
python extract.py
