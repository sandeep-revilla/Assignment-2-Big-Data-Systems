# Assignment 2 – Big Data Systems
## MongoDB & Neo4j Implementation

---

## 📂 1. Data Set Sources

The datasets used in this assignment are included in this [repository](https://github.com/sandeep-revilla/Assignment-2-Big-Data-Systems).

### 🔹 MongoDB – Banking Transaction Dataset
- **File:** `banking_transactions.json`
- **Description:** This dataset contains banking transaction records stored in MongoDB Atlas.  
- **Each document includes fields such as:**
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
- **File:** `aircraft_graph.cypher`
- **Description:** This dataset contains Cypher statements used to create nodes and relationships in Neo4j Aura.  
- **Modeled entities (node labels):**
  - `Aircraft`
  - `Part`
  - `Substance`
  - `Regulation`
  - `Vendor`
- **Modeled relationships:**
  - `(Aircraft)-[:HAS_PART]->(Part)`
  - `(Part)-[:CONTAINS]->(Substance)`
  - `(Substance)-[:REGULATED_BY]->(Regulation)`
  - `(Vendor)-[:SUPPLIES]->(Part)`

---

## 📊 2. Description of Datasets and Analysis

### 🏦 MongoDB – Banking Transaction System
- **Description:** Models a real-world banking transaction environment for analytics.  
- **Use cases / analyses enabled:**
  - Revenue trends
  - Customer spending behavior
  - Payment mode performance
  - Fraud-style high-value transaction detection
  - Monthly growth analysis
  - Credit vs Debit comparisons
- **MongoDB aggregation operators used:**  
  - `$match`, `$group`, `$sum`, `$avg`, `$sort`, `$limit`, `$project`, `$cond`, `$bucket`
- **Implementation note:** A total of **15 meaningful analysis scenarios** (5 per student) were implemented.

### ✈️ Neo4j – Aircraft Compliance Graph System
- **Description:** Models aircraft parts and regulatory compliance relationships as a graph.  
- **Use cases / analyses enabled:**
  - Compliance traceability
  - Vendor risk assessment
  - Substance impact ranking
  - Aircraft risk classification
  - Multi-hop traversal queries
  - Shortest path analysis
- **Cypher features used:**  
  - `MATCH`, `WHERE`, `WITH`, `COUNT`, `DISTINCT`, `ORDER BY`, `LIMIT`, `COLLECT`, `OPTIONAL MATCH`, `CASE`, `shortestPath`
- **Implementation note:** A total of **15 Cypher analysis scenarios** (5 per student) were implemented.

---

## 4. MongoDB Analysis Scenarios (Summary)

### 1. Total Completed Credit Amount per City
- **Description:** Compute the total amount of completed credit transactions grouped by city.
- **Operators used:** `$match`, `$group`, `$sum`, `$sort`.

### 2. Account Type Transaction Analysis
- **Description:** Compare total and average transaction amounts for each account type, split by Credit and Debit.
- **Operators used:** `$group`, `$sum`, `$avg`, `$cond`.

### 3. Monthly Transaction Volume & Amount
- **Description:** Aggregate transactions by year/month to produce monthly counts and total amounts.
- **Operators used:** `$addFields`, `$toDate`, `$year`, `$month`, `$group`, `$sort`.

### 4. High-Value Transaction Detection
- **Description:** Identify accounts with multiple high-value transactions (threshold-based) to flag potential anomalies.
- **Operators used:** `$match`, `$group`, `$sum`, conditional filters.

### 5. Top 5 Customers by Debit Spending
- **Description:** Rank customers by total debit spend and show the top 5.
- **Operators used:** `$match`, `$group`, `$sort`, `$limit`.

### 6. Payment Mode Success Rate
- **Description:** Compute the percentage of successful (Completed) transactions per payment mode.
- **Operators used:** `$group`, `$sum`, `$cond`, `$project`.

### 7. City & Device Transaction Analysis
- **Description:** Multi-dimensional aggregation showing transaction counts and totals by city and device type.
- **Operators used:** `$group`, `$sum`, `$sort`.

### 8. Merchant Category Average Analysis
- **Description:** For each merchant category compute total transactions, total amount, and average transaction amount.
- **Operators used:** `$group`, `$sum`, `$avg`, `$project`, `$round`.

### 9. Credit vs Debit Comparison by Category
- **Description:** For each merchant category compare total Credit vs Debit amounts and compute net flow difference.
- **Operators used:** `$group`, `$cond`, `$subtract`, `$project`.

### 10. Transaction Amount Bucketing
- **Description:** Segment transactions into buckets (e.g., Low / Medium / High / Very High) using `$bucket` and compute counts and totals per bucket.
- **Operators used:** `$bucket`, `$sum`.

### 11. Top Cities by Revenue
- **Description:** Rank cities by total completed transaction amount.
- **Operators used:** `$match`, `$group`, `$sum`, `$sort`, `$limit`.

### 12. Above-Average Customers
- **Description:** Identify customers whose average transaction amount is greater than the overall average.
- **Operators used:** `$group`, `$avg`, pipeline stage to compute overall average, `$match`.

### 13. Monthly Growth Trend
- **Description:** Produce a month-over-month view (counts & totals) to visualize growth or decline.
- **Operators used:** `$addFields`, `$toDate`, `$year`, `$month`, `$group`, `$sort`.

### 14. Failed Transaction Percentage by City
- **Description:** For each city compute percentage of failed transactions vs total transactions.
- **Operators used:** `$group`, `$sum`, `$cond`, `$project`.

### 15. Multi-Metric Summary Analysis (Facet)
- **Description:** Produce a dashboard-style pipeline using `$facet` to return multiple aggregated metrics (counts, totals, top payment mode) in a single query.
- **Operators used:** `$facet`, `$count`, `$group`, `$sort`, `$limit`.

---

## 5. Neo4j Analysis Scenarios (Summary)

### 1. Aircraft impacted by REACH Regulation
- **Description:** Find aircraft connected to substances regulated under REACH.

### 2. Regulated Substance Count per Aircraft
- **Description:** Count distinct regulated substances per aircraft.

### 3. Top 5 Risky Parts
- **Description:** Rank parts by number or severity of regulated substances contained.

### 4. Regulation Impact Ranking
- **Description:** Rank regulations by the number of affected parts/substances.

### 5. Compliance Traceability Path
- **Description:** Return traceability paths from aircraft → part → substance → regulation.

### 6. Vendor Risk Ranking
- **Description:** Rank vendors by the risk profile of the parts they supply.

### 7. Part Type Risk Distribution
- **Description:** Show distribution of risk across part types.

### 8. Aircraft with High Substance Exposure
- **Description:** Identify aircraft with the largest number of regulated substances.

### 9. Most Connected Substances
- **Description:** Find substances with the most connections to parts and aircraft.

### 10. Shortest Compliance Path
- **Description:** Compute the shortest path between an aircraft and a regulating entity for traceability verification.

### 11. Aircraft Part Count Ranking
- **Description:** Rank aircraft by number of parts.

### 12. Regulation Impact on Substances
- **Description:** Show which substances are impacted by which regulations.

### 13. Substance Mapping per Aircraft
- **Description:** List substances mapped to each aircraft.

### 14. Aircraft Risk Classification
- **Description:** Classify aircraft risk based on part/substance/regulation linkage and severity.

### 15. Parts Without Associated Substances
- **Description:** Identify parts that have no associated substances in the graph.

## 💻 3. Programming Language Connectivity

### 🔹 MongoDB Atlas – Python Connection
```python
# MongoDB Atlas - Python example
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
#python
# Neo4j Aura - Python example
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

driver.close() ```python
