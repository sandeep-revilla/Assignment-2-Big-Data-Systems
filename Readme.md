# Assignment 2 – Big Data Systems  
## MongoDB & Neo4j Implementation

---

## 📂 1. Data Set Sources

The datasets used in this assignment are included in this repository.

### 🔹 MongoDB – Banking Transaction Dataset
File:
- `banking_transactions.json`

This dataset contains banking transaction records stored in MongoDB Atlas.  
Each document represents a transaction with attributes such as:

- `transaction_id`
- `account_id`
- `customer_name`
- `account_type`
- `transaction_type`
- `amount`
- `merchant_category`
- `transaction_date`
- `city`
- `payment_mode`
- `status`
- `device_type`

---

### 🔹 Neo4j – Aircraft Compliance Graph Dataset
File:
- `aircraft_graph.cypher`

This dataset contains Cypher statements used to create nodes and relationships in Neo4j Aura.

It models an Aircraft Compliance System including:

**Node Labels**
- `Aircraft`
- `Part`
- `Substance`
- `Regulation`
- `Vendor`

**Relationships**
- `(Aircraft)-[:HAS_PART]->(Part)`
- `(Part)-[:CONTAINS]->(Substance)`
- `(Substance)-[:REGULATED_BY]->(Regulation)`
- `(Vendor)-[:SUPPLIES]->(Part)`

---

## 📊 2. Description of Datasets and Analysis

### 🏦 MongoDB – Banking Transaction System

This system models a real-world banking transaction environment.  
The dataset allows analysis of:

- Revenue trends
- Customer spending behavior
- Payment mode performance
- Fraud-style high-value transaction detection
- Monthly growth analysis
- Credit vs Debit comparisons

MongoDB Aggregation operators used include:

- `$match`
- `$group`
- `$sum`
- `$avg`
- `$sort`
- `$limit`
- `$project`
- `$cond`
- `$bucket`

A total of **15 meaningful analysis scenarios** (5 per student) were implemented.

---

### ✈️ Neo4j – Aircraft Compliance Graph System

This graph database models aircraft parts and regulatory compliance relationships.

The graph structure enables:

- Compliance traceability
- Vendor risk assessment
- Substance impact ranking
- Aircraft risk classification
- Multi-hop traversal queries
- Shortest path analysis

Cypher features used include:

- `MATCH`
- `WHERE`
- `WITH`
- `COUNT`
- `DISTINCT`
- `ORDER BY`
- `LIMIT`
- `COLLECT`
- `OPTIONAL MATCH`
- `CASE`
- `shortestPath`

A total of **15 Cypher analysis scenarios** (5 per student) were implemented.

---

## 💻 3. Programming Language Connectivity

### 🔹 MongoDB Atlas – Python Connection

```python
from pymongo import MongoClient

connection_string = "mongodb+srv://USERNAME:PASSWORD@cluster.mongodb.net/banking_system?retryWrites=true&w=majority"

client = MongoClient(connection_string)
db = client["banking_system"]
collection = db["transactions"]

print("Connected to MongoDB Atlas")

print("Total Documents:", collection.count_documents({}))

for doc in collection.find().limit(5):
    print(doc)
### 🔹 Neo4j Aura – Python Connection

```python
from neo4j import GraphDatabase

URI = "neo4j+s://YOUR_INSTANCE_ID.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "YOUR_PASSWORD"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

with driver.session() as session:
    result = session.run("""
        MATCH (a:Aircraft)
        RETURN a.msn AS Aircraft_MSN
        LIMIT 5
    """)
    for record in result:
        print(record["Aircraft_MSN"])

driver.close()
