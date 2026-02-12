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


# 4. MongoDB Analysis Scenarios (Summary)

1. **Total Completed Credit Amount per City**  
   - Compute the total amount of completed credit transactions grouped by city.  
   - Operators used: `$match`, `$group`, `$sum`, `$sort`.

2. **Account Type Transaction Analysis**  
   - Compare total and average transaction amounts for each account type, split by Credit and Debit.  
   - Operators used: `$group`, `$sum`, `$avg`, `$cond`.

3. **Monthly Transaction Volume & Amount**  
   - Aggregate transactions by year/month to produce monthly counts and total amounts.  
   - Operators used: `$addFields`, `$toDate`, `$year`, `$month`, `$group`, `$sort`.

4. **High-Value Transaction Detection**  
   - Identify accounts with multiple high-value transactions (threshold-based) to flag potential anomalies.  
   - Operators used: `$match`, `$group`, `$sum`, conditional filters.

5. **Top 5 Customers by Debit Spending**  
   - Rank customers by total debit spend and show the top 5.  
   - Operators used: `$match`, `$group`, `$sort`, `$limit`.

6. **Payment Mode Success Rate**  
   - Compute the percentage of successful (Completed) transactions per payment mode.  
   - Operators used: `$group`, `$sum`, `$cond`, `$project`, arithmetic operators.

7. **City & Device Transaction Analysis**  
   - Multi-dimensional aggregation showing transaction counts and totals by city and device type.  
   - Operators used: `$group`, `$sum`, `$sort`.

8. **Merchant Category Average Analysis**  
   - For each merchant category compute total transactions, total amount, and average transaction amount.  
   - Operators used: `$group`, `$sum`, `$avg`, `$project`, `$round`.

9. **Credit vs Debit Comparison by Category**  
   - For each merchant category compare total Credit vs Debit amounts and compute net flow difference.  
   - Operators used: `$group`, `$cond`, `$subtract`, `$project`.

10. **Transaction Amount Bucketing**  
    - Segment transactions into buckets (e.g., Low / Medium / High / Very High) using `$bucket` and compute counts and totals per bucket.  
    - Operators used: `$bucket`, `$sum`.

11. **Top Cities by Revenue**  
    - Rank cities by total completed transaction amount.  
    - Operators used: `$match`, `$group`, `$sum`, `$sort`, `$limit`.

12. **Above-Average Customers**  
    - Identify customers whose average transaction amount is greater than the overall average.  
    - Operators used: `$group`, `$avg`, pipeline stage to compute overall average, `$match`.

13. **Monthly Growth Trend**  
    - Produce a month-over-month view (counts & totals) to visualize growth or decline.  
    - Operators used: `$addFields`, `$toDate`, `$year`, `$month`, `$group`, `$sort`.

14. **Failed Transaction Percentage by City**  
    - For each city compute percentage of failed transactions vs total transactions.  
    - Operators used: `$group`, `$sum`, `$cond`, `$project`, arithmetic operations.

15. **Multi-Metric Summary Analysis (Facet)**  
    - Produce a dashboard-style pipeline using `$facet` to return multiple aggregated metrics (counts, totals, top payment mode) in a single query.  
    - Operators used: `$facet`, `$count`, `$group`, `$sort`, `$limit`.

---

# 5. Neo4j Analysis Scenarios (Summary)

1. **Aircraft impacted by REACH Regulation**  
2. **Regulated Substance Count per Aircraft**  
3. **Top 5 Risky Parts**  
4. **Regulation Impact Ranking**  
5. **Compliance Traceability Path**  
6. **Vendor Risk Ranking**  
7. **Part Type Risk Distribution**  
8. **Aircraft with High Substance Exposure**  
9. **Most Connected Substances**  
10. **Shortest Compliance Path**  
11. **Aircraft Part Count Ranking**  
12. **Regulation Impact on Substances**  
13. **Substance Mapping per Aircraft**  
14. **Aircraft Risk Classification**  
15. **Parts Without Associated Substances**

---

# 6. Output Snapshots

Include screenshots in the final PDF for the following outputs (place each image under the corresponding scenario in your submission document):

- **MongoDB (Atlas UI and/or Python terminal)**  
  - Aggregation pipeline results for representative scenarios (e.g., total credit by city, monthly trend, top 5 customers).  
  - CRUD operation outputs demonstrating Insert / Read / Update / Delete executed via Python.

- **Neo4j (Browser and/or Python terminal)**  
  - Neo4j Browser graph view for traceability and path queries (visual graph snapshots).  
  - Table view results for aggregated Cypher queries (e.g., vendor risk ranking, part-type distribution).  
  - Python terminal outputs showing query execution results.

**Tip:** For each scenario include:
- Scenario heading  
- The query/pipeline used (copy-paste)  
- A one-line explanation of what it measures  
- The output snapshot (annotate if needed)

---

# 7. Conclusion

This submission demonstrates:

- Document-oriented modeling and analysis using **MongoDB Atlas** (suitable for transaction-level, nested, or time-series data).  
- Relationship-centric modeling and traceability using **Neo4j Aura** (suitable for dependency and compliance networks).  
- Execution of a broad set of analytical scenarios (15 for each DB type across 3 students) that use a wide range of aggregation and graph traversal features.  
- Full Python-based connectivity and execution for both MongoDB and Neo4j, enabling reproducible query runs and terminal output capture for the assignment deliverables.

---

# Appendix — Quick Run Instructions (Optional)

## MongoDB (Python)
1. Install driver:
   ```bash
   pip install "pymongo[srv]"
