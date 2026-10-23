# Eksplorasi Data Pabrik Kasur

Repositori ini berisi skrip Python sederhana untuk melakukan eksplorasi data (EDA - Exploratory Data Analysis) tahap awal pada dataset operasional atau produksi dari sebuah pabrik kasur. Skrip ini berfokus pada pengecekan struktur data, optimalisasi tipe data, serta pemeriksaan kualitas data (data quality check).

## 📁 File dalam Proyek

*   **`Dataset_Pabrik_Kasur_Besar.csv`**: File dataset utama yang memuat data pabrik kasur. Pastikan file ini berada di direktori yang sama dengan skrip Python sebelum dijalankan.
*   **`EksploarasiData.py`**: Skrip Python yang berisi kode untuk memuat dan menganalisis dataset.

## 🛠️ Prasyarat

Untuk menjalankan skrip ini, Anda membutuhkan instalasi Python dan library `pandas`. Anda bisa menginstal library yang dibutuhkan menggunakan pip:

```bash
pip install pandas
```

## 🚀 Cara Menjalankan

Buka terminal atau command prompt, arahkan ke direktori tempat file disimpan, lalu jalankan perintah berikut:

```bash
python EksploarasiData.py
```

## 📊 Alur Kerja Skrip (`EksploarasiData.py`)

Saat dijalankan, skrip akan melakukan 3 tahapan utama:

1.  **Informasi Dataset (Loading Data)**
    *   Membaca file `Dataset_Pabrik_Kasur_Besar.csv`.
    *   Menampilkan jumlah baris dan kolom. Skrip juga memverifikasi apakah syarat minimal jumlah baris (>= 1000) telah terpenuhi.

2.  **Pengecekan dan Konversi Tipe Data**
    *   Menampilkan tipe data asli dari setiap kolom.
    *   Mengonversi kolom yang bersifat kategorikal (`Jenis_Kasur`, `Status_QC`, dan `Supervisor`) dari tipe `object` menjadi tipe `category`. Hal ini berguna untuk optimasi penggunaan memori dan mempercepat proses komputasi pada analisis lanjutan.
    *   Menampilkan kembali tipe data setelah konversi dilakukan.

3.  **Pemeriksaan Duplikat & Null (Data Quality)**
    *   Menghitung dan menampilkan jumlah baris data yang duplikat.
    *   Memeriksa kelengkapan data dengan menampilkan jumlah nilai *null* (kosong) pada masing-masing kolom.
    *   Menghitung total keseluruhan sel yang bernilai *null* dalam dataset.

---
*Dokumen ini dibuat secara otomatis untuk mendampingi skrip eksplorasi data.*