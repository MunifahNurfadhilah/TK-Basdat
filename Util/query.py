import psycopg2
from psycopg2 import Error

try:
    # Connect to an existing database
    connection = psycopg2.connect(user="postgres",
                                  password="a9nhUoVy1jPgQRnQs8qC",
                                  host="tk-basdat-production.up.railway.app",
                                  port="7959",
                                  database="railway")

    # Create a cursor to perform database operations
    cursor = connection.cursor()
    # Print PostgreSQL details
    print("PostgreSQL server information")
    print(connection.get_dsn_parameters(), "\n")
    # Executing a SQL query
    cursor.execute("SELECT version();")
    # Fetch result
    record = cursor.fetchone()
    print("You are connected to - ", record, "\n")

    cursor.execute("SET search_path TO babadu")

except (Exception, Error) as error:
    print("Error while connecting to PostgreSQL", error)
