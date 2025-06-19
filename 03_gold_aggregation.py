# Databricks notebook source
# read table
df_silver = spark.read.table("breweries_analytics.silver.breweries_transformation")


# COMMAND ----------

# Aggregation
df_gold = df_silver.groupBy("state", "brewery_type").count()


# COMMAND ----------

# save table
df_gold.write.format("delta").mode("overwrite").saveAsTable("breweries_analytics.gold.breweries_aggregation")
