# by Kami Bigdely
# Actor class
class Actor:
    def __init__(self, first_name, last_name, birth_year, movies, email):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.movies = movies
        self.email = email

    def is_young(self):
        return self.birth_year > 1985

    def display(self):
        print(self.first_name, self.last_name)
        print('Movies Played: ', end='')
        for m in self.movies:
            print(m, end=', ')
        print()

    def send_hiring_email(self):
        print("email sent to: ", self.email)

actors = [
    Actor(
        'elizabeth',
        'debicki',
        1990,
        ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
        'deb@makeschool.com',
    ),
    Actor(
        'Jim',
        'Carrey',
        1962,
        ['Ace Ventura', 'The Mask', 'Dubm and Dumber', 'The Truman Show', 'Yes Man'],
        'jim@makeschool.com',
    ),
]

for actor in actors:
    if actor.is_young():
        actor.display()
        actor.send_hiring_email()
