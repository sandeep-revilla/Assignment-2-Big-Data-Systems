import random

aircraft_count = 5
part_count = 50
substance_count = 20
regulations = ["REACH", "RoHS", "EPA", "OSHA", "ITAR"]
part_types = ["DDT", "STPT", "DASSY"]

cypher_statements = []

# Create Aircraft
for i in range(1, aircraft_count + 1):
    cypher_statements.append(
        f'CREATE (:Aircraft {{msn: "MSN{i}"}});'
    )

# Create Parts
for i in range(1, part_count + 1):
    cypher_statements.append(
        f'CREATE (:Part {{part_number: "PN{i}", part_type: "{random.choice(part_types)}", part_description: "Aircraft component {i}"}});'
    )

# Create Substances
for i in range(1, substance_count + 1):
    cypher_statements.append(
        f'CREATE (:Substance {{cas_number: "CAS{i}", substance_name: "Substance_{i}"}});'
    )

# Create Regulations
for reg in regulations:
    cypher_statements.append(
        f'CREATE (:Regulation {{regulation_name: "{reg}"}});'
    )

# Save file
with open("aircraft_graph.cypher", "w") as f:
    for stmt in cypher_statements:
        f.write(stmt + "\n")

print("Synthetic aircraft graph data generated!")
