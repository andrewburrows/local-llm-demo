Feature: Content Access Permissions

Background:
Given the customer has an active subscription
And the customer is authenticated

Scenario Outline: Customer with <role> role can access <content>
Given the customer has the role "<role>"
When the customer requests access to "<content>"
Then the customer should be granted access
Examples:
| role        | content         |
| standard    | basic_content   |
| premium     | premium_content |
| trial       | trial_content   |

Scenario Outline: Customer with <role> role cannot access <content>
Given the customer has the role "<role>"  
When the customer requests access to "<content>"
Then the customer should be denied access
And an "access_denied" error message should be returned
Examples:
| role     | content         |
| standard | premium_content |  
| trial    | premium_content |
| expired  | basic_content   |

Scenario: Unauthenticated customer cannot access any content
Given the customer is not authenticated
When the customer requests access to any content
Then the customer should be denied access
And an "authentication_required" error message should be returned

Scenario: Customer with no active subscription cannot access any content
Given the customer does not have an active subscription
When the customer requests access to any content
Then the customer should be denied access
And a "subscription_required" error message should be returned


