from celery import shared_task
import datetime
import requests


@shared_task
def generate_crm_report():
    query = """
    query {
      customers { id }
      orders { id totalamount }
    }
    """
    try:
        response = requests.post("http://localhost:8000/graphql", json={"query": query})
        data = response.json().get("data", {})
        customers = data.get("customers", [])
        orders = data.get("orders", [])

        total_customers = len(customers)
        total_orders = len(orders)
        total_revenue = sum(order.get("totalamount", 0) for order in orders)

        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        report = f"{timestamp} - Report: {total_customers} customers, {total_orders} orders, {total_revenue} revenue"

        with open("/tmp/crm_report_log.txt", "a") as log:
            log.write(report + "\n")

    except Exception as e:
        with open("/tmp/crm_report_log.txt", "a") as log:
            log.write(f"{datetime.datetime.now()} - Error: {str(e)}\n")
