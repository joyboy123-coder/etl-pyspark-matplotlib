from pyspark.sql import SparkSession
from pyspark.sql.functions import col
import pandas as pd
import logging
import os
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas
from pathlib import Path

# Initialize Spark Session
spark = SparkSession.builder.appName("PySpark_Snowflake").getOrCreate()

# Set up logging
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "etl_log.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

try:
    cleaned_data_path = input("Enter the file path for 'cleaned_data.csv': ")

    # Read the CSV file
    df = spark.read.csv(cleaned_data_path, header=True, inferSchema=True)
    logging.info("Successfully loaded cleaned data into Spark DataFrame.")

    # Change PySpark DataFrame to Pandas DataFrame
    pandas_df = df.toPandas()


    print("Please enter your Snowflake credentials:")

    user = input("Snowflake Username: ")
    password = input("Snowflake Password: ")
    account = input("Snowflake Account: ")
    warehouse = input("Snowflake Warehouse: ")
    database = input("Snowflake Database: ")
    schema = input("Snowflake Schema: ")

    # Connect to Snowflake using the provided credentials
    conn = snowflake.connector.connect(
       user=user,
       password=password,
       account=account,
       warehouse=warehouse,
       database=database,
       schema=schema)
    
    # Load DataFrame into Snowflake
    table_name = input("Enter your table name: ")

    # Write to Snowflake using Pandas
    write_pandas(conn, pandas_df, table_name=table_name, auto_create_table=True)
    logging.info("Data successfully loaded into Snowflake.")

except Exception as e:
    logging.error(f"Error loading into Snowflake: {e}")
