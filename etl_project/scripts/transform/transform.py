from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, initcap, when, regexp_replace, lower, split, avg, lit, concat_ws
import random
import logging
import os
from pathlib import Path
import pandas as pd


# Initialize Spark session
spark = SparkSession.builder.appName('ETL Pipeline').getOrCreate()

# Set up logging
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

log_file_path = os.path.join(log_dir, "etl_log.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Prompt user for file path
file_path = input("Enter your file path for raw data: ")

try:
    # Extract: Read raw data
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    logging.info("Successfully extracted data for transformation.")

    # Transformation steps
    logging.info("Starting data transformations...")

    # Convert ID to integer
    df = df.withColumn("ID", col("ID").cast("int"))

    # Clean Name column
    df = df.withColumn("Name", initcap(trim(col("Name"))))

    # Clean Department column
    df = df.withColumn("Department", initcap(trim(col("Department"))))
    df = df.withColumn("Department", when(col("Department").contains("/"), split(col("Department"), "/").getItem(1)).otherwise(col("Department")))
    df = df.withColumn("Department", when(col("Department").contains(","), split(col("Department"), ",").getItem(0)).otherwise(col("Department")))

    # Clean City column
    df = df.withColumn("City", initcap(trim(col("City"))))

    df = df.withColumn("Salary", when(col("Salary").isNull(), lit(50000)).otherwise(col("Salary")))
    df = df.withColumn("Salary", regexp_replace(col("Salary"), "[^0-9.]", "").cast("double"))
   

    # Clean Email column
    df = df.withColumn("Email", lower(trim(col("Email"))))
    df = df.withColumn("Email", regexp_replace(col("Email"), " ", ""))
    
    # Replace email domain with a random one
    domains = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
    random_domain = random.choice(domains)
    df = df.withColumn("Email", concat_ws("", split(col("Email"), "@").getItem(0), lit(random_domain)))

    logging.info("Transformation completed successfully.")

    pandas_df = df.toPandas()
    
    # Get the absolute path of the script's directory
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Define the correct output path inside the project root
    output_dir = os.path.join(script_dir, "data", "cleaned_data")
    output_path = os.path.join(output_dir, "cleaned_data.csv")

    # Ensure 'cleaned_data' folder exists
    os.makedirs(output_dir, exist_ok=True)

    # Save the DataFrame as CSV
    pandas_df.to_csv(output_path, index=False)
    logging.info("Data successfully saved as CSV using Pandas.")
except Exception as e:
    logging.error(f"Error transforming data: {e}")
    print(f"❌ Error: {e}")


print(pandas_df[pandas_df["Salary"].isna()])
