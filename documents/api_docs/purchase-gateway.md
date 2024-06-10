# Purchase Gateway API Documentation

The Purchase Gateway API acts as the entry point for customer purchase requests. It validates the customer's JWT, sends product requests to the Purchase Orchestrator, and handles the purchase process.

## Base URL
https://api.example.com/purchase-gateway/

## Authentication

All API requests require authentication using a valid JWT (JSON Web Token) obtained from the Authentication Server. Include the JWT in the `Authorization` header of each request.

## Endpoints

### Initiate Purchase

Initiates a purchase request for one or more products.

- **URL:** `/purchases`
- **Method:** `POST`
- **Request Headers:**
    - `Authorization: Bearer <JWT>`
- **Request Body:**
  ```json
  {
    "products": [
      {
        "id": "string",
        "quantity": integer
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

400 Bad Request - Invalid purchase request
401 Unauthorized - Invalid or missing JWT
429 Too Many Requests - Rate limit exceeded
500 Internal Server Error - An unexpected error occurred
503 Service Unavailable - Purchase Orchestrator or Authentication Server unavailable


### Get Purchase Status
Retrieves the status of a purchase.

- **URL:** /purchases/{purchaseId}
- **Method:** GET
- **Request Headers:**

Authorization: Bearer <JWT>


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
]
}
```
- **Error:**

401 Unauthorized - Invalid or missing JWT
404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred





### Cancel Purchase
Cancels a purchase.

- **URL:** /purchases/{purchaseId}/cancel
- **Method:** POST
- **Request Headers:**

Authorization: Bearer <JWT>


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

401 Unauthorized - Invalid or missing JWT
404 Not Found - Purchase not found
500 Internal Server Error - An unexpected error occurred


## Error Responses
The API may return the following error responses:

400 Bad Request - The request is invalid or missing required parameters.
401 Unauthorized - Authentication failed or missing JWT.
404 Not Found - The requested resource or endpoint does not exist.
429 Too Many Requests - The rate limit has been exceeded.
500 Internal Server Error - An unexpected error occurred on the server.
503 Service Unavailable - The Purchase Orchestrator or Authentication Server is unavailable.