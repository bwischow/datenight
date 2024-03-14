from flask import Flask, render_template, request, g
import random
import sqlite3

app = Flask(__name__)

DATABASE = 'movie_night.db'

# Connect to the SQLite database
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

# Close the database connection at the end of each request
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Updated movie database
movies = {
    "Glass Onion": "Netflix",
    "Damsel": "Hulu",
    "The Circle": "Amazon Prime",
    "Kate": "Netflix",
    "Don't Look Up": "Netflix"
}

# User and DateNight classes (unchanged)

# Routes
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            db = get_db()
            db.execute("INSERT INTO users (name, date_night_partner) VALUES (?, ?)", (name, ""))
            db.commit()
    db = get_db()
    users = db.execute("SELECT name FROM users").fetchall()
    return render_template('index.html', users=users)

# Other routes (unchanged)

if __name__ == '__main__':
    app.run(debug=True)
