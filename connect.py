import psycopg2

def check_database_working(host, port, user, password, database):
    # Connect to the database
    conn = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    cursor = conn.cursor()

    # Run a simple query to check the health of the database
    cursor.execute("SELECT 1")
    result = cursor.fetchone()


    # Check the result of the query
    if result == (1,):
        print("Database is working")
    else:
        print("Database is not working")

# Test the function with some sample connection details
check_database_working(host="192.168.56.5", port=5432, user="ahmed", password="Ahmed216!", database="test")