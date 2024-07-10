import pandas as pd
from prettytable import PrettyTable
import math

##Star Mencari Nilai Acak
class MCG:
    def __init__(self, seed, a, m):
        self.seed = seed
        self.a = a
        self.m = m
        self.state = seed

    def next(self):
        self.state = (self.a * self.state) % self.m
        return self.state

# Meminta input dari pengguna
seed = int(input("Masukkan nilai z0: "))
a = int(input("Masukkan nilai a: "))
m = int(input("Masukkan nilai m: "))
n = int(input("Masukkan jumlah angka acak yang diinginkan: "))

# Buat instance dari MCG
mcg = MCG(seed, a, m)

# Generate angka acak dan simpan dalam daftar
data = []
previous_state = seed

for i in range(0, n + 1):
    zi = mcg.next()
    ui = zi / m
    X100 = round(100 * ui)  # Membulatkan nilai X100
    data.append([i, previous_state, zi, ui, X100])
    previous_state = zi

# Membuat tabel dengan PrettyTable
table = PrettyTable()
table.field_names = ["i", "zi-1", "zi(Random Integer Number)", "ui(Uniform R,N)", "X100"]

for row in data:
    table.add_row(row)

# Menampilkan tabel
print(table)
###End Nilai AcaK

print( )
print()


#Star Data
# Data
data = {
    'TAHUN': [1971, 1972, 1973, 1974, 1975, 1976, 1977, 1978, 1979, 1980,
              1981, 1982, 1983, 1984, 1985, 1986, 1987, 1988, 1989, 1990,
              1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000,
              2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010,
              2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020,
              2021, 2022],
    'Jumlah Penduduk Laki-Laki': [59985, 61928, 63328, 64982, 66152, 69012, 70989, 72652, 73768, 74398,
                                  75933, 77500, 79845, 80693, 82566, 83786, 85899, 87327, 88577, 89939,
                                  92021, 93877, 95765, 96991, 97541, 98003, 98989, 99569, 99898, 100898,
                                  103309, 105496, 107992, 108749, 109212, 110703, 111502, 115056, 117656, 118221,
                                  119877, 120999, 122789, 125567, 126483, 129910, 131310, 132683, 134025, 135337,
                                  138298, 139388],
    'Jumlah Penduduk Perempuan': [59212, 60682, 62782, 63458, 65659, 68531, 69995, 71773, 72565, 73600,
                                  74667, 76887, 78564, 79887, 81089, 82580, 84566, 86876, 87899, 89909,
                                  91732, 92340, 94702, 95902, 96809, 97450, 99821, 101003, 104201, 106765,
                                  108055, 109453, 110987, 111945, 112004, 113054, 115481, 116968, 118547, 119332,
                                  120554, 122121, 123456, 125989, 126889, 128586, 130044, 131478, 132886, 143266,
                                  134333, 136384]
}

print(f"{'Jumlah Penduduk Indonesia':^72}")
# Create PrettyTable
tabledata = PrettyTable()

# Add columns
tabledata.add_column("TAHUN", data['TAHUN'])
tabledata.add_column("Jumlah Penduduk Laki-Laki", data['Jumlah Penduduk Laki-Laki'])
tabledata.add_column("Jumlah Penduduk Perempuan", data['Jumlah Penduduk Perempuan'])

# Display table
print(tabledata)
###END Data

print()
print()


# Calculate statistics
jumlah_penduduk_laki_laki = data['Jumlah Penduduk Laki-Laki']
nilai_tertinggi = max(jumlah_penduduk_laki_laki)
nilai_terendah = min(jumlah_penduduk_laki_laki)
rentang = nilai_tertinggi - nilai_terendah
jumlah_kelas = round(1 + 3.3 * math.log10(len(jumlah_penduduk_laki_laki)))
interval_kelas = round(rentang / jumlah_kelas)
batas_bawah= nilai_terendah - 1


# Create PrettyTable
tableHitung = PrettyTable()

print(f"{'Jumlah Penduduk Laki-Laki'}")
# Add columns
tableHitung.add_column("Nama", ["Nilai Tertinggi", "Nilai Terendah", "Rentang", "Jumlah Kelas", "Interval Kelas", "Batas Bawah"])
tableHitung.add_column("Jumlah", [
    nilai_tertinggi, nilai_terendah, rentang, jumlah_kelas, interval_kelas,batas_bawah
])

# Display table
print(tableHitung)

print()
print()


# Creating interval classes
interval_classes = []
frekuensi = []
start = batas_bawah
for i in range(jumlah_kelas):
    end = start + interval_kelas 
    interval_classes.append((start, end))
    # Count frequency
    count = sum(1 for x in jumlah_penduduk_laki_laki if start <= x <= end)
    frekuensi.append(count)
    start = end + 1

# Create PrettyTable for interval classes
tableInterval = PrettyTable()

print(f"{'Interval Kelas Jumlah Penduduk Laki-Laki':^10}")
tableInterval.add_column("Kelas", [f"Kelas {i+1}" for i in range(jumlah_kelas)])
tableInterval.add_column("Interval", [f"{start}-{end}" for start, end in interval_classes])
tableInterval.add_column("Frekuensi", frekuensi)

# Adding a separator row
tableInterval.add_row(["-"*5, "-"*15, "-"*8])
# Adding total row
total_frekuensi = sum(frekuensi)
tableInterval.add_row([" ", "TOTAL", total_frekuensi])

# Adding a separator row
tableInterval.add_row(["-"*5, "-"*15, "-"*8])

# Display table
print(tableInterval)

print()
print()

# Calculating probabilities
total_data = len(jumlah_penduduk_laki_laki)
probabilitas = [freq / total_data for freq in frekuensi]
probabilitas_kumulatif = [sum(probabilitas[:i+1]) for i in range(len(probabilitas))]
probabilitas_kumulatif_x100 = [pk * 100 for pk in probabilitas_kumulatif]

# Creating interval angka acak
interval_angka_acak = []
current_low = 0
for pk_x100 in probabilitas_kumulatif_x100:
    current_high = int(pk_x100) 
    interval_angka_acak.append(f"{current_low} - {current_high}")
    current_low = current_high + 1

# Adjust the last interval
interval_angka_acak[-1] = f"{interval_angka_acak[-2].split('-')[1].strip()} - 100"

# Create and display the probability table
tableProbabilitas = PrettyTable()
print(f"{'Probabilitas Jumlah Penduduk Laki-Laki':^72}")
tableProbabilitas.add_column("Jumlah Penduduk Laki-Laki", [f"{start}-{end}" for start, end in interval_classes])
tableProbabilitas.add_column("Frekuensi", frekuensi)
tableProbabilitas.add_column("Probabilitas", [f"{p:.4f}" for p in probabilitas])
tableProbabilitas.add_column("Probabilitas Kumulatif", [f"{pk:.4f}" for pk in probabilitas_kumulatif])
tableProbabilitas.add_column("Probabilitas Kumulatif (x100)", [f"{int(pk*100)}" for pk in probabilitas_kumulatif])
tableProbabilitas.add_column("Interval Angka Acak", interval_angka_acak)
print(tableProbabilitas)

print()
print()
