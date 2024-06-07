High Level Architecture of PPS (Product Purchaser Solution)

Products and Catalogue Service:
The Products and Catalogue Service serves as the central repository for managing and retrieving product information 
and the overall product catalogue. This service is responsible for storing and organizing product details, such as product names, 
descriptions, pricing, and availability. It exposes a set of RESTful APIs that allow other services and applications 
to retrieve product data efficiently.

The Products and Catalogue Service is built using a microservices architecture, ensuring scalability and flexibility. 
It utilizes a distributed database, such as Apache Cassandra or MongoDB, to handle large amounts of product data and 
provide high availability. The service implements caching mechanisms, like Redis, to improve performance and reduce 
the load on the database. It also incorporates advanced search and filtering capabilities using technologies like 
Elasticsearch, enabling users to quickly find desired products based on various criteria.

The user's Device connects directly to the products and catalogue Service using a React web frontend.
The product and catalogue service receives the REST request from the device, checks the database using a filter and then
returns the relevant products back to the device.
The webui on the Device then allows the user to purchase shown products, when the user initiates a purchase
then a REST request is sent to the purchase gateway service.


Purchase Gateway:
The Purchase Gateway has an API that allows the user to make a purchase of a selected product from the Products and
Catalogue Service. The user must provide a valid JWT.
The Purchase Gateway validates the user's JWT by sending it to the authentication server.
If the validation is successful then a product request is made to the Purchase Orchestrator.


Authentication Server (JWT):
The Authentication Server is responsible for handling user authentication and generating JSON Web Tokens (JWTs) for authenticated users. 
It plays a crucial role in securing the system and ensuring that only authorized users can access protected resources. 
When a user logs in, the Authentication Server validates their credentials against the user database and, upon successful 
authentication, generates a JWT containing relevant user information and access privileges.

The Authentication Server is designed to be highly secure and scalable. It employs industry-standard encryption algorithms, 
such as HMAC or RSA, to sign the JWTs, ensuring their integrity and preventing tampering. The server may integrate with 
external identity providers, such as OAuth or SAML, to support single sign-on (SSO) and facilitate seamless authentication 
across multiple systems. Additionally, the Authentication Server implements rate limiting and security measures to protect 
against brute-force attacks and unauthorized access attempts.


Product Provisioner:
The Product Provisioner is a critical component that handles the provisioning and management of products for customers. 
When a customer requests a product, the Product Provisioner receives the request, validates it against the product catalogue, 
and initiates the provisioning process. It communicates with various downstream systems, such as inventory management 
and order fulfillment, to ensure that the requested product is available and can be delivered to the customer.

The Product Provisioner is designed to handle complex provisioning workflows and support a wide range of product types. 
It utilizes a workflow engine, such as Apache Airflow or Camunda, to define and execute provisioning processes. 
The provisioner integrates with external systems through APIs or message queues to exchange data and trigger required 
actions. It also incorporates error handling and retry mechanisms to handle failures gracefully and ensure reliable 
provisioning. Additionally, the Product Provisioner may include features like provisioning templates, customization options, 
and real-time status tracking to enhance the provisioning experience.


Purchase Orchestrator:
The Purchase Orchestrator is a service responsible for coordinating the end-to-end purchase process for customers. It
acts as a central hub that orchestrates the interactions between various components involved in a purchase, such as the
Third Party Payment Transaction Service and the Product Provisioner.
The Purchase Orchestrator receives purchase requests from the Purchase Gateway, validates them, and triggers the necessary 
steps to complete the purchase.

The Purchase Orchestrator is designed to handle complex purchase workflows and ensure a seamless customer experience.
It utilizes a state machine or workflow engine to define and manage the purchase process, allowing for flexibility and
extensibility. The orchestrator communicates with other services through well-defined APIs or event-driven architectures,
such as message queues or event buses. It incorporates error handling, compensating transactions, and retry mechanisms
to maintain data consistency and handle failures gracefully. Additionally, the Purchase Orchestrator may include features
like purchase tracking, order status updates, and integration with customer communication channels to keep customers
informed throughout the purchase journey.

The Purchase Orchestrator sends a request payment to the Third Party Payment Transaction service and if successful will
send the product request to the Product Provisioner.


Third-Party Payment Transaction Service:
The Third-Party Payment Transaction Service is an external service that handles the processing of financial transactions
for product purchases. It securely integrates with the system to facilitate the transfer of funds from customers to the business.
The service supports various payment methods, such as credit cards, debit cards, digital wallets, and bank transfers,
providing flexibility and convenience to customers.

The Third-Party Payment Transaction Service is responsible for ensuring the security and compliance of financial transactions.
It implements industry-standard security measures, such as encryption, tokenization, and secure communication protocols,
to protect sensitive payment information. The service complies with relevant regulations and standards,
such as PCI DSS (Payment Card Industry Data Security Standard), to maintain the integrity and confidentiality of customer
payment data. It also incorporates fraud detection and prevention mechanisms to identify and mitigate potential fraudulent
activities. The Third-Party Payment Transaction Service provides APIs or SDKs that allow seamless integration with the system,
enabling smooth and secure payment processing.


Product Provisioner:
The Product Provisioner is responsible for checking the inventory and stock of products. It will send an alert if inventory
is running low on a product.
The Product Provisioner also hosts an API that is used by the Purchase Orchestrator to update the inventory for the product.
If the product is available then it will submit a rquest to 
The Product Provisioner will periodically check its inventory and if its running low on a stock for the item then it will
automatically make an external request to update its inventory.
The Product Provisioner is able to query it's stock by calling the Product Store.


Product Store:
The Product Store is the central service that stores information about provisioned products and their associated metadata
in a cassandra database.
The Product Store provides an API that allows users access to the database whilst performing verification, validation and
retrieval.
It acts as a persistent storage layer for the entire system, capturing details such as product instances, configurations, 
and customer-specific customizations. The Product Store is designed to handle a large volume of data and provide efficient 
querying and retrieval capabilities.

The Product Store employs a scalable and distributed database architecture using Apache Cassandra  to ensure high availability 
and performance. It organizes data in a denormalized manner, optimizing for read-heavy workloads and minimizing the need for 
complex joins. The store may incorporate indexing and partitioning techniques to enable fast lookups based on various attributes. 
Additionally, the Product Store implements data consistency mechanisms, such as eventual consistency or strong consistency, 
depending on the specific requirements of the system. It also includes backup and disaster recovery procedures to protect 
against data loss and ensure business continuity.



Authentication Database:
The Authentication Database is a secure storage system that holds user credentials and authentication-related information. 
It is tightly coupled with the Authentication Server and serves as the primary data source for user authentication and 
authorization. The database stores user accounts, passwords (hashed and salted), roles, permissions, and other relevant 
attributes.

The Authentication Database is designed with security as a top priority. It employs strong encryption techniques to protect 
sensitive user data at rest and in transit. The database may utilize specialized security features, such as hardware security 
\modules (HSMs) or encrypted filesystems, to provide an additional layer of protection. Access to the Authentication Database 
is strictly controlled and audited, with only the Authentication Server having direct access. Regular security audits and 
penetration testing are conducted to identify and mitigate any potential vulnerabilities.



