import streamlit as st
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import csv
import os

# Initialize Sentiment Analyzer
nltk.download("vader_lexicon")
sia = SentimentIntensityAnalyzer()

# Database setup
conn = sqlite3.connect("mood_tracker.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )
''')
cursor.execute('''
    CREATE TABLE IF NOT EXISTS moods (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        mood TEXT,
        note TEXT,
        date TEXT,
        sentiment REAL,
        FOREIGN KEY(username) REFERENCES users(username)
    )
''')
conn.commit()

# Authentication
st.title("😃 Mood Tracker App")
st.sidebar.header("User Authentication")
username = st.sidebar.text_input("Username")
password = st.sidebar.text_input("Password", type="password")

if st.sidebar.button("Login/Register"):
    cursor.execute("SELECT * FROM users WHERE username=?", (username,))
    user = cursor.fetchone()
    if user:
        st.sidebar.success("Logged in successfully!")
    else:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        st.sidebar.success("User registered successfully!")

if username:
    st.subheader(f"Welcome, {username}!")
    
    # Mood Logging
    mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Neutral", "Angry", "Excited"])
    note = st.text_area("Add a note (Optional)")
    
    # AI Mood Prediction
    sentiment_score = sia.polarity_scores(note)["compound"]
    predicted_mood = "Positive" if sentiment_score > 0 else "Negative" if sentiment_score < 0 else "Neutral"
    st.write(f"AI Predicted Mood: {predicted_mood}")
    
    if st.button("Save Entry"):
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cursor.execute("INSERT INTO moods (username, mood, note, date, sentiment) VALUES (?, ?, ?, ?, ?)",
                       (username, mood, note, date, sentiment_score))
        conn.commit()
        st.success("Mood logged successfully!")

    # Display Past Entries
    st.subheader("📅 Mood History")
    df = pd.read_sql_query("SELECT * FROM moods WHERE username=? ORDER BY date DESC", conn, params=(username,))

    if not df.empty:
        st.dataframe(df[["date", "mood", "note"]])
        
        # Mood Count Visualization
        st.subheader("📊 Mood Distribution")
        mood_counts = df["mood"].value_counts()
        fig, ax = plt.subplots()
        mood_counts.plot(kind="bar", color=["green", "red", "gray", "orange", "blue"], ax=ax)
        st.pyplot(fig)
        
        # Sentiment Trend Analysis
        st.subheader("📈 Sentiment Trend Over Time")
        df["date"] = pd.to_datetime(df["date"])
        df.sort_values("date", inplace=True)
        fig, ax = plt.subplots()
        ax.plot(df["date"], df["sentiment"], marker="o", linestyle="-")
        ax.axhline(0, color="black", linestyle="--")  # Neutral sentiment line
        st.pyplot(fig)

        # Export Data as CSV
        st.subheader("📤 Export Data")
        if st.button("Download CSV"):
            csv_path = "mood_data.csv"
            df.to_csv(csv_path, index=False)
            st.download_button(
                label="Download CSV",
                data=open(csv_path, "rb").read(),
                file_name="mood_data.csv",
                mime="text/csv"
            )
    else:
        st.info("No mood entries found. Start tracking today!")

# Close DB Connection
conn.close()
