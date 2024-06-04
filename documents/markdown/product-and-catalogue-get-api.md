Created by Smith, Christopher (Senior Engineering Manager), last modified on May 30, 2024
Overview
The get products and catalogue interface will retrieve all available products available in a territory

Example Request
HTTP/1.1 GET /availableProducts
Accept: application/vnd.availableProducts.v1+json
Authorization: Basic ajkdhiu93406uiyaehr
X-TraceId: f81d4fae-7dec-11d0-a765-00a0c91e6bf6
X-Territory: GB


Household id in this case is the OTT household Id (not the DTH household id) - so the value will be either Party id (for DTH propositions) or profile id for Non-DTH propositions.



Field Descriptions


Attribute	Mandatory	Description
Security Headers
Authorization	Y	Basic auth credentials
Versioning Headers
Accept	Y
See version header

Monitoring Headers

X-Territory	Y
the territory of the user

X-TraceId	N
used for request tracing in log



Success Response
HTTP/1.1 200 OK
X-TraceId: f81d4fae-7dec-11d0-a765-00a0c91e6bf6

Content-Type: vnd.availableProducts.v1+json
{
"products": [
{
"name": "Alpha",
"productId":"abc"
"priceInGBP":3,
"duration":"1M"
"voucherAvailability":"true"
},
{
"name": "Beta",
"productId":"def"
"priceInGBP":4,
"duration":"1W"
"voucherAvailability":"false"
}

}
Success Response (no available products)
HTTP/1.1 200 OK
X-TraceId: f81d4fae-7dec-11d0-a765-00a0c91e6bf6

Content-Type: vnd.availableProducts.v1+json
{
"products": []
}
Please note that the products returned by this API are NOT ordered.





Error Response
HTTP/1.1 403 FORBIDDEN
Content-Type: application/json
{
"errorCode": "cat_00001",
"description": "Security failure"
}
HTTP Status	Error Code	Error Message	Description
Request Validations cat_000xx)
400	cat_00001	Missing mandatory attribute: <attribute>	Mandatory attribute is whitespace/null/empty/missing
Security Failures (cat_003xx)
403	cat_00306	Security Failure	Security failure due to bad credentials, etc
System Failures (cat_001xx)
500	cat_00100	Unexpected Error	Uncaught exception occurred
500	cat_00102	Downstream System Failure: {system}
e.g. db down