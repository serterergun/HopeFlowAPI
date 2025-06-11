# API Endpoints Documentation

This document lists all the endpoints available in our API, including payloads and return values.

## Base URL
All endpoints are prefixed with `/api/v1`.

## Authentication
- **Endpoint**: `/api/v1/auth/token`
- **Method**: `POST`
- **Payload**: `{ "email": "string", "password": "string" }`

## User Endpoints
- **Endpoint**: `/api/v1/users`
- **Method**: `GET`
- **Return**: `[{ "id": "integer", "first_name": "string", "last_name": "string", "email": "string"}]`

- **Endpoint**: `/api/v1/users/{user_id}`
- **Method**: `GET`
- **Return**: `{ "id": "integer", "first_name": "string", "last_name": "string", "email": "string"}`

- **Endpoint**: `/api/v1/users`
- **Method**: `POST`
- **Payload**: `{ "first_name": "string", "last_name": "string", "email": "string", "password": "string" }`
- **Return**: `{ "id": "integer", "first_name": "string", "last_name": "string", "email": "string"}`

- **Endpoint**: `/api/v1/users/{user_id}`
- **Method**: `PUT`
- **Return**: `{ "id": "integer", "first_name": "string", "last_name": "string", "email": "string"}`

## Company Endpoints
- **GET /companies**: Retrieve a list of companies.
  - **Return**: `[{ "id": "integer", "name": "string", "type": "string" }]`
- **GET /companies/{company_id}**: Retrieve a specific company by ID.
  - **Return**: `{ "id": "integer", "name": "string", "type": "string" }`
- **POST /companies**: Create a new company.
  - **Payload**: `{ "name": "string", "type": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "type": "string" }`
- **PUT /companies/{company_id}**: Update a company by ID.
  - **Payload**: `{ "name": "string", "type": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "type": "string" }`
- **DELETE /companies/{company_id}**: Delete a company by ID.
  - **Return**: `204 No Content`

## Request Endpoints
- **GET /requests**: Retrieve a list of requests.
  - **Return**: `[{ "id": "integer", "title": "string", "description": "string", "status": "string" }]`
- **GET /requests/{request_id}**: Retrieve a specific request by ID.
  - **Return**: `{ "id": "integer", "title": "string", "description": "string", "status": "string" }`
- **POST /requests**: Create a new request.
  - **Payload**: `{ "title": "string", "description": "string" }`
  - **Return**: `{ "id": "integer", "title": "string", "description": "string", "status": "string" }`
- **PUT /requests/{request_id}**: Update a request by ID.
  - **Payload**: `{ "title": "string", "description": "string", "status": "string" }`
  - **Return**: `{ "id": "integer", "title": "string", "description": "string", "status": "string" }`
- **DELETE /requests/{request_id}**: Delete a request by ID.
  - **Return**: `204 No Content`

## Request Offer Endpoints
- **GET /request-offers**: Retrieve a list of request offers.
  - **Return**: `[{ "id": "integer", "request_id": "integer", "offer": "string", "status": "string" }]`
- **GET /request-offers/{offer_id}**: Retrieve a specific request offer by ID.
  - **Return**: `{ "id": "integer", "request_id": "integer", "offer": "string", "status": "string" }`
- **POST /request-offers**: Create a new request offer.
  - **Payload**: `{ "request_id": "integer", "offer": "string" }`
  - **Return**: `{ "id": "integer", "request_id": "integer", "offer": "string", "status": "string" }`
- **PUT /request-offers/{offer_id}**: Update a request offer by ID.
  - **Payload**: `{ "offer": "string", "status": "string" }`
  - **Return**: `{ "id": "integer", "request_id": "integer", "offer": "string", "status": "string" }`
- **DELETE /request-offers/{offer_id}**: Delete a request offer by ID.
  - **Return**: `204 No Content`

## Payment Transaction Endpoints
- **GET /payment-transactions**: Retrieve a list of payment transactions.
  - **Return**: `[{ "id": "integer", "amount": "float", "status": "string" }]`
- **GET /payment-transactions/{transaction_id}**: Retrieve a specific payment transaction by ID.
  - **Return**: `{ "id": "integer", "amount": "float", "status": "string" }`
- **POST /payment-transactions**: Create a new payment transaction.
  - **Payload**: `{ "amount": "float" }`
  - **Return**: `{ "id": "integer", "amount": "float", "status": "string" }`
- **PUT /payment-transactions/{transaction_id}**: Update a payment transaction by ID.
  - **Payload**: `{ "status": "string" }`
  - **Return**: `{ "id": "integer", "amount": "float", "status": "string" }`
- **DELETE /payment-transactions/{transaction_id}**: Delete a payment transaction by ID.
  - **Return**: `204 No Content`

## User Type Endpoints
- **GET /user-types**: Retrieve a list of user types.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /user-types/{type_id}**: Retrieve a specific user type by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /user-types**: Create a new user type.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /user-types/{type_id}**: Update a user type by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /user-types/{type_id}**: Delete a user type by ID.
  - **Return**: `204 No Content`

## Company Type Endpoints
- **GET /company-types**: Retrieve a list of company types.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /company-types/{type_id}**: Retrieve a specific company type by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /company-types**: Create a new company type.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /company-types/{type_id}**: Update a company type by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /company-types/{type_id}**: Delete a company type by ID.
  - **Return**: `204 No Content`

## City Endpoints
- **GET /cities**: Retrieve a list of cities.
  - **Return**: `[{ "id": "integer", "name": "string", "country": "string" }]`
- **GET /cities/{city_id}**: Retrieve a specific city by ID.
  - **Return**: `{ "id": "integer", "name": "string", "country": "string" }`
- **POST /cities**: Create a new city.
  - **Payload**: `{ "name": "string", "country": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "country": "string" }`
- **PUT /cities/{city_id}**: Update a city by ID.
  - **Payload**: `{ "name": "string", "country": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "country": "string" }`
- **DELETE /cities/{city_id}**: Delete a city by ID.
  - **Return**: `204 No Content`

## Country Endpoints
- **GET /countries**: Retrieve a list of countries.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /countries/{country_id}**: Retrieve a specific country by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /countries**: Create a new country.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /countries/{country_id}**: Update a country by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /countries/{country_id}**: Delete a country by ID.
  - **Return**: `204 No Content`

## Residency Type Endpoints
- **GET /residency-types**: Retrieve a list of residency types.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /residency-types/{type_id}**: Retrieve a specific residency type by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /residency-types**: Create a new residency type.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /residency-types/{type_id}**: Update a residency type by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /residency-types/{type_id}**: Delete a residency type by ID.
  - **Return**: `204 No Content`

## Activity Type Endpoints
- **GET /activity-types**: Retrieve a list of activity types.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /activity-types/{type_id}**: Retrieve a specific activity type by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /activity-types**: Create a new activity type.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /activity-types/{type_id}**: Update an activity type by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /activity-types/{type_id}**: Delete an activity type by ID.
  - **Return**: `204 No Content`

## User User Type Endpoints
- **GET /user-user-types**: Retrieve a list of user user types.
  - **Return**: `[{ "id": "integer", "user_id": "integer", "type_id": "integer" }]`
- **GET /user-user-types/{type_id}**: Retrieve a specific user user type by ID.
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer" }`
- **POST /user-user-types**: Create a new user user type.
  - **Payload**: `{ "user_id": "integer", "type_id": "integer" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer" }`
- **PUT /user-user-types/{type_id}**: Update a user user type by ID.
  - **Payload**: `{ "user_id": "integer", "type_id": "integer" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer" }`
- **DELETE /user-user-types/{type_id}**: Delete a user user type by ID.
  - **Return**: `204 No Content`

## User Activity Transaction Endpoints
- **GET /user-activity-transactions**: Retrieve a list of user activity transactions.
  - **Return**: `[{ "id": "integer", "user_id": "integer", "activity_id": "integer", "status": "string" }]`
- **GET /user-activity-transactions/{transaction_id}**: Retrieve a specific user activity transaction by ID.
  - **Return**: `{ "id": "integer", "user_id": "integer", "activity_id": "integer", "status": "string" }`
- **POST /user-activity-transactions**: Create a new user activity transaction.
  - **Payload**: `{ "user_id": "integer", "activity_id": "integer" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "activity_id": "integer", "status": "string" }`
- **PUT /user-activity-transactions/{transaction_id}**: Update a user activity transaction by ID.
  - **Payload**: `{ "status": "string" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "activity_id": "integer", "status": "string" }`
- **DELETE /user-activity-transactions/{transaction_id}**: Delete a user activity transaction by ID.
  - **Return**: `204 No Content`

## User Residency Endpoints
- **GET /user-residencies**: Retrieve a list of user residencies.
  - **Return**: `[{ "id": "integer", "user_id": "integer", "residency_id": "integer", "status": "string" }]`
- **GET /user-residencies/{residency_id}**: Retrieve a specific user residency by ID.
  - **Return**: `{ "id": "integer", "user_id": "integer", "residency_id": "integer", "status": "string" }`
- **POST /user-residencies**: Create a new user residency.
  - **Payload**: `{ "user_id": "integer", "residency_id": "integer" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "residency_id": "integer", "status": "string" }`
- **PUT /user-residencies/{residency_id}**: Update a user residency by ID.
  - **Payload**: `{ "status": "string" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "residency_id": "integer", "status": "string" }`
- **DELETE /user-residencies/{residency_id}**: Delete a user residency by ID.
  - **Return**: `204 No Content`

## Document Endpoints
- **GET /documents**: Retrieve a list of documents.
  - **Return**: `[{ "id": "integer", "name": "string", "url": "string" }]`
- **GET /documents/{document_id}**: Retrieve a specific document by ID.
  - **Return**: `{ "id": "integer", "name": "string", "url": "string" }`
- **POST /documents**: Create a new document.
  - **Payload**: `{ "name": "string", "url": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "url": "string" }`
- **PUT /documents/{document_id}**: Update a document by ID.
  - **Payload**: `{ "name": "string", "url": "string" }`
  - **Return**: `{ "id": "integer", "name": "string", "url": "string" }`
- **DELETE /documents/{document_id}**: Delete a document by ID.
  - **Return**: `204 No Content`

## Company User Endpoints
- **GET /company-users**: Retrieve a list of company users.
  - **Return**: `[{ "id": "integer", "company_id": "integer", "user_id": "integer", "role": "string" }]`
- **GET /company-users/{user_id}**: Retrieve a specific company user by ID.
  - **Return**: `{ "id": "integer", "company_id": "integer", "user_id": "integer", "role": "string" }`
- **POST /company-users**: Create a new company user.
  - **Payload**: `{ "company_id": "integer", "user_id": "integer", "role": "string" }`
  - **Return**: `{ "id": "integer", "company_id": "integer", "user_id": "integer", "role": "string" }`
- **PUT /company-users/{user_id}**: Update a company user by ID.
  - **Payload**: `{ "role": "string" }`
  - **Return**: `{ "id": "integer", "company_id": "integer", "user_id": "integer", "role": "string" }`
- **DELETE /company-users/{user_id}**: Delete a company user by ID.
  - **Return**: `204 No Content`

## Company User Role Endpoints
- **GET /company-user-roles**: Retrieve a list of company user roles.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /company-user-roles/{role_id}**: Retrieve a specific company user role by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /company-user-roles**: Create a new company user role.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /company-user-roles/{role_id}**: Update a company user role by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /company-user-roles/{role_id}**: Delete a company user role by ID.
  - **Return**: `204 No Content`

## Subscription Type Endpoints
- **GET /subscription-types**: Retrieve a list of subscription types.
  - **Return**: `[{ "id": "integer", "name": "string", "price": "float" }]`
- **GET /subscription-types/{type_id}**: Retrieve a specific subscription type by ID.
  - **Return**: `{ "id": "integer", "name": "string", "price": "float" }`
- **POST /subscription-types**: Create a new subscription type.
  - **Payload**: `{ "name": "string", "price": "float" }`
  - **Return**: `{ "id": "integer", "name": "string", "price": "float" }`
- **PUT /subscription-types/{type_id}**: Update a subscription type by ID.
  - **Payload**: `{ "name": "string", "price": "float" }`
  - **Return**: `{ "id": "integer", "name": "string", "price": "float" }`
- **DELETE /subscription-types/{type_id}**: Delete a subscription type by ID.
  - **Return**: `204 No Content`

## Subscription Endpoints
- **GET /subscriptions**: Retrieve a list of subscriptions.
  - **Return**: `[{ "id": "integer", "user_id": "integer", "type_id": "integer", "status": "string" }]`
- **GET /subscriptions/{subscription_id}**: Retrieve a specific subscription by ID.
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer", "status": "string" }`
- **POST /subscriptions**: Create a new subscription.
  - **Payload**: `{ "user_id": "integer", "type_id": "integer" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer", "status": "string" }`
- **PUT /subscriptions/{subscription_id}**: Update a subscription by ID.
  - **Payload**: `{ "status": "string" }`
  - **Return**: `{ "id": "integer", "user_id": "integer", "type_id": "integer", "status": "string" }`
- **DELETE /subscriptions/{subscription_id}**: Delete a subscription by ID.
  - **Return**: `204 No Content`

## Subscription Refund Endpoints
- **GET /subscription-refunds**: Retrieve a list of subscription refunds.
  - **Return**: `[{ "id": "integer", "subscription_id": "integer", "amount": "float", "status": "string" }]`
- **GET /subscription-refunds/{refund_id}**: Retrieve a specific subscription refund by ID.
  - **Return**: `{ "id": "integer", "subscription_id": "integer", "amount": "float", "status": "string" }`
- **POST /subscription-refunds**: Create a new subscription refund.
  - **Payload**: `{ "subscription_id": "integer", "amount": "float" }`
  - **Return**: `{ "id": "integer", "subscription_id": "integer", "amount": "float", "status": "string" }`
- **PUT /subscription-refunds/{refund_id}**: Update a subscription refund by ID.
  - **Payload**: `{ "status": "string" }`
  - **Return**: `{ "id": "integer", "subscription_id": "integer", "amount": "float", "status": "string" }`
- **DELETE /subscription-refunds/{refund_id}**: Delete a subscription refund by ID.
  - **Return**: `204 No Content`

## Request Category Endpoints
- **GET /request-categories**: Retrieve a list of request categories.
  - **Return**: `[{ "id": "integer", "name": "string" }]`
- **GET /request-categories/{category_id}**: Retrieve a specific request category by ID.
  - **Return**: `{ "id": "integer", "name": "string" }`
- **POST /request-categories**: Create a new request category.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **PUT /request-categories/{category_id}**: Update a request category by ID.
  - **Payload**: `{ "name": "string" }`
  - **Return**: `{ "id": "integer", "name": "string" }`
- **DELETE /request-categories/{category_id}**: Delete a request category by ID.
  - **Return**: `204 No Content`

## Request Image Endpoints
- **GET /request-images**: Retrieve a list of request images.
  - **Return**: `[{ "id": "integer", "request_id": "integer", "url": "string" }]`
- **GET /request-images/{image_id}**: Retrieve a specific request image by ID.
  - **Return**: `{ "id": "integer", "request_id": "integer", "url": "string" }`
- **POST /request-images**: Create a new request image.
  - **Payload**: `{ "request_id": "integer", "url": "string" }`
  - **Return**: `{ "id": "integer", "request_id": "integer", "url": "string" }`
- **PUT /request-images/{image_id}**: Update a request image by ID.
  - **Payload**: `{ "url": "string" }`
  - **Return**: `{ "id": "integer", "request_id": "integer", "url": "string" }`
- **DELETE /request-images/{image_id}**: Delete a request image by ID.
  - **Return**: `204 No Content`

## Request Offer Review Endpoints
- **GET /request-offer-reviews**: Retrieve a list of request offer reviews.
  - **Return**: `[{ "id": "integer", "offer_id": "integer", "rating": "integer", "comment": "string" }]`
- **GET /request-offer-reviews/{review_id}**: Retrieve a specific request offer review by ID.
  - **Return**: `{ "id": "integer", "offer_id": "integer", "rating": "integer", "comment": "string" }`
- **POST /request-offer-reviews**: Create a new request offer review.
  - **Payload**: `{ "offer_id": "integer", "rating": "integer", "comment": "string" }`
  - **Return**: `{ "id": "integer", "offer_id": "integer", "rating": "integer", "comment": "string" }`
- **PUT /request-offer-reviews/{review_id}**: Update a request offer review by ID.
  - **Payload**: `{ "rating": "integer", "comment": "string" }`
  - **Return**: `{ "id": "integer", "offer_id": "integer", "rating": "integer", "comment": "string" }`
- **DELETE /request-offer-reviews/{review_id}**: Delete a request offer review by ID.
  - **Return**: `204 No Content` 