from pyspark.sql import SparkSession
from pyspark.sql.functions import col, trim, initcap, when, regexp_replace, lower, split, avg, expr,concat,lit
from pyspark.sql.functions import concat_ws
import random
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
    df = spark.read.csv(file_path,header = True,inferSchema = True)
    logging.info('Succesfully data extracted for transformations ')

    # Convert ID to integer
    logging.info("Converting ID column to integer...")
    df = df.withColumn("ID", col("ID").cast("int"))

    # Clean Name column
    logging.info("Cleaning Name column...")
    df = df.withColumn("Name", initcap(trim(col("Name"))))

    # Clean Department column
    logging.info("Cleaning Department column...")
    df = df.withColumn("Department", initcap(trim(col("Department"))))
    df = df.withColumn("Department", when(col("Department").contains("/"), split(col("Department"), "/").getItem(1)).otherwise(col("Department")))
    df = df.withColumn("Department", when(col("Department").contains(","), split(col("Department"), ",").getItem(0)).otherwise(col("Department")))

    # Clean City column
    logging.info("Cleaning City column...")
    df = df.withColumn("City", initcap(trim(col("City"))))

    # Convert Salary to numeric and fill nulls with mean
    logging.info("Handling Salary column...")
    salary_mean = df.select(avg(col("Salary"))).collect()[0][0]
    df = df.withColumn("Salary", when(col("Salary").isNull(), salary_mean).otherwise(col("Salary")))
    df = df.withColumn("Salary", col("Salary").cast("double"))

    # Clean Email column
    logging.info("Cleaning Email column...")
    df = df.withColumn("Email", lower(trim(col("Email"))))
    df = df.withColumn("Email", regexp_replace(col("Email"), " ", ""))

    domains = ["@gmail.com", "@yahoo.com", "@hotmail.com"]
    random_domain = random.choice(domains)  # Select a random domain
    df = df.withColumn("Email", concat_ws("", split(col("Email"), "@").getItem(0), lit(random_domain)))

    logging.info("Transformation completed!")
    df.show(5)

except Exception as e:
    logging.warning(f"Error transforming data: {e}")