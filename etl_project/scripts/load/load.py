from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
import logging
import os
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path

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
    # Use relative path to dynamically get the correct file path based on script location
    project_root = Path(__file__).resolve().parents[2]  # Move up two levels to reach the project root
    cleaned_data = project_root / "data" / "cleaned_data" / "cleaned_data.csv"  # Build the relative path

    # Convert path to string (needed for Spark to read)
    cleaned_data_path_str = str(cleaned_data)

    # Read the CSV file
    df = spark.read.csv(cleaned_data_path_str, header=True, inferSchema=True)
    logging.info("Successfully loaded cleaned data into Spark DataFrame.")

    # Change PySpark DataFrame to Pandas DataFrame
    pandas_df = df.toPandas()


    conn = snowflake.connector.connect(
       user="YOUR_USER_NAME",
       password="YOUR_PASSWORD",
       account="YOUR_ACCOUNT",
       warehouse="YOUR_WAREHOUSE",
       database="YOUR_DATABASE",
       schema="YOUR_SCHEMA")
    
    # ✅ Step 6: Load DataFrame into Snowflake
    table_name = "PEOPLE"

    # Write to Snowflake using Pandas
    write_pandas(conn, pandas_df, table_name=table_name, auto_create_table=True)
    logging.info("Data successfully loaded into Snowflake.")

except Exception as e:
    logging.error(f"Error loading into Snowflake: {e}")
    print(f"❌ Error: {e}")
