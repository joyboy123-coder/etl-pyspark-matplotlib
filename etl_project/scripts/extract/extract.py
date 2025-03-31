from pyspark.sql import SparkSession
import logging
import os


spark = SparkSession.builder.appName('ETL Pipeline').getOrCreate()


# Set the correct logs directory at the project root
log_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "logs"))
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file_path = os.path.join(log_dir, "etl_log.log")
logging.basicConfig(
    filename=log_file_path,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


file_path = input("Enter your file path for raw data: ")

try:
    df = spark.read.csv(file_path, header=True, inferSchema=True)
    logging.info(f"Successfully extracted data from {file_path}")
    df.show(5)  # Show first 5 rows
except Exception as e:
    logging.warning(f"Error extracting data from {file_path}: {e}")