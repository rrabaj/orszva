import streamlit as st
import sqlite3

conn = sqlite3.connect("adatok.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (nev TEXT, eletkor INTEGER)")
conn.commit()

st.title("Adatfeltöltő táblázat")

nev = st.text_input("Név")
eletkor = st.number_input("Életkor", min_value=0, max_value=120, step=1)

if st.button("Mentés"):
    c.execute("INSERT INTO users (nev, eletkor) VALUES (?, ?)", (nev, eletkor))
    conn.commit()
    st.success("Sikeresen mentve!")

st.subheader("Tárolt adatok:")
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    st.write(row)
