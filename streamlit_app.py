import streamlit as st
import sqlite3

conn = sqlite3.connect("adat.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (nev TEXT, betu TEXT, orszag TEXT, varos TEXT, fiu TEXT, lany TEXT, noveny TEXT, allat TEXT, hires TEXT,hegy TEXT, viz TEXT,targy TEXT)")
conn.commit()

st.title("Ország város játék")

nev = st.text_input("Név")
betu = st.text_input("Betű")
orszag = st.text_input("Ország")
varos = st.text_input("Város")
fiu = st.text_input("Fiú")
lany = st.text_input("Lány")
noveny = st.text_input("Növény")
allat = st.text_input("Állat")
hires = st.text_input("Híres ember")
hegy = st.text_input("Hegy")
viz = st.text_input("Víz")
targy = st.text_input("Tárgy")

if st.button("Mentés"):
    c.execute("INSERT INTO users (nev, betu , orszag , varos , fiu , lany , noveny , allat , hires ,hegy , viz ,targy) VALUES (?, ?)", (nev, betu , orszag , varos , fiu , lany , noveny , allat , hires ,hegy , viz ,targy))
    conn.commit()
    st.success("Sikeresen mentve!")

st.subheader("Tárolt adatok:")
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    st.write(row)
