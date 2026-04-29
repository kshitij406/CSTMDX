# Import the MySQL connector library
# This library allows Python to interact with a MySQL database.
import mysql.connector as mysql

# Establish a connection to the MySQL server
# Specify the host (server), user credentials, and the target database.
conn = mysql.connect(
    host="localhost",      # The server where the database is hosted; "localhost" refers to the local machine.
    user="root",           # The username for the MySQL database; here, it is "root".
    password="Magic123",   # The password for the root user account.
    database="shop"        # The name of the database to connect to.
)

# Create a cursor object to execute SQL queries
# The cursor acts as a pointer that helps execute and fetch query results.
cursor = conn.cursor()

# Define the SQL query for inserting data into the Products table
query = "INSERT INTO Products (productID, productName, price, stock) VALUES (%s, %s, %s, %s)"

# Define the values to be inserted
values = (1, 'Sneakers', 49.99, 10)

# Execute the query with the provided values
cursor.execute(query, values)

# Commit the transaction to save changes in the database
conn.commit()

# Confirm the data was inserted
print(f"Inserted {cursor.rowcount} record(s) into the Products table.")

# Close the cursor and connection to free up resources
cursor.close()
conn.close()

# Note: This script inserts a single product into the Products table in the "shop" database.
