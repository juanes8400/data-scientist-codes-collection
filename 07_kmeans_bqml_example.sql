-- Example of training a KMeans clustering model using BigQuery ML

-- Create a training dataset using RFM features
CREATE OR REPLACE MODEL `project.dataset.rfm_kmeans_model`
OPTIONS(
  model_type = 'kmeans',
  num_clusters = 4,
  standardize_features = TRUE
) AS
SELECT recency_days, frequency, monetary
FROM (
  SELECT r.customer_id,
         r.recency_days,
         r.frequency,
         r.monetary
  FROM {{ ref('02_features_rfm') }} r
  WHERE r.recency_days IS NOT NULL
);