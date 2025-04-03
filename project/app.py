import os
from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime, timedelta
import sqlite3
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import Flow
from googleapiclient.discovery import build

app = Flask(__name__)
app.secret_key = os.urandom(24)
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'  # For development only

# Configure OAuth flow
flow = Flow.from_client_secrets_file(
     'credentials.json',
     scopes=["https://www.googleapis.com/auth/calendar", "https://www.googleapis.com/auth/calendar.events"],
     redirect_uri='http://127.0.0.1:8000/callback'
 )


# Database functions
def get_db_connection():
    conn = sqlite3.connect('photography.db')
    conn.row_factory = sqlite3.Row
    return conn

def create_tables():
    conn = get_db_connection()
    conn.execute('''CREATE TABLE IF NOT EXISTS users
                    (id INTEGER PRIMARY KEY, username TEXT UNIQUE NOT NULL, 
                    email TEXT UNIQUE NOT NULL, hash TEXT NOT NULL)''')
    conn.commit()
    conn.close()

def insert_user(username, email, hashed_pass):
    conn = get_db_connection()
    try:
        conn.execute('INSERT INTO users (username, email, hash) VALUES (?, ?, ?)',
                     (username, email, hashed_pass))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def user_exists(username, email):
    conn = get_db_connection()
    user = conn.execute('SELECT * FROM users WHERE username = ? OR email = ?',
                        (username, email)).fetchone()
    conn.close()
    return user is not None

# Routes
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    session.clear()
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if not username or not password:
            return render_template('error.html', message='Please provide username and password')
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()
        conn.close()
        
        if user and check_password_hash(user['hash'], password):
            session['user_id'] = user['id']
            session['username'] = username
            return redirect(url_for('index'))
        return render_template('error.html', message='Invalid username or password')
    return render_template("login.html")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm')
        
        if password != confirm:
            return render_template('error.html', message='Passwords do not match')
        
        if user_exists(username, email):
            return render_template('error.html', message='User already exists')
        
        hashed_pass = generate_password_hash(password)
        if insert_user(username, email, hashed_pass):
            return redirect(url_for('login'))
        return render_template('error.html', message='Registration failed')
    return render_template("register.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/auth')
def auth():
    authorization_url, state = flow.authorization_url(
        access_type='offline',
        include_granted_scopes='true',
        prompt='consent'
    )
    session['state'] = state
    return redirect(authorization_url)

@app.route('/callback')
def callback():
    flow.fetch_token(authorization_response=request.url)
    if not session['state'] == request.args['state']:
        return 'Invalid state parameter', 400

    credentials = flow.credentials
    session['credentials'] = {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }
    return redirect(url_for('create_appointment'))

@app.route('/create_appointment', methods=['GET', 'POST'])
def create_appointment():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        
        date = request.form.get('date')  # Retrieve 'date' from the form data
        time = request.form.get('time')  # Ensure 'time' is also retrieved
        if not date or not time:
            return render_template('error.html', message='Date and time are required')
        start_datetime = datetime.fromisoformat(f"{date}T{time}:00")
        end_datetime = start_datetime + timedelta(hours=1)

        username = session.get('username')  # Retrieve username from session
        event = {
            'summary': f'Photo Session - {username}',
            'description': f'Client: {username}\nSession Type: Photography',
            'start': {'dateTime': start_datetime.isoformat(), 'timeZone': 'Europe/Budapest'},
            'end': {'dateTime': end_datetime.isoformat(), 'timeZone': 'Europe/Budapest'}
        }
        
        credentials = Credentials(**session['credentials'])
        service = build('calendar', 'v3', credentials=credentials)
        event = service.events().insert(calendarId='e752ad0838b9acddbb60ce1ae26e00b056c1a1fff1c8501607ad8c417bc82826@group.calendar.google.com', body=event).execute()
        return render_template('success.html', 
                               message='Appointment created!',
                               username=username,
                               event_time=start_datetime)
    
    # This handles GET requests
    return render_template('create_appointment.html')



if __name__ == '__main__':
    create_tables()
    app.run(debug=True, port=8000)
