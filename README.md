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
