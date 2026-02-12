import random
import json
from datetime import datetime, timedelta

# Configuration
NUM_RECORDS = 2000

cities = ["Hyderabad", "Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata"]
account_types = ["Savings", "Current"]
transaction_types = ["Credit", "Debit"]
merchant_categories = ["Groceries", "Electronics", "Travel", "Food", "Utilities", "Shopping"]
payment_modes = ["UPI", "Credit Card", "Debit Card", "Net Banking"]
statuses = ["Completed", "Failed"]
device_types = ["Mobile", "Web", "ATM"]

data = []

start_date = datetime(2024, 1, 1)

for i in range(NUM_RECORDS):
    transaction_date = start_date + timedelta(days=random.randint(0, 365))

    transaction_type = random.choice(transaction_types)

    if transaction_type == "Credit":
        amount = round(random.uniform(1000, 100000), 2)
    else:
        amount = round(random.uniform(100, 50000), 2)

    record = {
        "transaction_id": 100000 + i,
        "account_id": random.randint(5000, 5100),
        "customer_name": f"Customer_{random.randint(1, 100)}",
        "account_type": random.choice(account_types),
        "transaction_type": transaction_type,
        "amount": amount,
        "merchant_category": random.choice(merchant_categories),
        "transaction_date": transaction_date.strftime("%Y-%m-%d"),
        "city": random.choice(cities),
        "payment_mode": random.choice(payment_modes),
        "status": random.choice(statuses),
        "device_type": random.choice(device_types)
    }

    data.append(record)

# Save to JSON file
with open("banking_transactions.json", "w") as f:
    json.dump(data, f, indent=4)

print("✅ 2000 banking transaction records generated successfully!")
