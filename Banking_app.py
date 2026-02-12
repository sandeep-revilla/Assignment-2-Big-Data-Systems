from pymongo import MongoClient
connection_string = "mongodb+srv://2024c104019_db_user:1pvMYZxHQYWifCS5@cluster0.vn3em5x.mongodb.net/?appName=Cluster0"

client = MongoClient(connection_string)

db = client["banking_system"]
collection = db["transactions"]

print("✅ Connected to MongoDB Atlas")

# READ example
print("\n--- Sample Transactions ---")
for doc in collection.find().limit(5):
    print(doc)

# COUNT documents
count = collection.count_documents({})
print(f"\nTotal Documents: {count}")

print("\n--- INSERT Operation ---")

new_transaction = {
    "transaction_id": 999999,
    "account_id": 6000,
    "customer_name": "Test_User",
    "account_type": "Savings",
    "transaction_type": "Debit",
    "amount": 2500.50,
    "merchant_category": "Food",
    "transaction_date": "2024-12-01",
    "city": "Hyderabad",
    "payment_mode": "UPI",
    "status": "Completed",
    "device_type": "Mobile"
}

result = collection.insert_one(new_transaction)
print("Inserted ID:", result.inserted_id)
print("\n--- READ Operation ---")


doc = collection.find_one({"transaction_id": 999999})
print(doc)

print("\n--- UPDATE Operation ---")

collection.update_one(
    {"transaction_id": 999999},
    {"$set": {"status": "Failed"}}
)

updated_doc = collection.find_one({"transaction_id": 999999})
print(updated_doc)


print("\n--- DELETE Operation ---")

collection.delete_one({"transaction_id": 999999})

deleted_check = collection.find_one({"transaction_id": 999999})
print("After Deletion:", deleted_check)

