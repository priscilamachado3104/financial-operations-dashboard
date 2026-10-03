-- inserts sample customers
INSERT INTO customers (first_name, last_name, email)
VALUES 
    ('Priscila', 'Machado', 'priscila.machado@example.com'),
    ('Adonai', 'Finda', 'adonai.finda@example.com'),
    ('Patricia','Lopes', 'patricia.lopes@example.com');

-- inserts sample accounts
INSERT INTO accounts (customer_id, account_type, balance)
VALUES
    (1, 'Checking', 1500.00),
    (1, 'Savings', 5000.00),
    (2, 'Checking', 850.50),
    (3, 'Checking', 2200.75);

-- inserts sample transactions
INSERT INTO transactions (account_id, amount, transaction_type, status)
VALUES
    (1, 250.00, 'Deposit', 'Completed'),
    (1, 75.50, 'Payment', 'Completed'),
    (2, 500.00, 'Deposit', 'Completed'),
    (3, 100.00, 'Withdrawal', 'Pending'),
    (4, 300.00, 'Transfer', 'Failed');
    