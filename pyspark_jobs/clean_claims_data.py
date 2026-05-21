from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date, when

spark = SparkSession.builder.appName("CleanClaimsData").getOrCreate()

claims = spark.read.option("header", True).csv("data/sample_claims.csv")

clean_claims = (
    claims
    .dropDuplicates(["claim_id"])
    .withColumn("claim_date", to_date(col("claim_date")))
    .withColumn("claim_amount", col("claim_amount").cast("double"))
    .withColumn(
        "claim_status",
        when(col("claim_status").isin("Approved", "Rejected", "Pending"), col("claim_status"))
        .otherwise("Unknown")
    )
    .filter(col("claim_amount") > 0)
)

clean_claims.show()
clean_claims.write.mode("overwrite").parquet("output/silver_claims")
