-- Calculate Recency, Frequency and Monetary (RFM) features for each customer

WITH last_transaction AS (
  SELECT customer_id, MAX(transaction_date) AS last_purchase_date
  FROM transactions
  GROUP BY customer_id
),
purchase_frequency AS (
  SELECT customer_id, COUNT(*) AS total_purchases
  FROM transactions
  GROUP BY customer_id
),
total_monetary AS (
  SELECT customer_id, SUM(amount) AS total_spent
  FROM transactions
  GROUP BY customer_id
)
SELECT c.customer_id,
       DATE_DIFF(CURRENT_DATE(), lt.last_purchase_date, DAY) AS recency_days,
       pf.total_purchases AS frequency,
       tm.total_spent AS monetary
FROM customers c
LEFT JOIN last_transaction lt ON c.customer_id = lt.customer_id
LEFT JOIN purchase_frequency pf ON c.customer_id = pf.customer_id
LEFT JOIN total_monetary tm ON c.customer_id = tm.customer_id;