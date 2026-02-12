from neo4j import GraphDatabase
URI = "neo4j+s://56b0c282.databases.neo4j.io"
USERNAME = "neo4j"
PASSWORD = "HXRZAXEGaW75RIeZTKWweWs46H6t1tqO1w-ApGqEVig"

driver = GraphDatabase.driver(URI, auth=(USERNAME, PASSWORD))
def scenario1(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(p:Part)
          -[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(r:Regulation {regulation_name: "REACH"})
    RETURN DISTINCT a.msn AS Aircraft_MSN
    ORDER BY Aircraft_MSN
    """
    result = tx.run(query)
    return [record["Aircraft_MSN"] for record in result]

def scenario2(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(:Part)
          -[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    RETURN a.msn AS Aircraft_MSN,
           COUNT(DISTINCT s) AS Regulated_Substance_Count
    ORDER BY Regulated_Substance_Count DESC
    """
    result = tx.run(query)
    return [(record["Aircraft_MSN"], record["Regulated_Substance_Count"]) for record in result]
def scenario3(tx):
    query = """
    MATCH (p:Part)-[:CONTAINS]->(s:Substance)
          -[:REGULATED_BY]->(:Regulation)
    RETURN p.part_number AS Part_Number,
           p.part_type AS Part_Type,
           COUNT(DISTINCT s) AS Regulated_Substances
    ORDER BY Regulated_Substances DESC
    LIMIT 5
    """
    result = tx.run(query)
    return [
        (
            record["Part_Number"],
            record["Part_Type"],
            record["Regulated_Substances"]
        )
        for record in result
    ]
def scenario4(tx):
    query = """
    MATCH (a:Aircraft)-[:HAS_PART]->(:Part)
          -[:CONTAINS]->(:Substance)
          -[:REGULATED_BY]->(r:Regulation)
    RETURN r.regulation_name AS Regulation,
           COUNT(DISTINCT a) AS Impacted_Aircraft
    ORDER BY Impacted_Aircraft DESC
    """
    result = tx.run(query)
    return [
        (record["Regulation"], record["Impacted_Aircraft"])
        for record in result
    ]
def scenario5(tx):
    query = """
    MATCH path = (a:Aircraft)-[:HAS_PART]->(p:Part)
                 -[:CONTAINS]->(s:Substance)
                 -[:REGULATED_BY]->(r:Regulation)
    RETURN a.msn AS Aircraft,
           p.part_number AS Part,
           s.substance_name AS Substance,
           r.regulation_name AS Regulation
    LIMIT 10
    """
    result = tx.run(query)
    return [
        (
            record["Aircraft"],
            record["Part"],
            record["Substance"],
            record["Regulation"]
        )
        for record in result
    ]

with driver.session() as session:
    print("\n--- Scenario 1: Aircraft impacted by REACH Regulation ---\n")

    aircraft_list = session.execute_read(scenario1)

    if aircraft_list:
        for aircraft in aircraft_list:
            print("Aircraft:", aircraft)
    else:
        print("No aircraft found under REACH regulation.")

    print("\n--- Scenario 2: Regulated Substance Count per Aircraft ---\n")

    substance_counts = session.execute_read(scenario2)

    if substance_counts:
        for aircraft, count in substance_counts:
            print(f"Aircraft: {aircraft} | Regulated Substances: {count}")
    else:
        print("No regulated substances found.")

    print("\n--- Scenario 3: Top 5 Parts by Regulated Substances ---\n")

    top_parts = session.execute_read(scenario3)

    if top_parts:
        for part_number, part_type, count in top_parts:
            print(f"Part: {part_number} | Type: {part_type} | Regulated Substances: {count}")
    else:
        print("No regulated parts found.")

    print("\n--- Scenario 4: Regulations Ranked by Aircraft Impact ---\n")

    regulation_impact = session.execute_read(scenario4)

    if regulation_impact:
        for regulation, count in regulation_impact:
            print(f"Regulation: {regulation} | Impacted Aircraft: {count}")
    else:
        print("No regulation impact data found.")
    print("\n--- Scenario 5: Compliance Traceability Path ---\n")

    traceability = session.execute_read(scenario5)

    if traceability:
        for aircraft, part, substance, regulation in traceability:
            print(f"Aircraft: {aircraft} -> Part: {part} -> Substance: {substance} -> Regulation: {regulation}")
    else:
        print("No compliance paths found.")


driver.close()
