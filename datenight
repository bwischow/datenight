import tkinter as tk
import random

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

class MovieNightApp:
    def __init__(self, root):
        self.root = root
        self.users = {}
        self.create_user_ui()

    def create_user_ui(self):
        self.user_label = tk.Label(self.root, text="Create User Account")
        self.user_label.pack()

        self.user_entry = tk.Entry(self.root)
        self.user_entry.pack()

        self.create_user_button = tk.Button(self.root, text="Create User", command=self.create_user)
        self.create_user_button.pack()

    def create_user(self):
        name = self.user_entry.get()
        if name:
            self.users[name] = User(name)
            self.user_label.config(text=f"User {name} created")
            self.create_date_night_ui(name)
        else:
            self.user_label.config(text="Please enter a name")

    def create_date_night_ui(self, name):
        self.date_night_label = tk.Label(self.root, text="Create Date Night")
        self.date_night_label.pack()

        self.find_partner_label = tk.Label(self.root, text="Find Date Night Partner")
        self.find_partner_label.pack()

        self.partner_entry = tk.Entry(self.root)
        self.partner_entry.pack()

        self.find_partner_button = tk.Button(self.root, text="Find Partner", command=lambda: self.find_date_night_partner(name))
        self.find_partner_button.pack()

    def create_date_night(self, name):
        if name in self.users:
            self.users[name].create_date_night()
            self.date_night_label.config(text=f"Date Night created with {self.users[name].partner}")
            self.create_movie_night_ui(name)
        else:
            self.date_night_label.config(text="User not found")

    def find_date_night_partner(self, name):
        partner_name = self.partner_entry.get()
        if partner_name in self.users:
            self.users[name].find_date_night_partner(partner_name)
            self.find_partner_label.config(text=f"Date Night partner found: {partner_name}")
            self.create_date_night(name)
        else:
            self.find_partner_label.config(text="Partner not found")

    def create_movie_night_ui(self, name):
        self.movie_label = tk.Label(self.root, text="")
        self.movie_label.pack()

        self.watch_button = tk.Button(self.root, text="Watch", command=lambda: self.watch_movie(name))
        self.watch_button.pack(side=tk.LEFT)

        self.skip_button = tk.Button(self.root, text="Skip", command=lambda: self.skip_movie(name))
        self.skip_button.pack(side=tk.RIGHT)

        self.next_movie(name)

    def next_movie(self, name):
        if self.users[name].date_night is None:
            self.movie_label.config(text="Create or find a date night first!")
        else:
            self.users[name].date_night.next_movie()
            self.movie_label.config(text=self.users[name].date_night.current_movie)

    def watch_movie(self, name):
        if self.users[name].date_night is not None:
            self.users[name].date_night.movies_list.remove(self.users[name].date_night.current_movie)
            if not self.users[name].date_night.movies_list:
                self.movie_label.config(text="No more movies!")
            else:
                self.next_movie(name)

    def skip_movie(self, name):
        self.next_movie(name)

root = tk.Tk()
app = MovieNightApp(root)
root.mainloop()
