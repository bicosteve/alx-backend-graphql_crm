import datetime
import requests
import logging
from gql.transport.requests import RequestsHTTPTransport
from gql import Client


def log_crm_heartbeat():
    now = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")
    message = f"{now} CRM is alive"

    # Append to the heartbeat log
    with open("/tmp/crm_heartbeat_log.txt", "a") as logfile:
        logfile.write(message + "\n")

    # Optional: GraphQL check
    try:
        response = requests.post(
            "http://localhost:8000/graphql", json={"query": "{ hello }"}
        )
        if response.status_code == 200 and "hello" in response.text:
            print("GraphQL endpoint is responsive.")
    except Exception as e:
        logging.warning(f"GraphQL heartbeat check failed: {e}")


def update_low_stock():
    # GraphQL mutation string
    mutation = """
    mutation {
      updateLowStockProducts {
        updatedProducts {
          name
          stock
        }
        success
      }
    }
    """

    try:
        response = requests.post(
            "http://localhost:8000/graphql", json={"query": mutation}
        )

        if response.status_code == 200:
            data = response.json().get("data", {}).get("updateLowStockProducts", {})
            timestamp = datetime.datetime.now().strftime("%d/%m/%Y-%H:%M:%S")

            with open("/tmp/low_stock_updates_log.txt", "a") as log:
                for product in data.get("updatedProducts", []):
                    log.write(
                        f"{timestamp} - Updated: {product['name']} to {product['stock']}\n"
                    )
        else:
            logging.error(f"Mutation failed with status {response.status_code}")
    except Exception as e:
        logging.warning(f"Exception during update_low_stock: {e}")
