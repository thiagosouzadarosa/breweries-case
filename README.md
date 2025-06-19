# BEES Data Engineering – Breweries Case

## 📑 Description

This project implements a data pipeline using the **Medallion architecture** (Bronze, Silver, Gold) in **Databricks**, consuming data from the public API [Open Brewery DB](https://www.openbrewerydb.org/).

## 🏗️ Architecture

- **Bronze:** Raw data from the API.
- **Silver:** Cleaned data, partitioned by state (`state`).
- **Gold:** Aggregated data — number of breweries by type and state.

## 🔧 Technologies

- Databricks + Delta Lake  
- PySpark  
- Python (requests, pandas)   

## 🗺️ Data Lake Architecture
/Unity Catalog/breweries_analytics/  
├── bronze/breweries.json  
├── silver/breweries_transformed (Delta table partitioned by state)  
└── gold/breweries_aggregated (Delta table view with the count aggregated by type and location)


## 🚀 Notebooks Execution

1. **Bronze:** Collects and stores raw data from the API.  
2. **Silver:** Performs data cleaning and transformation, partitioned by state.  
3. **Gold:** Creates an analytical table with the number of breweries by type and state.  

## 🔔 Monitoring

- Monitoring through Databricks Workflows.  
- Alerts in case of pipeline failures (email, Slack, webhook).  
- Implemented data quality checks:  
  - Schema validation.  
  - Null checks on critical fields (`id`, `state`).  
