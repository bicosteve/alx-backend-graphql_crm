#!/bin/bash

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOG_FILE="/tmp/customer_cleanup_log.txt"

# Run shell command to delete inactive customers and count them
DELETED_COUNT=$(python manage.py shell <<EOF
from django.utils import timezone
from datetime import timedelta

from crm.models import Customer

cutoff_date = timezone.now() - timedelta(days=365)

inactive_customers = Customer.objects.exclude(order__order_date__gte=cutoff_date).distinct()
count = inactive_customers.count()
inactive_customers.delete()
print(count)
EOF
)

# Log result with timestamp
echo "$TIMESTAMP - Deleted $DELETED_COUNT inactive customer(s)" >> "$LOG_FILE"
