import mysql.connector
from mysql.connector import Error

# Database credentials
db_host = "172.25.0.2"
db_user = "semaphore"
db_password = "google@123"
db_name = "semaphore"  # Specify the database name

def get_table_counts():
    try:
        # Establish the connection
        connection = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name  # Connect to the specified database
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Query to get all tables in the specified database
            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()

            print(f"Number of tables in the '{db_name}' database: {len(tables)}")
            print(f"Tables and their row counts:")
            
            # Iterate over the tables and get their row counts
            for (table_name,) in tables:
                # Wrap the table name in backticks to avoid syntax errors
                cursor.execute(f"SELECT COUNT(*) FROM `{table_name}`")
                count = cursor.fetchone()[0]
                print(f"{table_name}: {count} rows")

    except Error as e:
        print(f"Error connecting to MySQL: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    get_table_counts()
