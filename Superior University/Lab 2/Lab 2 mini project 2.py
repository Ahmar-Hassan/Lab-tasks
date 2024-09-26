
def add_movies(movie_list):
    num = int(input("How many movies would you like to add? "))
    for _ in range(num):
        name = input("Enter the movie name: ")
        budget = int(input("Enter the movie budget: "))
        movie_list.append((name, budget))


def analyze_movies(movie_list):
    if not movie_list:
        print("No movies to analyze.")
        return

    total_budget = sum(movie[1] for movie in movie_list)
    average_budget = total_budget / len(movie_list)

    high_budget_movies = [(movie[0], movie[1] - average_budget) for movie in movie_list if movie[1] > average_budget]

 
    print(f"\nAverage movie budget is: ${average_budget:.2f}\n")
    print("Movies with a budget higher than the average:")
    for movie in high_budget_movies:
        print(f"{movie[0]} is ${movie[1]:.2f} above average")

    print(f"\nTotal number of movies above average budget: {len(high_budget_movies)}")


movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]


add_movies(movies)


analyze_movies(movies)
