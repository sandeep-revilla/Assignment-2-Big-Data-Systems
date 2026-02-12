import random

aircraft_count = 5
part_count = 50
substance_count = 20
vendor_count = 10

part_types = ["DDT", "STPT", "DASSY"]
regulations = ["REACH", "RoHS", "EPA", "OSHA", "ITAR"]

cypher = []

# Create Aircraft
for i in range(1, aircraft_count + 1):
    cypher.append(f'CREATE (:Aircraft {{msn: "MSN{i}"}});')

# Create Vendors
for i in range(1, vendor_count + 1):
    cypher.append(f'CREATE (:Vendor {{vendor_name: "Vendor_{i}"}});')

# Create Parts
for i in range(1, part_count + 1):
    cypher.append(
        f'CREATE (:Part {{part_number: "PN{i}", part_type: "{random.choice(part_types)}", part_description: "Aircraft Component {i}"}});'
    )

# Create Substances
for i in range(1, substance_count + 1):
    cypher.append(
        f'CREATE (:Substance {{cas_number: "CAS{i}", substance_name: "Substance_{i}"}});'
    )

# Create Regulations
for reg in regulations:
    cypher.append(f'CREATE (:Regulation {{regulation_name: "{reg}"}});')

# Relationships

# Aircraft -> Parts
for i in range(1, part_count + 1):
    aircraft_id = random.randint(1, aircraft_count)
    cypher.append(f'''
    MATCH (a:Aircraft {{msn: "MSN{aircraft_id}"}}),
          (p:Part {{part_number: "PN{i}"}})
    CREATE (a)-[:HAS_PART]->(p);
    ''')

# Part -> Substance
for i in range(1, part_count + 1):
    substance_id = random.randint(1, substance_count)
    cypher.append(f'''
    MATCH (p:Part {{part_number: "PN{i}"}}),
          (s:Substance {{cas_number: "CAS{substance_id}"}})
    CREATE (p)-[:CONTAINS]->(s);
    ''')

# Substance -> Regulation
for i in range(1, substance_count + 1):
    regulation = random.choice(regulations)
    cypher.append(f'''
    MATCH (s:Substance {{cas_number: "CAS{i}"}}),
          (r:Regulation {{regulation_name: "{regulation}"}})
    CREATE (s)-[:REGULATED_BY]->(r);
    ''')

# Vendor -> Part
for i in range(1, part_count + 1):
    vendor_id = random.randint(1, vendor_count)
    cypher.append(f'''
    MATCH (v:Vendor {{vendor_name: "Vendor_{vendor_id}"}}),
          (p:Part {{part_number: "PN{i}"}})
    CREATE (v)-[:SUPPLIES]->(p);
    ''')

with open("aircraft_graph.cypher", "w") as f:
    for stmt in cypher:
        f.write(stmt + "\n")

print("Aircraft compliance graph data generated successfully!")
