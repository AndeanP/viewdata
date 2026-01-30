📊 ViewData

Upload CSV → Visualisasi Grafik → Simpan ke Database (per User & File)

🔎 Deskripsi Singkat

ViewData adalah aplikasi web berbasis Python untuk:
Login user (username & password)
Upload file CSV
Menampilkan grafik otomatis untuk setiap kolom numerik
Menyimpan data upload ke database SQLite berdasarkan username dan nama file
Aplikasi dijalankan menggunakan Docker Compose
Frontend menggunakan Tailwind CSS
Backend berjalan di port 5001

🧱 Tech Stack
Layer	Teknologi
Backend	Python (Flask)
Database	SQLite
Frontend	HTML + TailwindCSS
Chart	Chart.js
Auth	Session-based Login
Container	Docker & Docker Compose
📁 Struktur Project
viewdata/
│
├── app/
│   ├── __init__.py
│   ├── app.py              # Entry point Flask
│   ├── models.py           # Database schema
│   ├── routes.py           # Routing logic
│   ├── auth.py             # Login & authentication
│   ├── utils.py            # CSV parsing & helpers
│   │
│   ├── templates/
│   │   ├── login.html
│   │   ├── upload.html
│   │   └── dashboard.html
│   │
│   └── static/
│       └── css/
│           └── tailwind.css
│
├── data/
│   └── uploads/             # File CSV tersimpan
│
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── README.md
└── agents.md

🔐 User Default
Username : admin
Password : admin123

🔄 Alur Aplikasi (Flow)
Login
  ↓
Upload CSV
  ↓
Parsing CSV
  ↓
Simpan Metadata ke DB
  ↓
Generate Grafik per Kolom
  ↓
Tampilkan Dashboard

🗄️ Database Schema (SQLite)
users
column	type
id	INTEGER (PK)
username	TEXT
id	INTEGER (PK)
user_id	INTEGER (FK)
file_name	TEXT
uploaded_at	DATETIME