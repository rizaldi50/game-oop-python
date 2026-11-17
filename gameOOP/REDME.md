# Identitas Developer

Nama : [Rizaldi Sa'ad] | NIM : [14012500065] | Kelas : [3A-KOM]

⚔️ **OOP Battle Arena (Console Game)**

Projek game pertarungan interaktif berbasis teks (Console/Terminal) ini dibangun untuk mengimplementasikan seluruh materi Pemrograman Berorientasi Objek (OOP) Python.

---

### 📌 Pemetaan Materi OOP pada Kode

| No | Konsep OOP | Implementasi Kode pada Projek | Berkas |
| :--- | :--- | :--- | :--- |
| **1** | **Class & Instance Object** | Pembuatan blueprint kelas (`Karakter`, `Hero`, `Monster`) dan instansiasi objek (`pahlawan`, `musuh`). | `karakter.py`, `hero.py`, `monster.py`, `main.py` |
| **2** | **Encapsulation** | Pembungkusan atribut privat (`self._nama`, `self._hp`) menggunakan Getter dan Setter agar nilai HP aman. | `karakter.py` |
| **3** | **Inheritance (Pewarisan)** | Kelas `Hero` dan `Monster` mewarisi atribut dan metode dari induk kelas `Karakter`. | `karakter.py`, `hero.py`, `monster.py` |
| **4** | **Polymorphism** | Override metode `serang()` di dalam kelas anak (`Hero` dan `Monster`) dengan perilaku aksi yang berbeda. | `hero.py`, `monster.py` |
| **5** | **Abstraction** | Menggunakan modul `abc` (`ABC` dan `@abstractmethod`) pada kelas `Karakter` agar wajib di-override. | `karakter.py` |

---

### 🚀 Cara Menjalankan Projek

1. Pastikan komputer Anda sudah terinstal Python.
2. Unduh atau clone repository ini ke komputer Anda.
3. Buka terminal/CMD di dalam folder project, lalu jalankan perintah berikut:
   ```bash
   python main.py