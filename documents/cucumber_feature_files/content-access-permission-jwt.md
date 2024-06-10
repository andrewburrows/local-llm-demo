Feature: Advanced Content Access Permissions

Background:
Given the customer has an active subscription
And the customer is authenticated with a valid JWT token

Scenario: Customer access based on JWT claims and feature flags
Given the customer's JWT token contains the following claims:
| claim    | value      |
| userId   | 123        |
| roles    | manager    |
| country  | GB         |
And the feature flag "premium_content" is enabled for the customer's userId
And the feature flag "experimental_feature" is disabled globally
When the customer requests access to "premium_content"
Then the access should be granted based on the JWT roles claim and feature flag

Scenario Outline: Customer access based on role graph
Given the role graph is defined as:
"""
admin:
- editor
- viewer
editor:
- reviewer
- contributor  
viewer:
- reader
- guest
"""
And the customer has the role "<role>"
When the customer requests access to "<content>"
Then the access should be "<access>" based on the role graph
Examples:
| role        | content           | access    |
| admin       | restricted_area   | granted   |
| editor      | drafts            | granted   |
| viewer      | published_content | granted   |
| contributor | restricted_area   | denied    |
| guest       | drafts            | denied    |

Scenario: Access denied if JWT is missing required claims
Given the customer's JWT token is missing the "roles" claim
When the customer requests access to any content
Then the access should be denied
And an "invalid_token" error message should be returned

Scenario: Access denied if JWT has expired
Given the customer's JWT token has expired
When the customer requests access to any content
Then the access should be denied
And a "token_expired" error message should be returned

Scenario: Access denied if required feature flag is disabled
Given the feature flag "beta_feature" is disabled
When the customer requests access to "beta_feature"
Then the access should be denied
And a "feature_not_available" error message should be returned