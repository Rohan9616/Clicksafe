import sqlite3

def insert_interaction(email, clicked):
    # Connect to SQLite database
    conn = sqlite3.connect('phishing_interactions.db')
    c = conn.cursor()
    
    # Insert data into the interactions table
    c.execute("INSERT INTO interactions (email_address, clicked_link) VALUES (?, ?)", (email, clicked))
    
    conn.commit()  # Commit the changes
    conn.close()  # Close the connection

# Insert a test interaction
insert_interaction('test@example.com', 1)
