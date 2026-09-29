# Proyek Analisis Data: Bike Sharing Dataset ✨

- **Nama:** Eyzar Hermanio
- **Email:** hermanioeyzar@gmail.com
- **ID Dicoding:** B26B14S005

---

## 📌 Deskripsi Singkat
Proyek ini melakukan analisis data mendalam menggunakan *Bike Sharing Dataset* [4] untuk memahami pola penyewaan sepeda berdasarkan kondisi lingkungan, musim, dan waktu operasional. Hasil akhir dari analisis ini disajikan secara interaktif melalui dashboard Streamlit.

---

## 📂 Struktur Direktori
```text
Dicoding_DataAnalyst/
├── BikeSharing_Dataset/
│   ├── day.csv
│   └── hour.csv
├── dashboard.py
├── Eyzar_Hermanio_Proyek_Analisis_Data.ipynb
├── README.md
├── requirements.txt
└── url.txt


## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```