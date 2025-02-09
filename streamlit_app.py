import streamlit as st
import sqlite3

conn = sqlite3.connect("adat.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, nev TEXT, betu TEXT, orszag TEXT, varos TEXT, fiu TEXT, lany TEXT, noveny TEXT, allat TEXT, hires TEXT,hegy TEXT, viz TEXT,targy TEXT)")
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
    c.execute("INSERT INTO users (nev, betu , orszag , varos , fiu , lany , noveny , allat , hires ,hegy , viz ,targy) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (nev, betu , orszag , varos , fiu , lany , noveny , allat , hires ,hegy , viz ,targy))
    conn.commit()
    st.success("Sikeresen mentve!")
    st.rerun()


st.subheader("Tárolt adatok:")
c.execute("SELECT * FROM users")
rows = c.fetchall()
for row in rows:
    st.write(row)

# Adatok lekérdezése
def get_data():
    c.execute("SELECT * FROM users")
    return c.fetchall()




# Sor törlése
def delete_user(user_id):
    c.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()

st.title("SQLite adatbázis sor törlése")

# Meglévő adatok lekérdezése
data = get_data()

if data:
    # Felhasználó kiválasztása törléshez
    user_options = {f"{row[0]} - {row[1]} ({row[2]} )": row[0] for row in data}
    selected_user = st.selectbox("Válassz egy felhasználót törlésre:", list(user_options.keys()))

    # Kiválasztott user ID-je
    user_id = user_options[selected_user]

    # Törlés gomb
    if st.button("Felhasználó törlése"):
        delete_user(user_id)
        st.success("Felhasználó sikeresen törölve!")
        st.rerun()  # Az oldal újratöltése az adatok frissítéséhez

st.subheader("Adatok listája")
# st.write(get_data())