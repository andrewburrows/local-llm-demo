Feature: Get Available Products API

Background:
Given the API endpoint is "GET /availableProducts"
And the Accept header is set to "application/vnd.availableProducts.v1+json"
And the Authorization header is set to "Basic ajkdhiu93406uiyaehr"

Scenario Outline: Validate missing mandatory attributes
Given the X-Territory header is set to "<territory>"
And the X-TraceId header is set to "<traceId>"
When a request is sent to the available products API
Then the response status code should be 400
And the response body should contain error code "cat_00001"
And the response body should contain error message "Missing mandatory attribute: <attribute>"

    Examples:
      | territory | traceId                           | attribute         |
      | ""        | f81d4fae-7dec-11d0-a765-00a0c91e6bf6 | X-Territory       |
      | GB        |                                   | X-TraceId         |

Scenario Outline: Validate incorrect Authorization header
Given the X-Territory header is set to "GB"
And the X-TraceId header is set to "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
And the Authorization header is set to "<authHeader>"
When a request is sent to the available products API
Then the response status code should be 403
And the response body should contain error code "cat_00306"
And the response body should contain error message "Security Failure"

    Examples:
      | authHeader                |
      | "Basic invalidtoken"      |
      | ""                        |

Scenario: Validate system failure (unexpected error)
Given the X-Territory header is set to "GB"
And the X-TraceId header is set to "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
When a request is sent to the available products API
Then the response status code should be 500
And the response body should contain error code "cat_00100"
And the response body should contain error message "Unexpected Error"

Scenario: Validate downstream system failure
Given the X-Territory header is set to "GB"
And the X-TraceId header is set to "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
When a request is sent to the available products API
Then the response status code should be 500
And the response body should contain error code "cat_00102"
And the response body should contain error message "Downstream System Failure: db down"

Scenario: Validate successful response with available products
Given the X-Territory header is set to "GB"
And the X-TraceId header is set to "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
When a request is sent to the available products API
Then the response status code should be 200
And the response body should contain a list of products

Scenario: Validate successful response with no available products
Given the X-Territory header is set to "GB"
And the X-TraceId header is set to "f81d4fae-7dec-11d0-a765-00a0c91e6bf6"
When a request is sent to the available products API
Then the response status code should be 200
And the response body should contain an empty list of products