# Identitas Developer

Nama : (Rizaldi Sa'ad)
NIM : (14012500065) 
Kelas : (3A-KOM)

---

# ⚔️ OOP Python Game Project (Battle Arena)

Proyek game pertarungan interaktif berbasis Konsol/OOP ini dibangun untuk mengimplementasikan seluruh materi Pemrograman Berorientasi Objek (OOP) Pertemuan 1–7.

---

## 📌 Pemetaan Materi OOP pada Kode

| No | Konsep OOP | Implementasi Kode | Berkas |
| :--- | :--- | :--- | :--- |
| **1** | **Class & Instance Object** | Instansiasi objek dari class `Karakter`, `Hero`, dan `Monster` | `karakter.py`, `hero.py`, `monster.py`, `main.py` |
| **2** | **Constructor & Validation** | Penetapan atribut awal pada method `__init__` | `karakter.py`, `hero.py`, `monster.py` |
| **3** | **Inheritance (Pewarisan)** | `Hero` dan `Monster` mewarisi sifat-sifat dari parent class `Karakter` | `hero.py`, `monster.py`, `karakter.py` |
| **4** | **Encapsulation** | Pembatasan akses atribut dan pengelolaan status HP karakter | `karakter.py` |
| **5** | **Polymorphism & Overriding** | Kustomisasi method `serang()` / `skill_khusus()` pada subclass | `hero.py`, `monster.py` |
| **6** | **Object Interaction** | Method interaksi menyerang dan menerima damage antar objek | `main.py`, `karakter.py` |
| **7** | **Game Loop & Control** | Pengendalian alur giliran bermain menggunakan `while` dan `break` | `main.py` |

---

## 📂 Struktur Berkas

* **`karakter.py`** : Kelas induk (*parent class*) yang mengatur atribut dasar dan fungsi universal karakter.
* **`hero.py`** : Kelas turunan (*subclass*) untuk pemain utama dengan tambahan skill khusus.
* **`monster.py`** : Kelas turunan (*subclass*) untuk musuh/monster dalam game.
* **`main.py`** : Berkas utama tempat eksekusi program dan logika *game loop*.
* **`README.md`** : Dokumentasi proyek, identitas developer, dan pemetaan materi.

---

## 🚀 Cara Menjalankan Game

1. Pastikan Python 3.x telah terinstal di perangkat Anda[cite: 12].
2. Buka terminal VS Code di dalam folder proyek[cite: 12].
3. Jalankan perintah berikut[cite: 12]:
   ```bash
   python main.py
   ---

### Cara Terakhir Kirim ke GitHub:
Setelah file `README.md` disimpan (*Ctrl + S*), buka terminal VS Code Anda dan jalankan perintah ini untuk memperbarui repository di GitHub:

```bash
git add .
git commit -m "Final update README dan Identitas Developer"
git push -u origin main