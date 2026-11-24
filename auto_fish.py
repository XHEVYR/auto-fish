import time
import threading
import cv2
import mss
import numpy as np
from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Listener as KeyboardListener

# ================= KONFIGURASI =================
HOLD_LEMPAR = 0.05        # Durasi tahan klik untuk melempar (detik). Ubah misal ke 0.8 jika ingin mencoba 'Perfect'
JEDA_SETELAH_LEMPAR = 1.5 # Jeda aman agar tidak double-click saat pelampung baru meluncur
INTERVAL_SPAM_KLIK = 0.04 # Kecepatan klik saat minigame (0.04 detik = ~25 klik/detik)
BATAS_TUNGGU_MAX = 35.0   # Timeout (detik) jika pelampung tidak kunjung disambar / gagal lempar
THRESHOLD = 0.75          # Tingkat kemiripan gambar (0.0 - 1.0)
# ===============================================

mouse = MouseController()
running = False
program_aktif = True

# Muat gambar referensi
template_cast = cv2.imread("cast_ui.png", cv2.IMREAD_COLOR)
template_reel = cv2.imread("reel_ui.png", cv2.IMREAD_COLOR)

if template_cast is None or template_reel is None:
    raise FileNotFoundError("Pastikan 'cast_ui.png' dan 'reel_ui.png' ada di folder yang sama dengan skrip ini!")


def klik_kiri(durasi_tahan=0.02):
    """Melakukan klik kiri dengan jeda tahan singkat agar terbaca oleh engine Roblox."""
    mouse.press(Button.left)
    time.sleep(durasi_tahan)
    mouse.release(Button.left)


def deteksi_template(sct, region, template):
    """Menangkap area layar tertentu dan mencocokkannya dengan gambar referensi."""
    screenshot = np.array(sct.grab(region))
    frame_bgr = cv2.cvtColor(screenshot, cv2.COLOR_BGRA2BGR)
    hasil = cv2.matchTemplate(frame_bgr, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(hasil)
    return max_val >= THRESHOLD


def on_press(key):
    """Hotkey F6 untuk Start/Pause, F7 untuk mematikan program."""
    global running, program_aktif
    if key == Key.f6:
        running = not running
        status = "AKTIF" if running else "DIJEDA (PAUSE)"
        print(f"\n[INFO] Status Bot: {status}")
    elif key == Key.f7:
        print("\n[INFO] Menutup program...")
        running = False
        program_aktif = False
        return False


def loop_memancing():
    global running, program_aktif

    with mss.mss() as sct:
        monitor = sct.monitors[1]  # Monitor utama
        lebar = monitor["width"]
        tinggi = monitor["height"]

        # Area pantau tengah layar (untuk UI 'Tahan untuk Melempar')
        area_tengah = {
            "top": int(tinggi * 0.20),
            "left": int(lebar * 0.20),
            "width": int(lebar * 0.60),
            "height": int(tinggi * 0.60),
        }

        # Area pantau bawah layar (untuk tombol merah 'BERHENTI')
        area_bawah = {
            "top": int(tinggi * 0.65),
            "left": int(lebar * 0.10),
            "width": int(lebar * 0.80),
            "height": int(tinggi * 0.35),
        }

        state = "SIAP_LEMPAR"
        waktu_mulai_tunggu = 0.0

        print("=== BOT MEMANCING STEAL AN EGG SIAP ===")
        print("Tekan [F6] untuk Mulai / Pause")
        print("Tekan [F7] untuk Keluar")

        while program_aktif:
            if not running:
                state = "SIAP_LEMPAR"
                time.sleep(0.1)
                continue

            # 1. TAHAP MELEMPAR PANCING
            if state == "SIAP_LEMPAR":
                if deteksi_template(sct, area_tengah, template_cast):
                    print("[1/3] UI Lempar terdeteksi -> Melempar pelampung...")
                    klik_kiri(HOLD_LEMPAR)
                    time.sleep(JEDA_SETELAH_LEMPAR)
                    state = "MENUNGGU_UMPAN"
                    waktu_mulai_tunggu = time.time()
                    print("[2/3] Pelampung di air -> Menunggu sambaran (mouse diam)...")
                else:
                    time.sleep(0.1)

            # 2. TAHAP MENUNGGU UMPAN (DILARANG KLIK)
            elif state == "MENUNGGU_UMPAN":
                if deteksi_template(sct, area_bawah, template_reel):
                    state = "KLIK_CEPAT"
                    print("[3/3] Tanda seru / UI Minigame muncul -> Spam klik kiri!")
                elif time.time() - waktu_mulai_tunggu > BATAS_TUNGGU_MAX:
                    print("[WARN] Waktu tunggu habis, mengulang siklus...")
                    state = "SIAP_LEMPAR"
                else:
                    time.sleep(0.05)

            # 3. TAHAP SPAM KLIK CEPAT SAAT UI MUNCUL
            elif state == "KLIK_CEPAT":
                if deteksi_template(sct, area_bawah, template_reel):
                    klik_kiri(0.02)
                    time.sleep(INTERVAL_SPAM_KLIK)
                else:
                    print("[SELESAI] UI Minigame hilang -> Kembali ke siklus awal.\n")
                    time.sleep(1.2)  # Jeda animasi hasil tangkapan sebelum lempar ulang
                    state = "SIAP_LEMPAR"


if __name__ == "__main__":
    listener = KeyboardListener(on_press=on_press)
    listener.start()
    loop_memancing()