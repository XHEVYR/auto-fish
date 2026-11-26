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

## 🚀 Panduan Setup Awal (Untuk Pemula / Belum Punya Python)

Jika Anda belum pernah menggunakan Python atau Git sebelumnya, ikuti langkah-langkah berikut dari awal:

### Langkah 1: Install Python
1. Buka situs resmi Python: [python.org/downloads](https://www.python.org/downloads/)
2. Klik tombol kuning **Download Python 3.x.x**.
3. Jalankan file installer yang sudah diunduh.
4. **PENTING:** Di layar pertama installer, **WAJIB centang** kotak **"Add python.exe to PATH"** di bagian bawah sebelum menekan tombol **Install Now**.
   *(Jika lupa mencentang ini, perintah `python` dan `pip` tidak akan dikenali oleh Windows).*
5. Tunggu hingga selesai, lalu klik **Close**.

### Langkah 2: Download Script Ini
Anda tidak perlu menginstall Git. Cukup unduh langsung dari GitHub:
1. Di halaman GitHub ini, klik tombol hijau **`<> Code`** di bagian kanan atas.
2. Pilih **Download ZIP**.
3. Buka file `.zip` yang baru diunduh, lalu **Extract / Ekstrak** foldernya ke tempat yang mudah ditemukan (misalnya di `Desktop` atau `Documents`).

### Langkah 3: Buka Terminal (CMD) di Dalam Folder
1. Buka folder hasil ekstrak tadi (yang di dalamnya ada file `auto_fish.py`).
2. Klik pada **bilah alamat (Address Bar)** di bagian atas jendela File Explorer (tempat tulisan lokasi folder, misal `C:\Users\...\auto-fish-main`).
3. Ketik **`cmd`** lalu tekan **Enter**. Jendela hitam Command Prompt akan terbuka langsung di folder tersebut.

*(Tips: Jika nantinya bot tidak merespons saat jendela Roblox aktif, buka **Command Prompt** lewat Start Menu dengan klik kanan -> **Run as administrator**, lalu masuk ke folder menggunakan perintah `cd C:\lokasi\folder\anda`).*

### Langkah 4: Install Library yang Dibutuhkan
Di dalam jendela CMD tadi, ketik perintah berikut lalu tekan **Enter**:
```bash
pip install -r requirements.txt
```
Tunggu beberapa saat sampai proses download & instalasi selesai. Langkah ini cukup dilakukan **1 kali saja**.

### Langkah 5: Jalankan Bot
Untuk menjalankan script, ketik perintah berikut di CMD lalu tekan **Enter**:
```bash
python auto_fish.py
```
Jika muncul tulisan `=== BOT MEMANCING STEAL AN EGG SIAP ===`, berarti bot sudah siap digunakan!

---

## 💻 Panduan Cepat (Untuk yang Sudah Punya Python & Git)

```bash
# 1. Clone repositori
git clone https://github.com/XHEVYR/auto-fish.git
cd auto-fish

# 2. (Opsional) Buat dan aktifkan Virtual Environment
python -m venv venv
venv\Scripts\activate

# 3. Install dependensi
pip install -r requirements.txt

# 4. Jalankan script
python auto_fish.py
```

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

