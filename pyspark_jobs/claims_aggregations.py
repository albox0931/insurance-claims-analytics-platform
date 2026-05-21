from pyspark.sql import SparkSession
from pyspark.sql.functions import sum, avg, count

spark = SparkSession.builder.appName("ClaimsAggregations").getOrCreate()

claims = spark.read.option("header", True).csv("data/sample_claims.csv", inferSchema=True)

summary = (
    claims
    .groupBy("claim_type", "claim_status")
    .agg(
        count("*").alias("total_claims"),
        sum("claim_amount").alias("total_claim_amount"),
        avg("claim_amount").alias("avg_claim_amount")
    )
)

summary.show()
summary.write.mode("overwrite").parquet("output/gold_claims_summary")
