# Author: Kyle Klausen
# Date: 07/04/25
# Assignment7_2
# Description: The code connects to a MySQL database and retrieves data from studio, genre, and movie tables.

import mysql.connector

def main():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="KyleKKlausen@24865", 
        database="movies"
    )

    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    print("-- DISPLAYING Studio RECORDS --")
    cursor.execute("SELECT studio_id, studio_name FROM studio") 
    studios = cursor.fetchall()
    for studio in studios:
        print(f"Studio ID: {studio[0]}")
        print(f"Studio Name: {studio[1]}\n")

    # Query 2: Select all fields from the genre table
    print("-- DISPLAYING Genre RECORDS --")
    cursor.execute("SELECT genre_id, genre_name FROM genre") 
    genres = cursor.fetchall()
    for genre in genres:
        print(f"Genre ID: {genre[0]}")
        print(f"Genre Name: {genre[1]}\n")

    # Query 3: Select movie names for movies with runtime less than 2 hours (120 minutes)
    print("-- DISPLAYING Short Film RECORDS --")
    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    short_movies = cursor.fetchall()
    for film in short_movies:
        print(f"Film Name: {film[0]}")
        print(f"Runtime: {film[1]}\n")

    # Query 4: Get a list of film names and directors grouped by director
    print("-- DISPLAYING Director RECORDS in Order --")
    cursor.execute("""
        SELECT film_director, film_name
        FROM film
        ORDER BY film_director, film_name;
    """)
    films_by_director_raw = cursor.fetchall()

    # Grouping logic for director and films to match the requested output format
    films_by_director_grouped = {}
    for director_name, film_name in films_by_director_raw:
        if director_name not in films_by_director_grouped:
            films_by_director_grouped[director_name] = []
        films_by_director_grouped[director_name].append(film_name)

    for director, films in films_by_director_grouped.items():
        print(f"Director: {director}")
        for film in films:
            print(f"  Film Name: {film}")
        print() # Add a blank line for separation

    cursor.close()
    db.close()

if __name__ == "__main__":
    main()