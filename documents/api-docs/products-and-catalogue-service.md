# Products and Catalogue Service API Documentation

The Products and Catalogue Service API allows retrieval, search, and management of product information in the catalogue. It provides endpoints for retrieving product details, searching products by various criteria, updating product information, and managing the product catalogue.

## Base URL
https://api.example.com/products-catalogue/

## Authentication

All API requests require authentication using a valid JWT (JSON Web Token) obtained from the Authentication Server. Include the JWT in the `Authorization` header of each request.

## Endpoints

### Retrieve Product Details

Retrieves the details of a product by its ID.

- **URL:** `/products/{productId}`
- **Method:** `GET`
- **Path Parameters:**
    - `productId` - The ID of the product to retrieve
- **Response:**
    - **Success:** `200 OK`
      ```json
      {
        "id": "string",
        "name": "string",
        "description": "string",
        "price": number,
        "availability": boolean
      }
      ```
    - **Error:**
        - `404 Not Found` - Product not found
        - `500 Internal Server Error` - An unexpected error occurred

### Search Products

Searches for products based on various criteria such as keyword, category, and price range.

- **URL:** `/products/search`
- **Method:** `GET`
- **Query Parameters:**
    - `keyword` - Keyword to search for in product names and descriptions
    - `category` - Category to filter products by
    - `minPrice` - Minimum price of products to include in the search results
    - `maxPrice` - Maximum price of products to include in the search results
    - `sort` - Sorting option for the search results (e.g., `price:asc`, `price:desc`)
- **Response:**
    - **Success:** `200 OK`
      ```json
      [
        {
          "id": "string",
          "name": "string",
          "description": "string",
          "price": number,
          "availability": boolean
        }
      ]
      ```
    - **Error:**
        - `400 Bad Request` - Invalid search parameters
        - `500 Internal Server Error` - An unexpected error occurred

### Update Product Details

Updates the details of a product in the catalogue.

- **URL:** `/products/{productId}`
- **Method:** `PUT`
- **Path Parameters:**
    - `productId` - The ID of the product to update
- **Request Body:**
  ```json
  {
    "name": "string",
    "description": "string",
    "price": number,
    "availability": boolean
  }
  ```
- **Response:**

  - **Success:** `200 OK`
      ```json
      {
      "id": "string",
      "name": "string",
      "description": "string",
      "price": number,
      "availability": boolean
      }
      ```
  - **Error:**
    - 400 Bad Request - Invalid update parameters
    - 404 Not Found - Product not found
    - 500 Internal Server Error - An unexpected error occurred

### Add Product

Adds a new product to the catalogue.

- **URL:** /products
- **Method:** POST
- **Request Body:**
  ```json
    {
    "name": "string",
    "description": "string",
    "price": number,
    "availability": boolean
    }
  ```
- **Response:**

  - **Success:** 201 Created
      ```json
        {
        "id": "string",
        "name": "string",
        "description": "string",
        "price": number,
        "availability": boolean
        }
      ```

  - **Error:**
    - 400 Bad Request - Missing mandatory fields or invalid product data
    - 500 Internal Server Error - An unexpected error occurred

### Delete Product

Deletes a product from the catalogue.

- **URL:** /products/{productId}
- **Method:** DELETE
- **Path Parameters:**
  - productId - The ID of the product to delete
- **Response:**
  - **Success:** 204 No Content
  - **Error:**
    - 404 Not Found - Product not found
    - 500 Internal Server Error - An unexpected error occurred