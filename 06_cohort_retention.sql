-- Cohort retention analysis to understand customer retention over time

WITH cohorts AS (
  SELECT customer_id,
         EXTRACT(YEAR FROM MIN(transaction_date)) AS cohort_year,
         EXTRACT(MONTH FROM MIN(transaction_date)) AS cohort_month
  FROM transactions
  GROUP BY customer_id
),
transactions_enriched AS (
  SELECT t.customer_id,
         c.cohort_year,
         c.cohort_month,
         EXTRACT(YEAR FROM t.transaction_date) AS transaction_year,
         EXTRACT(MONTH FROM t.transaction_date) AS transaction_month
  FROM transactions t
  JOIN cohorts c ON t.customer_id = c.customer_id
)
SELECT cohort_year,
       cohort_month,
       CONCAT(transaction_year, '-', transaction_month) AS period,
       COUNT(DISTINCT customer_id) AS active_customers
FROM transactions_enriched
GROUP BY cohort_year, cohort_month, transaction_year, transaction_month
ORDER BY cohort_year, cohort_month, transaction_year, transaction_month;