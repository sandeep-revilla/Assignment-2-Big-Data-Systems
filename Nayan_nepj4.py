from neo4j import GraphDatabase

# Replace with your details
URI = "neo4j+s://56b0c282.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "HXRZAXEGaW75RIeZTKWweWs46H6t1tqO1w-ApGqEVig"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))

def scenario6(tx):
    query = """
    MATCH (v:Vendor)-[:SUPPLIES]->(p:Part)
          -[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    RETURN v.vendor_name AS Vendor,
           COUNT(DISTINCT s) AS Regulated_Substances
    ORDER BY Regulated_Substances DESC
    """
    result = tx.run(query)
    return [(record["Vendor"], record["Regulated_Substances"]) for record in result]


# ---------------- Scenario 7 ----------------
def scenario7(tx):
    query = """
    MATCH (p:Part)-[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    RETURN p.part_type AS Part_Type,
           COUNT(DISTINCT s) AS Regulated_Substances
    ORDER BY Regulated_Substances DESC
    """
    result = tx.run(query)
    return [(record["Part_Type"], record["Regulated_Substances"]) for record in result]


# ---------------- Scenario 8 ----------------
def scenario8(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(:Part)
          -[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    WITH a, COUNT(DISTINCT s) AS substance_count
    WHERE substance_count > 3
    RETURN a.msn AS Aircraft,
           substance_count
    ORDER BY substance_count DESC
    """
    result = tx.run(query)
    return [(record["Aircraft"], record["substance_count"]) for record in result]


# ---------------- Scenario 9 ----------------
def scenario9(tx):
    query = """
    MATCH (p:Part)-[:CONTAINS]->(s:Substance)
    RETURN s.substance_name AS Substance,
           COUNT(DISTINCT p) AS Part_Count
    ORDER BY Part_Count DESC
    LIMIT 5
    """
    result = tx.run(query)
    return [(record["Substance"], record["Part_Count"]) for record in result]


# ---------------- Scenario 10 ----------------
def scenario10(tx):
    query = """
    MATCH (a:Aircraft), (r:Regulation)
    MATCH path = shortestPath(
        (a)-[:HAS_PART|CONTAINS|REGULATED_BY*]->(r)
    )
    RETURN a.msn AS Aircraft,
           r.regulation_name AS Regulation,
           length(path) AS Path_Length
    LIMIT 5
    """
    result = tx.run(query)
    return [
        (record["Aircraft"], record["Regulation"], record["Path_Length"])
        for record in result
    ]


# ---------------- Execution ----------------
with driver.session() as session:

    print("\n--- Scenario 6: Vendor Risk Ranking ---\n")
    results6 = session.execute_read(scenario6)
    for vendor, count in results6:
        print(f"Vendor: {vendor} | Regulated Substances: {count}")

    print("\n--- Scenario 7: Part Type Risk Distribution ---\n")
    results7 = session.execute_read(scenario7)
    for part_type, count in results7:
        print(f"Part Type: {part_type} | Regulated Substances: {count}")

    print("\n--- Scenario 8: Aircraft with High Substance Exposure ---\n")
    results8 = session.execute_read(scenario8)
    for aircraft, count in results8:
        print(f"Aircraft: {aircraft} | Substance Count: {count}")

    print("\n--- Scenario 9: Most Connected Substances ---\n")
    results9 = session.execute_read(scenario9)
    for substance, count in results9:
        print(f"Substance: {substance} | Appears in Parts: {count}")

    print("\n--- Scenario 10: Shortest Compliance Path ---\n")
    results10 = session.execute_read(scenario10)
    for aircraft, regulation, length_val in results10:
        print(f"Aircraft: {aircraft} -> Regulation: {regulation} | Path Length: {length_val}")

driver.close()
