# Tugas-Data-Mining

# Prediksi Status Quality Control (QC) Pabrik Kasur (DATA MINING)

Repositori ini berisi implementasi proyek Data Mining untuk memprediksi status Quality Control (QC) pada produksi di pabrik kasur. Model *machine learning* yang dibangun menggunakan algoritma Decision Tree Classifier.

**Deskripsi Proyek**
Sistem ini bertujuan untuk memprediksi apakah suatu produk kasur akan diklasifikasikan sebagai Lolos QC, Reject (Gagal), atau Cacat Minor (Perbaikan). Klasifikasi ini diproses dengan menganalisis tiga variabel utama dari dataset `Dataset_Pabrik_Kasur_Besar.csv`:

* **Usia Mesin**: Diubah dari teks berformat tahun/bulan/hari (contoh: "14 thn 10 bln 1 hr") menjadi kalkulasi total usia mesin dalam satuan hari.
* **Jenis Kasur**: Mencakup berbagai tipe produk seperti Busa (Foam), Hybrid, Kasur Lipat, Kasur Sorong, Latex, Orthopedic, dan Spring Bed.
* **Supervisor**: Mengidentifikasi pengawas lapangan yang bertugas, seperti Bu Ratna, Bu Siti, Pak Andi, Pak Budi, dan Pak Mandra.



**Alur Pemrosesan (Pipeline)**

1. **Pembersihan Data (Preprocessing)**: Baris data yang tidak memiliki label target (`Status_QC`) dihapus, perhitungan usia mesin dikonversi ke dalam variabel numerik hari, dan nilai yang kosong pada kolom jenis kasur atau supervisor diisi dengan label 'Unknown'.

2. **Ekstraksi Fitur**: Proses *One-Hot Encoding* diterapkan untuk memecah data kategorikal (Jenis Kasur dan Supervisor) menjadi kolom-kolom biner numerik agar dapat dipelajari oleh model.


3. **Pelatihan Model**: Data dibagi dengan proporsi 80% untuk pelatihan dan 20% untuk pengujian. Algoritma Decision Tree kemudian dilatih dengan pengaturan pembatasan kedalaman cabang maksimal (`max_depth`) di angka 4.

4. **Evaluasi & Penyimpanan**: Model dievaluasi menggunakan metrik akurasi, *classification report*, dan *confusion matrix*. Setelah itu, pohon keputusan divisualisasikan menjadi bentuk gambar, lalu bobot model diekspor ke format `.pkl`.


**Struktur File**
* `DataMiningMesinKasur.py`: *Script* utama yang berisi kode *end-to-end* mulai dari pembacaan data, prapemrosesan, pelatihan *machine learning*, hingga uji prediksi sampel.
* `Dataset_Pabrik_Kasur_Besar.csv`: Dataset mentah yang digunakan sebagai bahan dasar analitik.
* `decision_tree_kasur.pkl`: File model pohon keputusan yang telah dilatih dan siap digunakan untuk memprediksi data baru.
* `model_features.pkl`: File yang menyimpan daftar urutan kolom fitur untuk memastikan konsistensi format input saat melakukan prediksi.
* `decision_tree_kasur.jpg`: Visualisasi alur logika (aturan percabangan) dari model Decision Tree.


**Cara Menjalankan Kode**
Pastikan *library* Python seperti `pandas`, `scikit-learn`, `matplotlib`, dan `joblib` sudah terpasang. Jalankan perintah berikut di terminal Anda:

```
python DataMiningMesinKasur.py

```





# Eksplorasi Data Pabrik Kasur (EKSPLORASI DATA)

Repositori ini berisi skrip Python sederhana untuk melakukan eksplorasi data (EDA - Exploratory Data Analysis) tahap awal pada dataset operasional atau produksi dari sebuah pabrik kasur. Skrip ini berfokus pada pengecekan struktur data, optimalisasi tipe data, serta pemeriksaan kualitas data (data quality check).
📁 File dalam Proyek
`Dataset_Pabrik_Kasur_Besar.csv`: File dataset utama yang memuat data pabrik kasur. Pastikan file ini berada di direktori yang sama dengan skrip Python sebelum dijalankan.
`EksploarasiData.py`: Skrip Python yang berisi kode untuk memuat dan menganalisis dataset.
🛠️ Prasyarat
Untuk menjalankan skrip ini, Anda membutuhkan instalasi Python dan library `pandas`. Anda bisa menginstal library yang dibutuhkan menggunakan pip:
```bash
pip install pandas
```
🚀 Cara Menjalankan
Buka terminal atau command prompt, arahkan ke direktori tempat file disimpan, lalu jalankan perintah berikut:
```bash
python EksploarasiData.py
```
📊 Alur Kerja Skrip (`EksploarasiData.py`)
Saat dijalankan, skrip akan melakukan 3 tahapan utama:
Informasi Dataset (Loading Data)
Membaca file `Dataset_Pabrik_Kasur_Besar.csv`.
Menampilkan jumlah baris dan kolom. Skrip juga memverifikasi apakah syarat minimal jumlah baris (>= 1000) telah terpenuhi.
Pengecekan dan Konversi Tipe Data
Menampilkan tipe data asli dari setiap kolom.
Mengonversi kolom yang bersifat kategorikal (`Jenis_Kasur`, `Status_QC`, dan `Supervisor`) dari tipe `object` menjadi tipe `category`. Hal ini berguna untuk optimasi penggunaan memori dan mempercepat proses komputasi pada analisis lanjutan.
Menampilkan kembali tipe data setelah konversi dilakukan.
Pemeriksaan Duplikat & Null (Data Quality)
Menghitung dan menampilkan jumlah baris data yang duplikat.
Memeriksa kelengkapan data dengan menampilkan jumlah nilai null (kosong) pada masing-masing kolom.
Menghitung total keseluruhan sel yang bernilai null dalam dataset.
---
Dokumen ini dibuat secara otomatis untuk mendampingi skrip eksplorasi data.

Saat dijalankan, *script* akan mencetak hasil evaluasi model ke layar terminal, melakukan satu simulasi prediksi data baru (contoh: mesin berusia 2500 hari, produksi Spring Bed, diawasi oleh Pak Budi), menampilkan jendela gambar struktur pohon keputusan, dan menghasilkan file `.pkl`.



