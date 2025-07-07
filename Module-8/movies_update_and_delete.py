# Author: Kyle Klausen
# Assignment8_2
# Date: 07/05/25
# Description: Displays, inserts, updates, and deletes movie records in a MySQL database using Python and joins.

import mysql.connector
from mysql.connector import errorcode
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Database config from .env
config = {
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "host": os.getenv("DB_HOST"),
    "database": os.getenv("DB_NAME"),
    "raise_on_warnings": True
}

# Function to show films
def show_films(cursor, title):
    # SQL with INNER JOINs to get genre and studio names
    query = """
        SELECT film_name AS Name,
               film_director AS Director,
               genre_name AS Genre,
               studio_name AS Studio
        FROM film
        INNER JOIN genre ON film.genre_id = genre.genre_id
        INNER JOIN studio ON film.studio_id = studio.studio_id
    """
    
    cursor.execute(query)
    films = cursor.fetchall()

    # --- MODIFIED FORMATTING HERE ---
    print("\n--- {} ---".format(title)) # Changed header dashes
    for film in films:
        print("Film Name: {}".format(film[0]))      # Changed label and added newline
        print("Director: {}".format(film[1]))
        print("Genre Name ID: {}".format(film[2]))  # Changed label
        print("Studio Name: {}".format(film[3]))    # Changed label
        print() # Added a blank line for spacing between films
    # --- END MODIFIED FORMATTING ---

try:
    # Connect to the movies database
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Initial display
    show_films(cursor, "DISPLAYING FILMS")

    # Insert new film (Make sure the studio_id and genre_id exist in your DB)
    # Note: The expected output image shows 'Star Wars' inserted, your script inserts 'Inception'.
    # This example keeps 'Inception' as per your original script.
    cursor.execute("""
        INSERT INTO film (film_name, film_releaseDate, film_runtime, film_director, studio_id, genre_id)
        VALUES ('Inception', '2010', 148, 'Christopher Nolan', 3, 2)
    """)
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER INSERT")

    # Update Alien to Horror (find genre_id for Horror)
    cursor.execute("UPDATE film SET genre_id = 1 WHERE film_name = 'Alien'")
    db.commit()

    # The expected output image has "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror"
    show_films(cursor, "DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror")

    # Delete Gladiator
    cursor.execute("DELETE FROM film WHERE film_name = 'Gladiator'")
    db.commit()

    show_films(cursor, "DISPLAYING FILMS AFTER DELETE") # Expected output uses just "DISPLAYING FILMS AFTER DELETE"

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Invalid credentials")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    try:
        if cursor:
            cursor.close()
        if db:
            db.close()
    except NameError:
        pass