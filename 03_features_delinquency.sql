-- Derive delinquency related features: days past due and count of late payments

SELECT p.customer_id,
       AVG(DATE_DIFF(p.payment_date, p.due_date, DAY)) AS avg_days_past_due,
       SUM(CASE WHEN p.payment_date > p.due_date THEN 1 ELSE 0 END) AS num_late_payments
FROM payments p
GROUP BY p.customer_id;