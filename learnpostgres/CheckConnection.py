import psycopg2

try:

     conn = psycopg2.connect(     user="postgres",
                                  password="Pass@123",
                                  host="127.0.0.1",
                                  port="5432",
                                  database="mydatabase")
     
     print("Database is successfully connected.")

except:
    print("Failure to connect to the database")


cur = conn.cursor()

cur.execute("""
    CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);""")

cur.execute("""INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
            Values (1, 'Cena', 'John', 'Malaysia', 'Kuala Lumpur');
            """)

conn.commit()
cur.close()


