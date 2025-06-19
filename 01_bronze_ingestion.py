# Databricks notebook source
import requests
import json
from pyspark.sql.functions import current_timestamp

# COMMAND ----------

# API endpoint
url = "https://api.openbrewerydb.org/v1/breweries"

# COMMAND ----------

response = requests.get(url)

# Check if request succeeded
if response.status_code == 200:
    data = response.json()  # this is a list of dicts
else:
    raise Exception(f"Failed to fetch data. Status code: {response.status_code}")
# get data
response = requests.get(url)
data = response.json()

# COMMAND ----------

# volume path
volume_path = "/Volumes/breweries_analytics/bronze/api_raw_data/breweries.json"


# COMMAND ----------

# save json
dbutils.fs.put(volume_path, json.dumps(data, indent=2), overwrite=True)