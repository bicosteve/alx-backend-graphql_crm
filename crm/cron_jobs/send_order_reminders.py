#!/usr/bin/env python3

import datetime
import logging
from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Setup logging
logging.basicConfig(
    filename="/tmp/order_reminders_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
)

# GraphQL setup
transport = RequestsHTTPTransport(
    url="http://localhost:8000/graphql",
    verify=False,
    retries=3,
)

client = Client(transport=transport, fetch_schema_from_transport=True)

# Define query for orders within the last 7 days
query = gql(
    """
query getRecentOrders($startDate: DateTime!) {
  orders(filter: {order_date_Gte: $startDate}) {
    id
    customer {
      email
    }
  }
}
"""
)

# Calculate date 7 days ago
seven_days_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).isoformat()

# Execute query
response = client.execute(query, variable_values={"startDate": seven_days_ago})

# Log results
for order in response.get("orders", []):
    log_msg = f"Order ID: {order['id']}, Customer Email: {order['customer']['email']}"
    logging.info(log_msg)

print("Order reminders processed!")
