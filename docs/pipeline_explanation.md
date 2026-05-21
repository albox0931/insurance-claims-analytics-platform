# Pipeline Explanation

## Step 1: Raw Data Ingestion
Raw claims, policies, and customer files are received in CSV and JSON formats.

## Step 2: Schema Standardization
PySpark reads each file and standardizes column names, data types, and date formats.

## Step 3: Data Cleaning
The pipeline removes duplicates, handles null values, validates claim amounts, and filters invalid records.

## Step 4: Transformation
Claims data is joined with policy and customer data.

## Step 5: Load to Snowflake
Processed data is loaded into Snowflake Bronze, Silver, and Gold tables.

## Step 6: Reporting
Gold-layer tables are consumed by BI tools like Power BI.
