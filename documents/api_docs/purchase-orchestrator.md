# Purchase Orchestrator API Documentation

The Purchase Orchestrator API coordinates the end-to-end purchase process, including product availability checks, payment processing, product provisioning, and order management. It provides endpoints for initiating purchases, handling purchase failures, and managing custom business rules.

## Base URL
https://api.example.com/purchase-orchestrator/

## Authentication

All API requests require authentication using a valid JWT (JSON Web Token) obtained from the Authentication Server. Include the JWT in the `Authorization` header of each request.

## Endpoints

### Initiate Purchase

Initiates a purchase for one or more products.

- **URL:** `/purchases`
- **Method:** `POST`
- **Request Body:**
```json
  {
    "customerId": "string",
    "products": [
      {
        "id": "string",
        "quantity": integer
      }
    ],
    "paymentDetails": {
      "method": "string",
      "transactionId": "string"
    },
    "shippingAddress": {
      "name": "string",
      "address": "string",
      "city": "string",
      "country": "string",
      "postalCode": "string"
    }
  }
```
- **Response:**

- **Success:** 201 Created
```json
{
"purchaseId": "string",
"status": "string",
"message": "string"
}
```
- **Error:**

400 Bad Request - Invalid purchase request
500 Internal Server Error - An unexpected error occurred


### Get Purchase Status
Retrieves the status of a purchase.

- **URL:** /purchases/{purchaseId}
- **Method:** GET
- **Path Parameters:**

purchaseId - The ID of the purchase


- **Response:**

- **Success:** 200 OK
```json
{
"purchaseId": "string",
"status": "string",
"products": [
{
"id": "string",
"quantity": integer,
"status": "string"
}
],
"paymentStatus": "string",
"shippingStatus": "string"
}
```
- **Error:**

404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred


### Update Purchase
Updates an existing purchase.

- **URL:** /purchases/{purchaseId}
- **Method:** PUT
- **Path Parameters:**

purchaseId - The ID of the purchase


- **Request Body:**
```json
{
"products": [
{
"id": "string",
"quantity": integer
}
],
"shippingAddress": {
"name": "string",
"address": "string",
"city": "string",
"country": "string",
"postalCode": "string"
}
}
```
- **Response:**

- **Success:** 200 OK
```
{
"purchaseId": "string",
"status": "string",
"message": "string"
}
```
- **Error:**

400 Bad Request - Invalid update request
404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred


### Cancel Purchase
Cancels a purchase.

- **URL:** /purchases/{purchaseId}/cancel
- **Method:** POST
- **Path Parameters:**

purchaseId - The ID of the purchase


- **Response:**

- **Success:** 200 OK
```json
{
"purchaseId": "string",
"status": "string",
"message": "string"
}
```
- **Error:**

404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred


### Apply Custom Business Rules
Applies custom business rules to a purchase.

- **URL:** /purchases/{purchaseId}/apply-rules
- **Method:** POST
- **Path Parameters:**

purchaseId - The ID of the purchase


- **Request Body:**
```json
{
"rules": [
{
"id": "string",
"parameters": {}
}
]
}
```
- **Response:**

- **Success:** 200 OK
```json
{
"purchaseId": "string",
"status": "string",
"message": "string"
}
```
- **Error:**

400 Bad Request - Invalid custom rules
404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred





