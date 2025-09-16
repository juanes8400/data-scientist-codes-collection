-- Simple customer lifetime value (CLV) estimation using average monetary value and churn probability

WITH avg_monetary AS (
  SELECT customer_id, AVG(amount) AS avg_amount
  FROM transactions
  GROUP BY customer_id
),
churn_prob AS (
  SELECT customer_id,
         CASE WHEN DATE_DIFF(CURRENT_DATE(), MAX(transaction_date), DAY) > 365 THEN 0.8 ELSE 0.2 END AS churn_probability
  FROM transactions
  GROUP BY customer_id
)
SELECT am.customer_id,
       am.avg_amount,
       cp.churn_probability,
       -- Basic CLV estimation: expected value divided by churn probability
       am.avg_amount / NULLIF(cp.churn_probability, 0) AS estimated_clv
FROM avg_monetary am
JOIN churn_prob cp ON am.customer_id = cp.customer_id;