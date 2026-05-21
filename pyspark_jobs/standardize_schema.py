from pyspark.sql import SparkSession
from pyspark.sql.functions import lower, col

spark = SparkSession.builder.appName("StandardizeSchema").getOrCreate()

claims = spark.read.option("header", True).csv("data/sample_claims.csv")

standardized = claims.select([col(c).alias(c.lower().strip()) for c in claims.columns])

standardized.show()
standardized.write.mode("overwrite").parquet("output/standardized_claims")
