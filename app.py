from flask import Flask, render_template, request, redirect  # Imports Flask and the function used to render HTML templates
import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

def get_connection():
    return psycopg.connect(
        dbname=os.getenv("DB_NAME", "financial_operations"),
        user=os.getenv("DB_USER", "priscilamachado"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )

def get_customers():
    connection = get_connection() #opens a connection to the financial-operations database
    cursor = connection.cursor() #creates a cursor to execute SQL commands
    cursor.execute("SELECT * FROM customers") # executes a SQL query that gets all customers
    customers = cursor.fetchall() #retrieves all the customer rows from the database
    cursor.close() 
    connection.close()
    return customers
print(get_customers())

def get_accounts():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM accounts")
    accounts = cursor.fetchall()
    cursor.close()
    connection.close()
    return accounts

def get_transactions():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()

    formatted_transactions = []

    for transaction in transactions:
        formatted_transaction = list(transaction)
        formatted_transaction[4] = transaction[4].strftime("%b %d, %Y %I:%M %p")
        formatted_transactions.append(formatted_transaction)

    cursor.close()
    connection.close()

    return formatted_transactions



def search_transaction(transaction_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM transactions WHERE transaction_id = %s",
        (transaction_id,)
    )
    transaction = cursor.fetchone()
    cursor.close()
    connection.close()
    return transaction


def validate_transaction(transaction_id):
    transaction = search_transaction(transaction_id)

    if transaction is None:
        return "Transaction not found."

    amount = transaction[2]
    status = transaction[5]

    if amount <= 0:
        return (
            f"Transaction #{transaction_id} is invalid "
            f"because the amount (${amount:.2f}) must be greater than $0."
        )

    if status not in ["Completed", "Pending", "Failed"]:
        return (
            f"Transaction #{transaction_id} is invalid "
            f"because '{status}' is not an accepted transaction status."
        )

    return (
        f"Transaction #{transaction_id} is valid "
        f"because the amount (${amount:.2f}) is greater than $0 "
        f"and the status ({status}) is an accepted transaction status."
    )

def update_investigation_status(transaction_id, investigation_status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        UPDATE transactions
        SET investigation_status = %s
        WHERE transaction_id = %s
        """,
        (investigation_status, transaction_id)
    )

    connection.commit()
    cursor.close()
    connection.close()


def add_transaction(account_id, amount, transaction_type, status):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO transactions
        (account_id, amount, transaction_type, status)
        VALUES (%s, %s, %s, %s)
        """,
        (account_id, amount, transaction_type, status)
    )

    connection.commit()
    cursor.close()
    connection.close()



@app.route("/customers")  # Creates a URL route called /customers
def customers():  # Defines the function that runs when someone visits /customers
    customers = get_customers()  # Calls get_customers() and stores the database results
    accounts = get_accounts()
    transactions = get_transactions()

    transaction_id = request.args.get("transaction_id")
    status = request.args.get("status")
    investigation_status = request.args.get("investigation_status")

    search_result = None

    if transaction_id:
        transaction = search_transaction(transaction_id)
        
        if transaction:
            transactions = [transaction]
            search_result = f"Transaction #{transaction_id} found."
        else:
            transactions = []
            search_result = f"Transaction #{transaction_id} was not found."

    if status:
        transactions = [
            transaction
            for transaction in transactions
            if transaction[5] == status
        ]
        
    if investigation_status:
        transactions = [
            transaction
            for transaction in transactions
            if transaction[6] == investigation_status
        ]
            
    return render_template("index.html", customers=customers, accounts=accounts, transactions=transactions, validation_result=None, search_result=search_result)  # Sends the financial data to the HTML template


@app.route("/validate")
def validate():
    transaction_id = request.args.get("transaction_id")

    customers = get_customers()
    accounts = get_accounts()
    transactions = get_transactions()

    validation_result = None

    if transaction_id:
        validation_result = validate_transaction(transaction_id)

    return render_template(
        "index.html",
        customers=customers,
        accounts=accounts,
        transactions=transactions,
        validation_result=validation_result
    )

@app.route("/update-investigation", methods=["GET"])
def update_investigation():
    transaction_id = request.args.get("transaction_id")
    investigation_status = request.args.get("investigation_status")

    if transaction_id and investigation_status:
        update_investigation_status(
            transaction_id,
            investigation_status
        )

        message = (
            f"Transaction #{transaction_id} updated successfully. "
            f"Investigation status changed to {investigation_status}."
        )
    else:
        message = "Please provide a transaction ID and investigation status."

    customers = get_customers()
    accounts = get_accounts()
    transactions = get_transactions()

    return render_template(
        "index.html",
        customers=customers,
        accounts=accounts,
        transactions=transactions,
        validation_result=None,
        update_result=message
    )

@app.route("/add-transaction", methods=["GET"])
def add_transaction_route():
    account_id = request.args.get("account_id")
    amount = request.args.get("amount")
    transaction_type = request.args.get("transaction_type")
    status = request.args.get("status")

    if account_id and amount and transaction_type and status:
        add_transaction(
            account_id,
            amount,
            transaction_type,
            status
        )

    return redirect("/customers")
    
if __name__ == "__main__":  # Checks whether this file is being run directly
    app.run()  # Starts the Flask development server