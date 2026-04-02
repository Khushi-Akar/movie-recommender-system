import streamlit as st
import pandas as pd
import pickle
import requests
import gzip

# Function to fetch movie poster
def fetch_poster(movie_id):
    response = requests.get(f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=90ee519131350ebeefdbf9c8990c196e")
    data = response.json()
    return "https://image.tmdb.org/t/p/w185" + data['poster_path']

# Function to recommend movies
def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    recommended_movies_posters = []

    for i in distances[1:6]:  # Top 5 recommendations
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters

# Load data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
with gzip.open('similarity.pkl.gz', 'rb') as f:
    similarity = pickle.load(f)

# Streamlit UI
st.title('Movie Recommender System')

selected_movie_name = st.selectbox('Select a movie:', movies['title'].values)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    # Display recommended movies in columns
    cols = st.columns(5)
    for col, name, poster in zip(cols, names, posters):
        with col:
            st.text(name)
            st.image(poster)
