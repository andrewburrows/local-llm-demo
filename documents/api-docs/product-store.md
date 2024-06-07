# Product Store API Documentation

The Product Store API allows storing, retrieving, updating, and deleting provisioned products. It provides endpoints for managing product data and performing various operations on the stored products.

## Base URL
https://api.example.com/product-store/

## Authentication

All API requests require authentication using a valid JWT (JSON Web Token) obtained from the Authentication Server. Include the JWT in the Authorization header of each request.

## Endpoints

### Store a Product
Stores a provisioned product in the Product Store.

- **URL:** /products
- **Method:** POST
- **Request Body:**
```{
"id": "string",
"name": "string",
"description": "string",
"price": number,
"customAttributes": {
"key": "value"
}
}
```

- **Response:**

  - **Success:** 201 Created
    ```{
    "id": "string",
    "name": "string",
    "description": "string",
    "price": number,
    "customAttributes": {
    "key": "value"
    }
    }
    ```

- **Error:**
  - 400 Bad Request - Invalid product data
  - 500 Internal Server Error - An unexpected error occurred

### Retrieve a Product
Retrieves a stored product by its ID.

- **URL:** /products/{productId}
- **Method:** GET
- **Path Parameters:**

  - productId - The ID of the product to retrieve


- **Response:**

  - **Success:** 200 OK
    ```{
    "id": "string",
    "name": "string",
    "description": "string",
    "price": number,
    "customAttributes": {
    "key": "value"
    }
    }
    ```

  - **Error:**

    - 404 Not Found - Product not found
    - 500 Internal Server Error - An unexpected error occurred

### Update a Product
Updates the details of a stored product.

- **URL:** /products/{productId}
- **Method:** PUT
- **Path Parameters:**

  - productId - The ID of the product to update


- **Request Body:**
  ```
  {
  "name": "string",
  "description": "string",
  "price": number,
  "customAttributes": {
    "key": "value"
    }
  }
  ```

- **Response:**

- **Success:** 200 OK
  ```
    {
  "id": "string",
  "name": "string",
  "description": "string",
  "price": number,
  "customAttributes": {
  "key": "value"
  }
  }
  ```
- **Error:**
  - 400 Bad Request - Invalid product data
  - 404 Not Found - Product not found
  - 500 Internal Server Error - An unexpected error occurred

### Delete a Product
Deletes a stored product.

- **URL:** /products/{productId}
- **Method:** DELETE
- **Path Parameters:**
  - productId - The ID of the product to delete

- **Response:**
  - **Success:** 204 No Content
  - **Error:**
    - 404 Not Found - Product not found
    - 500 Internal Server Error - An unexpected error occurred

### Search Products
Searches for products based on specific attribute criteria.

- **URL:** /products/search
- **Method:** GET
  - **Query Parameters:**
  ...
  attribute1 - Value for attribute1
  attribute2 - Value for attribute2
  ...


- **Response:**

- **Success:** 200 OK
  ```
  [
  {
  "id": "string",
  "name": "string",
  "description": "string",
  "price": number,
  "customAttributes": {
  "key": "value"
  }
  }
  ]
  ```
- **Error:**

- 500 Internal Server Error - An unexpected error occurred

### Retrieve Products with Pagination
Retrieves a paginated list of stored products.

- **URL:** /products
- **Method:** GET
- **Query Parameters:**

  page - Page number (default: 1)
  size - Number of products per page (default: 10)


- **Response:**

  - **Success:** 200 OK
    ```
      {
      "content": [
      {
      "id": "string",
      "name": "string",
      "description": "string",
      "price": number,
      "customAttributes": {
      "key": "value"
      }
      }
      ],
      "pageNumber": integer,
      "pageSize": integer,
      "totalElements": integer,
      "totalPages": integer
      }
    ```
  - **Error:**

    - 500 Internal Server Error - An unexpected error occurred