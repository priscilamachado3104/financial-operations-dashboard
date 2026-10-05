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


if __name__ == "__main__":
    unittest.main()