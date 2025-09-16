# SQL Portfolio

This directory contains a series of SQL scripts that demonstrate how to perform common tasks in data warehousing and analytics environments using BigQuery. These examples illustrate schema definition, data quality checks, feature engineering, modeling dataset assembly, simple customer lifetime value estimation, cohort retention analysis, and training a KMeans clustering model with BigQuery ML.

## File overview

| File                       | Purpose                                                            |
|----------------------------|--------------------------------------------------------------------|
| `00_schema_ddl.sql`        | Defines the base tables (`customers`, `transactions`, `payments`). |
| `01_data_quality_checks.sql`| Performs simple data quality checks on key columns and values.     |
| `02_features_rfm.sql`      | Calculates Recency, Frequency, Monetary features.                 |
| `03_features_delinquency.sql` | Derives delinquency related features (days past due and late payment count). |
| `04_modeling_dataset.sql`  | Assembles a modeling dataset by joining features and labelling churn. |
| `05_clv_estimation.sql`    | Estimates a basic customer lifetime value using average spend and churn probability. |
| `06_cohort_retention.sql`  | Performs a cohort retention analysis to track customer activity across months. |
| `07_kmeans_bqml_example.sql`| Demonstrates training a KMeans model using BigQuery ML on RFM features. |

These scripts can be adapted to other SQL dialects such as PostgreSQL or Spark SQL by adjusting syntax (e.g. date functions) and removing BigQuery specific options.