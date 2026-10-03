# Database Design

## 1. Overview

The Financial Operations System uses a relational database to store information about customers, accounts, and financial transactions.

The database is designed to reduce duplicate information and maintain relationships between customers, accounts, and transactions.

## 2. Entities

The system contains three primary entities:

- Customer
- Account
- Transaction

## 3. Customer Table

The Customer table stores information about customers.

| Column | Data Type | Key | Description |
|---|---|---|---|
| customer_id | Integer | Primary Key | Unique customer identifier |
| first_name | VARCHAR | | Customer's first name |
| last_name | VARCHAR | | Customer's last name |
| email | VARCHAR | | Customer's email address |

## 4. Account Table

The Account table stores information about customer accounts.

| Column | Data Type | Key | Description |
|---|---|---|---|
| account_id | Integer | Primary Key | Unique account identifier |
| customer_id | Integer | Foreign Key | Customer who owns the account |
| account_type | VARCHAR | | Type of account |
| balance | DECIMAL | | Current account balance |

## 5. Transaction Table

The Transaction table stores financial transaction information.

| Column | Data Type | Key | Description |
|---|---|---|---|
| transaction_id | Integer | Primary Key | Unique transaction identifier |
| account_id | Integer | Foreign Key | Account associated with the transaction |
| amount | DECIMAL | | Transaction amount |
| transaction_type | VARCHAR | | Type of transaction |
| transaction_date | TIMESTAMP | | Date and time of transaction |
| status | VARCHAR | | Current transaction status |
| investigation_status | VARCHAR | | Investigation state |

## 6. Relationships

### Customer to Account

One customer can have multiple accounts.

**Relationship:** One-to-Many

```text
Customer 1 ──────── Many Accounts