# Import the MySQL connector library
# This library allows Python to interact with a MySQL database.
import mysql.connector as mysql

# Establish a connection to the MySQL server
# Specify the host (server), user credentials, and optionally a database.
conn = mysql.connect(
    host="localhost",      # The server where the database is hosted; "localhost" refers to the local machine.
    user="root",           # The username for the MySQL database; here, it is "root".
    password="Magic123"    # The password for the root user account.
)

# Create a cursor object to execute SQL queries
# The cursor acts as a pointer that helps execute and fetch query results.
cursor = conn.cursor()

# Execute a query to show all databases on the server
# "SHOW DATABASES" lists all the databases available in the MySQL server instance.
cursor.execute("SHOW DATABASES")

# Fetch all the databases returned by the query
databases = cursor.fetchall()  # Returns a list of tuples, each containing a database name

# Print each database name to the console
for database in databases:
    print(database)  # Each database is printed as a tuple (e.g., ('database_name',))

# Close the cursor to release server resources
cursor.close()

# Optional: Close the connection to the database server
conn.close()

# Note: This script connects to the MySQL server and lists all existing databases.
