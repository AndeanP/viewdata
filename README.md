# 📊 ViewData

**ViewData** adalah aplikasi web sederhana untuk mengunggah file CSV dan memvisualisasikan datanya secara otomatis dalam bentuk grafik. Aplikasi ini dibangun dengan Python (Flask) dan berjalan menggunakan Docker.

## 🚀 Fitur Utama

- **Login Aman**: Sistem autentikasi pengguna.
- **Upload CSV**: Unggah file dataset CSV Anda dengan mudah.
- **Visualisasi Otomatis**: Aplikasi otomatis membaca kolom numerik dan membuat grafik (Line Chart).
- **Dashboard**: Kelola dan lihat riwayat file yang telah diunggah.
- **Data Preview**: Lihat cuplikan data (10 baris pertama) langsung di browser.

## 🛠️ Teknologi yang Digunakan

- **Backend**: Python (Flask)
- **Database**: SQLite (Tersimpan otomatis)
- **Frontend**: HTML + Tailwind CSS
- **Charting**: Chart.js
- **Container**: Docker & Docker Compose

## 📋 Prasyarat

Pastikan Anda sudah menginstal:
- [Docker Desktop](https://www.docker.com/products/docker-desktop) (atau Docker Engine + Docker Compose)

## 🏃‍♂️ Cara Menjalankan Aplikasi

1.  **Clone atau Siapkan Folder Project**
    Pastikan Anda berada di dalam folder project ini di terminal.

2.  **Jalankan dengan Docker Compose**
    ```bash
    docker-compose up
    ```
    Tunggu sebentar saat pertama kali dijalankan karena aplikasi akan menginstal dependensi (pip install) secara otomatis.

3.  **Buka di Browser**
    Akses aplikasi melalui alamat:
    👉 [http://localhost:5001](http://localhost:5001)

## 🔐 Akun Default

Gunakan akun berikut untuk login:

- **Username**: `admin`
- **Password**: `admin123`

## 📂 Struktur Project

```
viewdata/
├── app/                  # Kode sumber aplikasi (Python & HTML)
├── data/                 # Folder data (Database & file upload)
├── docker-compose.yml    # Konfigurasi Docker
├── Dockerfile            # Blueprint image Docker
└── requirements.txt      # Daftar dependensi Python
```

## 📝 Cara Menggunakan

1.  Login dengan akun `admin`.
2.  Di halaman Dashboard, klik area **Upload New File** atau drop file CSV Anda di sana.
3.  Setelah upload sukses, file akan muncul di daftar "Your Files".
4.  Klik nama file untuk melihat grafik visualisasi dan data tabelnya.

---
*Dibuat untuk memudahkan analisis data CSV secara cepat.*
