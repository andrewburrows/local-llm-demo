# Third-Party Payment Transaction Service API Documentation

The Third-Party Payment Transaction Service API allows processing of payment transactions, including authorization, refunds, and secure storage of payment information. It provides endpoints for initiating payments, handling refunds, and managing payment transactions.

## Base URL
https://api.example.com/payment-transaction/

## Authentication

All API requests require authentication using a valid API key. Include the API key in the `Authorization` header of each request.

## Endpoints

### Process Payment

Processes a payment transaction.

- **URL:** `/payments`
- **Method:** `POST`
- **Request Body:**
```json
  {
    "transactionId": "string",
    "amount": number,
    "currency": "string",
    "paymentMethod": {
      "type": "string",
      "cardNumber": "string",
      "expiryMonth": "string",
      "expiryYear": "string",
      "cvv": "string"
    },
    "billingDetails": {
      "name": "string",
      "email": "string",
      "phone": "string",
      "address": {
        "line1": "string",
        "line2": "string",
        "city": "string",
        "state": "string",
        "country": "string",
        "postalCode": "string"
      }
    }
  }
```
- **Response:**

- **Success:** 200 OK
```json
{
"transactionId": "string",
"status": "string",
"authorizationCode": "string"
}
```
- **Error:**

400 Bad Request - Invalid payment request
401 Unauthorized - Invalid API key
500 Internal Server Error - An unexpected error occurred





### Refund Payment
Processes a refund for a payment transaction.

- **URL:** /payments/{transactionId}/refund
- **Method:** POST
- **Path Parameters:**

transactionId - The ID of the payment transaction to refund


- **Request Body:**
```json
{
"amount": number,
"reason": "string"
}
```
- **Response:**

- **Success:** 200 OK
```json
{
"transactionId": "string",
"refundId": "string",
"status": "string"
}
```
- **Error:**

400 Bad Request - Invalid refund request
401 Unauthorized - Invalid API key
404 Not Found - Transaction not found
500 Internal Server Error - An unexpected error occurred





### Get Payment Status
Retrieves the status of a payment transaction.

- **URL:** /payments/{transactionId}
- **Method:** GET
- **Path Parameters:**

transactionId - The ID of the payment transaction


- **Response:**

- **Success:** 200 OK
```json
{
"transactionId": "string",
"status": "string",
"amount": number,
"currency": "string",
"paymentMethod": {
"type": "string",
"lastFourDigits": "string"
},
"billingDetails": {
"name": "string",
"email": "string",
"phone": "string",
"address": {
"line1": "string",
"line2": "string",
"city": "string",
"state": "string",
"country": "string",
"postalCode": "string"
}
}
}
```
- **Error:**

401 Unauthorized - Invalid API key
404 Not Found - Transaction not found
500 Internal Server Error - An unexpected error occurred





### Void Payment
Voids a payment transaction.

- **URL:** /payments/{transactionId}/void
- **Method:** POST
- **Path Parameters:**

transactionId - The ID of the payment transaction to void


- **Response:**

- **Success:** 200 OK
```json
{
"transactionId": "string",
"status": "string"
}
```
- **Error:**

400 Bad Request - Invalid void request
401 Unauthorized - Invalid API key
404 Not Found - Transaction not found
500 Internal Server Error - An unexpected error occurred





### Webhooks
The Third-Party Payment Transaction Service can send webhooks to notify your application about payment events. To receive webhooks, you need to configure the webhook URL in your account settings.
Payment Processed
Triggered when a payment transaction is processed.

- **Event Type:** payment.processed
- **Webhook Payload:**
```json
{
"transactionId": "string",
"status": "string",
"amount": number,
"currency": "string",
"paymentMethod": {
"type": "string",
"lastFourDigits": "string"
},
"billingDetails": {
"name": "string",
"email": "string",
"phone": "string",
"address": {
"line1": "string",
"line2": "string",
"city": "string",
"state": "string",
"country": "string",
"postalCode": "string"
}
}
}
```

### Payment Refunded
Triggered when a payment transaction is refunded.

- **Event Type:** payment.refunded
- **Webhook Payload:**
```json
{
"transactionId": "string",
"refundId": "string",
"status": "string",
"amount": number,
"currency": "string"
}
```