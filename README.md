# Roblox Auto Fish Bot 🎣

Bot otomatisasi memancing untuk game Roblox (seperti *Steal an Egg* atau game memancing lainnya dengan mekanisme UI serupa) menggunakan **Computer Vision** (OpenCV) dan simulasi input mouse/keyboard.

---

## 📋 Fitur
- **Deteksi UI Otomatis**: Mendeteksi saat siap melempar pancingan (`cast_ui.png`) dan saat minigame/ikan menyambar (`reel_ui.png`).
- **Aman & Efisien**: Tidak melakukan spam klik saat pelampung berada di air agar tidak membatalkan pancingan.
- **Fast Clicking (Spam Klik)**: Klik cepat otomatis begitu minigame muncul hingga ikan tertangkap.
- **Hotkey Global**: Kontrol mudah menggunakan keyboard (`F6` untuk Start/Pause, `F7` untuk Stop).

---

## 🛠️ Persyaratan Sistem
- Sistem Operasi: Windows 10 / 11
- Python: Versi 3.8 ke atas
- Resolusi layar: Disarankan 1080p (Full HD) atau sesuaikan template screenshot jika resolusi berbeda.

---

## 🚀 Panduan Instalasi & Menjalankan

### 1. Clone atau Unduh Repositori
```bash
git clone https://github.com/XHEVYR/auto-fish.git
cd roblox-auto-fish
```

### 2. (Opsional tapi Disarankan) Buat Virtual Environment
```bash
python -m venv venv

# Aktivasi di Windows (Command Prompt):
venv\Scripts\activate

# Atau di PowerShell:
venv\Scripts\Activate.ps1
```

### 3. Install Dependensi
Jalankan perintah berikut untuk menginstal semua library yang dibutuhkan:
```bash
pip install -r requirements.txt
```

### 4. Menjalankan Script
Jalankan bot dengan perintah:
```bash
python auto_fish.py
```
> **Catatan:** Pastikan terminal/command prompt dijalankan dengan hak akses yang cukup (beberapa sistem memerlukan *Run as Administrator* agar `pynput` dapat mengirim input klik ke jendela Roblox).

---

## 🎮 Cara Menggunakan di Game
1. Buka game Roblox dan posisikan karakter di dekat air / spot memancing.
2. Siapkan alat pancing (pegang pancingan).
3. Jalankan script `python auto_fish.py`.
4. Beralih ke jendela Roblox.
5. Tekan **`[F6]`** untuk mengaktifkan bot. Bot akan mulai mencari UI dan memancing otomatis.
6. Tekan **`[F6]`** lagi untuk menjeda (Pause).
7. Tekan **`[F7]`** untuk mematikan program sepenuhnya.

---

## ⚙️ Konfigurasi (`auto_fish.py`)

Anda dapat menyesuaikan beberapa pengaturan di bagian atas file `auto_fish.py`:

```python
HOLD_LEMPAR = 0.05        # Durasi tahan klik saat melempar (detik)
JEDA_SETELAH_LEMPAR = 1.5 # Waktu tunggu setelah melempar sebelum mulai mendeteksi umpan
INTERVAL_SPAM_KLIK = 0.04 # Kecepatan klik saat minigame (~25 klik/detik)
BATAS_TUNGGU_MAX = 35.0   # Batas waktu tunggu jika umpan tidak kunjung disambar
THRESHOLD = 0.75          # Tingkat akurasi kemiripan gambar (0.0 - 1.0)
```

---

## 🖼️ Menyesuaikan Gambar Referensi (UI Template)
Jika UI game Roblox Anda berbeda atau bot gagal mendeteksi gambar:
1. Ambil screenshot area UI lempar dan simpan sebagai `cast_ui.png`.
2. Ambil screenshot tombol/ikon saat ikan menyambar dan simpan sebagai `reel_ui.png`.
3. Pastikan format gambar `.png` dan diletakkan di satu folder yang sama dengan `auto_fish.py`.

---

## ⚠️ Disclaimer
Penggunaan script otomasi/bot di Roblox memiliki risiko terhadap akun Anda sesuai dengan *Terms of Service* (ToS) platform yang bersangkutan. Script ini dibuat untuk tujuan edukasi dan pembelajaran Computer Vision. Gunakan dengan bijak dan risiko ditanggung sendiri.

