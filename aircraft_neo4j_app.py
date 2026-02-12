from neo4j import GraphDatabase

# Replace with your details
URI = "neo4j+s://56b0c282.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "HXRZAXEGaW75RIeZTKWweWs46H6t1tqO1w-ApGqEVig"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def run_query(query):
    with driver.session() as session:
        result = session.run(query)
        return [record for record in result]

print("✅ Connected to Neo4j Aura")

# Example Query: Count all nodes
query = """
MATCH (a:Aircraft)-[:HAS_PART]->(p:Part)
RETURN a.msn AS aircraft, count(p) AS part_count
ORDER BY part_count DESC
LIMIT 5
"""
# Top 5 Aircraft with Most Parts:
query = """
MATCH (a:Aircraft)-[:HAS_PART]->(p:Part)
RETURN a.msn AS aircraft, count(p) AS part_count
ORDER BY part_count DESC
LIMIT 5
"""

results = run_query(query)
print(results)
# Example Query: Count all nodes
query = "MATCH (n) RETURN count(n) AS total_nodes"
results = run_query(query)

for record in results:
    print("Total Nodes:", record["total_nodes"])

for record in results:
    print("Total Nodes:", record["total_nodes"])

driver.close()
