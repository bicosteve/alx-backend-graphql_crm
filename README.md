# alx-backend-graphql_crm

```bash
0. Task 0: Schedule a Customer Cleanup Script

Objective
Set up a GraphQL endpoint and define your first schema and query.

Instructions
1. Create a Shell Script: * Create a shell script clean_inactive_customers.sh in the crm/cron_jobs directory. * The script should:

Use Django’s manage.py shell to execute a Python command that deletes customers with no orders since a year ago.
Log the number of deleted customers to a /tmp/customer_cleanup_log.txt with a timestamp.
Include a shebang (#!/bin/bash) and ensure the script is executable (chmod +x).

2. Create a Crontab Entry:

Create a filecrm/cron_jobs/customer_cleanup_crontab.txt with a single line specifying the cron job to run the script every Sunday at 2:00 AM.
Ensure no extra newlines in the file.

Repo:
GitHub repository: alx-backend-graphql_crm
File: clean_inactive_customers.sh, customer_cleanup_crontab.txt
```

```bash
1. Schedule a GraphQL-Based Order Reminder Script

Objective
Create a Python script that uses a GraphQL query to find pending orders (order_date within the last week) and logs reminders, scheduled to run daily using a cron job.

Instructions
Create a Python Script:
Create send_order_reminders.py in crm/cron_jobs.
The script should:
Use the gql library to query the GraphQL endpoint (http://localhost:8000/graphql) for orders with order_date within the last 7 days.
Log each order’s ID and customer email to /tmp/order_reminders_log.txt with a timestamp.
Print "Order reminders processed!"to the console.

Create a Crontab Entry:

Create crm/cron_jobs/order_reminders_crontab.txt with a single line to run the script daily at 8:00 AM.

Ensure no extra newlines.

Repo:

GitHub repository: alx-backend-graphql_crm
File: send_order_reminders.py, order_reminders_crontab.txt
```

```bash
2. Heartbeat Logger with django-crontab

Objective
Implement a django-crontab job that logs a heartbeat message every 5 minutes to confirm the CRM application’s health, integrating with the GraphQL schema.

Instructions
Install django-crontab:
Add django-crontab to requirements.txt.
Add django_crontab to INSTALLED_APPS incrm/settings.py.
Define the Cron Job:
In crm/cron.py, define a function log_crm_heartbeat that:
Logs a message in the formatDD/MM/YYYY-HH:MM:SS CRM is alive to/tmp/crm_heartbeat_log.txt.
Appends to the file (does not overwrite).

Optionally, queries the GraphQL hello field to verify the endpoint is responsive.

Configure the Cron Job:
In crm/settings.py, add to CRONJOBS:

CRONJOBS = [
    ('*/5 * * * *', 'crm.cron.log_crm_heartbeat'),
]

Repo:

GitHub repository: alx-backend-graphql_crm
File: crm/cron.py, crm/settings.py, requirements.txt
```

```bash
3. Schedule a GraphQL Mutation for Product Stock Alerts

Objective
Create a django-crontab job that runs every 12 hours, uses a GraphQL mutation to update low-stock products (stock < 10), and logs the updates.

Instructions
Define a GraphQL Mutation:
In crm/schema.py, add a UpdateLowStockProducts mutation that:

Queries products with stock < 10.
Increments their stock by 10 (simulating restocking).
Returns a list of updated products and a success message.
Create a Cron Job:
In crm/cron.py, define update_low_stock that:

Executes the UpdateLowStockProducts mutation via the GraphQL endpoint.
Logs updated product names and new stock levels to /tmp/low_stock_updates_log.txt with a timestamp.
In crm/settings.py, add to CRONJOBS:


CRONJOBS = [
    ('0 */12 * * *', 'crm.cron.update_low_stock'),
]


Repo:

GitHub repository: alx-backend-graphql_crm
File: crm/schema.py, crm/cron.py, crm/settings.py
```

```bash
4. Celery Task for Generating CRM Reports

Objective
Configure a Celery task with Celery Beat to generate a weekly CRM report (summarizing total orders, customers, and revenue) and log it, integrating with the GraphQL schema.

Instructions:
1. Set Up Celery:

Add celery and django-celery-beat to requirements.txt.
Add django_celery_beat to INSTALLED_APPS in crm/settings.py.
Create crm/celery.py to initialize the Celery app with Redis as the broker (redis://localhost:6379/0).
Update crm/__init__.py to load the Celery app.
2. Define the Celery Task:

In crm/tasks.py, define a task generate_crm_report that:
Uses a GraphQL query to fetch: * Total number of customers. * Total number of orders. * Total revenue (sum of totalamount from orders).
Logs the report to/tmp/crm_report_log.txt with a timestamp in the format YYYY-MM-DD HH:MM:SS - Report: X customers, Y orders, Z revenue.
3. Schedule with Celery Beat:

In crm/settings.py, configure:
CELERY_BEAT_SCHEDULE = {
    'generate-crm-report': {
        'task': 'crm.tasks.generate_crm_report',
        'schedule': crontab(day_of_week='mon', hour=6, minute=0),
    },
}
4. Document Setup:

Create crm/README.md with steps to:

InstallRedis and dependencies.
Run migrations (python manage.py migrate).
Start Celery worker (celery -A crm worker -l info).
Start Celery Beat (celery -A crm beat -l info).
Verify logs in /tmp/crm_report_log.txt.

Repo:

GitHub repository: alx-backend-graphql_crm
File: crm/celery.py, crm/tasks.py, crm/settings.py, crm/__init__.py, requirements.txt, crm/README.md
```

# CRM Weekly Report Setup

## 1. Install Redis and Dependencies

```bash
sudo apt install redis-server
pip install -r requirements.txt
```
