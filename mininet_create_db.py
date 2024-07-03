# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3


def create_database():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    # Close the connection to the database
    connection.close()
    print("Database 'mininet.db' created successfully.")


def create_subscriptions_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the Subscriptions table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Subscriptions (
        SubscriptionID INTEGER PRIMARY KEY,
        PlanName TEXT NOT NULL,
        Price REAL NOT NULL,
        Duration INTEGER NOT NULL
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'Subscriptions' created successfully.")


def create_users_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the Users table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Users (
        UserID INTEGER PRIMARY KEY,
        Username TEXT NOT NULL,
        Email TEXT NOT NULL,
        Password TEXT NOT NULL,
        City TEXT NOT NULL,
        Country TEXT NOT NULL,
        Age INTEGER NOT NULL,
        SubscriptionID INTEGER,
        FOREIGN KEY (SubscriptionID) REFERENCES Subscriptions(SubscriptionID)
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'Users' created successfully.")


def create_movies_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the Movies table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Movies (
        MovieID INTEGER PRIMARY KEY,
        Title TEXT NOT NULL,
        Genre TEXT NOT NULL,
        ReleaseDate TEXT NOT NULL
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'Movies' created successfully.")


def create_actors_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the Actors table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Actors (
        ActorID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        City TEXT NOT NULL,
        DateOfBirth TEXT NOT NULL,
        Age INTEGER NOT NULL
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'Actors' created successfully.")


def create_reviews_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the Reviews table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Reviews (
        ReviewID INTEGER PRIMARY KEY,
        UserID INTEGER,
        MovieID INTEGER,
        Score INTEGER CHECK (Score BETWEEN 0 AND 5),
        Comment TEXT,
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'Reviews' created successfully.")


def create_favorite_movies_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the FavoriteMovies table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS FavoriteMovies (
        FavoriteID INTEGER PRIMARY KEY,
        UserID INTEGER,
        MovieID INTEGER,
        Score INTEGER CHECK (Score BETWEEN 0 AND 5),
        FOREIGN KEY (UserID) REFERENCES Users(UserID),
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID)
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'FavoriteMovies' created successfully.")


def create_movie_actors_table():
    # Connect to the SQLite database. If the database does not exist, it will be created.
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()

    # SQL query to create the MovieActors table
    create_table_query = """
    CREATE TABLE IF NOT EXISTS MovieActors (
        MovieActorID INTEGER PRIMARY KEY,
        MovieID INTEGER,
        ActorID INTEGER,
        Role TEXT NOT NULL,
        FOREIGN KEY (MovieID) REFERENCES Movies(MovieID),
        FOREIGN KEY (ActorID) REFERENCES Actors(ActorID)
    );
    """

    # Execute the query to create the table
    cursor.execute(create_table_query)
    
    # Commit the transaction
    connection.commit()

    # Close the connection
    connection.close()

    print("Table 'MovieActors' created successfully.")


# Main function to run all steps
def main():
    
    # Call the function to create the database
    create_database()

    # Call the function to create the tables
    create_subscriptions_table()
    create_users_table()
    create_movies_table()
    create_actors_table()
    create_reviews_table()
    create_favorite_movies_table()
    create_movie_actors_table()

    
if __name__ == "__main__":
    main()