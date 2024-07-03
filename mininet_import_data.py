# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:36:22 2024

@author: UgoGard
"""

import sqlite3


def insert_into_subscriptions():
    data = [
        (1, 'HD', 12.00, 1),
        (2, 'UHD', 18.00, 1)
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Subscriptions (SubscriptionID, PlanName, Price, Duration) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'Subscriptions' table successfully.")


def insert_into_users():
    data = [
        (1, 'john_doe', 'john@example.com', 'password1', 'New York', 'USA', 28, 1),
        (2, 'alice_smith', 'alice@example.com', 'password2', 'Los Angeles', 'USA', 34, 1),
        (3, 'jane_doe', 'jane@example.com', 'password3', 'Chicago', 'USA', 21, 2),
        (4, 'bob_jones', 'bob@example.com', 'password4', 'Boston', 'USA', 30, 2),
        (5, 'emma_johnson', 'emma@example.com', 'password5', 'San Francisco', 'USA', 25, 1)
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Users (UserID, Username, Email, Password, City, Country, Age, SubscriptionID) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'Users' table successfully.")


def insert_into_movies():
    data = [
        (1, 'Stranger Things', 'Sci-Fi', '2016-07-15'),
        (2, 'Breaking Bad', 'Drama', '2008-01-20'),
        (3, 'The Office', 'Comedy', '2005-03-24'),
        (4, 'Parks and Recreation', 'Comedy', '2009-04-09'),
        (5, 'The Godfather', 'Crime', '1972-03-24')
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Movies (MovieID, Title, Genre, ReleaseDate) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'Movies' table successfully.")


def insert_into_actors():
    data = [
        (1, 'Millie Bobby Brown', 'Los Angeles', '2004-02-19', 20),
        (2, 'Bryan Cranston', 'Hollywood', '1956-03-07', 68),
        (3, 'Winona Ryder', 'New York', '1971-10-29', 52),
        (4, 'Aaron Paul', 'Boise', '1979-08-27', 44),
        (5, 'David Harbour', 'White Plains', '1975-04-10', 49)
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Actors (ActorID, Name, City, DateOfBirth, Age) VALUES (?, ?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'Actors' table successfully.")


def insert_into_reviews():
    data = [
        (1, 1, 1, 5, 'Amazing show!'),
        (2, 2, 2, 3, 'Good show'),
        (3, 3, 3, 4, 'Funny and smart'),
        (4, 4, 4, 2, 'Not my taste'),
        (5, 5, 5, 5, 'A classic!')
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO Reviews (ReviewID, UserID, MovieID, Score, Comment) VALUES (?, ?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'Reviews' table successfully.")


def insert_into_favorite_movies():
    data = [
        (1, 1, 3, 5),
        (2, 1, 4, 4),
        (3, 2, 5, 3),
        (4, 3, 1, 5),
        (5, 4, 2, 4)
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO FavoriteMovies (FavoriteID, UserID, MovieID, Score) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'FavoriteMovies' table successfully.")


def insert_into_movie_actors():
    data = [
        (1, 1, 1, 'Eleven'),
        (2, 2, 2, 'Walter White'),
        (3, 1, 3, 'Joyce Byers'),
        (4, 2, 4, 'Jesse Pinkman'),
        (5, 1, 5, 'Jim Hopper')
    ]
    connection = sqlite3.connect('mininet.db')
    cursor = connection.cursor()
    cursor.executemany("INSERT INTO MovieActors (MovieActorID, MovieID, ActorID, Role) VALUES (?, ?, ?, ?)", data)
    connection.commit()
    connection.close()
    print("Data inserted into 'MovieActors' table successfully.")


# Main function to run all steps
def main():
    
    # Call the functions to insert data into each table
    insert_into_subscriptions()
    insert_into_users()
    insert_into_movies()
    insert_into_actors()
    insert_into_reviews()
    insert_into_favorite_movies()
    insert_into_movie_actors()
    
if __name__ == "__main__":
    main()