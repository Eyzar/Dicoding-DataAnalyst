import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Konfigurasi Tampilan Halaman Streamlit
st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

# Memuat Dataset (Pastikan file day.csv berada dalam satu folder atau sesuaikan path-nya)
@st.cache_data
def load_data():
    # Sesuaikan path file CSV jika diperlukan, misal '../data/day.csv' atau 'day.csv'
    df_day = pd.read_csv('BikeSharing_Dataset/day.csv')
    df_hour = pd.read_csv('BikeSharing_Dataset/hour.csv')
    
    # Mengubah tipe data tanggal
    df_day['dteday'] = pd.to_datetime(df_day['dteday'])
    df_hour['dteday'] = pd.to_datetime(df_hour['dteday'])
    
    return df_day, df_hour

df_day, df_hour = load_data()

# --- SIDEBAR (FILTER) ---
st.sidebar.header("Filter Data 🔍")

# Filter Rentang Tanggal
min_date = df_day['dteday'].min()
max_date = df_day['dteday'].max()

start_date, end_date = st.sidebar.date_input(
    label="Rentang Waktu",
    value=[min_date, max_date],
    min_value=min_date,
    max_value=max_date
)

# Filter berdasarkan data utama
main_df = df_day[(df_day['dteday'] >= pd.to_datetime(start_date)) & 
                 (df_day['dteday'] <= pd.to_datetime(end_date))]

main_hour_df = df_hour[(df_hour['dteday'] >= pd.to_datetime(start_date)) & 
                       (df_hour['dteday'] <= pd.to_datetime(end_date))]

# --- MAIN CONTENT ---
st.title("🚲 Bike Sharing Analysis Dashboard")
st.markdown("Dashboard interaktif ini menyajikan hasil analisis data penyewaan sepeda (*Bike Sharing Dataset*) untuk mendukung pengambilan keputusan bisnis yang lebih baik [4].")

# 1. METRICS (KPIs)
total_rentals = main_df['cnt'].sum()
avg_daily_rentals = round(main_df['cnt'].mean(), 2)
total_casual = main_df['casual'].sum()
total_registered = main_df['registered'].sum()

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Penyewaan", f"{total_rentals:,}")
with col2:
    st.metric("Rata-rata Harian", f"{avg_daily_rentals:,}")
with col3:
    st.metric("Pengguna Casual", f"{total_casual:,}")
with col4:
    st.metric("Pengguna Registered", f"{total_registered:,}")

st.divider()

# 2. VISUALISASI PERTANYAAN 1: Pengaruh Cuaca & Hari Kerja
st.subheader("📊 Perbandingan Penyewaan Berdasarkan Kondisi Cuaca & Hari Kerja")

fig, ax = plt.subplots(figsize=(10, 5))
# Mapping cuaca sederhana untuk label
weather_mapping = {1: 'Cerah/Berawan', 2: 'Kabut/Berawan', 3: 'Hujan/Salju Ringan'}
main_df['weather_label'] = main_df['weathersit'].map(weather_mapping)

sns.barplot(
    x='weather_label', 
    y='cnt', 
    hue='workingday', 
    data=main_df, 
    palette='Set2', 
    ax=ax, 
    ci=None
)
ax.set_title("Rata-rata Penyewaan Berdasarkan Cuaca dan Hari Kerja", fontsize=14)
ax.set_xlabel("Kondisi Cuaca", fontsize=12)
ax.set_ylabel("Rata-rata Penyewaan (cnt)", fontsize=12)
ax.legend(title="Tipe Hari", labels=['Libur/Weekend', 'Hari Kerja'])
st.pyplot(fig)

st.markdown("""
**Insight:**
- Kondisi cuaca yang cerah (`Cerah/Berawan`) mendominasi tingkat penyewaan sepeda tertinggi secara konsisten.
- Cuaca buruk seperti hujan atau salju ringan menurunkan tingkat penggunaan layanan secara drastis [4].
""")

st.divider()

# 3. VISUALISASI PERTANYAAN 2: Tren Penyewaan Berdasarkan Jam (Hourly Trend)
st.subheader("⏰ Tren Rata-rata Penyewaan Sepeda Berdasarkan Jam dalam Sehari")

fig2, ax2 = plt.subplots(figsize=(12, 5))
hourly_trend = main_hour_df.groupby(['hr', 'workingday'])['cnt'].mean().reset_index()

sns.lineplot(
    x='hr', 
    y='cnt', 
    hue='workingday', 
    data=hourly_trend, 
    marker='o', 
    palette='coolwarm', 
    ax=ax2
)
ax2.set_title("Pola Jam Sibuk Penyewaan Sepeda", fontsize=14)
ax2.set_xlabel("Jam (0 - 23)", fontsize=12)
ax2.set_ylabel("Rata-rata Penyewaan", fontsize=12)
ax2.set_xticks(range(0, 24))
ax2.legend(title="Tipe Hari", labels=['Libur/Weekend', 'Hari Kerja'])
st.pyplot(fig2)

st.markdown("""
**Insight:**
- Pada hari kerja, terdapat dua puncak (*spike*) utama penyewaan sepeda, yaitu pada jam 08.00 pagi dan jam 17.00–18.00 sore.
- Hal ini menunjukkan bahwa sebagian besar pengguna memanfaatkan sepeda sebagai sarana transportasi penunjang mobilitas kerja (*commuter*) [4].
""")

# Copyright Footer
st.markdown("---")
st.markdown("<p style='text-align: center;'>© 2026 - Proyek Analisis Data Dicoding</p>", unsafe_allow_html=True)