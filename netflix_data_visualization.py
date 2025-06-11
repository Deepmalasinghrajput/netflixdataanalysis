import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("📊 Netflix Data Visualization")

# Load the CSV
df = pd.read_csv("netflix_titles.csv")

# Clean data
df = df.dropna(subset=['type', 'release_year', 'rating', 'country', 'duration'])

# Type count (Movies vs TV Shows)
st.subheader("1. Number of Movies vs TV Shows on Netflix")
type_counts = df['type'].value_counts()
fig1, ax1 = plt.subplots()
ax1.bar(type_counts.index, type_counts.values, color=['skyblue', 'orange'])
ax1.set_title('Number of Movies vs TV Shows')
ax1.set_xlabel('Type')
ax1.set_ylabel('Count')
st.pyplot(fig1)

# Content Ratings
st.subheader("2. Percentage of Content Ratings")
rating_counts = df['rating'].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
ax2.set_title('Content Ratings')
st.pyplot(fig2)

# Movie durations
st.subheader("3. Movie Duration Distribution")
movie_df = df[df['type'] == 'Movie'].copy()
movie_df['duration_int'] = movie_df['duration'].str.replace('min', '').astype(int)
fig3, ax3 = plt.subplots()
ax3.hist(movie_df['duration_int'], bins=30, color='seagreen', edgecolor='black')
ax3.set_title('Movie Duration Distribution')
ax3.set_xlabel('Duration (minutes)')
ax3.set_ylabel('Number of Movies')
st.pyplot(fig3)

# Release year vs show count
st.subheader("4. Release Year vs Number of Shows")
release_counts = df['release_year'].value_counts().sort_index()
fig4, ax4 = plt.subplots()
ax4.scatter(release_counts.index, release_counts.values, color='red')
ax4.set_title('Release Year vs Number of Shows')
ax4.set_xlabel('Release Year')
ax4.set_ylabel('Number of Shows')
st.pyplot(fig4)

# Top 10 countries
st.subheader("5. Top 10 Countries by Number of Shows")
country_counts = df['country'].value_counts().head(10)
fig5, ax5 = plt.subplots()
ax5.barh(country_counts.index, country_counts.values, color='teal')
ax5.set_title('Top 10 Countries')
ax5.set_xlabel('Number of Shows')
ax5.set_ylabel('Country')
st.pyplot(fig5)

# Movies vs TV Shows Over the Years
st.subheader("6. Movies vs TV Shows Released Over Years")
content_by_year = df.groupby(['release_year', 'type']).size().unstack().fillna(0)
fig6, ax6 = plt.subplots()
ax6.plot(content_by_year.index, content_by_year['Movie'], color='blue', label='Movies')
ax6.plot(content_by_year.index, content_by_year['TV Show'], color='gold', label='TV Shows')
ax6.set_title('Movies and TV Shows Over the Years')
ax6.set_xlabel('Year')
ax6.set_ylabel('Count')
ax6.legend()
st.pyplot(fig6)
