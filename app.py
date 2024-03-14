from flask import Flask, render_template, request
import random
import sqlite3

app = Flask(__name__)

# Connect to the SQLite database
conn = sqlite3.connect('movie_night.db')
c = conn.cursor()

# Create the users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (name text, date_night_partner text)''')
conn.commit()

# Updated movie database
movies = {
    "Glass Onion": "Netflix",
    "Damsel": "Hulu",
    "The Circle": "Amazon Prime",
    "Kate": "Netflix",
    "Don't Look Up": "Netflix"
}

class User:
    def __init__(self, name):
        self.name = name
        self.date_night = None
        self.partner = None

    def create_date_night(self):
        if self.date_night is None:
            self.date_night = DateNight()

    def find_date_night_partner(self, partner_name):
        if self.date_night is None and partner_name != self.name:
            self.partner = partner_name

class DateNight:
    def __init__(self):
        self.movies_list = list(movies.keys())
        self.current_movie = None

    def next_movie(self):
        self.current_movie = random.choice(self.movies_list)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        if name:
            c.execute("INSERT INTO users (name, date_night_partner) VALUES (?, ?)", (name, ""))
            conn.commit()
    c.execute("SELECT name FROM users")
    users = c.fetchall()
    return render_template('index.html', users=users)

@app.route('/create_date_night', methods=['POST'])
def create_date_night():
    name = request.form.get('name')
    partner_name = request.form.get('partner_name')
    if name and partner_name:
        c.execute("UPDATE users SET date_night_partner=? WHERE name=?", (partner_name, name))
        conn.commit()
    return '', 204

@app.route('/movie_night/<name>', methods=['GET', 'POST'])
def movie_night(name):
    if request.method == 'POST':
        partner_name = request.form.get('partner_name')
        c.execute("SELECT name FROM users WHERE name=?", (partner_name,))
        partner = c.fetchone()
        if partner:
            user = User(name)
            user.find_date_night_partner(partner_name)
            user.create_date_night()
    c.execute("SELECT date_night_partner FROM users WHERE name=?", (name,))
    partner = c.fetchone()
    if partner:
        date_night_partner = partner[0]
        return render_template('movie_night.html', name=name, date_night_partner=date_night_partner)
    else:
        return 'User not found', 404

if __name__ == '__main__':
    app.run(debug=True)
