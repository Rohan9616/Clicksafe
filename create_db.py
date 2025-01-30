import sqlite3

# Function to initialize the database and create the table
def init_db():
    # Connect to the SQLite database (this will create the file if it doesn't exist)
    conn = sqlite3.connect('phishing_interactions.db')
    c = conn.cursor()
    
    # Create the table 'interactions' if it doesn't already exist
    c.execute('''
    CREATE TABLE IF NOT EXISTS interactions (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        email_address TEXT NOT NULL,
        clicked_link INTEGER NOT NULL,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()

# Call the function to initialize the database
init_db()
