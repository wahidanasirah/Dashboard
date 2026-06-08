import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

st.image(r'C:\Users\welcome\Desktop\BSMS1306\streamlit\h.jpg')
st.image('h.jpg')
st.set_page_config(page_title="Student Performance Dashboard", layout="wide")

st.title("📊 Student Performance Analytics Dashboard")
st.write("Welcome! This interactive dashboard visualizes student performance data based on various demographic factors.")
st.date_input("Select a date")

df = pd.read_csv("cleaned_students_performance.csv")

st.subheader("Raw Data")
st.write(df)

st.subheader("Histogram")
fig, ax = plt.subplots(figsize = (10,6))
ax.hist(df['writing score'], bins=10, alpha=0.5, label='writing', color='pink')
ax.hist(df['reading_score'], bins=10, alpha=0.5, label='Reading', color='silver')
ax.set_title('Distribution of Student Scores')
ax.set_xlabel('Score')
ax.set_ylabel('Frequency')
ax.legend()
st.pyplot(fig)

st.subheader("Gender Distribution")
fig, ax = plt.subplots(figsize = (10,6))
df.groupby('gender').size().plot(kind='pie', autopct='%1.0f%%', ax=ax)
ax.set_title('Gender Distribution')
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("Test Preparation Course")
fig, ax = plt.subplots(figsize = (10,6))
colors = ['pink', 'silver']
explode = (0.05, 0.05)
df.groupby('test_preparation_course').size().plot(kind='pie', autopct='%1.0f%%', colors=colors, explode=explode, ax=ax)
ax.set_title('Test Preparation Course')
ax.set_ylabel('')
st.pyplot(fig)

st.subheader("Maximum Average Score by Lunch Type")
fig, ax = plt.subplots(figsize = (10,6))
lunch_max = df.groupby('lunch')['average_score'].max()
lunch_max.plot(kind='bar', ax=ax)
ax.set_title('Maximum Average Score by Lunch Type')
ax.set_xlabel('Lunch Type')
ax.set_ylabel('Maximum Average Score')
st.pyplot(fig)

st.subheader("Distribution of Parental Education Levels")
fig, ax = plt.subplots(figsize = (10,6))
df['parental_level_of_education'].value_counts().plot(kind='bar', ax=ax)
ax.set_title('Distribution of Parental Education Levels')
ax.set_xlabel('Parental Education Level')
ax.set_ylabel('Number of Students')
plt.xticks(rotation=45)
st.pyplot(fig)