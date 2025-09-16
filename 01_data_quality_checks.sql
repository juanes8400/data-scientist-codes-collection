-- Data quality checks for the banking dataset

-- Check for nulls in customer_id fields
SELECT 'transactions' AS table_name, COUNT(*) AS null_customer_ids
FROM transactions
WHERE customer_id IS NULL;

SELECT 'payments' AS table_name, COUNT(*) AS null_customer_ids
FROM payments
WHERE customer_id IS NULL;

-- Check that transaction amounts are positive
SELECT COUNT(*) AS negative_transactions
FROM transactions
WHERE amount < 0;