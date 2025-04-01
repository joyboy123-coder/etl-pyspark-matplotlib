# ETL Project 🚀

## 🗂 Repository Structure

### 📁 Project Files Overview
- **data**: Contains raw and cleaned datasets.
- **logs**: Log files from the ETL process.
- **scripts**: Python scripts for extraction, transformation, and loading (ETL).
- **visualization**: Stores charts and visualizations.
- **README.md**: Project description and instructions.
- **requirements.txt**: Required libraries for the project.

---

## 📝 File Descriptions

### 1. **extract.py** 📝
This script handles the extraction of raw data from the provided file and logs the process in `etl_log.log`.

### 2. **transform.py** 🔄
This file transforms the raw data by applying various cleaning and formatting steps. After transformation, the cleaned data is saved as a CSV file in the `data/cleaned_data/` directory.

### 3. **analyze.py** 📊
This script analyzes the cleaned data, calculates total salaries by department, and generates a bar plot saved as `salary_distribution.png`.

---

## 📄 Logs and Data Flow

- **etl_log.log** 📂: Logs the ETL process, including data extraction and transformation steps. This file will be populated with logs after running the ETL scripts.
- **raw_data** 📁: Contains the raw dataset (e.g., `realistic_messy_dataset_100k.csv`).
- **cleaned_data** 📁: Stores the transformed dataset after data cleaning in `cleaned_data.csv`.

---

## 📦 Requirements

The project requires the following libraries, specified in `requirements.txt`:

- `pyspark==3.3.1` for large-scale data processing.
- `pandas==1.5.3` for data manipulation and cleaning.
- `matplotlib==3.6.2` for data visualization.
- `numpy==1.23.3` for numerical operations.

---

## 📈 Visualizations

### **Salary Distribution** 💸

- A bar plot representing the total salary by department, showing departments with a total count greater than 1000.
- The plot is saved as `salary_distribution.png`.

---

## 📅 Project Workflow

1. **Extract**: Use `extract.py` to read the raw data.
2. **Transform**: Clean and transform the data using `transform.py`. The cleaned data is stored in `data/cleaned_data/`.
3. **Analyze**: Perform analysis on the cleaned data with `analyze.py` and generate visualizations.
4. **Logs**: Track the entire process in `etl_log.log`.

---

## 🔧 How to Run the ETL Pipeline

1. Ensure that you have the necessary Python libraries installed by running `pip install -r requirements.txt`.
2. Run the **extract.py** script to extract the raw data.
3. Run the **transform.py** script to clean and transform the data.
4. Run **analyze.py** to perform data analysis and generate visualizations.

