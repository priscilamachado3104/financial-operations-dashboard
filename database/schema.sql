-- creates the customers table
CREATE TABLE customers (
    customer_id SERIAL PRIMARY KEY,
    first_name VARCHAR(20) NOT NULL,
    last_name VARCHAR(20) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE

);

-- creates the accounts table
CREATE TABLE accounts (
    account_id SERIAL PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    account_type VARCHAR(30) NOT NULL,
    balance DECIMAL(12, 2) NOT NULL DEFAULT 0.00,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)


);

-- creates the transactions table
CREATE TABLE transactions (
    transaction_id SERIAL PRIMARY KEY,
    account_id INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL,
    transaction_type VARCHAR (30) NOT NULL,
    transaction_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(30) NOT NULL,
    investigation_status VARCHAR(30) NOT NULL DEFAULT 'Not investigated',

    FOREIGN KEY (account_id)
        REFERENCES accounts(account_id)

);