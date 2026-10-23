import re
import joblib
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree

# ==============================================================================
# 1. READ DATASET & PREPROCESSING
# ==============================================================================
print('--- 1. Membaca & Memproses Dataset ---')
df = pd.read_csv('Dataset_Pabrik_Kasur_Besar.csv')

# Menghapus baris yang tidak memiliki target (Status_QC)
df_clean = df.dropna(subset=['Status_QC']).copy()


# Fungsi parsing kolom Usia_Mesin teks ("14 thn 10 bln 1 hr") ke total hari
def parse_usia_mesin(text):
  if pd.isna(text):
    return 0
  thn = re.search(r'(\d+)\s*thn', str(text))
  bln = re.search(r'(\d+)\s*bln', str(text))
  hr = re.search(r'(\d+)\s*hr', str(text))

  years = int(thn.group(1)) if thn else 0
  months = int(bln.group(1)) if bln else 0
  days = int(hr.group(1)) if hr else 0

  return years * 365 + months * 30 + days


df_clean['Usia_Mesin_Hari'] = df_clean['Usia_Mesin'].apply(parse_usia_mesin)

# Mengisi missing value pada kolom kategorikal jika ada
df_clean['Jenis_Kasur'] = df_clean['Jenis_Kasur'].fillna('Unknown')
df_clean['Supervisor'] = df_clean['Supervisor'].fillna('Unknown')

# ==============================================================================
# 2. ONE-HOT ENCODING & DATA SPLITTING
# ==============================================================================
print('--- 2. Memisahkan Fitur & Label (One-Hot Encoding) ---')
X = pd.get_dummies(
    df_clean[['Usia_Mesin_Hari', 'Jenis_Kasur', 'Supervisor']], drop_first=False
)
y = df_clean['Status_QC']

# Pembagian data latih (80%) dan data uji (20%)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================================================================
# 3. BUILD & TRAIN DECISION TREE MODEL
# ==============================================================================
print('--- 3. Melatih Model Decision Tree ---')
tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)
tree_model.fit(X_train, y_train)

# ==============================================================================
# 4. MODEL EVALUATION & FEATURE IMPORTANCE
# ==============================================================================
print('\n=================== 4. EVALUASI MODEL ===================')
y_pred = tree_model.predict(X_test)

print('Akurasi Model:', round(accuracy_score(y_test, y_pred), 3))
print('\nClassification Report:\n', classification_report(y_test, y_pred))
print('Confusion Matrix:\n', confusion_matrix(y_test, y_pred))

# Melihat Fitur Paling Berpengaruh
importances = pd.Series(
    tree_model.feature_importances_, index=X.columns
).sort_values(ascending=False)
print('\nFeature Importances (Top Features):')
print(importances[importances > 0])

# ==============================================================================
# 5. PREDIKSI DATA BARU (SAMPLE TEST)
# ==============================================================================
print('\n=================== 5. PREDIKSI DATA BARU ===================')
# Kasus: Usia Mesin = 2500 hari, Jenis = Spring Bed, Supervisor = Pak Budi
sample_data = pd.DataFrame(0, index=[0], columns=X.columns)
sample_data['Usia_Mesin_Hari'] = 2500
if 'Jenis_Kasur_Spring Bed' in sample_data.columns:
  sample_data['Jenis_Kasur_Spring Bed'] = 1
if 'Supervisor_Pak Budi' in sample_data.columns:
  sample_data['Supervisor_Pak Budi'] = 1

prediksi_baru = tree_model.predict(sample_data)
print('Hasil Prediksi Status QC:', prediksi_baru[0])

# ==============================================================================
# 6. VISUALISASI DECISION TREE
# ==============================================================================
print('\n--- 6. Membuat Visualisasi Pohon Keputusan ---')
plt.figure(figsize=(20, 10))
plot_tree(
    tree_model,
    feature_names=X.columns,
    class_names=tree_model.classes_,
    filled=True,
    rounded=True,
    fontsize=9,
)
plt.title('Visualisasi Decision Tree Status QC Pabrik Kasur', fontsize=14)
plt.savefig('decision_tree_kasur.png', bbox_inches='tight', dpi=300)
plt.show()

# ==============================================================================
# 7. EXPORT MODEL
# ==============================================================================
print('\n--- 7. Menyimpan Model ---')
joblib.dump(tree_model, 'decision_tree_kasur.pkl')
joblib.dump(X.columns.tolist(), 'model_features.pkl')
print('Model dan daftar fitur berhasil disimpan ke file .pkl!')