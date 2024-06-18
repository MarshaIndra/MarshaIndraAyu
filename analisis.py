import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib_venn import venn2

# Data penjualan
data = {
    'Tanggal Penjualan': ['01-01-2023', '02-01-2023', '03-01-2023', '04-01-2023', '05-01-2023', '06-01-2023', 
                          '07-01-2023', '08-01-2023', '09-01-2023', '10-01-2023'],
    'Jenis Kendaraan': ['Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Motor', 'Mobil', 'Motor'],
    'Merek': ['Toyota', 'Honda', 'Honda', 'Yamaha', 'Suzuki', 'Kawasaki', 'Mitsubishi', 'Honda', 'Nissan', 'Suzuki'],
    'Model': ['Avanza', 'Beat', 'Jazz', 'Nmax', 'Ertiga', 'Ninja 250', 'Pajero', 'Vario', 'X-Trail', 'Satria FU'],
    'Jumlah Terjual': [5, 10, 3, 7, 4, 2, 2, 8, 1, 5],
    'Harga Satuan (Rp)': [200000000, 16000000, 250000000, 30000000, 190000000, 70000000, 500000000, 18000000, 350000000, 20000000],
    'Total Penjualan (Rp)': [1000000000, 160000000, 750000000, 210000000, 760000000, 140000000, 1000000000, 144000000, 350000000, 100000000]
}

# Membuat DataFrame
df = pd.DataFrame(data)

# Mengatur tema seaborn
sns.set_theme(style="whitegrid", palette="pastel")

# Scatter plot
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='Jumlah Terjual', y='Total Penjualan (Rp)', hue='Jenis Kendaraan', style='Jenis Kendaraan', s=100)
plt.title('Scatter Plot Jumlah Terjual vs Total Penjualan')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Total Penjualan (Rp)')
plt.legend(title='Jenis Kendaraan')
plt.show()

# Histogram
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Jumlah Terjual', hue='Jenis Kendaraan', multiple='stack', bins=10, kde=True)
plt.title('Histogram Jumlah Terjual')
plt.xlabel('Jumlah Terjual')
plt.ylabel('Frekuensi')
plt.show()

# Diagram Venn
plt.figure(figsize=(10, 6))
mobil_terjual = set(df[df['Jenis Kendaraan'] == 'Mobil']['Model'])
motor_terjual = set(df[df['Jenis Kendaraan'] == 'Motor']['Model'])
venn2([mobil_terjual, motor_terjual], ('Mobil', 'Motor'))
plt.title('Diagram Venn Penjualan Mobil dan Motor')
plt.show()

# Pie chart
plt.figure(figsize=(10, 6))
penjualan_per_jenis = df.groupby('Jenis Kendaraan')['Total Penjualan (Rp)'].sum()
penjualan_per_jenis.plot(kind='pie', autopct='%1.1f%%', colors=sns.color_palette('pastel'), startangle=90)
plt.title('Pie Chart Total Penjualan Berdasarkan Jenis Kendaraan')
plt.ylabel('')
plt.show()

# Bar chart
plt.figure(figsize=(10, 6))
sns.barplot(data=df, x='Merek', y='Total Penjualan (Rp)', hue='Jenis Kendaraan')
plt.title('Bar Chart Total Penjualan per Merek dan Jenis Kendaraan')
plt.xlabel('Merek')
plt.ylabel('Total Penjualan (Rp)')
plt.xticks(rotation=45)
plt.legend(title='Jenis Kendaraan')
plt.show()
