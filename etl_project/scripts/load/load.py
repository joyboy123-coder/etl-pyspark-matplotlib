from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
import logging
import os
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas


# ✅ Step 1: Initialize Spark Session
spark = SparkSession.builder.appName("PySpark_Snowflake").getOrCreate()

# ✅ Step 2: Set up logging
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "etl_log.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    # ✅ Step 3: Read cleaned data into Spark DataFrame
    cleaned_data = r"C:\Users\yamin\OneDrive\etl-pyspark-matplotlib\etl_project\data\cleaned_data\cleaned_data.csv"
    df = spark.read.csv(cleaned_data, header=True, inferSchema=True)
    logging.info("Successfully loaded cleaned data into Spark DataFrame.")

    #Change pyspark to pandas for loading data
    pandas_df = df.toPandas()

    # Snowflake Connection Details
    conn = snowflake.connector.connect(
       user="YOUR_USER_NAME",
       password="YOUR_PASSWORD",
       account="YOUR_ACCOUNT",
       warehouse="YOUR_WAREHOUSE",
       database="YOUR_DATABASE",
       schema="YOUR_SCHEMA")
    
    # ✅ Step 6: Load DataFrame into Snowflake

    table_name = "PEOPLE"


    write_pandas(conn,pandas_df,table_name = table_name ,auto_create_table =True)
    logging.info("Data successfully loaded into Snowflake.")

except Exception as e:
    logging.error(f"Error loading into Snowflake: {e}")
    print(f"❌ Error: {e}")


