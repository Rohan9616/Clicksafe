from flask import Flask, render_template, request, redirect
from flask_mail import Mail, Message
import sqlite3
import os
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env
load_dotenv()

# Flask-Mail configuration (same as before)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')  # Your email
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')  # Your app password
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_USERNAME')  # Set the default sender

mail = Mail(app)

def insert_interaction(email, clicked):
    """Insert user interaction data into the database"""
    conn = sqlite3.connect('phishing_interactions.db')
    c = conn.cursor()
    c.execute("INSERT INTO interactions (email_address, clicked_link) VALUES (?, ?)", (email, clicked))
    conn.commit()
    conn.close()

@app.route('/send-email')
def send_email():
    recipient_email = "user@example.com"  # Change this to the test recipient email
    msg = Message(
        subject="Security Alert: Verify Your Account",
        sender=app.config['MAIL_DEFAULT_SENDER'],
        recipients=[recipient_email]
    )
    msg.body = "Dear User,\n\nWe detected unusual activity. Click here to verify: http://fake-login.com"
    
    try:
        mail.send(msg)
        return f"Phishing email sent to {recipient_email}!"
    except Exception as e:
        return f"Error: {str(e)}"

@app.route('/click-link')
def click_link():
    """Simulate a user clicking the phishing link"""
    user_email = request.args.get('email')  # Get the email address from query parameter
    insert_interaction(user_email, clicked=1)  # Insert the interaction as 'clicked'
    
    return f"Thank you for clicking the link, {user_email}! We have logged your interaction."

@app.route('/report')
def report():
    """Display a report of all interactions"""
    conn = sqlite3.connect('phishing_interactions.db')
    c = conn.cursor()
    c.execute("SELECT * FROM interactions")
    rows = c.fetchall()
    conn.close()

    # Render the data in a simple HTML table (you can customize this template)
    return render_template('report.html', rows=rows)

if __name__ == '__main__':
    app.run(debug=True)
