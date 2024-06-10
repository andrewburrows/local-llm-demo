

The Device uses a webui that calls the product and catalogue service to obtain the available products.
The product and catalogue service receives the REST request from the device, checks the database using a filter and then
returns the relevant products back to the device.

The webui on the Device then allows the user to purchase shown products, when the user initiates a purchase
then a REST request is sent to the purchase gateway service.

The purchase gateway service first validates the user's JWT by sending it to the authentication server.

If the JWT is valid that then purchase gateway service will submit the request product to the purchase orchestrator service.

The purchase orchestrator will route the payment request to the third party payment transaction service.
The third party payment transaction service will then initiate the actual payment and return back to the
purchase orchestrator about the status of the order.

If the order is successful then the purchase orchestrator will send the product request to the product provisioner service.
The product provisioner will then send a request to the product store to check the product's availability and if there
are not enough available inventory will provision the product.
The product store has a database that stores the full list of products along with the amount stored in the warehouse.
