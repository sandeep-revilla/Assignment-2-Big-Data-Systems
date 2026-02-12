from pymongo import MongoClient

connection_string = "mongodb+srv://2024c104019_db_user:1pvMYZxHQYWifCS5@cluster0.vn3em5x.mongodb.net/?appName=Cluster0"

client = MongoClient(connection_string)
db = client["banking_system"]
collection = db["transactions"]

print("\n--- Nayan: Analysis 1 - Payment Mode Success Rate ---")

pipeline1 = [
    {
        "$group": {
            "_id": "$payment_mode",
            "total_transactions": {"$sum": 1},
            "successful_transactions": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$status", "Completed"]},
                        1,
                        0
                    ]
                }
            }
        }
    },
    {
        "$project": {
            "total_transactions": 1,
            "successful_transactions": 1,
            "success_rate_percentage": {
                "$multiply": [
                    {"$divide": ["$successful_transactions", "$total_transactions"]},
                    100
                ]
            }
        }
    },
    {
        "$sort": {"success_rate_percentage": -1}
    }
]

results = collection.aggregate(pipeline1)

for result in results:
    print(result)

print("\n---Scenario 7 - City and Device Transaction Analysis ---")

pipeline2 = [
    {
        "$group": {
            "_id": {
                "city": "$city",
                "device_type": "$device_type"
            },
            "total_transactions": {"$sum": 1},
            "total_amount": {"$sum": "$amount"}
        }
    },
    {
        "$sort": {"total_amount": -1}
    }
]

results2 = collection.aggregate(pipeline2)

for result in results2:
    print(result)


print("\n--- Scenario 8: Average Transaction Amount by Merchant Category ---")

pipeline3 = [
    {
        "$group": {
            "_id": "$merchant_category",
            "total_transactions": {"$sum": 1},
            "total_amount": {"$sum": "$amount"},
            "average_transaction_amount": {"$avg": "$amount"}
        }
    },
    {
        "$project": {
            "total_transactions": 1,
            "total_amount": 1,
            "average_transaction_amount": {
                "$round": ["$average_transaction_amount", 2]
            }
        }
    },
    {
        "$sort": {"average_transaction_amount": -1}
    }
]

results3 = collection.aggregate(pipeline3)

for result in results3:
    print(result)


print("\n--- Scenario 9: Credit vs Debit Amount by Merchant Category ---")

pipeline4 = [
    {
        "$group": {
            "_id": "$merchant_category",
            "total_credit_amount": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$transaction_type", "Credit"]},
                        "$amount",
                        0
                    ]
                }
            },
            "total_debit_amount": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$transaction_type", "Debit"]},
                        "$amount",
                        0
                    ]
                }
            },
            "total_transactions": {"$sum": 1}
        }
    },
    {
        "$project": {
            "total_credit_amount": 1,
            "total_debit_amount": 1,
            "total_transactions": 1,
            "net_flow_difference": {
                "$subtract": ["$total_credit_amount", "$total_debit_amount"]
            }
        }
    },
    {
        "$sort": {"net_flow_difference": -1}
    }
]

results4 = collection.aggregate(pipeline4)

for result in results4:
    print(result)


print("\n--- Scenario 10: Transaction Amount Distribution (Bucketing) ---")

pipeline5 = [
    {
        "$bucket": {
            "groupBy": "$amount",
            "boundaries": [0, 5000, 20000, 50000, 1000000],
            "default": "Other",
            "output": {
                "transaction_count": {"$sum": 1},
                "total_amount": {"$sum": "$amount"}
            }
        }
    }
]

results5 = collection.aggregate(pipeline5)

for result in results5:
    print(result)
