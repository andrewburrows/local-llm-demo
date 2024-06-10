Feature: Client User Journeys

Scenario: Acme Corporation User Journey
Given the user is an Acme Corporation customer
And the user has the role "acme_buyer"
And the user has the permission "view_acme_products"
When the user logs in to the Acme Corporation application
Then the user should be authenticated successfully
And the user should receive a JWT with the claim "client_id" set to "acme_corp"
And the user should be able to view Acme Corporation products
And the user should not be able to manage Acme Corporation products

Scenario: Globex Industries User Journey
Given the user is a Globex Industries employee
And the user has the access level "globex_level2"
And the user belongs to the department with ID "globex_sales"
When the user logs in to the Globex Industries internal application using SSO
Then the user should be authenticated successfully
And the user should receive a JWT with the claim "client_id" set to "globex_ind"
And the user should have access to resources based on their access level and department
And the user's activities should be logged for compliance and security monitoring

Scenario: Initech LLC User Journey
Given the user is an Initech LLC customer
And the user has the role "initech_project_manager"
And the user has the permission "create_initech_project"
And the user has the subscription tier "initech_premium"
When the user registers for an account on the Initech LLC application
And the user logs in to the Initech LLC application using MFA
Then the user should be authenticated successfully
And the user should receive a JWT with the claim "client_id" set to "initech"
And the user should be able to create and manage Initech projects
And the user's requests should be subject to rate limiting and validation

Scenario: Umbrella Corporation User Journey
Given the user is an Umbrella Corporation researcher
And the user has the role "umbrella_researcher"
And the user has the permission "access_umbrella_lab"
And the user is associated with the project ID "umbrella_project_x"
When the user logs in to the Umbrella Corporation research platform using the custom authentication plugin
Then the user should be authenticated successfully
And the user should receive a JWT with the claim "client_id" set to "umbrella_corp"
And the user should have access to the research platform based on their role and project association
And the user's sensitive research data should be encrypted and protected

Scenario: Stark Industries User Journey
Given the user is a Stark Industries customer
And the user has the role "stark_homeowner"
And the user has the permission "control_stark_devices"
When the user authenticates using the Stark Industries IoT device authorization flow
Then the user should be authenticated successfully
And the user's device should receive an access token
And the user should be able to control their Stark Industries smart home devices
And the user should receive real-time notifications related to device events

Scenario: Cyberdyne Systems User Journey
Given the user is a Cyberdyne Systems engineer
And the user has the role "cyberdyne_engineer"
And the user has the permission "train_cyberdyne_models"
And the user is associated with the AI platform "cyberdyne_skynet"
When the user logs in to the Cyberdyne Systems AI platform using OAuth 2.0 and JWT
Then the user should be authenticated successfully
And the user should receive a JWT with the claim "client_id" set to "cyberdyne"
And the user's access attempts should be monitored for anomalies
And the user should have access to train AI models based on their role and permissions
And the user's sensitive data should be stored using secure key management