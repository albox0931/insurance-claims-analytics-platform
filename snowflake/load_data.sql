-- Example Snowflake loading pattern
-- In real AWS integration, configure external stage pointing to S3.

COPY INTO INSURANCE_ANALYTICS.BRONZE.RAW_CLAIMS
FROM @insurance_claims_stage/sample_claims.csv
FILE_FORMAT = (TYPE = CSV FIELD_OPTIONALLY_ENCLOSED_BY = '"' SKIP_HEADER = 1);
