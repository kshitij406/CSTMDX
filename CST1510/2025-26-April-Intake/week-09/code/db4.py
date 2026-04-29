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

# Execute the SQL query to list all tables in the current database
cursor.execute("SHOW TABLES")  # SHOW TABLES lists all the tables in the "shop" database.

# Fetch and display the list of tables
print("Tables in the 'shop' database:")
for table in cursor:
    print(table[0])  # Each table name is returned as a tuple, so we print only the first element.

# Close the cursor and connection to free up resources
cursor.close()
conn.close()

# Note: This script lists all tables in the "shop" database and prints their names.
