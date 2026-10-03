# Acceptance Criteria

## AC01: View Transactions

### User Story
As an operations analyst, I want to view transactions so that I can review financial activity.

### Acceptance Criteria

- The system displays a list of transactions.
- Each transaction displays its transaction ID.
- Each transaction displays the customer.
- Each transaction displays the transaction amount.
- Each transaction displays its current status.
- If no transactions exist, the system displays an appropriate message.

---

## AC02: Search Transactions

### User Story
As an operations analyst, I want to search for a transaction by ID so that I can quickly locate a specific transaction.

### Acceptance Criteria

- The analyst can enter a transaction ID.
- If the transaction exists, the system displays the matching transaction.
- If the transaction does not exist, the system displays an appropriate message.
- Searching does not modify the transaction data.

---

## AC03: Filter Transactions

### User Story
As an operations analyst, I want to filter transactions by status so that I can identify transactions requiring attention.

### Acceptance Criteria

- The analyst can select a transaction status.
- The system displays only transactions matching the selected status.
- Selecting "All" displays all transactions.
- If no transactions match the selected status, the system displays an appropriate message.

---

## AC04: Add Transactions

### User Story
As an operations analyst, I want to add a new transaction so that new financial activity can be recorded.

### Acceptance Criteria

- The analyst can enter the required transaction information.
- The system validates the required information.
- A valid transaction is saved to the database.
- The newly created transaction appears in the transaction list.
- Invalid information prevents the transaction from being saved.
- The system provides an appropriate error message when validation fails.

---

## AC05: Update Transaction Status

### User Story
As an operations analyst, I want to update the status of a transaction so that I can track its current state.

### Acceptance Criteria

- The analyst can select a transaction.
- The analyst can change its status.
- The system saves the updated status.
- The updated status is displayed when the transaction is viewed again.

---

## AC06: Validate Transaction Data

### User Story
As an operations analyst, I want the system to validate transaction data
so that invalid information is not stored.

### Acceptance Criteria

- Required fields cannot be empty.
- Transaction amounts must be valid numeric values.
- Transaction amounts cannot be negative.
- Invalid data is rejected.
- The system displays a message explaining the validation error.

---

## AC07: Identify Issues

### User Story
As an operations analyst, I want the system to identify transactions containing invalid or missing data so that problems can be investigated.

### Acceptance Criteria

- The system identifies transactions containing validation errors.
- The system indicates why the transaction was flagged.
- Flagged transactions can be distinguished from valid transactions.

---

## AC08: Investigate Transactions

### User Story
As an operations analyst, I want to mark transactions for investigation
so that issues can be tracked and reviewed.

### Acceptance Criteria

- The analyst can mark a transaction for investigation.
- The transaction's investigation status is saved.
- The transaction appears in the investigation list.
- The analyst can remove the investigation status when the issue is resolved.