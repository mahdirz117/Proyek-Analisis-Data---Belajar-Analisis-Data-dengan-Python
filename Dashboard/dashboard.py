import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


# Memuat data dari URL CSV
url = "https://raw.githubusercontent.com/mahdirz117/Proyek-Analisis-Data---Belajar-Analisis-Data-dengan-Python/main/Bike-sharing-dataset/day.csv"
bike_df = pd.read_csv(url)

# Judul aplikasi
st.title("Analisis Dataset Bike Sharing")

# Sidebar untuk filter dan pengaturan
with st.sidebar:
    st.subheader('Bike Sharing :sparkles:')
    st.image("https://www.sefiles.net/merchant/5219/images/site/IMG_0928.JPG")
    st.header("Filter dan Pengaturan")
    show_summary = st.checkbox("Tampilkan Ringkasan Informasi")
    show_first_rows = st.checkbox("Tampilkan Lima Baris Pertama")
    show_duplicates = st.checkbox("Periksa Duplikasi")
    show_statistics = st.checkbox("Tampilkan Statistik")
    show_visualizations = st.checkbox("Tampilkan Visualisasi")

# Informasi DataFrame jika dicentang
if show_summary:
    st.subheader("Informasi Mengenai Dataset")
    st.write("""
    Bike sharing systems are new generation of traditional bike rentals where whole process from membership, rental and return 
    back has become automatic. Through these systems, user is able to easily rent a bike from a particular position and return 
    back at another position. Currently, there are about over 500 bike-sharing programs around the world which is composed of 
    over 500 thousands bicycles. Today, there exists great interest in these systems due to their important role in traffic, 
    environmental and health issues. 

    Apart from interesting real world applications of bike sharing systems, the characteristics of data being generated by
    these systems make them attractive for the research. Opposed to other transport services such as bus or subway, the duration
    of travel, departure and arrival position is explicitly recorded in these systems. This feature turns bike sharing system into
    a virtual sensor network that can be used for sensing mobility in the city. Hence, it is expected that most of important
    events in the city could be detected via monitoring these data.
    """)

# Tampilkan lima baris pertama DataFrame jika dicentang
if show_first_rows:
    st.subheader("Lima Baris Pertama DataFrame")
    st.write(bike_df.head())

# Periksa duplikasi jika dicentang
if show_duplicates:
    num_duplicates = bike_df.duplicated().sum()
    st.subheader("Periksa Duplikasi")
    st.write(f"Jumlah Duplikasi: {num_duplicates}")

# Tampilkan ringkasan statistik DataFrame jika dicentang
if show_statistics:
    st.subheader("Ringkasan Statistik DataFrame")
    st.write(bike_df.describe())

# Visualisasi data jika dicentang
if show_visualizations:
    # Membuat plot pie untuk persentase penyewaan sepeda pada hari libur
    avg_holiday = bike_df.groupby('holiday_day')['cnt_day'].mean().reset_index()
    fig1, ax1 = plt.subplots()
    ax1.pie(avg_holiday['cnt_day'], labels=['Tidak Libur', 'Libur'], autopct='%1.1f%%', colors=['lightblue', 'lightgreen'])
    ax1.set_title('Persentase Rata-rata Penyewaan Sepeda pada Hari Libur')
    st.subheader("Persentase Rata-rata Penyewaan Sepeda pada Hari Libur")
    st.pyplot(fig1)

    # Membuat plot bar untuk rata-rata jumlah pengguna sepeda berdasarkan kondisi cuaca
    weather_avg_cnt = bike_df.groupby('weather_label')['cnt_day'].mean().reset_index()
    weather_avg_cnt_sorted = weather_avg_cnt.sort_values("cnt_day")
    plt.figure(figsize=(10, 7))
    plt.bar(weather_avg_cnt_sorted['weather_label'], weather_avg_cnt_sorted['cnt_day'], color='skyblue')
    plt.title('Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca')
    plt.xlabel('Kondisi Cuaca')
    plt.ylabel('Rata-rata Jumlah Pengguna Sepeda')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.subheader("Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca")
    st.pyplot(plt)

    # Grafik interaktif menggunakan Plotly
    # Visualisasi menggunakan Plotly untuk persentase penyewaan sepeda pada hari libur
    fig1 = px.pie(avg_holiday, values='cnt_day', names='holiday_day', title='Persentase Rata-rata Penyewaan Sepeda pada Hari Libur')
    st.plotly_chart(fig1)

    # Visualisasi menggunakan Plotly untuk rata-rata jumlah pengguna sepeda berdasarkan kondisi cuaca
    fig2 = px.bar(weather_avg_cnt_sorted, x='weather_label', y='cnt_day', title='Rata-rata Jumlah Pengguna Sepeda berdasarkan Kondisi Cuaca', 
                  labels={'weather_label': 'Kondisi Cuaca', 'cnt_day': 'Rata-rata Jumlah Pengguna Sepeda'})
    fig2.update_xaxes(tickangle=45)
    st.plotly_chart(fig2)

# Estetika tambahan
st.caption('Copyright (c) Mahdi Romzuz Zaki 2024')
