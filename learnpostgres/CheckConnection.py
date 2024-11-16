import psycopg2

#check connection with the database
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

#create person table in the database
cur.execute("""
    CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);""")

#insert data in the table column
cur.execute("""INSERT INTO Persons(PersonID, LastName, FirstName, Address, City)
            Values (1, 'Cena', 'John', 'Malaysia', 'Kuala Lumpur'),
            (2, 'Ramlee', 'Putih', 'Malaysia', 'Selayang');
            """)

conn.commit()
cur.close()


