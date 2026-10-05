import unittest
from unittest.mock import patch

from app import validate_transaction


class TestTransactionValidation(unittest.TestCase):

    @patch("app.search_transaction")
    def test_valid_transaction(self, mock_search):
        mock_search.return_value = (
            1,
            1,
            250.00,
            "Deposit",
            None,
            "Completed",
            "Not investigated"
        )

        result = validate_transaction(1)

        self.assertIn("is valid", result)

    @patch("app.search_transaction")
    def test_invalid_amount(self, mock_search):
        mock_search.return_value = (
            2,
            1,
            0.00,
            "Deposit",
            None,
            "Completed",
            "Not investigated"
        )

        result = validate_transaction(2)

        self.assertIn("must be greater than $0", result)

    @patch("app.search_transaction")
    def test_invalid_status(self, mock_search):
        mock_search.return_value = (
            3,
            1,
            100.00,
            "Deposit",
            None,
            "Under review",
            "Not investigated"
        )

        result = validate_transaction(3)

        self.assertIn("not an accepted transaction status", result)

    @patch("app.search_transaction")
    def test_transaction_not_found(self, mock_search):
        mock_search.return_value = None

        result = validate_transaction(999)

        self.assertEqual(result, "Transaction not found.")


    @patch("app.get_connection")
    def test_search_existing_transaction(self, mock_connection):
        mock_cursor = mock_connection.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = (
            1,
            1,
            250.00,
            "Deposit",
            None,
            "Completed",
            "Not investigated"
        )

        from app import search_transaction

        result = search_transaction(1)

        self.assertEqual(result[0], 1)
        self.assertEqual(result[2], 250.00)

        
    @patch("app.get_connection")
    def test_search_missing_transaction(self, mock_connection):
        mock_cursor = mock_connection.return_value.cursor.return_value
        mock_cursor.fetchone.return_value = None

        from app import search_transaction

        result = search_transaction(999)

        self.assertIsNone(result)


    @patch("app.get_connection")
    def test_update_investigation_status(self, mock_connection):
        mock_cursor = mock_connection.return_value.cursor.return_value

        from app import update_investigation_status

        update_investigation_status(5, "Resolved")

        mock_cursor.execute.assert_called_once_with(
            """
        UPDATE transactions
        SET investigation_status = %s
        WHERE transaction_id = %s
        """,
            ("Resolved", 5)
        )

        mock_connection.return_value.commit.assert_called_once()

    @patch("app.get_connection")
    def test_add_transaction(self, mock_connection):
        mock_cursor = mock_connection.return_value.cursor.return_value

        from app import add_transaction

        add_transaction(1, 100.00, "Deposit", "Completed")

        mock_cursor.execute.assert_called_once_with(
            """
        INSERT INTO transactions
        (account_id, amount, transaction_type, status)
        VALUES (%s, %s, %s, %s)
        """,
            (1, 100.00, "Deposit", "Completed")
        )

        mock_connection.return_value.commit.assert_called_once()

    @patch("app.get_transactions")
    @patch("app.get_accounts")
    @patch("app.get_customers")
    def test_customers_route(
        self,
        mock_customers,
        mock_accounts,
        mock_transactions
    ):
        mock_customers.return_value = []
        mock_accounts.return_value = []
        mock_transactions.return_value = []

        from app import app

        client = app.test_client()

        response = client.get("/customers")

        self.assertEqual(response.status_code, 200)



if __name__ == "__main__":
    unittest.main()