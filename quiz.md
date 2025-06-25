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
