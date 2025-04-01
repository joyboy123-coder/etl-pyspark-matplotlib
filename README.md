# 🚀 **ETL PySpark Matplotlib Project**

## 📋 **Project Overview**

This project automates an **ETL pipeline** (Extract, Transform, Load) using **PySpark** and **Matplotlib**. It extracts data from a raw dataset, transforms it into a clean format, and loads it into **Snowflake** for further analysis. Finally, it generates a basic **visualization** 📊 of the transformed data.

---

## 🛠️ **How to Use the Project**

- First, **clone the repository** and run the `requirements.txt` 📑 to install dependencies.

- Go to `extract.py` and run it in the terminal using `python extract.py` 💻.
  - It will ask you to provide the path to the raw data. 
  - For example, in your cloned repository, the raw data is stored in `data/raw_data/raw_messy_data100k.csv` 📂.
  - After running, check the `logs` folder 📂 for messages indicating the extraction was successful ✅.

- Next, run `transform.py` 🔄 in the same way.
  - It will prompt you for the extracted data path.
  - At the end, it will ask where to save the cleaned data. Provide the path `data/cleaned_data/cleaned_data.csv` 🗃️.
  - Once transformed, check the logs again for a message confirming the transformation was successful 🟢.

- Then, run `load.py` to load the cleaned data into **Snowflake** ❄️.
  - It will ask for the path to the cleaned data (use the `cleaned_data.csv` saved earlier).
  - You’ll also be prompted for your **Snowflake credentials** 🔑.
  - After successful loading, check the logs to confirm the data was loaded into Snowflake ✅.

- Finally, to visualize the data 📊, go to the `visualization` folder and run `analyze.py` in the terminal.
  - This will generate a bar chart 📉 showing department salaries for those with more than 1000 employees 🏢.

---

## 📈 **Summary**

This ETL pipeline extracts raw data, transforms it, loads it into **Snowflake** ❄️, and generates a basic visualization 📊.
