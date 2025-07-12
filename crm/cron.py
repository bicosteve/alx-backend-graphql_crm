import datetime
import requests
import logging
from gql.transport.requests import RequestsHTTPTransport


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
