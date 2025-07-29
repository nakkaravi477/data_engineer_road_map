def update_movies_list():
    # Initial list
    movies = ["Inception", "The Matrix", "Interstellar", "The Godfather", "Parasite"]

    # Append two more titles
    movies.append("The Dark Knight")
    movies.append("Pulp Fiction")

    # Remove the third element (index 2)
    removed = movies.pop(2)  # This removes "Interstellar"

    # Print results
    print("Removed movie:", removed)
    print("Updated movies list:", movies)




def dict_operations():
    # Initial dictionary
    movie_years = {
        "Inception": 2010,
        "The Matrix": 1999,
        "The Godfather": 1972,
        "Parasite": 2019,
        "The Dark Knight": 2008,
        "Pulp Fiction": 1994
    }

    # Remove the oldest movie
    oldest = min(movie_years, key=movie_years.get)
    removed_year = movie_years.pop(oldest)

    # Print removed entry and remaining dict
    print(f"Removed oldest movie: {oldest} ({removed_year})")
    print("Updated movie_years:")
    for title, year in movie_years.items():
        print(f"Movie: {title}, Year: {year}")

def nested_collections():
    movie_list = [
        {"title": "Inception", "year": 2010, "rating": 8.8},
        {"title": "The Matrix", "year": 1999, "rating": 8.7},
        {"title": "The Godfather", "year": 1972, "rating": 9.2},
        {"title": "Parasite", "year": 2019, "rating": 8.6},
        {"title": "The Dark Knight", "year": 2008, "rating": 9.0},
        {"title": "Pulp Fiction", "year": 1994, "rating": 8.9}
    ]

    # Extract titles with rating ≥ 8.5
    high_rated = [m["title"] for m in movie_list if m["rating"] >= 8.5]
    print("High-rated movies (≥8.5):", high_rated)

    # Function to get movies by year
    def get_movie_by_year(movies, year):
        return [m["title"] for m in movies if m["year"] == year]

    # Test the function
    print("Movies from 1999:", get_movie_by_year(movie_list, 1999))
    print("Movies from 2010:", get_movie_by_year(movie_list, 2010))

def main():
    update_movies_list()
    print("-" * 40)
    dict_operations()
    print("-" * 40)
    nested_collections()
    print("-" * 40)

if __name__ == "__main__":
    main()