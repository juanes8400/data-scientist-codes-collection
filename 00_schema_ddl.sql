-- Example schema for a simplified banking dataset in BigQuery dialect

CREATE TABLE IF NOT EXISTS customers (
  customer_id STRING NOT NULL,
  signup_date DATE,
  country STRING,
  PRIMARY KEY (customer_id)
);

CREATE TABLE IF NOT EXISTS transactions (
  transaction_id STRING NOT NULL,
  customer_id STRING NOT NULL,
  transaction_date DATE,
  amount NUMERIC,
  currency STRING,
  PRIMARY KEY (transaction_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE IF NOT EXISTS payments (
  payment_id STRING NOT NULL,
  customer_id STRING NOT NULL,
  payment_date DATE,
  amount NUMERIC,
  due_date DATE,
  PRIMARY KEY (payment_id),
  FOREIGN KEY (customer_id) REFERENCES customers (customer_id)
);