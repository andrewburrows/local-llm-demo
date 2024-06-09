Feature: Third-Party Payment Transaction Service

Background:
Given the Third-Party Payment Transaction Service is available and properly integrated

Scenario: Successful payment transaction
Given a customer has initiated a payment for a product
And the payment details are valid
When the payment transaction is processed
Then the payment should be successfully authorized
And the payment status should be updated to "authorized"
And a transaction ID should be generated and returned

Scenario: Payment transaction with invalid card details
Given a customer has initiated a payment for a product
And the provided card details are invalid
When the payment transaction is processed
Then the payment should be declined
And an "invalid_card_details" error should be returned

Scenario: Payment transaction with insufficient funds
Given a customer has initiated a payment for a product
And the customer's account has insufficient funds
When the payment transaction is processed
Then the payment should be declined
And an "insufficient_funds" error should be returned

Scenario: Payment transaction with expired card
Given a customer has initiated a payment for a product
And the provided card has expired
When the payment transaction is processed
Then the payment should be declined
And an "expired_card" error should be returned

Scenario: Payment transaction with fraudulent activity
Given a customer has initiated a payment for a product
And the payment is flagged as potentially fraudulent
When the payment transaction is processed
Then the payment should be declined
And a "fraudulent_activity" error should be returned
And the transaction should be flagged for review

Scenario: Refunding a payment transaction
Given a payment transaction has been successfully processed
When a refund request is initiated for the transaction
Then the refund should be processed successfully
And the payment status should be updated to "refunded"
And the refunded amount should match the original payment amount

Scenario: Partial refund of a payment transaction
Given a payment transaction has been successfully processed
When a partial refund request is initiated for the transaction
Then the partial refund should be processed successfully
And the payment status should be updated to "partially_refunded"
And the refunded amount should match the requested partial amount

Scenario: Refunding a non-existent transaction
Given a transaction ID that does not exist
When a refund request is initiated for the transaction
Then a "transaction_not_found" error should be returned

Scenario: Handling payment gateway downtime
Given the payment gateway is experiencing downtime
When a payment transaction is processed
Then the transaction should be queued for later processing
And a "payment_gateway_unavailable" error should be returned
And the transaction should be processed once the payment gateway is available

Scenario: Secure storage of payment information
Given a customer has initiated a payment for a product
When the payment transaction is processed
Then the payment information should be securely stored
And sensitive data should be encrypted and protected
And the stored payment information should comply with industry standards (e.g., PCI DSS)

Scenario: Handling concurrent payment transactions
Given multiple customers are initiating payment transactions simultaneously
When the payment transactions are processed
Then the Third-Party Payment Transaction Service should handle the concurrent transactions correctly
And each transaction should be processed independently
And the payment statuses should be updated accurately for each transaction

Scenario: Integration with multiple payment gateways
Given the Third-Party Payment Transaction Service supports multiple payment gateways
When a payment transaction is processed
Then the service should route the transaction to the appropriate payment gateway based on the payment method
And the transaction should be processed successfully
And the payment status should be updated consistently across all integrated payment gateways