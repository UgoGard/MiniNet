# MiniNet
This repository contains the documents and code used to implement the MiniNet project - Big Data Analytics


mininet_create_db.py

Description:
This script is responsible for creating the MiniNet database schema. It connects to a SQLite database named mininet.db and creates the necessary tables to store user data, subscription plans, movies, actors, user reviews, favorite movies, and actor-movie relationships.

Functions:
create_mininet_database(): Creates the mininet.db SQLite database.
create_users_table(): Creates the Users table.
create_subscriptions_table(): Creates the Subscriptions table.
create_movies_table(): Creates the Movies table.
create_actors_table(): Creates the Actors table.
create_reviews_table(): Creates the Reviews table.
create_favorite_movies_table(): Creates the FavoriteMovies table.
create_movie_actors_table(): Creates the MovieActors table.

mininet_import_data.py

Description:
This script imports initial data into the MiniNet database. It connects to the mininet.db SQLite database and populates the tables with predefined data. The script ensures that all necessary initial data is available for the application to function correctly.

Functions:
insert_into_subscriptions(): Inserts initial data into the Subscriptions table.
insert_into_users(): Inserts initial data into the Users table.
insert_into_movies(): Inserts initial data into the Movies table.
insert_into_actors(): Inserts initial data into the Actors table.
insert_into_reviews(): Inserts initial data into the Reviews table.
insert_into_favorite_movies(): Inserts initial data into the FavoriteMovies table.
insert_into_movie_actors(): Inserts initial data into the MovieActors table.

mininet.py

Description:
This script provides an interactive interface to query the MiniNet database. Users can select different options to retrieve information from the database, such as user subscriptions, actor-movie associations, and favorite movies. The script runs a series of SQL queries based on user input and displays the results.

Functions:
query_hd_subscriptions(): Queries and retrieves users based on their subscription type (HD or UHD).
query_actors_and_movies(): Retrieves all data about actors and their associated movies.
query_actors_grouped_by_city(): Groups actors by city and retrieves the count and average age for each city.
query_favorite_comedy_movies_for_user(): Retrieves all favorite comedy movies for a specified user.
query_subscription_count_per_country(): Counts the number of subscriptions per country.
Main Function:

main(): Interacts with the user, allowing them to choose different query options and displaying the results accordingly.
