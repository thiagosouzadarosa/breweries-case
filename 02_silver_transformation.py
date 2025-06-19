# Databricks notebook source
import pandas as pd
from pyspark.sql.functions import col
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

# read table
path_bronze = "/Volumes/breweries_analytics/bronze/api_raw_data/breweries.json"


# COMMAND ----------

# create a spark dataframe
df_pd = pd.read_json(path_bronze)

# Convert to Spark DataFrame
df_bronze = spark.createDataFrame(df_pd)

# COMMAND ----------

# insert ingestion_date column
df_bronze = df_bronze.withColumn("ingestion_date", current_timestamp())

# COMMAND ----------

# transformation and clean null values
df_silver = df_bronze.select(
    col("id").alias("brewery_id"),
    col("name"),
    col("brewery_type"),
    col("city"),
    col("state"),
    col("country"),
    col("longitude").cast("double"),
    col("latitude").cast("double"),
    col("website_url"),
    col("ingestion_date")
).filter(col("state").isNotNull())


# COMMAND ----------

# save table by state
df_silver.write.format("delta").mode("overwrite").partitionBy("state").saveAsTable("breweries_analytics.silver.breweries_transformation")