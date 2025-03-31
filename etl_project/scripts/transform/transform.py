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

    # Convert Salary to numeric and fill nulls with mean
    salary_mean = df.select(avg(col("Salary"))).collect()[0][0]
    df = df.withColumn("Salary", when(col("Salary").isNull(), salary_mean).otherwise(col("Salary")))
    df = df.withColumn("Salary", col("Salary").cast("double"))

    # Clean Email column
    df = df.withColumn("Email", lower(trim(col("Email"))))
    df = df.withColumn("Email", regexp_replace(col("Email"), " ", ""))
    
    # Replace email domain with a random one
    domains = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
    random_domain = random.choice(domains)
    df = df.withColumn("Email", concat_ws("", split(col("Email"), "@").getItem(0), lit(random_domain)))

    logging.info("Transformation completed successfully.")

    pandas_df = df.toPandas()

    # Define output path
    output_path = r"C:\Users\yamin\OneDrive\etl-pyspark-matplotlib\etl_project\data\cleaned_data\cleaned_data.csv"

    # Save as CSV using Pandas
    pandas_df.to_csv(output_path, index=False)

    logging.info("Data successfully saved as CSV using Pandas.")
except Exception as e:
    logging.error(f"Error transforming data: {e}")
    print(f"❌ Error: {e}")
