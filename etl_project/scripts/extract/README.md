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

## 🔧 Usage  

### Run the Script  
```bash
python extract.py

