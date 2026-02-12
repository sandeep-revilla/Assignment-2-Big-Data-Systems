from pymongo import MongoClient

connection_string = "mongodb+srv://2024c104019_db_user:1pvMYZxHQYWifCS5@cluster0.vn3em5x.mongodb.net/?appName=Cluster0"

client = MongoClient(connection_string)
db = client["banking_system"]
collection = db["transactions"]


print("\n--- Scenario 11: Top 5 Cities by Completed Transaction Amount ---")

pipeline1 = [
    {
        "$match": {
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": "$city",
            "total_amount": {"$sum": "$amount"},
            "transaction_count": {"$sum": 1}
        }
    },
    {
        "$sort": {"total_amount": -1}
    },
    {
        "$limit": 5
    }
]

results1 = collection.aggregate(pipeline1)

for result in results1:
    print(result)
print("\n--- Scenario 12: Customers Above Overall Average Transaction ---")

# Step 1: Calculate overall average
overall_avg = collection.aggregate([
    {"$group": {"_id": None, "overall_avg": {"$avg": "$amount"}}}
])

overall_avg_value = list(overall_avg)[0]["overall_avg"]

# Step 2: Find customers above that average
pipeline2 = [
    {
        "$group": {
            "_id": "$account_id",
            "customer_name": {"$first": "$customer_name"},
            "avg_amount": {"$avg": "$amount"},
            "total_transactions": {"$sum": 1}
        }
    },
    {
        "$match": {
            "avg_amount": {"$gt": overall_avg_value}
        }
    },
    {
        "$sort": {"avg_amount": -1}
    }
]

results2 = collection.aggregate(pipeline2)

for result in results2:
    print(result)
print("\n--- Scenario 13: Monthly Growth Trend ---")

pipeline3 = [
    {
        "$addFields": {
            "transaction_date_obj": {"$toDate": "$transaction_date"}
        }
    },
    {
        "$match": {
            "status": "Completed"
        }
    },
    {
        "$group": {
            "_id": {
                "year": {"$year": "$transaction_date_obj"},
                "month": {"$month": "$transaction_date_obj"}
            },
            "total_amount": {"$sum": "$amount"},
            "transaction_count": {"$sum": 1}
        }
    },
    {
        "$sort": {"_id.year": 1, "_id.month": 1}
    }
]

results3 = collection.aggregate(pipeline3)

for result in results3:
    print(result)
print("\n--- Scenario 14: Failed Transaction Percentage by City ---")

pipeline4 = [
    {
        "$group": {
            "_id": "$city",
            "total_transactions": {"$sum": 1},
            "failed_transactions": {
                "$sum": {
                    "$cond": [
                        {"$eq": ["$status", "Failed"]},
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
            "failed_transactions": 1,
            "failure_percentage": {
                "$multiply": [
                    {"$divide": ["$failed_transactions", "$total_transactions"]},
                    100
                ]
            }
        }
    },
    {
        "$sort": {"failure_percentage": -1}
    }
]

results4 = collection.aggregate(pipeline4)

for result in results4:
    print(result)
print("\n--- Scenario 15: Dashboard Summary using Facet ---")

pipeline5 = [
    {
        "$facet": {
            "total_transactions": [
                {"$count": "count"}
            ],
            "total_completed_amount": [
                {"$match": {"status": "Completed"}},
                {"$group": {"_id": None, "total": {"$sum": "$amount"}}}
            ],
            "top_payment_mode": [
                {"$group": {"_id": "$payment_mode", "count": {"$sum": 1}}},
                {"$sort": {"count": -1}},
                {"$limit": 1}
            ]
        }
    }
]

results5 = collection.aggregate(pipeline5)

for result in results5:
    print(result)
