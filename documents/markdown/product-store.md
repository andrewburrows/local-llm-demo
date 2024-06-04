Feature: Product Store

Background:
Given the Product Store is available and properly configured

Scenario: Storing a provisioned product
Given a product has been provisioned successfully
When the product details are sent to the Product Store
Then the product should be stored in the Product Store
And the stored product details should match the provisioned product

Scenario: Retrieving a stored product by ID
Given a product is stored in the Product Store
When a request is made to retrieve the product by its ID
Then the correct product details should be returned

Scenario: Retrieving a non-existent product
Given a product ID that does not exist in the Product Store
When a request is made to retrieve the product by its ID
Then a "product_not_found" error should be returned

Scenario: Updating product details
Given a product is stored in the Product Store
When an update request is made with new product details
Then the product details should be updated in the Product Store
And the updated details should be reflected when retrieving the product

Scenario: Updating a non-existent product
Given a product ID that does not exist in the Product Store
When an update request is made with new product details
Then an "invalid_product_id" error should be returned

Scenario: Storing a product with custom attributes
Given a provisioned product with custom attributes
When the product details are sent to the Product Store
Then the product should be stored in the Product Store
And the stored product should include the custom attributes

Scenario: Searching for products by attribute
Given multiple products are stored in the Product Store
When a search request is made with specific attribute criteria
Then the matching products should be returned

Scenario: Searching for products with no matching attributes
Given multiple products are stored in the Product Store
When a search request is made with attribute criteria that do not match any products
Then an empty result set should be returned

Scenario: Deleting a stored product
Given a product is stored in the Product Store
When a delete request is made for the product
Then the product should be removed from the Product Store
And subsequent retrieval requests for the deleted product should return a "product_not_found" error

Scenario: Handling concurrent product updates
Given a product is stored in the Product Store
When multiple update requests are made concurrently for the same product
Then the Product Store should handle the concurrent updates correctly
And the final stored product details should reflect the latest update

Scenario: Storing products with large data volumes
Given a large number of provisioned products
When the product details are sent to the Product Store
Then all the products should be stored successfully in the Product Store
And the Product Store should maintain acceptable performance and response times

Scenario: Handling data consistency during product updates
Given a product is stored in the Product Store
When an update request is made with partial product details
Then the Product Store should ensure data consistency
And the stored product should contain the updated details while preserving existing data

Scenario: Retrieving products with pagination
Given a large number of products are stored in the Product Store
When a retrieval request is made with pagination parameters
Then the Product Store should return the products in paginated format
And the pagination metadata should be included in the response