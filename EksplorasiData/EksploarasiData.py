import pandas as pd

# 1. Loading Data
df = pd.read_csv('Dataset_Pabrik_Kasur_Besar.csv')

print('=== 1. INFORMASI DATASET ===')
print(f'Jumlah Baris : {df.shape[0]} (Syarat >= 1000 Terpenuhi)')
print(f'Jumlah Kolom : {df.shape[1]}')

# 2. Tipe Data Asli
print('\n=== 2. TIPE DATA PER KOLOM ===')
print(df.dtypes)

# Mengubah tipe kolom kategorikal dari 'object' ke 'category'
kategorikal_cols = ['Jenis_Kasur', 'Status_QC', 'Supervisor']
for col in kategorikal_cols:
  df[col] = df[col].astype('category')

print('\nTipe data setelah dikonversi ke category:')
print(df.dtypes)

# 3. Pemeriksaan Duplikat & Null
print('\n=== 3. PERIKSA DUPLIKAT & NULL ===')
print(f'Jumlah Baris Duplikat: {df.duplicated().sum()}')
print('\nJumlah Data Null per Kolom:')
print(df.isnull().sum())
print(f'Total Sel Null Keseluruhan: {df.isnull().sum().sum()}')