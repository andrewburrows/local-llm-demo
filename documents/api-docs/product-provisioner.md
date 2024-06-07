# Product Provisioner API Documentation

The Product Provisioner API allows customers to provision products and manage their inventory. It provides endpoints for provisioning products, checking product availability, and handling customization options.

## Base URL
```
https://api.example.com/product-provisioner/
```
## Authentication
All API requests require authentication using a valid JWT (JSON Web Token) obtained from the Authentication Server. Include the JWT in the Authorization header of each request.

## Endpoints
### Provision a Product
Provisions a product for the customer.
- **URL:** /products
- **Method:** POST
- **Request Body:**
```{
"productId": "string",
"quantity": integer,
"customization": {
"key": "value"
}
}
```
- **Response:**

- **Success:** 200 OK
```{
"message": "Product provisioned successfully",
"provisionedProducts": [
{
"id": "string",
"productId": "string",
"quantity": integer,
"customization": {
"key": "value"
}
}
]
}
```
- **Error:**
  - 400 Bad Request - Invalid product selection or missing customization details
  - 404 Not Found - Product not found
  - 409 Conflict - Product not available in the inventory or quota exceeded
  - 500 Internal Server Error - An unexpected error occurred

### Check Product Availability
Checks the availability of a product in the inventory.

- **URL:** /products/{productId}/availability
- **Method:** GET
- **Path Parameters:**

productId - The ID of the product to check availability for


- **Response:**

- **Success:** 200 OK
```json
{
"productId": "string",
"available": boolean,
"quantity": integer
}
```
- **Error:**
  - 404 Not Found - Product not found
  - 500 Internal Server Error - An unexpected error occurred

### Get Provisioned Products
Retrieves the list of provisioned products for the customer.

- **URL:** /provisioned-products
- **Method:** GET
- **Response:**
- **Success:** 200 OK
```
[
    {
        "id": "string",
        "productId": "string",
        "quantity": integer,
        "customization": {
            "key": "value"
            }
    }
]
```
- **Error:**
  - 500 Internal Server Error - An unexpected error occurred

## Error Responses
The API may return the following error responses:

- 400 Bad Request - The request is invalid or missing required parameters.
- 401 Unauthorized - Authentication failed or missing JWT.
- 404 Not Found - The requested resource or endpoint does not exist.
- 409 Conflict - The requested operation conflicts with the current state of the resource.
- 500 Internal Server Error - An unexpected error occurred on the server.