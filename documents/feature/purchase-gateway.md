Feature: Purchase Gateway

Background:
Given the Purchase Gateway is available and properly configured
And the required services are integrated and accessible

Scenario: Successful purchase with valid JWT
Given a customer has a valid JWT
And the customer has selected a product to purchase
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the Purchase Gateway should send a product request to the Purchase Orchestrator
And the customer should receive a success response

Scenario: Purchase attempt with invalid JWT
Given a customer has an invalid JWT
And the customer has selected a product to purchase
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the JWT validation should fail
And the customer should receive an "invalid_token" error response

Scenario: Purchase attempt with expired JWT
Given a customer has an expired JWT
And the customer has selected a product to purchase
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the JWT validation should fail
And the customer should receive an "expired_token" error response

Scenario: Purchase attempt without JWT
Given a customer has not provided a JWT
And the customer has selected a product to purchase
When the customer initiates a purchase request
Then the Purchase Gateway should reject the request
And the customer should receive a "missing_token" error response

Scenario: Purchase Orchestrator unavailable
Given a customer has a valid JWT
And the customer has selected a product to purchase
And the Purchase Orchestrator is unavailable
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the Purchase Gateway should attempt to send a product request to the Purchase Orchestrator
And the Purchase Gateway should handle the Purchase Orchestrator unavailability gracefully
And the customer should receive a "service_unavailable" error response

Scenario: Authentication Server unavailable
Given a customer has a valid JWT
And the customer has selected a product to purchase
And the Authentication Server is unavailable
When the customer initiates a purchase request
Then the Purchase Gateway should attempt to validate the JWT with the Authentication Server
And the Purchase Gateway should handle the Authentication Server unavailability gracefully
And the customer should receive a "service_unavailable" error response

Scenario: Invalid product request
Given a customer has a valid JWT
And the customer has selected an invalid product
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the Purchase Gateway should send a product request to the Purchase Orchestrator
And the Purchase Orchestrator should reject the invalid product request
And the customer should receive an "invalid_product" error response

Scenario: Successful purchase with multiple products
Given a customer has a valid JWT
And the customer has selected multiple products to purchase
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the Purchase Gateway should send a product request to the Purchase Orchestrator
And the Purchase Orchestrator should process the purchase for all selected products
And the customer should receive a success response

Scenario: Purchase Gateway rate limiting
Given a customer has a valid JWT
And the customer has exceeded the rate limit for purchase requests
When the customer initiates a purchase request
Then the Purchase Gateway should reject the request
And the customer should receive a "rate_limit_exceeded" error response

Scenario: Purchase Gateway circuit breaker
Given a customer has a valid JWT
And the Purchase Orchestrator is experiencing high failure rates
And the circuit breaker is open
When the customer initiates a purchase request
Then the Purchase Gateway should validate the JWT with the Authentication Server
And the Purchase Gateway should immediately reject the request due to the open circuit breaker
And the customer should receive a "service_unavailable" error response