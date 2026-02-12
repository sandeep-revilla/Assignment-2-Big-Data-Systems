from neo4j import GraphDatabase
URI = "neo4j+s://56b0c282.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "HXRZAXEGaW75RIeZTKWweWs46H6t1tqO1w-ApGqEVig"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

# ---------------- Scenario 11 ----------------
# Aircraft with highest number of parts
def scenario11(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(p:Part)
    RETURN a.msn AS Aircraft,
           COUNT(p) AS Part_Count
    ORDER BY Part_Count DESC
    """
    result = tx.run(query)
    return [(r["Aircraft"], r["Part_Count"]) for r in result]


# ---------------- Scenario 12 ----------------
# Regulation affecting highest number of substances
def scenario12(tx):
    query = """
    MATCH (s:Substance)-[:REGULATED_BY]->(r:Regulation)
    RETURN r.regulation_name AS Regulation,
           COUNT(DISTINCT s) AS Substance_Count
    ORDER BY Substance_Count DESC
    """
    result = tx.run(query)
    return [(r["Regulation"], r["Substance_Count"]) for r in result]


# ---------------- Scenario 13 ----------------
# Collect all substances per Aircraft
def scenario13(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(:Part)
          -[:CONTAINS]->(s:Substance)
    RETURN a.msn AS Aircraft,
           COLLECT(DISTINCT s.substance_name) AS Substances
    """
    result = tx.run(query)
    return [(r["Aircraft"], r["Substances"]) for r in result]


# ---------------- Scenario 14 ----------------
# Risk classification using CASE
def scenario14(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(:Part)
          -[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    WITH a, COUNT(DISTINCT s) AS substance_count
    RETURN a.msn AS Aircraft,
           substance_count,
           CASE
               WHEN substance_count > 10 THEN "HIGH RISK"
               WHEN substance_count > 5 THEN "MEDIUM RISK"
               ELSE "LOW RISK"
           END AS Risk_Level
    ORDER BY substance_count DESC
    """
    result = tx.run(query)
    return [(r["Aircraft"], r["substance_count"], r["Risk_Level"]) for r in result]


# ---------------- Scenario 15 ----------------
# Optional match – Parts without substances
def scenario15(tx):
    query = """
    MATCH (p:Part)
    OPTIONAL MATCH (p)-[:CONTAINS]->(s:Substance)
    WITH p, COUNT(s) AS substance_count
    WHERE substance_count = 0
    RETURN p.part_number AS Part_Without_Substances
    """
    result = tx.run(query)
    return [r["Part_Without_Substances"] for r in result]


# ---------------- Execution ----------------
with driver.session() as session:

    print("\n--- Scenario 11: Aircraft Part Count Ranking ---\n")
    for aircraft, count in session.execute_read(scenario11):
        print(f"Aircraft: {aircraft} | Parts: {count}")

    print("\n--- Scenario 12: Regulation Impact on Substances ---\n")
    for regulation, count in session.execute_read(scenario12):
        print(f"Regulation: {regulation} | Substances: {count}")

    print("\n--- Scenario 13: Substance List per Aircraft ---\n")
    for aircraft, substances in session.execute_read(scenario13):
        print(f"Aircraft: {aircraft} | Substances: {substances}")

    print("\n--- Scenario 14: Aircraft Risk Classification ---\n")
    for aircraft, count, risk in session.execute_read(scenario14):
        print(f"Aircraft: {aircraft} | Substance Count: {count} | Risk: {risk}")

    print("\n--- Scenario 15: Parts Without Substances ---\n")
    for part in session.execute_read(scenario15):
        print(f"Part without substances: {part}")

driver.close()
