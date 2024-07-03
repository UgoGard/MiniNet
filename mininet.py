# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:31:56 2024

@author: UgoGard
"""

import sqlite3
import pandas as pd


def query_hd_subscriptions():
    connection = sqlite3.connect('mininet.db')
    query = "SELECT * FROM Users WHERE SubscriptionID = 1"
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def query_actors_and_movies():
    connection = sqlite3.connect('mininet.db')
    query = """
    SELECT Actors.ActorID, Actors.Name, Actors.City, Actors.DateOfBirth, Movies.MovieID, Movies.Title, Movies.Genre, Movies.ReleaseDate
    FROM Actors
    JOIN MovieActors ON Actors.ActorID = MovieActors.ActorID
    JOIN Movies ON MovieActors.MovieID = Movies.MovieID
    """
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def query_actors_grouped_by_city():
    connection = sqlite3.connect('mininet.db')
    query = """
    SELECT City, COUNT(*) AS NumberOfActors, AVG(Age) AS AverageAge
    FROM Actors
    GROUP BY City
    """
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


def query_favorite_comedy_movies_for_user(username):
    connection = sqlite3.connect('mininet.db')
    query = """
    SELECT Users.Username, Movies.MovieID, Movies.Title, Movies.Genre, Movies.ReleaseDate
    FROM FavoriteMovies
    JOIN Users ON FavoriteMovies.UserID = Users.UserID
    JOIN Movies ON FavoriteMovies.MovieID = Movies.MovieID
    WHERE Movies.Genre = 'Comedy' AND Users.Username = ?
    """
    df = pd.read_sql_query(query, connection, params=(username,))
    connection.close()
    return df


def query_subscription_count_per_country():
    connection = sqlite3.connect('mininet.db')
    query = """
    SELECT Country, COUNT(*) AS SubscriptionCount
    FROM Users
    GROUP BY Country
    """
    df = pd.read_sql_query(query, connection)
    connection.close()
    return df


# Main function to run all steps
def main():
    
    # Welcome message
    print("\nBonjour !")
    
    action = ''

    # User interactions
    while action != 'quit':
        action = input("\nIf you want information about users in the HD subscriptions enter '1',\n"
                       "If you want information about actors and their associated movies enter '2',\n"
                       "If you want information about the number of actors from a specific city and the average age (per city). enter '3',\n"
                       "If you want information about the favourite comedy movies for a specific user. enter '4'',\n"
                       "If you want information about the number of subscriptions per country enter '5',\n"
                       "If you want to quit enter 'quit'.\n"
                       "\nEnter your choice: ")

    # Call the function to query the database according to user input
    df_hd_subscriptions = query_hd_subscriptions()
    df_actors_and_movies = query_actors_and_movies()
    df_actors_grouped_by_city = query_actors_grouped_by_city()
    df_favorite_comedy_movies = query_favorite_comedy_movies_for_user('john_doe')
    df_subscription_count_per_country = query_subscription_count_per_country()


if __name__ == "__main__":
    main()