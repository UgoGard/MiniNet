# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 19:31:56 2024

@author: UgoGard
"""

import sqlite3
import pandas as pd

def query_hd_subscriptions():
    """
    Queries the Users table to fetch users based on their subscription type.
    Prompts the user to select a subscription type.
    """
    # Prompt user to select subscription type
    subscription_id = input("HD Subscription is 1\nUHD Subscription is 2\nSelect Subscription: ")

    # Connect to the SQLite database
    connection = sqlite3.connect('mininet.db')
    
    # SQL query to fetch users with the specified subscription type
    query = "SELECT * FROM Users WHERE SubscriptionID = ?"
    
    # Execute the query and fetch the results into a DataFrame
    df = pd.read_sql_query(query, connection, params=(subscription_id,))
    
    # Close the database connection
    connection.close()
    
    return df

def query_actors_and_movies():
    """
    Queries the Actors and Movies tables to fetch all data about actors and their associated movies.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect('mininet.db')
    
    # SQL query to fetch actors and their associated movies
    query = """
    SELECT Actors.ActorID, Actors.Name, Actors.City, Actors.DateOfBirth, Movies.MovieID, Movies.Title, Movies.Genre, Movies.ReleaseDate
    FROM Actors
    JOIN MovieActors ON Actors.ActorID = MovieActors.ActorID
    JOIN Movies ON MovieActors.MovieID = Movies.MovieID
    """
    
    # Execute the query and fetch the results into a DataFrame
    df = pd.read_sql_query(query, connection)
    
    # Close the database connection
    connection.close()
    
    return df

def query_actors_grouped_by_city():
    """
    Queries the Actors table to group actors by city and fetch the count and average age for each city.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect('mininet.db')
    
    # SQL query to group actors by city and fetch the count and average age
    query = """
    SELECT City, COUNT(*) AS NumberOfActors, AVG(Age) AS AverageAge
    FROM Actors
    GROUP BY City
    """
    
    # Execute the query and fetch the results into a DataFrame
    df = pd.read_sql_query(query, connection)
    
    # Close the database connection
    connection.close()
    
    return df

def query_favorite_comedy_movies_for_user():
    """
    Queries the FavoriteMovies and Movies tables to fetch all favorite comedy movies for a specific user.
    Prompts the user to enter a username.
    """
    # Prompt user to enter a username
    username = input("\nEnter a username: ")
    
    # Connect to the SQLite database
    connection = sqlite3.connect('mininet.db')
    
    # SQL query to fetch favorite comedy movies for the specified user
    query = """
    SELECT Users.Username, Movies.MovieID, Movies.Title, Movies.Genre, Movies.ReleaseDate
    FROM FavoriteMovies
    JOIN Users ON FavoriteMovies.UserID = Users.UserID
    JOIN Movies ON FavoriteMovies.MovieID = Movies.MovieID
    WHERE Movies.Genre = 'Comedy' AND Users.Username = ?
    """
    
    # Execute the query and fetch the results into a DataFrame
    df = pd.read_sql_query(query, connection, params=(username,))
    
    # Close the database connection
    connection.close()
    
    return df

def query_subscription_count_per_country():
    """
    Queries the Users table to count the number of subscriptions per country.
    """
    # Connect to the SQLite database
    connection = sqlite3.connect('mininet.db')
    
    # SQL query to count the number of subscriptions per country
    query = """
    SELECT Country, COUNT(*) AS SubscriptionCount
    FROM Users
    GROUP BY Country
    """
    
    # Execute the query and fetch the results into a DataFrame
    df = pd.read_sql_query(query, connection)
    
    # Close the database connection
    connection.close()
    
    return df

# Main function to run all steps
def main():
    """
    Main function to interact with the user and run the appropriate queries based on user input.
    """
    # Welcome message
    print("\nBonjour !")
    
    action = ''

    # User interactions
    while action != 'quit':
        action = input("\nIf you want information about users per subscription enter '1',\n"
                       "If you want information about actors and their associated movies enter '2',\n"
                       "If you want information about the number of actors per city and the average age (per city) enter '3',\n"
                       "If you want information about the favourite comedy movies for a specific user enter '4',\n"
                       "If you want information about the number of subscriptions per country enter '5',\n"
                       "If you want to quit enter 'quit'.\n"
                       "\nEnter your choice: ")
        
        if action == '1':
            # Call the function to query the database according to user input
            df = query_hd_subscriptions()
            
            if df.empty:
                print("\nNo data found")
            else:
                print("\n", df.to_string(index=False))
        
        elif action == '2':
            # Call the function to query the database according to user input
            df = query_actors_and_movies()
            
            if df.empty:
                print("\nNo data found")
            else:
                print("\n", df.to_string(index=False))
                
        elif action == '3':
            # Call the function to query the database according to user input
            df = query_actors_grouped_by_city()
            if df.empty:
                print("\nNo data found")
            else:
                print("\n", df.to_string(index=False))

        elif action == '4':
            # Call the function to query the database according to user input
            df = query_favorite_comedy_movies_for_user()
            
            if df.empty:
                print("\nNo data found")
            else:
                print("\n", df.to_string(index=False))
            
        elif action == '5':
            # Call the function to query the database according to user input
            df = query_subscription_count_per_country()
            
            if df.empty:
                print("\nNo data found")
            else:
                print("\n", df.to_string(index=False))
            
        elif action == 'quit':
            # Exit message
            print("\nAu revoir !")
            
        else:
            # Handle invalid input
            print("\nInvalid input")

# Execute the main function
if __name__ == "__main__":
    main()