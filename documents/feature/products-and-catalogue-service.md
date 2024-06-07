Feature: Products and Catalogue Service

Background:
Given the Products and Catalogue Service is available and properly configured

Scenario: Retrieve product details by ID
Given a product with ID "ABC123" exists in the catalogue
When a request is made to retrieve the product details by ID "ABC123"
Then the product details should be returned
And the response should include the product name, description, price, and availability

Scenario: Retrieve product details by non-existent ID
Given a product with ID "XYZ789" does not exist in the catalogue
When a request is made to retrieve the product details by ID "XYZ789"
Then a "product_not_found" error should be returned

Scenario: Search products by keyword
Given the catalogue contains products with names "Apple iPhone", "Samsung Galaxy", and "Google Pixel"
When a search request is made with the keyword "phone"
Then the search results should include products "Apple iPhone", "Samsung Galaxy", and "Google Pixel"
And the response should include the product details for each matching product

Scenario: Search products by category
Given the catalogue has categories "Electronics", "Clothing", and "Home Appliances"
And each category has associated products
When a search request is made for products in the "Electronics" category
Then the search results should include only products belonging to the "Electronics" category
And the response should include the product details for each matching product

Scenario: Filter products by price range
Given the catalogue contains products with various prices
When a search request is made with a price range filter of $100 to $500
Then the search results should include only products within the specified price range
And the response should include the product details for each matching product

Scenario: Sort products by price
Given the catalogue contains products with different prices
When a search request is made with a sort option of "price" in ascending order
Then the search results should be sorted by price in ascending order
And the response should include the product details for each matching product

Scenario: Update product details
Given a product with ID "DEF456" exists in the catalogue
When an update request is made to modify the price and availability of product "DEF456"
Then the product details should be updated in the catalogue
And the response should indicate a successful update
And subsequent retrieve requests for product "DEF456" should return the updated details

Scenario: Update non-existent product
Given a product with ID "MNO012" does not exist in the catalogue
When an update request is made to modify the price and availability of product "MNO012"
Then a "product_not_found" error should be returned

Scenario: Add a new product to the catalogue
Given a new product with valid details is provided
When a request is made to add the new product to the catalogue
Then the new product should be added to the catalogue
And the response should include the newly assigned product ID
And subsequent retrieve requests for the new product ID should return the product details

Scenario: Add a product with missing mandatory fields
Given a new product with missing mandatory fields is provided
When a request is made to add the new product to the catalogue
Then a "missing_mandatory_fields" error should be returned
And the product should not be added to the catalogue

Scenario: Delete a product from the catalogue
Given a product with ID "PQR789" exists in the catalogue
When a request is made to delete product "PQR789" from the catalogue
Then the product should be removed from the catalogue
And the response should indicate a successful deletion
And subsequent retrieve requests for product "PQR789" should return a "product_not_found" error

Scenario: Delete a non-existent product
Given a product with ID "STU456" does not exist in the catalogue
When a request is made to delete product "STU456" from the catalogue
Then a "product_not_found" error should be returned

Scenario: Retrieve product details with caching
Given a product with ID "XYZ123" exists in the catalogue
And the product details are cached in the system
When a request is made to retrieve the product details by ID "XYZ123"
Then the cached product details should be returned
And the response time should be faster compared to a non-cached retrieval

Scenario: Update product details with caching invalidation
Given a product with ID "MNO789" exists in the catalogue
And the product details are cached in the system
When an update request is made to modify the price and availability of product "MNO789"
Then the product details should be updated in the catalogue
And the cache should be invalidated for product "MNO789"
And subsequent retrieve requests for product "MNO789" should return the updated details