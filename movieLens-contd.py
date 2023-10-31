import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


pd.options.display.max_rows = 10

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('users.dat', sep='::', #filename, sep, header, names
                      header=None, names=unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('ratings.dat', sep='::',
                        header=None, names=rnames)

mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('movies.dat', sep='::',
                       header=None, names=mnames)
data= pd.merge(pd.merge(ratings, users), movies)
# print(data)



# /////////////////////////////////////////////////////////////////////////////
# Exercise:
# /////////////////////////////////////////////////////////////////////////////

# 1) Create a bar chart showing the number of ratings for each movie (Top 10 movies). 

movie_ratings = data['title'].value_counts()
# print(movie_ratings)

# Select the top 10 movies with the most ratings
top_10_movies = movie_ratings.head(10)

# Create a bar chart
plt.figure(figsize=(12, 6))
top_10_movies.plot(kind='bar', color='skyblue')
plt.title('Top 10 Movies with the Most Ratings')
plt.xlabel('Movie Title')
plt.ylabel('Number of Ratings')
plt.xticks(rotation=45, ha='right')
plt.show()



# 2) Plot a pie chart showing the distribution of users based on gender. Advanced Operations:

# Count the number of users for each gender category
gender_distribution = data['gender'].value_counts()
# print(gender_distribution)
# Create a pie chart
plt.figure(figsize=(6, 6))
colors = ['lightcoral', 'lightskyblue']
explode = (0.1, 0)  # Explode the first slice (Female)

# Plot the pie chart
plt.pie(gender_distribution, labels=gender_distribution.index, colors=colors, explode=explode,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Distribution of Users Based on Gender')
plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()



# 3) For each user, find out their most frequently rated genre. 
user_by_genre = data.groupby('user_id')['genres'].apply(lambda x: x.str.split('|').explode().mode()[0] if not x.empty else None)
user_by_genre = user_by_genre.dropna()
user_by_genre = pd.DataFrame({'user_id': user_by_genre.index, 'MostFrequentGenre': user_by_genre.values})
print(user_by_genre)



# 4 ) Are there any users who have rated the same movie multiple times? If so, list them.
duplicate_ratings = data.groupby(['user_id', 'movie_id']).size().reset_index(name='count')

# display counted rated movie_id's
print(duplicate_ratings)

# Filter the users who have rated the same movie multiple times
users_with_multiple_ratings = duplicate_ratings[duplicate_ratings['count'] > 1]

# Display the users with multiple ratings for the same movie
print(users_with_multiple_ratings)

