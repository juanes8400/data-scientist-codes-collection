-- Assemble a modeling dataset that joins customer attributes and engineered features

WITH rfm AS (
  SELECT *
  FROM /*+ LABEL(rfm) */ (
    {{ ref('02_features_rfm') }}
  )
),
delinquency AS (
  SELECT *
  FROM /*+ LABEL(delinquency) */ (
    {{ ref('03_features_delinquency') }}
  )
)
SELECT c.customer_id,
       c.signup_date,
       c.country,
       r.recency_days,
       r.frequency,
       r.monetary,
       d.avg_days_past_due,
       d.num_late_payments,
       -- Example label: churn indicator (synthesized)
       CASE WHEN r.recency_days > 180 OR d.num_late_payments > 3 THEN 1 ELSE 0 END AS label
FROM customers c
LEFT JOIN rfm r ON c.customer_id = r.customer_id
LEFT JOIN delinquency d ON c.customer_id = d.customer_id;