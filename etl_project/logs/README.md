## 📂 Logs Directory Overview

### 📜 logs/etl_log.log
The `logs` directory contains the log file `etl_log.log`, which stores all logs generated during the ETL (Extract, Transform, Load) process. These logs are particularly useful for tracking the progress and debugging issues in the data pipeline. 

### 📍 Importance of Logs
- **Only You** (or the person executing the ETL process) will be able to view these logs. They are stored locally and will provide detailed information about every step of the ETL process.
- Logs provide important insights for troubleshooting any errors that might occur during extraction, transformation, or loading of the data.

### 🔄 Logging Flow Example: Extract, Transform, and Load

Below is an example of how the logging will look in `etl_log.log` for each phase:

| **Phase**   | **Log Message**                                                                                             |
|-------------|------------------------------------------------------------------------------------------------------------|
| **Extract** | `[INFO] 2025-04-01 10:00:01 - Starting data extraction process...`                                          |
| **Extract** | `[INFO] 2025-04-01 10:00:05 - Successfully loaded 100,000 rows from 'raw_data.csv'`                        |
| **Transform** | `[INFO] 2025-04-01 10:05:00 - Starting data transformation process...`                                   |
| **Transform** | `[WARNING] 2025-04-01 10:05:03 - Some rows have invalid date formats, handling with default date`         |
| **Load**    | `[INFO] 2025-04-01 10:10:05 - Successfully loaded 100,000 rows to 'cleaned_data.csv'`                      |

### 🚨 Log Levels
The log file uses different log levels to categorize messages:
- **INFO**: Informational messages about the process, such as successful completions or data loading.
- **ERROR**: Errors that need immediate attention, like missing columns or failed processes.
- **WARNING**: Non-critical issues that may require attention but don’t necessarily stop the process.
- **DEBUG**: Detailed messages (if implemented) for debugging, generally used during development.

### 💻 Running ETL Process in Terminal
When you run the **Extract**, **Transform**, and **Load** processes in your terminal, make sure to check the `etl_log.log` file for the logs. These logs will give you detailed insights into each step, including any errors or warnings that may arise. 


