import sqlite3

def get_interactions():
    # Connect to SQLite database
    conn = sqlite3.connect('phishing_interactions.db')
    c = conn.cursor()
    
    # Query to retrieve all data
    c.execute("SELECT * FROM interactions")
    rows = c.fetchall()  # Fetch all rows
    
    for row in rows:
        print(row)
    
    conn.close()  # Close the connection

# Retrieve and print the data
get_interactions()
