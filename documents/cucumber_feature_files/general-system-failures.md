Feature: Error Codes

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_100
And the error response should contain error message Authentication token is missing

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_101
And the error response should contain error message Authentication token has expired

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_102
And the error response should contain error message Authentication token is invalid or malformed

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_103
And the error response should contain error message Authentication credentials are invalid

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_104
And the error response should contain error message User lacks sufficient permissions

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_105
And the error response should contain error message Access denied to the requested resource

Scenario Outline: Authentication Error Codes
Given the user is not authenticated
When the user makes a request to a protected resource
Then the service should return an error response with status code 401
And the error response should contain error code A_106
And the error response should contain error message Authentication rate limit exceeded

Scenario Outline: Authorization Error Codes
Given the user is authenticated
But the user lacks the required permissions
When the user makes a request to a protected resource
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                           |
      | 403    | AZ_100      | User does not have the required permission |
      | 403    | AZ_101           | User's role is invalid for the requested operation |
      | 403    | AZ_102     | User's scope is insufficient for the requested resource |
      | 403    | AZ_103  | Resource owner mismatch for the requested operation |

Scenario Outline: Resource Error Codes
Given the user is authenticated and authorized
When the user makes a request to a resource
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                                 |
      | 400    | R_100     | Invalid request payload or parameters         |
      | 404    | R_101           | Requested resource not found                  |
      | 409    | R_102            | Resource already exists or conflicts with existing data |
      | 422    | R_103 | Unprocessable entity or validation error      |
      | 429    | R_104  | Resource request rate limit exceeded          |

Scenario Outline: Server Error Codes
Given the user is authenticated and authorized
When the user makes a request to a resource
And an internal server error occurs
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                                 |
      | 500    | S_100        | Internal server error occurred                |
      | 502    | S_101           | Bad gateway or upstream server error          |
      | 503    | S_102   | Service temporarily unavailable or undergoing maintenance |
      | 504    | S_103       | Gateway timeout while processing the request  |

Scenario Outline: Integration Error Codes
Given the user is authenticated and authorized
When the user makes a request that requires integration with an external service
And an error occurs during the integration
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                                 |
      | 424    | I_100 | Failed dependency or external service unavailable |
      | 500    | I_101   | Internal error occurred during integration    |
      | 504    | I_102          | Timeout occurred while waiting for the external service |

Scenario Outline: Validation Error Codes
Given the user is authenticated and authorized
When the user makes a request with invalid data
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                                 |
      | 400    | V_100 | Invalid parameter value provided              |
      | 400    | V_101     | Required field is missing in the request      |
      | 400    | V_102   | Field format mismatch or invalid data type    |
      | 400    | V_103    | Field value exceeds the allowed range         |

Scenario Outline: Custom Error Codes
Given the user is authenticated and authorized
When the user makes a request that triggers a custom error condition
Then the service should return an error response with status code <status>
And the error response should contain error code <error_code>
And the error response should contain error message <error_message>
    Examples:
      | status | error_code                   | error_message                                 |
      | 400    | C_100 | Account is in an invalid state for the operation |
      | 400    | C_101  | Insufficient balance to perform the transaction |
      | 403    | C_102       | User's age does not meet the required threshold |
      | 403    | C_103   | User's location is restricted for the requested operation |
      | 409    | C_104  | Duplicate submission detected for the request |
      | 429    | C_105        | User has exceeded their allocated quota       |