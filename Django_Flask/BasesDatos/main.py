import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="master_python"
)

print(database)

cursor = database.cursor(buffered=True)  # <- importante
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")
cursor.execute("SHOW DATABASES")
for db in cursor:
    print(db)

cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
    Id int(10) auto_increment not null,
    marca varchar(40) not null,
    modelo varchar(40) not null,
    precio float(10,2) not null,
    CONSTRAINT pk_vehiculo PRIMARY KEY(Id)             
)
""")
cursor.execute("SHOW TABLES")
for table in cursor:
    print(table)

#single
#cursor.execute("INSERT INTO vehiculos VALUES(null, 'opel','astra',18000)")

#multiple
coches = [
    ('Opel', 'Astra', 18000),
    ('Ford', 'Focus', 19000),
    ('Toyota', 'Corolla', 21000),
    ('Honda', 'Civic', 22000),
    ('Volkswagen', 'Golf', 25000),
    ('BMW', 'Serie 3', 35000),
    ('Audi', 'A4', 37000),
    ('Mercedes', 'C200', 40000),
    ('Renault', 'Megane', 17000),
    ('Seat', 'Leon', 20000)
]

# Insert multiple
cursor.executemany("INSERT INTO vehiculos VALUES (null, %s, %s, %s)", coches)

# Confirmar els canvis
database.commit()

cursor.execute("SELECT * FROM vehiculos ")
result = cursor.fetchall()

print("------------------------------------------")

for coche in result:
    print(coche[1],coche[3])


