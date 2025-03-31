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

def extract(file_path):
    try:
        df = spark.read.option('header',True).csv(file_path)
        logging.info(f'Succesfully extracted from {file_path}')
        return df
    except Exception as e:
        logging.warning(f'Error Extracting data from {file_path}')
        return None
    

if __name__ == '__main__':
    file_path = input('Enter your file path: ')
    data = extract(file_path)