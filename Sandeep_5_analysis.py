from pymongo import MongoClient

connection_string = "mongodb+srv://2024c104019_db_user:1pvMYZxHQYWifCS5@cluster0.vn3em5x.mongodb.net/?appName=Cluster0"

client = MongoClient(connection_string)
db = client["banking_system"]
collection = db["transactions"]

print("\n--- Analysis 1: Total Completed Credit Amount Per City ---")

pipeline = [
    {
        "$match": {
            "transaction_type": "Credit",
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": "$city",
            "total_credit_amount": {"$sum": "$amount"},
            "transaction_count": {"$sum": 1}
        }
    },
    {
        "$sort": {"total_credit_amount": -1}
    }
]

results = collection.aggregate(pipeline)

for result in results:
    print(result)


print("\n--- Analysis 2: Account Type Transaction Analysis ---")

pipeline2 = [
    {
        "$group": {
            "_id": "$account_type",
            "total_transactions": {"$sum": 1},
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
            "average_transaction_amount": {"$avg": "$amount"}
        }
    }
]

results2 = collection.aggregate(pipeline2)

for result in results2:
    print(result)

print("\n--- Analysis 3: Monthly Transaction Volume and Amount (2024) ---")

pipeline3 = [
    {
        "$addFields": {
            "transaction_date_obj": {"$toDate": "$transaction_date"}
        }
    },
    {
        "$match": {
            "$expr": {
                "$eq": [{"$year": "$transaction_date_obj"}, 2024]
            }
        }
    },
    {
        "$group": {
            "_id": {
                "year": {"$year": "$transaction_date_obj"},
                "month": {"$month": "$transaction_date_obj"}
            },
            "total_transactions": {"$sum": 1},
            "total_amount": {"$sum": "$amount"}
        }
    },
    {
        "$sort": {
            "_id.year": 1,
            "_id.month": 1
        }
    }
]

results3 = collection.aggregate(pipeline3)

for result in results3:
    print(result)

print("\n--- Analysis 4: Accounts with Multiple High-Value Transactions ---")

pipeline4 = [
    {
        "$match": {
            "amount": {"$gt": 40000}
        }
    },
    {
        "$group": {
            "_id": "$account_id",
            "high_value_count": {"$sum": 1},
            "total_high_value_amount": {"$sum": "$amount"}
        }
    },
    {
        "$match": {
            "high_value_count": {"$gt": 5}
        }
    },
    {
        "$sort": {"total_high_value_amount": -1}
    }
]

results4 = collection.aggregate(pipeline4)

for result in results4:
    print(result)
print("\n--- Analysis 5: Top 5 Customers by Total Debit Spending ---")

pipeline5 = [
    {
        "$match": {
            "transaction_type": "Debit",
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": {
                "account_id": "$account_id",
                "customer_name": "$customer_name"
            },
            "total_debit_spent": {"$sum": "$amount"},
            "transaction_count": {"$sum": 1}
        }
    },
    {
        "$sort": {"total_debit_spent": -1}
    },
    {
        "$limit": 5
    }
]

results5 = collection.aggregate(pipeline5)

for result in results5:
    print(result)
