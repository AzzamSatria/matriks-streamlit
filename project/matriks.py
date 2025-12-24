import streamlit as st
from streamlit_option_menu import option_menu
import time
import random
import pandas as pd
import altair as alt
import sys
sys.setrecursionlimit(100000)

def algoritmaIteratif(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            _ = matrix[i][j]

def algoritmaRekursif(matrix, i, j):
    if i == len(matrix):
        return
    if j == len(matrix[0]):
        algoritmaRekursif(matrix, i + 1, 0)
        return
    _ = matrix[i][j]
    algoritmaRekursif(matrix, i, j + 1)

def generate_matrix(baris, kolom, nilai_min, nilai_max):
    matrix = []
    for i in range(baris):
        row = []
        for j in range(kolom):
            row.append(random.randint(nilai_min, nilai_max))
        matrix.append(row)
    return matrix

with st.sidebar:
    menu = option_menu(
        "Menu",
        ["Iteratif", "Rekursif", "Perbandingan"],
        default_index=0
    )

st.title("Perbandingan Algoritma Iteratif dan Rekursif pada Matriks 2D")
st.subheader("Pengaturan Input")
min_val = st.number_input("Nilai Minimum", value=0)
max_val = st.number_input("Nilai Maksimum", value=10000)

m1 = st.number_input("Matriks 1 (n x n)", 1, 100)
m3 = st.number_input("Matriks 3 (n x n)", 1, 100)
m2 = st.number_input("Matriks 2 (n x n)", 1, 100)
m4 = st.number_input("Matriks 4 (n x n)", 1, 100)

ukuran = [m1, m2, m3, m4]
dataMatriks = []
for s in ukuran:
    dataMatriks.append(generate_matrix(s, s, min_val, max_val))

waktuIteratif = []
waktuRekursif = []

namaMatriks = ["Matriks 1", "Matriks 2", "Matriks 3", "Matriks 4"]
for matrix in dataMatriks:
    start = time.time()
    algoritmaIteratif(matrix)
    waktuIteratif.append(time.time() - start)

    start = time.time()
    algoritmaRekursif(matrix, 0, 0)
    waktuRekursif.append(time.time() - start)

if menu == "Iteratif":
    st.header("Waktu Eksekusi Iteratif")
    for i in range(4):
        st.subheader(f"{namaMatriks[i]} ({ukuran[i]} x {ukuran[i]})")
        st.write("Isi Matriks:")
        st.table(dataMatriks[i])  
        st.write(f"Waktu: {waktuIteratif[i]:.6f} detik")

if menu == "Rekursif":
    st.header("Waktu Eksekusi Rekursif")
    for i in range(4):
        st.subheader(f"{namaMatriks[i]} ({ukuran[i]} x {ukuran[i]})")
        st.write("Isi Matriks:")
        st.table(dataMatriks[i])
        st.write(f"Waktu: {waktuRekursif[i]:.6f} detik")

if menu == "Perbandingan":
    st.header("Perbandingan Iteratif vs Rekursif")

    df = pd.DataFrame({
    "Matriks": namaMatriks,
    "Iteratif": waktuIteratif,
    "Rekursif": waktuRekursif
    })

    df_long = df.melt("Matriks", var_name="Algoritma", value_name="Waktu")

    chart = alt.Chart(df_long).mark_bar().encode(
    x=alt.X("Matriks:N", title="Matriks"),
    xOffset="Algoritma:N",
    y=alt.Y("Waktu:Q", title="Waktu Eksekusi (detik)"),
    color="Algoritma:N"
    )
    st.altair_chart(chart, use_container_width=True)

    st.subheader("Detail Waktu Eksekusi")
    for i in range(4):
        st.write(
            f"{namaMatriks[i]} : ", f"Iteratif: {waktuIteratif[i]:.6f} detik | ", f"Rekursif: {waktuRekursif[i]:.6f} detik"
        )