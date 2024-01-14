class Film:
    # Class variable to store information about all films
    films = []

    def __init__(self, title, director):
        self.title = title
        self.director = director
        # Adding the film to the class variable films
        Film.films.append(self)

    @classmethod
    def films_by_director(cls, director):
        # Filter films based on the given director
        return [film for film in cls.films if film.director == director]


# Creating instances of the Film class
film1 = Film("Inception", "Christopher Nolan")
film2 = Film("The Shawshank Redemption", "Frank Darabont")
film3 = Film("The Dark Knight", "Christopher Nolan")
film4 = Film("Pulp Fiction", "Quentin Tarantino")

# Using the class method to get films by a specific director
films_by_nolan = Film.films_by_director("Christopher Nolan")

# Printing the results
for film in films_by_nolan:
    print(f"{film.title} directed by {film.director}")
