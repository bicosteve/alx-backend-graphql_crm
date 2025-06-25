```bash
0. Set Up GraphQL Endpoint


Objective

Set up a GraphQL endpoint and define your first schema and query.


Instructions
Create Project and App

    Set up a new Django project called alx-backend-graphql_crm.
    Create an app named crm as the main app.

Install Required Libraries

    Install graphene-django and django-filters using pip:

     pip install graphene-django django-filter

Define GraphQL Schema

    In alx-backend-graphql/schema.py, define a Query class that inherits from graphene.ObjectType.

    Inside it, declare a single field:
        Name: hello
        Type: String
        It should return a default value of "Hello, GraphQL!" when queried.

Connect the GraphQL Endpoint

    In urls.py, connect the GraphQL endpoint using:

     from django.urls import path
     from graphene_django.views import GraphQLView
     from django.views.decorators.csrf import csrf_exempt

     urlpatterns = [
         path("graphql", csrf_exempt(GraphQLView.as_view(graphiql=True))),
     ]

Checkpoint

Visit: http://localhost:8000/graphql
Run the following query:

{
  hello
}

Repo:

    GitHub repository: alx-backend-graphql_crm
    File: settings.py,crm,schema.py
```

```bash
1. Task 1: Build and Seed a CRM Database with GraphQL Integration


Objective

Enhance the CRM system by adding GraphQL mutations to create Customer, Product, and Order instances. This includes:

    Bulk customer creation
    Nested order creation with product associations
    Robust validation and error handling

Instructions
1. Define the Mutations

In crm/schema.py, create the following mutation classes:
CreateCustomer

    Inputs:
        name (required, string)
        email (required, unique email)
        phone (optional, string)
    Validations:
        Ensure email is unique.
        Validate phone format (e.g., +1234567890 or 123-456-7890).
    Behavior:
        Saves the customer to the database.
        Returns the created customer object and a success message.
        Think: How will you handle validation errors (e.g., duplicate email)?

BulkCreateCustomers

    Inputs:
        A list of customers, each with name, email, and optional phone.
    Behavior:
        Validates each customer’s data.
        Creates customers in a single transaction.
        Returns:
        List of successfully created customers.
        List of errors for failed records.
    Challenge: Support partial success — create valid entries even if some fail.

CreateProduct

    Inputs:
        name (required, string)
        price (required, positive decimal)
        stock (optional, non-negative integer, default: 0)
    Validations:
        Ensure price is positive and stock is not negative.
    Behavior:
        Saves the product to the database.
        Returns the created product object.

CreateOrder

    Inputs:
        customer_id (required, existing customer ID)
        product_ids (required, list of existing product IDs)
        order_date (optional, defaults to now)
    Validations:
        Ensure customer and product IDs are valid.
        Ensure at least one product is selected.
    Behavior:
        Creates an order.
        Associates specified products.
        Calculates total_amount as the sum of product prices.
        Returns the created order object with nested customer and product data.
    Think: How will you ensure the total_amount is accurate?
    Challenge: Implement custom error handling with user-friendly messages (e.g., “Email already exists”, “Invalid product ID”).

2. Add Mutations to the Schema

In crm/schema.py:

    Define a Mutation class.
    Add mutation fields:

class Mutation(graphene.ObjectType):
    create_customer = CreateCustomer.Field()
    bulk_create_customers = BulkCreateCustomers.Field()
    create_product = CreateProduct.Field()
    create_order = CreateOrder.Field()

    Hint: Use Graphene’s Field and List types appropriately.

3. Integrate Into Main Schema

In graphql_crm/schema.py:

    Import Query and Mutation from crm.schema.
    Combine them:

import graphene
from crm.schema import Query as CRMQuery, Mutation as CRMMutation

class Query(CRMQuery, graphene.ObjectType):
    pass

class Mutation(CRMMutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)

    Think: Ensure support for nested objects and graceful error handling.

Checkpoint: Test Mutations at /graphql

# Create a single customer
mutation {
  createCustomer(input: {
    name: "Alice",
    email: "alice@example.com",
    phone: "+1234567890"
  }) {
    customer {
      id
      name
      email
      phone
    }
    message
  }
}

# Bulk create customers
mutation {
  bulkCreateCustomers(input: [
    { name: "Bob", email: "bob@example.com", phone: "123-456-7890" },
    { name: "Carol", email: "carol@example.com" }
  ]) {
    customers {
      id
      name
      email
    }
    errors
  }
}

# Create a product
mutation {
  createProduct(input: {
    name: "Laptop",
    price: 999.99,
    stock: 10
  }) {
    product {
      id
      name
      price
      stock
    }
  }
}

# Create an order with products
mutation {
  createOrder(input: {
    customerId: "1",
    productIds: ["1", "2"]
  }) {
    order {
      id
      customer {
        name
      }
      products {
        name
        price
      }
      totalAmount
      orderDate
    }
  }
}

Repo:

    GitHub repository: alx-backend-graphql_crm
    File: models.py,schema.py, graphql_crm/schema.py, seed_db.py


```
